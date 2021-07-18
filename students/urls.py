from django.urls import path
from .views import StudentRegistrationView, StudentEnrollCourseView, StudentCourseListView, \
    StudentCourseDetailView

app_name = 'students'

urlpatterns = [
    path('register/', StudentRegistrationView.as_view(), name='registration'),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='enroll_course'),
    path('courses/', StudentCourseListView.as_view(), name='course_list'),

    path('course/<pk>/', StudentCourseDetailView.as_view(), name='course_detail'),
    path('course/<pk>/<module_id>/', StudentCourseDetailView.as_view(), name='course_detail_module'),
]