from re import template
from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.views import View
from .models import Student, Project, StudentJoinProject
from .forms import StudentForm, ProjectForm, StudentJoinProjectForm
from .write_docx import ReportDocx
import json


# def index(request):
#     students = Student.get_all()
#     if request.method == "POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             # cleaned_data = form.cleaned_data
#             # student = Student()
#             # student.name = cleaned_data["name"]
#             # student.sex = cleaned_data["sex"]
#             # student.email = cleaned_data["email"]
#             # student.profession = cleaned_data["profession"]
#             # student.qq = cleaned_data["qq"]
#             # student.phone = cleaned_data["phone"]
#             # student.save()
#             form.save()
#             return HttpResponseRedirect(reverse("index"))
#     else:
#         form = StudentForm()

#     context = {"students": students, "form": form}

#     return render(request, "index.html", context=context)


class IndexView(View):
    template_name = "index.html"
    teacher_main_page = "teacher_main.html"
    student_main_page = "student_main.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        u = request.POST.get("_id")  # 学号或者教工号
        p = request.POST.get("pwd")
        if User.objects.filter(username=u):
            u_id = User.objects.get(username=u).id
            u_group = Group.objects.get(user=u_id).name
            user = authenticate(username=u, password=p)
            if user:
                if user.is_active:
                    login(request, user)
                    if u_group == "教师":
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
                            },
                        )
                else:
                    self.tips = "账号未激活，请联系管理员"
            else:
                self.tips = "帐号密码错误，请重新输入"
        else:
            self.tips = "用户不存在，请注册"

        return render(request, self.template_name, {"request": request, "user": u})


def logoutView(request):
    logout(request)
    return redirect("index")


@login_required(login_url="index")
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

    if infos:
        response += "<p>以下项目查询出错，很可能是没在项目表中找到对应的项目</p>"
        for i, info in enumerate(infos):
            a = "<p>" + f"{i+1}. " + info[0] + ": " + info[1] + "</p>"
            response += a

    return HttpResponse(response)
