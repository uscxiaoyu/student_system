from django.contrib import admin
from .models import OrganizationProcess, ScholarProcess

# Register your models here.
@admin.register(OrganizationProcess)
class OrganizationProcessAdmin(admin.ModelAdmin):
    search_fields = ("student_id", "state", "admin_id", "org_id")
    list_filter = ("state", "admin_id")
    list_display = ("admin_id", "student_id", "org_id", "state", "created_time", "update_time")


@admin.register(ScholarProcess)
class ScholarProcessAdmin(admin.ModelAdmin):
    search_fields = ("student_id", "state", "scholar_id")
    list_filter = ("state", "admin_id")
    list_display = ("admin_id", "student_id", "scholar_id", "state", "created_time", "update_time")