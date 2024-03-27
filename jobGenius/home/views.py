from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Job
from .forms import JobForm , JobSearchForm,HomeSearchForm
from django.db.models import Q 

@login_required(login_url='login')
def user_dashboard(request):
    return render(request, 'dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    jobs = Job.objects.all()

    # Handle search query
    search_form = HomeSearchForm(request.GET)
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        if search_query:
            jobs = jobs.filter(
                Q(title__icontains=search_query) |
                Q(location__icontains=search_query) |
                Q(company__icontains=search_query)
            )

    context = {'jobs': jobs, 'search_form': search_form}
    return render(request, 'index.html', context)
def signUp(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(response, "signUp.html", {"form":form})



def logIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Logged in as {username}')
                return redirect('home')  # Redirect to your home page
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request, 'logIn.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')   

def about(request):
    return render(request, 'about.html')   

def job_list(request):
    jobs = Job.objects.all()

    # Handle search query
    search_form = JobSearchForm(request.GET)
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        if search_query:
            jobs = jobs.filter(
                Q(title__icontains=search_query) |
                Q(location__icontains=search_query) |
                Q(company__icontains=search_query)
            )

    context = {'jobs': jobs, 'search_form': search_form}
    return render(request, 'jobs.html', context)

@login_required(login_url='login')
def publish_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user 
            job.save()
            return redirect('publish') 
    else:
        form = JobForm()

    return render(request, 'publish.html', {'form': form})


def job_details(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'job_details.html', {'job': job})


@login_required(login_url='login')
def apply_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    # Add logic for job application here
    # For example, you can save the application in the database
    # or redirect to an external application form
    return render(request, 'apply_job.html', {'job': job})