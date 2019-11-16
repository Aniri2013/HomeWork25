from django import forms

class RoomsForm(forms.Form):
    Number = forms.IntegerField(min_value=1, max_value=1000)
    Name_Student = forms.IntegerField(min_value=1, max_value=100)
    Last_nameStudent = forms.IntegerField(min_value=1, max_value=5)
    count_resident = forms.IntegerField(min_value=1, max_value=5)