from django.urls import path
from course.views import home,course_details,course_add,course_update,course_delete

urlpatterns=[
    path('',home),
    path('add/',course_add),
    path('view/<int:id>/',course_details),
    path('update/<int:id>/',course_update),
    path('delete/<int:id>/', course_delete),  


]