from EmployeeModule.models import Employee
from django import forms
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fullname', 'email', 'emp_code', 'mobile_no', 'position']