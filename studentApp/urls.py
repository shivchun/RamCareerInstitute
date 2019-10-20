from django.urls import path
from studentApp import views

urlpatterns = [
    path('signup/', views.sign_up_view),
    path('student/', views.student_index),
    path('thanku/', views.thanku),
    path('time_table/', views.time_table),
    path('exam/', views.exam),
    path('exam_registration_target/', views.exam_registration_target),
    path('exam_registration_12/', views.exam_registration_12),
    path('exam_registration_11/', views.exam_registration_11),
    path('exam_registration_10/', views.exam_registration_10),
    path('exam_registration_9/', views.exam_registration_9),
    path('exam_registration_8/', views.exam_registration_8),
    path('exam_registration_7/', views.exam_registration_7),
    path('exam_registration_6/', views.exam_registration_6),
    path('select_class/', views.result_page),
    path('result_of_class_target/', views.r_target),
    path('result_of_class_12/', views.r_12),
    path('result_of_class_11/', views.r_11),
    path('result_of_class_10/', views.r_10),
    path('result_of_class_9/', views.r_9),
    path('result_of_class_8/', views.r_8),
    path('result_of_class_7/', views.r_7),
    path('result_of_class_6/', views.r_6),
]
