from django.shortcuts import render
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

#our Logic
def contact(request):
    form_class = ContactForm

    #new logic
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            #email the profile with the contact information
            template = get_template('contact_template.txt')

            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,

            })
            context = template.render(context)

            email = EmailMessage(
                'New contact form submission',
                context,
                'Your website <hi@weddinglovely.com>',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return render('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
