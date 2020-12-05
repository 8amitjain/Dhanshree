
from .forms import NewsLetterForm
from .filters import ProductSearchFilter
from products.model import Product


def news_form(request):
    form2 = NewsLetterForm()
    return {form2: 'form2'}


def product_filter(request):
    context = {}
    current_query = Product.objects.all()
    product_search_filter = ProductSearchFilter(request.GET, queryset=current_query)

    context['filter'] = product_search_filter
    # context['object_list'] = product_search_filter.qs
    return context
