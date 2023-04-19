from django.shortcuts import render
from .models import Message
from django.template.loader import get_template
import datetime
from django.core.mail import EmailMultiAlternatives
from contact.forms.forms import ContactForm

def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'succes': 1}
            bd_message = Message()
            bd_message.name = form.cleaned_data['name']
            bd_message.email = form.cleaned_data['email']
            bd_message.message = form.cleaned_data['message']
            bd_message.issued = datetime.datetime.now()

            bd_message.save()
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'contact/contact.html', context=context)

def send_message(name, email, message):
    text = get_template('shop/message.html')
    html = get_template('shop/message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Message from user'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = text.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
