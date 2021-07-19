from django.urls import path
from .views import SubjectListView, SubjectDetailView, CourseEnrollView

app_name = 'courses'

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('courses/<int:pk>/enroll/', CourseEnrollView.as_view(), name='course_enroll'),
]