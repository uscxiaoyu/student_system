from django.db import models

# 未认证学生组织活动
class OrganizationProcess(models.Model):
    STATE_ITEMS = [(0, "提交"), (1, "完成"), (2, "驳回")]
    student_id = models.CharField(max_length=64, verbose_name="学号")
    org_id = models.IntegerField(verbose_name="活动序号")
    admin_id = models.CharField(max_length=64, null=True, verbose_name="教师用户名")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    update_time = models.DateTimeField(editable=False, null=True, verbose_name="最近更新时间")
    state = models.IntegerField(choices=STATE_ITEMS, verbose_name="状态")

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self) -> str:
        return "<student_id: {}, org_id: {}>".format(self.student_id, self.org_id)

    class Meta:
        verbose_name = verbose_name_plural = "组织活动流程信息"


# 未认证奖学金
class ScholarProcess(models.Model):
    STATE_ITEMS = [(0, "提交"), (1, "完成"), (2, "驳回")]
    student_id = models.CharField(max_length=64, verbose_name="学号")
    org_id = models.IntegerField(verbose_name="活动序号")
    admin_id = models.CharField(max_length=64, null=True, verbose_name="教师用户名")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    update_time = models.DateTimeField(editable=False, null=True, verbose_name="最近更新时间")
    state = models.IntegerField(choices=STATE_ITEMS, verbose_name="状态")

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self) -> str:
        return "<student_id: {}, org_id: {}>".format(self.student_id, self.org_id)

    class Meta:
        verbose_name = verbose_name_plural = "奖学金流程信息"
