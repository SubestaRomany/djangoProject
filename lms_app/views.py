from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.views.generic import ListView

# Create your views here.
def index(request):
    if request.method =='POST':
        add_book=BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_category=CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context={
        'category':Category.objects.all(),
        'books':Book.objects.all(),
        'form':BookForm(),
        'formcat':CategoryForm(),
        'books_count':Book.objects.all().count
    }
    return render(request,'pages/index.html',context)

class BookListView(ListView):
    model = Book
    template_name = 'pages/books.html'
    context_object_name = 'books'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()  
        return context

def update(request,id):
    book_id =Book.objects.get(id=id)
    if request.method =='POST':
        book_save=BookForm(request.POST,request.FILES,book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save=BookForm(instance=book_id)
        context= {
            'form':book_save,
        }
        return render(request,'pages/update.html',context)


def delete(request,id):
    book_delete=Book.objects.get(id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')
    