from django.views.generic import ListView, DetailView

from products.models import Casa


class CasaListView(ListView):
    model = Casa
    template_name = 'products/casa-list.html'
    context_object_name = 'casas'

class CasaDetailView(DetailView):
    model = Casa
    template_name = "products/casa-detail.html"