from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, Teacher, SchoolFacility, Laboratory
from .serializers import SchoolFacilitySerializer, LaboratorySerializer


class CourseDetailsView(APIView):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        data = {
            "course_name": course.course_name,
            "course_code": course.course_code,
        }
        return JsonResponse(data)


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        data = [
            {
                "name": teacher.name,
                "courses": [course.course_name for course in teacher.courses.all()],
            }
            for teacher in teachers
        ]
        print("hello")
        return JsonResponse({"teachers": data})


class SchoolFacilityListView(APIView):
    def get(self, request):
        facilities = SchoolFacility.objects.all()
        serializer = SchoolFacilitySerializer(facilities, many=True)
        return JsonResponse({"facilities": serializer.data})


class LaboratoryListView(APIView):
    def get(self, request):
        laboratories = Laboratory.objects.all()
        serializer = LaboratorySerializer(laboratories, many=True)
        return JsonResponse({"laboratories": serializer.data})
