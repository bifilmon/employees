from django.shortcuts import render,redirect
from owner.forms import EmpForm
from django.views.generic import View
from owner.models import EmpModels
class Empview(View):
    def get(self,request):
        form=EmpForm()
        return render(request,"emp_add.html",{"form":form})
    def post(self,request):
        form=EmpForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data.get("employee_name"))# here cleaned_data is used to get a dictionary
            # print(form.cleaned_data.get("designation"))
            # print(form.cleaned_data.get("experience"))
            # print(form.cleaned_data.get("salary"))
            # qs=EmpModels(
            #     employee_name=form.cleaned_data.get("employee_name"),
            #     designation=form.cleaned_data.get("designation"),
            #     experience=form.cleaned_data.get("experience"),
            #     salary=form.cleaned_data.get("salary")
            # )
            # qs.save()
            # return render(request,"emp_add.html",{"msg":"Employee list is created"})# here it will be saved in the server
            return redirect("Employee_list")
        else:
            return render(request,"emp_add.html",{"form":form})# here it will return to the form
class EmployeeList(View):
    def get(self,request):
        qs=EmpModels.objects.all()
        return render(request,"emp_list.html",{"employors":qs})

class EmpDetailView(View):
    def get(self,request,*args,**kwargs):# we could add many arguments
        # pass
            # kwargs={'id'=3}
        qs=EmpModels.objects.get(id=kwargs.get("id"))
        return render(request,"emp_details.html",{'employee':qs})

class EmpDeleteView(View):
    def get(self,request,*args,**kwargs):
        qs=EmpModels.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("Employee_list")

class EmpEditView(View):
    def get(self,request,*args,**kwargs):
        qs=EmpModels.objects.get(id=kwargs.get("id"))
        form=EmpForm(instance=qs)
        return render(request,"emp_edit.html", {"form": form})
    def post(self,request,*args,**kwargs):
        qs=EmpModels.objects.get(id=kwargs.get("id"))
        form=EmpForm(request.POST,instance=qs,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Employee_list")


