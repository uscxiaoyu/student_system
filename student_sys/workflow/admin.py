from django.contrib import admin
from .models import OrganizationProcess, ScholarProcess

# Register your models here.
@admin.register(OrganizationProcess)
class OrganizationProcessAdmin(admin.ModelAdmin):
    search_fields = ("student_id", "state")
    list_filter = ("state",)
    list_display = ("student_id", "org_id", "state", "admin_id", "created_time", "update_time")


@admin.register(ScholarProcess)
class ScholarProcessAdmin(admin.ModelAdmin):
    search_fields = ("student_id", "state")
    list_filter = ("state",)
    list_display = ("student_id", "org_id", "state", "admin_id", "created_time", "update_time")