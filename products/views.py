from django.views.generic import ListView, DetailView
from django.db.models import Q

from products.models import Casa
from products.filters import CasaFilter, ListCasaFilter


class CasaListView(ListView):
    template_name = 'products/casa-list.html'
    context_object_name = 'casas' 
    queryset = Casa.objects.all()

    # list of objects for display
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ListCasaFilter(self.request.GET, queryset=queryset)

        if self.request.GET:
            queryset = Casa.objects.filter(
                Q(category__contains=self.request.GET['category']) &
                Q(city__contains=self.request.GET['city']),
                #Q(price__lte=self.request.GET['price']),
                )
            return queryset

        return queryset

    # populate dictionary for template context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form 
        return context


class CasaDetailView(DetailView):
    model = Casa
    template_name = "products/casa-detail.html"


class HomeSearchView(ListView):
    model = Casa
    template_name = "products/casa-search.html"
    context_object_name = 'casas'

    # list of objects for display
    def get_queryset(self):

        if self.request.GET['id']:
            queryset = Casa.objects.filter(pk=self.request.GET['id'])
            return queryset
    
        if self.request.GET['category']:
            queryset = Casa.objects.filter(
                Q(category__contains=self.request.GET['category']) &
                Q(city__contains=self.request.GET['city']) &
                Q(price__lte=self.request.GET['price']),
                )
        
        if self.request.GET['city']:
            queryset = Casa.objects.filter(
                Q(category__contains=self.request.GET['category']) &
                Q(city__contains=self.request.GET['city']) &
                Q(price__lte=self.request.GET['price']),
                )        

        if self.request.GET['price']:
            queryset = Casa.objects.filter(
                Q(category__contains=self.request.GET['category']) &
                Q(city__contains=self.request.GET['city']) &
                Q(price__lte=self.request.GET['price']),
                )

        return queryset