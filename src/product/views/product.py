from django.views import generic
from datetime import datetime
from django.urls import reverse_lazy

from product.models import Product,ProductImage,ProductVariant,ProductVariantPrice,Variant
from product.filters import ProductFilter

class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.method == "GET":
            product_title = self.request.GET.get('title')
            product_variant = self.request.GET.get('variant')
            price_from = self.request.GET.get('price_from')
            price_to = self.request.GET.get('price_to')
            product_created_date = self.request.GET.get('date')
            #print("\n\n\n")
            #print()
            #print("\n\n\n")
            if product_title:
                queryset = queryset.filter(title__icontains = product_title)
            if product_created_date:
                queryset = queryset.filter(created_at__icontains= product_created_date)
            if price_from:
                queryset = queryset.filter(productvariantprice__price__gte=price_from)
            if price_to:
                queryset = queryset.filter(productvariantprice__price__lte=price_to)
            if product_variant:
                queryset = queryset.filter(productvariant__variant_title__icontains=product_variant)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        variants = ProductVariant.objects.all().values('id', 'variant_title').distinct()
        context['variants'] = list(variants.all().distinct())
        return context
    #extra_context = 'filter' 
'''
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        f = ProductFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = f
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.method == "GET":
            f = ProductFilter(self.request.GET, queryset=queryset)
            queryset = f.qs
        return queryset
'''


class ProductEditView(generic.UpdateView):
    model = Product
    fields = ["title","description","sku"]
    exclude = ('created_at','updated_at')
    success_url =reverse_lazy('product:list.product')
    template_name = 'products/update.html'


