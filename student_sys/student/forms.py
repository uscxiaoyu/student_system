from django import forms
import datetime

class StudentForm(forms.Form):
    student_id = forms.CharField(max_length=25, label="学号")
    student_name = forms.CharField(max_length=25, label="姓名")
    sex = forms.ChoiceField(choices=[(1, "男"), (2, "女")], label="性别")
    department_name = forms.CharField(max_length=25, label="学院")
    major_name = forms.CharField(max_length=25, label="专业")

class ProjectForm(forms.Form):
    project_id = forms.IntegerField(label="活动编号")
    name = forms.CharField(max_length=128, label="活动名称")
    department_name = forms.CharField(max_length=128, label="主办单位")
    semester = forms.CharField(max_length=64, label="活动时间")
    category = forms.CharField(max_length=64, label="活动类型")
    certify_state = forms.CharField(max_length=64, label="认证状态")

class StudentJoinProjectForm(forms.Form):
    s_id = forms.CharField(max_length=64, label="学号")
    student_name = forms.CharField(max_length=64, label="姓名")
    p_id = forms.IntegerField(label="活动编号")
    project_name = forms.CharField(max_length=128, label="活动名称")

class DepartmentForm(forms.Form):
    department_id = forms.IntegerField(label="部门编号")
    department_name = forms.CharField(max_length=128, label="部门名称")

class ScholarForm(forms.Form):
    c_year = datetime.date.today().year
    ITEMS = [(1, f"{c_year-4}-{c_year-3}"), (2, f"{c_year-3}-{c_year-2}"), 
             (3, f"{c_year-2}-{c_year-1}"), (4, f"{c_year-1}-{c_year}"),]
    scholar_year = forms.ChoiceField(choices=ITEMS, label="评奖学年")
    scholar_name = forms.CharField(max_length=100, label="奖学金名称")
    scholar_level = forms.CharField(max_length=20, label="奖学金级别")
    certify_state = forms.CharField(max_length=64, label="认证状态")