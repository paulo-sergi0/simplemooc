from django.db import models

class CourseManager(models.Manager):

    # Método pesquisa o parâmetro informado dentro do name e da description
    # "," entre os parâmetros é um and: Ira retornar somentos os registros que possuirem o parâmetro passado tanto no nome quanto na descrição
    # Para utilzar o "ou" é nescessário utilizar a class "Q" que está dentro do models
        # Dentro do "Q":
            # "&" e "," para and
            # "|" para or
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | 
            models.Q(description__icontains=query))


class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição Simples', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField('Data de Incío', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CourseManager()

    #Método sobreescrito para mostrar o nome do curso no painel "admin" do Django
    def __str__(self):
        return self.name

    #Decorator  que utiliza o método reverse (from django.core.urlresolvers import reverse) para regatar uma URL dado um nome
    #@models.permalink  #Esse decorator foi depreciado no Djanfo 2.0, portanto o get_absolute_url foi comentado (por ter comentado a opção "ver  no site" no painal Admin não é mais exibida)
    #ToDO: Descomentar o get_absolute_url e corrigir a exbição do link "ver no site"
   # def get_absolute_url(self):
   #     return ('courses:details', (), {'slug': self.slug})
        #O retorno desse método é uma tupla com as seguintes parâmetros
        #1 ('courses:details') : URL (namespace = courses e valor = details)
        #2 () : Argumentos não nomeados (que não está sendo utilizado no momento)
        #3 {'slug': self.slug} : Argumentos nomeaveis (um dictonary)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name'] # '-name' seria a order descrescente