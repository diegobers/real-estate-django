from django.views.generic import ListView

from products.models import Casa


class IndexView(ListView):
    template_name = "pages/index.html"
    context_object_name = "casas_list_index"

    def get_queryset(self):
        return Casa.objects.all()[:3]
