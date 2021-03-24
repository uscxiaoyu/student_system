from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("signUp", views.signUpView, name="signUp"),
    path("downloadDocx", views.downloadDocxView, name="downloadDocx"),
    path("checkDocx", views.checkDocxView, name="checkDocx"),
    path("logout", views.logoutView, name="logout"),
    path("insertStudentOrganization", views.insertStudentOrganization, name="insertStudentOrganization"),
    path("insertStudentScholar", views.insertStudentScholar, name="insertStudentScholar"),
    path("deleteStudentOrganization/<int:r_id>", views.deleteStudentOrganization, name="deleteStudentOrganization"),
    path("deleteStudentScholar/<int:r_id>", views.deleteStudentScholar, name="deleteStudentScholar"),
    path("updateStudentOrganizationState", views.updateOrganizationState, name="updateStudentOrganizationState"),
    path("updateStudentScholarState", views.updateScholarState, name="updateStudentScholarState"),
    path("updateStudentOrganization", views.updateStudentOrganization, name="updateStudentOrganization"),
    path("updateStudentScholar", views.updateStudentScholar, name="updateStudentScholar"),
]
