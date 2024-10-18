from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('home')  # Replace with your desired redirect after registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {'form': form})


def home(request):
    return render(request, 'blog/home.html')

@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})