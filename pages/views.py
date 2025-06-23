from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.conf import settings

import requests
from django.shortcuts import render

import requests
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_docker_banner'] = getattr(settings, "SHOW_DOCKER_BANNER", False)
        try:
            resp = requests.get("https://zenquotes.io/api/random", timeout=3)
            #print("got quote", resp.json())
            quotes = resp.json()
            quote = quotes[0] if quotes else {}
            #print("quote", quote)
            #print("quote.get('q')", quote.get('q'))
            context['quote_text'] = quote.get('q', "Keep going. Everything you need will come to you.")
            context['quote_author'] = quote.get('a', "Unknown")
        except Exception:
            context['quote_text'] = "Keep going. Everything you need will come to you."
            context['quote_author'] = "Unknown"
        return context


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
