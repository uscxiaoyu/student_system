import re
import xlrd
import openpyxl
import os, sys
import django

PROJ_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJ_ROOT)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student_sys.settings")
django.setup()

from student.models import Student, Project, StudentJoinProject

BASE_DIR = "data/"
def load_student():
    return
    
def load_project():
    return


def load_excel(f_path):
    if 'xlsx' in f_path:
        pass


def load_studentjoinproject():
    return

if __name__ == "__main__":
    student = Student.objects.all()[0]
    print(student.student_id, student.name, student.department_name)