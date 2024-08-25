from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return render(request, 'book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    return render(request, 'book_form.html')


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    return render(request, 'book_form.html')

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, pk):
    return render(request, 'book_form.html')