from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'create_at'] #campos que irão ser exibidos na tela de selecionar o curso
    search_fields = ['name', 'slug'] #A definicação dessa opção cria um campo de texto para a busca e faz um "ou", busca o texto digitado em "name" e "slug"
    prepopulated_fields = {'slug':('name',)} #Opção para preencher automaticamente campos de acordo com outros já preenchidos. Nesse exemplo após o "name" poderiam haver outros campos para composição do texto, ex: ('name', 'descricao')

admin.site.register(Course, CourseAdmin)


