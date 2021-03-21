from django.contrib import admin
from .models import Student, Department, Project, StudentJoinProject, StudentOrganization, StudentScholar, UserProfile

admin.site.site_title = "第二课堂成绩数据管理系统"
admin.site.site_header = "第二课堂成绩后台管理系统"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "name",
        "grade",
        "sex",
        "major_name",
        "department_name",
    )
    list_filter = ("department_name", "major_name")
    search_fields = ("student_id", "name")
    # filedsets = ((None, {"fileds": ("name", ("sex",), ("email", "phone"), "status")}),)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_id", "department_name")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_filter = (
        "semester",
        "category",
        "department_name",
    )
    search_fields = ("name", "department_name")
    list_display = ("project_id", "name", "department_name", "category", "certify_state")


@admin.register(StudentJoinProject)
class StudentJoinProjectAdmin(admin.ModelAdmin):
    search_fields = ("s_id", "student_name", "project_name")
    list_filter = ("semester",)
    list_display = ("s_id", "student_name", "project_name", "semester")


@admin.register(StudentOrganization)
class StudentOrgnizationAdmin(admin.ModelAdmin):
    search_fields = ("s_id", "org_name", "department_name")
    list_filter = ("department_name", "org_name", "certify_state")
    list_display = (
        "s_id",
        "org_name",
        "position",
        "start_time",
        "end_time",
        "department_name",
        "certify_state",
        "created_time",
        "update_time",
    )


@admin.register(StudentScholar)
class StudentScholarAdmin(admin.ModelAdmin):
    search_fields = ("s_id", "g_time", "scholar_name")
    list_filter = ("s_id", "scholar_name", "certify_state")
    list_display = (
        "s_id",
        "g_time",
        "scholar_name",
        "level",
        "certify_state",
        "created_time",
        "update_time",
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ("user", "department")
    list_filter = ("department",)
    list_display = ("id", "user", "department", "created_time")
