from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView

from filesAndForms.forms import InputForm
from filesAndForms.models import InputFile

def list(request):

	# take this away if you actually want memory of your files
	# if you keep this, it will delete all of the files that you used to
	# have listed
	#InputFile.objects.all().delete() # terribly unintended behavior
	
	if request.method == 'POST':
		form = InputForm(request.POST, request.FILES)
		if form.is_valid():
		# don't try to iterate over request.FILES
			newfile = InputFile(input = request.FILES['input'])
			newfile.next_one = request.FILES['next_one']
			newfile.name = request.POST['name']
			newfile.privacy = request.POST['privacy']
			newfile.save()
			return HttpResponseRedirect(reverse('filesAndForms.views.list'))
	else:
		form = InputForm()

	inputs = InputFile.objects.all()

	return render(request, 'filesAndForms/list.html', {'inputs' : inputs, 'form' : form})
