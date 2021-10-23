from django.conf.urls import url, include
from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('resume',views.resume,name='resume'),
    path('skills',views.skills,name='skills'),
    path('projects',views.projects,name='projects'),
    path('feedback',views.feedback,name='feedback'),
    path('thankyou',views.thankyou,name='thankyou'),
]
