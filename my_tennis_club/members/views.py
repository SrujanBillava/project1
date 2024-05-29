from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from django.urls import reverse # type: ignore
from django.template import loader # type: ignore
from .models import Member
from .forms import ContactModelForm


def members(request):
    return render(request, 'members/myfirst.html')

def allmembers(request):
    mymembers = Member.objects.all().values()
    context = {
    'mymembers': mymembers,
    }
    return render(request, 'members/all_members.html', context)

def details(request, id):
    mymember = Member.objects.get(id=id) # type: ignore
    context = {
        'mymember': mymember,
    }
    return render(request, 'members/details.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the model
            return redirect(reverse('contact_success'))  # Redirect to a success page
    else:
        form = ContactModelForm()
    return render(request, 'contact.html', {'form': form})


def contact_success_view(request):
    return render(request, 'success.html')