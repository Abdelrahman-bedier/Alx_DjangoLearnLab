from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required
from .views import list_books

# Create your views here.
def list_books(request):
      
      books = Book.objects.all()
      context = {'books': books}
      return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get default context data
        id = self.kwargs.get('pk')

        library = Library.objects.get(pk=id) # Retrieve the current book instance
        context['library'] = library
        return context

def register(request):
    form = UserCreationForm()
    
    # Check if the form is valid when submitted
    if form.is_valid():
        user = form.save()
        
        # Optionally log the user in after registration
        login(request, user)
        
        # Redirect to the login page upon successful registration
        return redirect(reverse_lazy('login'))
    
    # Render the registration form template
    return render(request, 'relationship_app/register.html', {'form': form})


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def admin_test(user):
    if user.role == "Admin":
        return True
    else:
        return False
    
@user_passes_test(admin_test)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


def member_test(user):
    if user.role == "Member":
        return True
    else:
        return False
    
@user_passes_test(member_test)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

def librarian_test(user):
    if user.role == "Librarian":
        return True
    else:
        return False
    
@user_passes_test(librarian_test)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')




@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    return render(request, 'edit_book.html')

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    return render(request, 'confirm_delete.html')

