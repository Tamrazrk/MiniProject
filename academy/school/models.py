from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)

    def __str__(self):
        return self.course_name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class SchoolFacility(models.Model):
    facility_name = models.CharField(max_length=100)
    usage_purpose = models.TextField(max_length=200)

    def __str__(self):
        return self.facility_name


class Laboratory(SchoolFacility):
    equipment_list = models.TextField(200)

    def __str__(self):
        return f"Laboratory: {self.facility_name}"
