from django.db import connection


def getOrgByDeptName(dept_name, certify_state="未认证"):
    res = []
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM student_view_organization WHERE school=%s AND certify_state=%s", [dept_name, certify_state]
        )
        for row in cursor:
            l = list(row)
            l[-2] = str(l[-2]) + "_O"
            res.append(l)

    return res


def getScholarByDeptName(dept_name, certify_state="未认证"):
    res = []
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM student_view_scholar WHERE school=%s AND certify_state=%s", [dept_name, certify_state]
        )
        for row in cursor:
            l = list(row)
            l[-2] = str(l[-2]) + "_S"
            res.append(l)

    return res
