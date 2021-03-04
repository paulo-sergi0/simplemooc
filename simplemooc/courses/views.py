from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import ContactCourse
#Quando se utiliza o "." na importação (ex> from .forms) está sendo indicado que é relatóvio a pasta atual (o pacote atual)
#get_object_or_404 : Para tratar quando for selecionado um id de curso que não existe

def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses':courses
    }
    return render(request, template_name, context)

#quando foi usado o id para buscar os cursos
#def details(request, pk ):
#    #course = Course.objects.get(pk=pk)
#    course = get_object_or_404(Course, pk=pk) 
#    context = {
#        'course': course
#    }
#    template_name = 'courses/details.html'
#    return render(request, template_name, context)

def details(request, slug ):
    #course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, slug=slug)
    #if de valiração se o método de envio é "POST". Se verdadeira passa a requisição via POST se não passa em branco
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            #Para acessar os campos do form é necessário usar o método (que disponibiliza um dicionário) cleaned_data (acessar direatamente não funcionara (ex: Form.name))
            #print(form.cleaned_data)
            #print(form.cleaned_data['name'])
            #print(form.clenead_data['message'])
            form.send_mail(course)
            form = ContactCourse() #Para limpar o formulário após o uso
    else:
        form = ContactCourse() 
    #context = {
    #    'course': course,
    #    'form':  form
    #}
    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)
