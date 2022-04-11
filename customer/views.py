from django.shortcuts import render,redirect
from owner.models import EmpModels
from django.views.generic import View
from customer.forms import UserRegistrationForm,LoginForm,PasswordResetForm
from django.contrib.auth import authenticate    #for checking the password is matching
from django.contrib.auth import login
from django.contrib.auth import logout



# Create your views here.
class CustomerIndex(View):
    def get(self, request, *args, **kwargs):
        qs = EmpModels.objects.all()
        return render(request, 'custhome.html', {"employees": qs})

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm
        return render(request,"signup.html",{"form":form})
    def  post(self,request):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return render(request,'signup.html', {"form": form})
class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"signin.html", {"form": form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)  # here we are using usermodel
            if user:
                print("Login success")
                login(request,user)   #evidanaano orru user nithiyathu anghoddu thirichu konddu pokkum
                return redirect("employee_home")

            else:
                print("Login failed")
            return render(request,"signin.html",{"form":form})
def signout(request):
    logout(request)
    return redirect("signin")

class PasswordResetView(View):
    def get(self,request,*args,**kwargs):
        form=PasswordResetForm
        return render(request,"password_reset_form.html",{"form":form})
    def post(self,request):
        form=PasswordResetForm(request.POST)
        if form.is_valid():
            old_password=form.cleaned_data.get("old_password")
            new_password=form.cleaned_data.get("new_password")
            user=authenticate(request,username=request.user,password=old_password)
            if user:
                user.set_password(new_password)
                user.save()
                return redirect("signin")
            else:
                return render(request,"password_reset_form.html",{"form":form})
        return render(request, "password_reset_form.html", {"form": form})







