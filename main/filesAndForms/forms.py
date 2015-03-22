from django import forms

class InputForm(forms.Form):
	name = forms.CharField(label = 'Username:', max_length=100)
	location = forms.CharField(label = 'Location of Incident:', max_length=500, required=False)
	time = forms.DateTimeField(label = 'Time of Incident:', required=False, input_formats = ['%m/%d/%Y', '%m/%d/%y'], help_text='format is like: 12/20/2014')
	desc = forms.CharField(label= 'Incident Description:', widget=forms.Textarea)
	privacy = forms.BooleanField(label = 'Is this a private report?')
	alt_privacy = forms.ChoiceField(label = 'Select privacy setting', choices=(('Private', 'PRIVATE'), ('Public','PUBLIC'),), required=False)
	input = forms.FileField(label = 'Select a file to upload')
	next_one = forms.FileField(label = 'input a second file')

	


