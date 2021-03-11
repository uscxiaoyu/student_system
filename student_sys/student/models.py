from django.db import models
from django.db.models.enums import Choices


# 学生表
class Student(models.Model):
    SEX_ITEMS = [
        (1, "男"),
        (2, "女"),
        (0, "未知"),
    ]

    student_id = models.CharField(primary_key=True, max_length=64, verbose_name="学号")
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别")
    department_name = models.CharField(max_length=64, default=None, verbose_name="学院")
    major_name = models.CharField(max_length=64, default=None, verbose_name="专业")
    grade = models.IntegerField(verbose_name="年级")

    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    def __str__(self) -> str:
        return "<student_id: {}, student_name: {}>".format(self.student_id, self.name)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = verbose_name_plural = "学生信息"


# 活动表
class Project(models.Model):
    project_id = models.IntegerField(primary_key=True, verbose_name="活动编号")
    name = models.CharField(max_length=128, verbose_name="活动名称")
    department_name = models.CharField(max_length=128, verbose_name="主办单位")
    semester = models.CharField(max_length=64, null=True, blank=True, default=None, verbose_name="活动时间")
    category = models.CharField(max_length=64, verbose_name="活动类型")
    certify_state = models.CharField(max_length=64, verbose_name="认证状态")

    def __str__(self) -> str:
        return "<project_id: {}, project_name: {}>".format(self.project_id, self.name)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = verbose_name_plural = "活动信息"


# 部门表
class Department(models.Model):
    department_id = models.IntegerField(primary_key=True, verbose_name="部门编号")
    department_name = models.CharField(max_length=128, unique=True, verbose_name="部门名称")

    def __str__(self) -> str:
        return "<department_id: {}, name: {}>".format(self.department_id, self.department_name)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = verbose_name_plural = "部门信息"


# 活动参与信息
class StudentJoinProject(models.Model):
    s_id = models.CharField(max_length=64, verbose_name="学号")
    student_name = models.CharField(max_length=64, verbose_name="姓名")
    p_id = models.IntegerField(default=None, verbose_name="活动编号")
    semester = models.CharField(max_length=64, null=True, blank=True, verbose_name="活动时间")
    project_name = models.CharField(max_length=128, verbose_name="活动名称")

    def __str__(self) -> str:
        return "<student_id: {}, project_id: {}>".format(self.s_id, self.p_id)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = verbose_name_plural = "学生参与活动信息"


# 学生组织活动经历
class StudentOrgnization(models.Model):
    s_id = models.CharField(max_length=64, verbose_name="学号")
    org_name = models.CharField(max_length=128, verbose_name="组织名称")
    position = models.CharField(max_length=64, verbose_name="职务")
    start_time = models.DateField(verbose_name="开始日期")
    end_time = models.DateField(verbose_name="结束日期")
    department_name = models.CharField(max_length=128, verbose_name="部门名称")
    certify_state = models.CharField(max_length=64, verbose_name="认证状态", default=None, blank=True)
    
    def __str__(self) -> str:
        return "<student_id: {}, org_name: {}, position: {}>".format(self.s_id, self.org_name, self.position)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = verbose_name_plural = "学生组织活动信息"
        

# 学生奖励
class StudentScholar(models.Model):
    s_id = models.CharField(max_length=64, verbose_name="学号")
    g_time = models.DateField(verbose_name="获奖时间")
    scholar_name = models.CharField(max_length=64, verbose_name="奖学金名称")
    level = models.CharField(max_length=64, verbose_name="奖学金级别")
    certify_state = models.CharField(max_length=64, verbose_name="认证状态", default=None, blank=True)
    def __str__(self) -> str:
        return "<student_id: {}, scholar_name: {}, level: {}>".format(self.s_id, self.scholar_name, self.level)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = verbose_name_plural = "学生获奖信息"
