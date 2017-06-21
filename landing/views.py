from django.shortcuts import render
from .forms import SubcriberForm

# Create your views here.
def landing(request):
    form = SubcriberForm(request.POST or None)
    if request.POST and form.is_valid():
        print(request.POST)
        data = form.cleaned_data
        print(data['name'])
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())