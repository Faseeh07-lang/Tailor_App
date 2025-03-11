from django import forms
from .models import Customer,Order_details,Size,Billing
from django.forms import modelformset_factory

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'address', 'number_of_suits']        
 
class Order_detailsForm(forms.ModelForm):
    class Meta:
        model= Order_details
        fields=['customer','given_date','delivery_date','status']
class SizeForm(forms.ModelForm):
    class Meta:
        model=Size
        fields = ['color', 'type', 'waist', 'sleeve_length', 'neck', 'shoulder_length', 'chest', 'suit_length', 'sleeve_width', 'shalwar_length']

SizeFormSet = modelformset_factory(Size, form=SizeForm, extra=1)

"""       
class Billing(forms.ModelForm):
    class Meta:
        model=Billing
        fields=['customer','suit_price','total_amount','payment_status','payment_method','transaction_date']         
     """             