from django.db import models


# Create your models here.

class Course(models.Model):
    conumber = models.AutoField(primary_key=True)
    coname = models.CharField(max_length=30)


class Clazz(models.Model):
    clnumber = models.AutoField(primary_key=True)
    clname = models.CharField(max_length=30)


class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    cno = models.ForeignKey(Clazz, on_delete=models.CASCADE)
    cour = models.ManyToManyField(Course)


def registerStu(sname, cname, *coname):
    # 插入班级
    cl = Clazz.objects.create(cname="cname")
    # 插入学生姓名
    st = Student.objects.create(sname="sname")
    # 插入课程名称
    for line in coname:
        Student.objects.create(sname="sname")
