from django import forms
from ordersapp.models import Order, OrderItem
from mainapp.models import Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # exclude = ('user', 'status')
        fields = []

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

    price = forms.CharField(label='цена', required=False, disabled=True)
    # result_price = forms.CharField(label='итого', required=False, disabled=True)


    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.active_items()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
