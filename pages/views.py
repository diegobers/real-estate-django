from django.views.generic import ListView

from products.models import Casa
from products.filters import CasaFilter


class IndexView(ListView):
    model = Casa
    template_name = "pages/index.html"
    context_object_name = 'casas'

    # list of objects for display
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CasaFilter(self.request.GET, queryset=queryset)
        return self.queryset

    # populate dictionary for template context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form 
        return context