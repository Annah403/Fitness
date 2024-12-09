import os.path

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from fitness.forms import ExerciseForm, ContactForm
from fitness.models import Exercise


# Create your views here.
def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, 'index.html')

@login_required
def about(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_services')
    else:
        form = ExerciseForm()

    return render(request, 'about.html', {'form': form, 'section': 'about'})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the data to the database
            form.save()
            return redirect('contact')  # Redirect to a thank you page or success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



def services(request):
    data = Exercise.objects.all()
    context = {'data': data}
    return render(request, 'services.html', context)


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

# def login_user(request):
#     if request.method == 'POST':
#         # Get username and password from the form
#         username = request.POST['username']
#         password = request.POST['password']
#
#         # Authenticate the user
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             # If the user is authenticated, log them in
#             login(request, user)
#             return redirect('about')  # Redirect to a homepage or a logged-in page
#         else:
#             # If authentication fails, show an error message
#             messages.error(request, 'Invalid username or password')
#
#     return render(request, 'login.html')

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        # Create a new UserCreationForm instance with POST data
        form = UserCreationForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save the user to the database
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('about')


        else:
            # If the form is not valid, render the form with error messages
            messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        # If the request is GET, show an empty form
        form = UserCreationForm()


    return render(request, 'register.html', {'form': form})

def admin_services(request):
    data = Exercise.objects.all()
    context = {'data': data}
    return render(request, 'admin_services.html', context)



def delete(request,id):
    exercise = get_object_or_404(Exercise,id=id)

    try:
        exercise.delete()
        messages.success(request, 'Exercise deleted successfully!')
    except Exception as e:
        messages.error(request, 'Exercise not deleted')
    return redirect('admin_services')

def update(request,id):
    exercise = get_object_or_404(Exercise, id=id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            form.save()

            if 'image' in request.FILES:
                file_name = os.path.basename(request.FILES['image'].name)
                messages.success(request, f'Exercise updated successfully! {file_name} uploaded')
            else:
                messages.error(request, 'Exercise details updated successfully')
            return redirect('admin_services')
        else:
            messages.error(request, 'Please confirm your changes')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'update.html',{'form':form,'customer':exercise})


