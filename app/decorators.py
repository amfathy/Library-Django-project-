from django.http import HttpResponse
from django.shortcuts import redirect

#If a user is logged in we'll restrict them from seeing login page or sign up
def unauthenticated_user(view_func):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_fun


#we will use groups, passing a list as a parameter so a single page allows multiple kinds of users
def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_fun(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")
        return wrapper_fun
    return decorator

def student_profile(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == "admin":
            return redirect('adminhome')
            
        if group == "student":
            return view_func(request, *args, *kwargs)
    return wrapper_func
        