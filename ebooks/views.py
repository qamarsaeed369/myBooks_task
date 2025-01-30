from django.shortcuts import render, redirect, get_object_or_404
from .models import Ebook
from .forms import EbookForm

# Create
def create_ebook(request):
    if request.method == "POST":
        form = EbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ebook_list')
    else:
        form = EbookForm()
    return render(request, 'create_ebook.html', {'form': form})

# Read
def ebook_list(request):
    ebooks = Ebook.objects.all()
    return render(request, 'ebook_list.html', {'ebooks': ebooks})

# Update
def update_ebook(request, pk):
    ebook = get_object_or_404(Ebook, pk=pk)
    if request.method == "POST":
        form = EbookForm(request.POST, instance=ebook)
        if form.is_valid():
            form.save()
            return redirect('ebook_list')
    else:
        form = EbookForm(instance=ebook)
    return render(request, 'update_ebook.html', {'form': form})

# Delete
def delete_ebook(request, pk):
    ebook = get_object_or_404(Ebook, pk=pk)
    if request.method == "POST":
        ebook.delete()
        return redirect('ebook_list')
    return render(request, 'delete_ebook.html', {'ebook': ebook})
from django.shortcuts import render
from .models import  myBooks

# Create your views here.
def home(request):
    books=myBooks.objects.all()
    context={'books':books}
    return render (request, 'index.html', context)
