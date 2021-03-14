from re import template
from django.contrib import auth
from django.http.response import Http404, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.views import View
from .models import Student, Project, StudentJoinProject, StudentOrganization, StudentScholar
from .write_docx import ReportDocx
import json


class LoginView(View):
    login_name = "login.html"
    teacher_main_page = "teacher_main.html"
    student_main_page = "student_main.html"

    def get(self, request):
        is_login = request.session.get("is_login", False)
        if is_login:
            u = request.session["username"]
            role = request.session["role"]
            print(u, role)
            if role == "教师":
                return render(request, self.teacher_main_page, {"request": request, "user": u})
            else:
                reportDoc = ReportDocx(u)
                infos = reportDoc.hint_list  # 错误提示
                report = reportDoc.student_report  # 学生信息
                print(request, report["参加活动经历"])
                return render(
                    request,
                    self.student_main_page,
                    {
                        "request": request,
                        "user": u,
                        "infos": infos,
                        "meta_info": report["基础信息"],
                        "activities": report["参加活动经历"],
                        "organization": report["学生组织经历"],
                        "scholar": report["获奖经历"],
                    },
                )
        else:
            return render(request, self.login_name)

    def post(self, request):
        u = request.POST.get("_id")  # 学号或者教工号
        p = request.POST.get("pwd")
        if User.objects.filter(username=u):
            u_id = User.objects.get(username=u).id
            u_group = Group.objects.get(user=u_id).name
            user = authenticate(username=u, password=p)
            if user:
                if user.is_active:
                    login(request, user)  # 登陆用户
                    # 在session中记录用户和角色
                    request.session["is_login"] = True
                    request.session["username"] = u
                    if u_group == "教师":
                        request.session["role"] = "教师"
                        return render(request, self.teacher_main_page, {"request": request, "user": u})
                    else:
                        request.session["role"] = "学生"
                        reportDoc = ReportDocx(u)
                        infos = reportDoc.hint_list  # 错误提示
                        report = reportDoc.student_report  # 学生信息
                        print(request, report["参加活动经历"])
                        return render(
                            request,
                            self.student_main_page,
                            {
                                "request": request,
                                "user": u,
                                "infos": infos,
                                "meta_info": report["基础信息"],
                                "activities": report["参加活动经历"],
                                "organization": report["学生组织经历"],
                                "scholar": report["获奖经历"],
                            },
                        )
                else:
                    self.tips = "账号未激活，请联系管理员"
            else:
                self.tips = "帐号密码错误，请重新输入"
        else:
            self.tips = "用户不存在，请注册"

        return render(request, self.login_name)


def logoutView(request):
    logout(request)
    return redirect("login")


def downloadDocxView(request):
    if request.method == "POST":
        student_id = request.POST.get("_id")
        reportDoc = ReportDocx(student_id)
        reportDoc.generate_docx()  # 生成docx文件
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        response["Content-Disposition"] = f"attachment; filename={student_id}-report.docx"
        reportDoc.document.save(response)
        return response
    else:
        return render(request, "main.html")


@login_required(login_url="")
def checkDocxView(request):
    body = request.body.decode("utf-8")
    res = json.loads(body)
    student_id = res["s_id"]
    reportDoc = ReportDocx(student_id)
    infos = reportDoc.hint_list
    report = reportDoc.student_report
    response = ""
    if not report:
        response += f"<p>学号{student_id}不存在！</p>"
        return HttpResponse(response)
    else:
        response = ""
        base_info = """
            <table id='base'>
                <tr>
                    <td>所在学院: %s</td><td>年级: %s</td><td>专业: %s</td>
                </tr>
                <tr>
                    <td>学号: %s</td><td>姓名: %s</td><td>性别: %s</td>
                </tr>
            </table>
            """ % tuple(
            report["基础信息"]
        )
        response += base_info
        head = "<tr> <th>%s</th> <th>%s</th> <th>%s</th> <th>%s</th> <th>%s</th></tr>" % (
            "序号",
            "活动日期",
            "活动名称",
            "主办单位",
            "认证状态",
        )

        for cate in report["参加活动经历"]:
            prj_html = f"<h3>{cate}</h3>"
            table = "<table class='content'>" + head
            for prj in report["参加活动经历"][cate]:
                row = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % tuple(prj)
                table += row

            table += "</table>"
            prj_html += table
            response += prj_html

        if report["学生组织经历"]:
            prj_html = f"<h3> 学生组织经历 </h3>"
            table = """<table class='content'>
                <tr>
                    <th>序号</th><th>开始时间</th><th>结束时间</th><th>组织名称</th><th>职位</th>
                    <th>指导单位</th><th>认证状态</th>
                </tr>
            """
            for prj in report["学生组织经历"]:
                row = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % tuple(
                    prj
                )
                table += row

            table += "</table>"
            prj_html += table
            response += prj_html

        if report["获奖经历"]:
            prj_html = f"<h3>获奖经历</h3>"
            table = """<table class='content'>
                <tr>
                    <th>序号</th><th>获奖时间</th><th>奖励名称</th><th>奖励级别</th><th>认证状态</th>
                </tr>
            """
            for prj in report["获奖经历"]:
                row = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % tuple(prj)
                table += row

            table += "</table>"
            prj_html += table
            response += prj_html

    if infos:
        response += "<p>以下项目查询出错，很可能是没在项目表中找到对应的项目</p>"
        for i, info in enumerate(infos):
            a = "<p>" + f"{i+1}. " + info[0] + ": " + info[1] + "</p>"
            response += a

    return HttpResponse(response)


def insertStudentScholar(request):
    body = request.body.decode("utf-8")
    res = json.loads(body)
    if "s_id" not in res:
        res["s_id"] = request.user
    try:
        StudentScholar.objects.create(**res)
        print(res, "插入成功!")
        return HttpResponse("<p>添加成功</p>")
    except Exception as e:
        print(e)
        return HttpResponse("添加失败" + str(e))


def insertStudentOrganization(request):
    body = request.body.decode("utf-8")
    res = json.loads(body)
    if "s_id" not in res:
        res["s_id"] = request.user
    try:
        StudentOrganization.objects.create(**res)
        print(res, "插入成功!")
        return HttpResponse("<p>添加成功</p>")
    except Exception as e:
        print(e)
        return HttpResponse("添加失败" + str(e))
