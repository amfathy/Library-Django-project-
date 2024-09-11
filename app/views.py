from app.decorators import unauthenticated_user
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from . decorators import *
# Create your views here.

def admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'you have loggedin success')
            return redirect('adminhome')
        else:
            messages.success(request, 'Error loggin in....')
            return redirect('adminn')

    else:
        return render(request, 'pages/admin.html', {})


@login_required(login_url = 'login')
def borrow(request):
    return render(request, 'pages/borrow.html')


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'you have loggedin success')
            return redirect('profile')
        else:
            messages.success(request, 'Error loggin in....')
            return redirect('/')

    else:
        return render(request, 'pages/home.html', {})


@login_required(login_url = 'login')
def period(request):
    return render(request, 'pages/period.html')

@login_required(login_url = 'login')
@student_profile
def profile(request):
    return render(request, 'pages/profile.html')


@login_required(login_url = 'login')
def showbooks(request):
    results = Book.objects.all()

    if request.method == "GET":

        query = request.GET.get('search')

        if query:
            results = Book.objects.filter(Q(publication_year__icontains=query) | Q(author__icontains=query) | Q(ISBN__icontains=query) )
    books ={
        'book' : results
    }
    return render(request, 'pages/showbooks.html', books)


@unauthenticated_user
def signup(request):
    return render(request, 'pages/signupOptions.html')
    

@login_required(login_url = 'login')
def updateform(request):
    if request.method == "POST":
        u_form = UpdateUserForm(request.POST, instance = request.user)
        p_form = PasswordUpdateForm(data = request.POST, user = request.user)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            update_session_auth_hash(request, p_form.user)
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            return redirect('updateform')
    else:
        u_form = UpdateUserForm(instance = request.user)
        p_form = PasswordUpdateForm(user = request.user)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'pages/updateform.html', context)




@login_required(login_url = 'login')
@allowed_user(allowed_roles=['admin'])
def addBook(request):
    bookForm = BookForm()
    if request.method == "POST":
        bookForm = BookForm(request.POST)
        if bookForm.is_valid():
            bookForm.save()
            return redirect('showbooks')
    context = {'bookForm' : bookForm}
    return render(request, 'pages/addBook.html', context)


@login_required(login_url = 'login')
@allowed_user(allowed_roles=['admin'])
def adminhome(request):
    return render(request, 'pages/adminHome.html')



@login_required(login_url = 'login')
@allowed_user(allowed_roles=['admin'])
def updateBook(request, id):  
    book_id = Book.objects.get(id = id)
    if request.method == 'POST':
        bookform = BookForm(request.POST, request.FILES, instance=book_id)
        if bookform.is_valid():
            bookform.save()
            return redirect('showbooks')
    else:
        bookform = BookForm(instance=book_id)
    context ={'updateform': bookform}
    return render(request, 'pages/UpdateBook.html', context)



@login_required(login_url = 'login')
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out...')
    return redirect('/')


@unauthenticated_user
def studentsignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            group = Group.objects.get(name = 'student')
            user.groups.add(group)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'registration successfull....')
            return redirect('profile')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'pages/Signup.html', context)

@unauthenticated_user
def adminsignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            group = Group.objects.get(name = 'admin')
            user.groups.add(group)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'registration successfull....')
            return redirect('adminhome')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'pages/Signup.html', context)


@login_required 
def search(request):
    return render(request, 'pages/search.html')

