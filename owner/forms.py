# from django import forms
# class EmpForm(forms.Form):
#     employee_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     experience=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     salary=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     def clean(self):
#         cleaned_data=super().clean()
#         salary=cleaned_data.get("salary")
#         if int(salary)<0:
#             msg="please enter a valid salary"
#             self.add_error("salary",msg)




# Simple method
from django import forms
from owner.models import EmpModels
class EmpForm(forms.ModelForm):
    class Meta:
        model=EmpModels
        fields="__all__"
        widgets={
            "employee_name":forms.TextInput(attrs={"class":"form-control"}),
            "designation":forms.TextInput(attrs={"class":"form-control"}),
            "experience":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
        }


