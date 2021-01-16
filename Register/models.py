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


def getCls(cname):
    try:
        cl = Clazz.objects.get(cname=cname)
    except Clazz.DoesNotExist:
        cl = Clazz.objects.create(cname=cname)
    return cl


def getStu(sname, cno):
    try:
        st = Student.objects.get(sname=sname, cno=cno)
    except Student.DoesNotExist:
        st = Student.objects.get(sname=sname, cno=cno)
    return st


def getcourseList(*coname):
    courseList = []
    for line in coname:
        try:
            c = Course.objects.get(coname=line)
        except Course.DoesNotExist:
            c = Course.objects.craete(coname=line)
        courseList.append(c)
    return courseList


def registerStu(sname, cname, *coname):
    # 1.获取班级对象
    cl = getCls(cname)

    # 插入学生姓名
    st = getStu(sname, cl.cno)

    # 获取课程对象
    co = getcourseList(*coname)
    st.cour.add(co)
