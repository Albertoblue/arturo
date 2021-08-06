from django.shortcuts import render,HttpResponse,reverse,redirect
from .forms import AutorForm,LibroForm
from .models import Escritor,Libro
from django.core.paginator import Paginator

# Create your views here.

def autores(request):
    #En la base de datos seria: "SELECT * FROM escritor"
    autores=Escritor.objects.all()
    paginator=Paginator(autores,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    form=AutorForm()
    return render(request,'autores.html',{"form":form,"page_obj":page_obj})
#path('autores/',views.autores,name='autores'),

def autoresForm(request):
    form=AutorForm()
    if request.method=='POST':
        form=AutorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuarios:autores'))
    return render(request,'autorForm.html',{"form":form})
#path('autoresForm/',views.autoresForm,name='autoresForm'),



def autorEdit(request,id):
    autor=Escritor.objects.get(id=id)
    autores=Escritor.objects.all()
    form=AutorForm(instance=autor)
    if(request.method=="POST"):
        form=AutorForm(data=request.POST,instance=autor)
        form.save()
        return redirect(reverse('usuarios:autores'))
    return render(request,'autorEdit.html',{"form":form,"autores":autores,"id":id})
#path('autorEdit/<int;id>',views.autorEdit,name='autorEdit'),

def autorDelete(request,id):
    autor=Escritor.objects.get(id=id)
    autor.delete()
    return redirect(reverse('usuarios:autores'))
#path('autorDelete/<int:id>',views.autorDelete,name='autorDelete'),


#path('libros/',views.libros,name='libros'),

def libros(request):
    libros=Libro.objects.all()
    paginator=Paginator(libros,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    form=LibroForm()
    return render(request,'libros.html',{"page_obj":page_obj,"form":form})
#path('librosForm/',views.librosForm,name='librosForm'),

def libroForm(request):
    form=LibroForm()
    if request.method=='POST':
        form=LibroForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuarios:libros'))
    return render(request,'librosForm.html',{"form":form})

#path('librosEdit/',views.librosEdit,name='librosEdit'),
def libroEdit(request,id):
    if request.method=="POST":
        libro=Libro.objects.get(id=id)
        form=LibroForm(instance=libro,data=request.POST)
        form.save()
        return redirect(reverse('usuarios:libros'))
    libros=Libro.objects.all()
    paginator=Paginator(libros,2)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    libro=Libro.objects.get(id=id)
    form=LibroForm(instance=libro)
    return render(request,'librosEdit.html',{"form":form,"page_obj":page_object,"id":id})

#path('librosDelete/<int:id>',views.librosDelete,name='librosDelete'),
def libroDelete(request,id):
    libro=Libro.objects.get(id=id)
    libro.delete()
    return redirect(reverse('usuarios:libros'))