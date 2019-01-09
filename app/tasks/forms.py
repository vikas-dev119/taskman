from django import forms


class AddTaskForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'autocomplete':'off','placeholder':'Name', 'class':'form-control'}))
    deadline_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
