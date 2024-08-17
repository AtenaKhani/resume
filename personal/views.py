from django.http import HttpResponseNotFound
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .form import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render


def dynamic_template_view(request, template_name):
    valid_templates = [
        'parent/base.html',
        'personal/services.html',
        'personal/resume.html',
        'personal/about.html',
        'personal/portfolio.html',
        'personal/index.html',
        'personal/service-details.html',
        'personal/portfolio-details.html',
    ]
    if template_name in valid_templates:
        return render(request, template_name)
    return HttpResponseNotFound("Page not found")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject,
                message,
                email,
                ['contact@example.com'],
                fail_silently=False,
            )
            # return render(request, 'personal/contact.html', {'form': form})
            return redirect("personal:index")
            # return render(request, '/contact.html', {'form': form})

    else:
        form = ContactForm()

    return render(request, 'personal/contact.html', {'form': form})

