import django_filters

from product.models import Product

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    gt_price = django_filters.NumberFilter(field_name='productvariantprice__price', lookup_expr='gt')
    lt_price = django_filters.NumberFilter(field_name='productvariantprice__price', lookup_expr='lt')
    d_date = django_filters.DateFilter(field_name='created_at', lookup_expr='contains')
    variant_choice = django_filters.CharFilter(field_name='productvariant__title', lookup_expr='icontains')
    #variant = django_filters.ChoiceFilter(choices=productvariant__set.all(),null_label='Any',lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['title', 'gt_price','lt_price','d_date','variant_choice']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(ProductFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['title'].field.widget.attrs.update({'class': 'col-md-2'})
        self.filters['gt_price'].field.widget.attrs.update({'class': 'col-md-2'})
        self.filters['lt_price'].field.widget.attrs.update({'class': 'col-md-2'})
        self.filters['d_date'].field.widget.attrs.update({'class': 'col-md-2'})
        self.filters['variant_choice'].field.widget.attrs.update({'class': 'col-md-2'})