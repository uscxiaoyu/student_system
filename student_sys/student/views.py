from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.http import StreamingHttpResponse
from django.http import FileResponse
from django.urls import reverse
from django.views import View
from .models import Student, Project, StudentJoinProject
from .forms import StudentForm, ProjectForm, StudentJoinProjectForm


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


def get_report(student_id):
    s = Student.objects.get(student_id=student_id)[:1]
    if s:
        if s.grade == 0:
            grade = int('20' + str(s.student_id[:2]))
        else:
            grade = s.grade
            
        sps = StudentJoinProject.objects.get(s_id=student_id)
        p_info = {}  # 写入参加活动信息
        for sp in sps:
            p_name = sp.project_name
            p = Project.objects.find(project_name=p_name)[:1]
            category = p.category
            if category in p_info:
                c = p_info[category][-1][0]
                p_info[category].append([c + 1, p.semester, p.p_name, p.department_name, p.certify_state])
            else:
                p_info[category] = [[1, p.semester, p.p_name, p.department_name, p.certify_state]]
        
        res_dict = {
            "基础信息": [s.department_name, grade, s.major_name, student_id, s.name, s.sex],
            "参加活动经历": p_info
        }
        return res_dict
    else:
        raise ValueError(f"学号{student_id}存在!")


class IndexView(View):
    template_name = "index.html"

    def get_context(self):
        students = Student.get_all()[:100]
        context = {"students": students}
        return context

    def get(self, request):
        form = StudentForm()
        context = self.get_context()
        context.update({"form": form})
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))

        context = self.get_context()
        context.update({"form": form})
        return render(request, self.template_name, context=context)
