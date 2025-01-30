from django.shortcuts import render, redirect, get_object_or_404
from .models import myBooks


# Home view, lists all books
def home(request):
    books = myBooks.objects.all()
    context = {'books': books}
    return render(request, 'index.html', context)


# Update book view
def update_book(request):
    if request.method == 'POST':
        # Fetch the book ID from the form submission
        book_id = request.POST.get('book_id')
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        # Get the book instance and update its fields
        book = get_object_or_404(myBooks, id=book_id)

        # Ensure fields are not empty
        if not title or not author or not genre or not price or not stock:
            return render(request, 'index.html', {
                'error_message': 'All fields must be filled out.',
                'books': myBooks.objects.all()
            })

        # Update the book instance
        book.title = title
        book.author = author
        book.genre = genre
        book.price = price
        book.stock = stock
        book.save()

        # Redirect after saving the changes
        return redirect('home')

    return redirect('home')


def delete_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')

        # Retrieve the book to delete
        book = get_object_or_404(myBooks, id=book_id)
        book.delete()  # Delete the book record from the database

        # Redirect back to the home page after deletion
        return redirect('home')

    # If it's not a POST request, just redirect to the home page
    return redirect('home')

# Create new book view
def create_book(request):
    if request.method == 'POST':
        # Get data from the form submission
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        # Create a new book object and save it to the database
        new_book = myBooks.objects.create(
            title=title,
            author=author,
            genre=genre,
            price=price,
            stock=stock
        )

        # Redirect to the home page after creating the book
        return redirect('home')

    return render(request, 'index.html')  # If it's not a POST request, just return the home page