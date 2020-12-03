from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic.edit import CreateView
from .forms import NewsLetterForm
from .models import Contact


class NewsLetterCreateView(View):
    def get(self, *args, **kwargs):
        form2 = NewsLetterForm()
        return render(self.request, 'home/home.html', {'form2': form2})

    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            form = NewsLetterForm(self.request.POST)
            if form.is_valid:
                form.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class ContactView(CreateView):
    model = Contact
    fields = ['name', 'email', 'mobile', 'description']
    template_name = "home/contact.html"
    success_url = '/contact/'

    def form_valid(self, form):
        phone_number = form.cleaned_data['mobile']
        if len(str(phone_number)) != 10:
            messages.warning(self.request, 'Invalid mobile number')
            return redirect('contact')
        messages.success(self.request, 'Message sent you will be contact soon!')
        return super().form_valid(form)

