from django.urls import path
from .views import (
    CourseDetailsView,
    TeacherListView,
    SchoolFacilityListView,
    LaboratoryListView,
)

urlpatterns = [
    path("course/<int:course_id>/", CourseDetailsView.as_view(), name="course_details"),
    path("teachers/", TeacherListView.as_view(), name="teacher_list"),
    path("facilities/", SchoolFacilityListView.as_view(), name="school_facilities"),
    path("laboratories/", LaboratoryListView.as_view(), name="laboratories"),
]
