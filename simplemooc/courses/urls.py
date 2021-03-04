from django.urls import path, re_path
from simplemooc.courses import views

app_name = 'courses'

urlpatterns = [ 
    re_path(r'^$' , views.index, name = 'index'),
    #re_path(r'^(?P<pk>\d+)/$' , views.details, name = 'details'), #quando foi usado o id para buscar os cursos
    re_path(r'^(?P<slug>[\w_-]+)/$' , views.details, name = 'details'),
]

#(?P<pk>\d+) : A expressão regular "\d+" o resto serve pra agrupar/nomear expressões regulares. Nomeação é utill pra o caso de existerem mais de um parâmetro (possiveis problemas com a ordem de envio dos parâmetros)