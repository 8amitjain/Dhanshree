from django.db import models
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import reverse


class NewsLetter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.email}"

    def get_absolute_url(self):  # Redirect to this link after adding review
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    mobile = models.IntegerField()
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.name}_{self.mobile}"

    def get_absolute_url(self):  # Redirect to this link after adding review
        return reverse("admin-contact")
