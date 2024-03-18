from django import forms


class OnlineExamForm(forms.Forms):
    name = forms.CharField(max_length=100, required=True, label="Enter your Name")
    age = forms.IntegerField(min_vaue=18, label="Enter your age")
    check = forms.BooleanField(required=False, label="Do you wnt to join us")
    check = forms.ChoiceField(choices=[('student', 'student'), ('teacher', 'teacher'), ('Administrator', 'Administrator')])

