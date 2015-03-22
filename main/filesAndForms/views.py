from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView

from filesAndForms.forms import InputForm
from filesAndForms.models import InputFile

def list(request):
	if request.method == 'POST':
		form = InputForm(request.POST, request.FILES)
		if form.is_valid():
			newfile = InputFile(input = request.FILES['input'])
			newfile.save()

			return HttpResponseRedirect(reverse('filesAndForms.views.list'))
	else:
		form = InputForm()

	inputs = InputFile.objects.all()

	return render(request, 'filesAndForms/list.html', {'inputs' : inputs, 'form' : form})
