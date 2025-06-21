from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.conf import settings

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class LanderPageView(TemplateView):
    template_name = 'pages/lander.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'



class TestTemplateView(View):
    def get(self, request):
        return render(request, 'pages/test.html')
    


@login_required
def test_email_view(request):
    try:
        send_mail(
            subject="test-email.txt",
            message = render_to_string("emails/test-email.txt"),
            from_email="mork@foxxelabs.com",
            recipient_list=["todd@toddwriter.com"],
            fail_silently=False,
        )
        return HttpResponse(f"✅ Email sent successfully using backend: {settings.EMAIL_BACKEND}")

    except Exception as e:
        return HttpResponse(f"❌ Email failed: {str(e)}", status=500)
