
from .forms import NewsLetterForm


def news_form(request):
    form2 = NewsLetterForm()
    return {form2: 'form2'}
