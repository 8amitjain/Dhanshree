from django import forms


class SendBulkMailForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)

