from django.shortcuts import render,redirect
from django.conf import settings as set
from bodhi.models import carousel,services,clients,about
from django.contrib import messages
from django.conf import settings as conf_set
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from bodhi.forms import ContactForm
from socket import gaierror
from smtplib import SMTPAuthenticationError, SMTPDataError
btech=set.CNAME

# Create your views here.
def homepage(request):
    return render(request,"layout/welayout.html")

def bodhi_homepage(request):
    page_title="index_page"
    text="N.K.orchid College"
    very_first=btech
    first="Why you choose Us?"
    second="our Clients"
    third="about us"
    car=carousel.objects.all()
    ser=services.objects.all()
    cli=clients.objects.all()
    ab=about.objects.all()



    context={'title':page_title,
            'text':text,
            'first_title':very_first,
            'second_title':first,
            'third_title':second,
            'fourth_title':third,
            'fifth_title':btech,
            'carousel':car,
            'services':ser,
            'clients':cli,
            'about':ab,

            
            }
    
    return render(request,"webpages/my_index.html",context)

#{'testme':page_title}

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            person_name_f=form.cleaned_data['f_name']
            person_name_l=form.cleaned_data['l_name']
            user_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            user_mobile=form.cleaned_data['mobile_no']
            message_send="\n Fname:"+person_name_f+"\n Lname:"+person_name_l+"\n Email:"+user_email+"\n Mob : "+user_mobile+"\n sub:"+subject
            from_email=conf_set.EMAIL_HOST_USER
            try:
                send_mail(subject,message_send,from_email, ['mayurirathod619@gamil.com'])
            except (BadHeaderError,gaierror,SMTPAuthenticationError,SMTPDataError):
                messages.error(request,"Check your Internet connection... Try again")
                return redirect('contact_mayuri')
            messages.success(request,"Thank you for contacting school! Your form successfully submited")
            return redirect('contact_mayuri')

    context={
        'form':form,
        }
    return render(request,"webpages/contact.html",context)