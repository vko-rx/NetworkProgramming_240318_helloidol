from django.urls import path

from MOOD import views

app_name = 'MOOD'

urlpatterns = [
    path('ksw/', views.show_ksw, name='ksw'),   #show_ksw 뒤에 괄호 X 시험나옴
    path('ajy/', views.show_ajy, name='ajy'),
]