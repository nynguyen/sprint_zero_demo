from django import forms

class InputForm(forms.Form):
	input = forms.FileField(label = 'Select a file to upload')


