from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from .models import Order, UserMain


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        labels = {
            'email': 'Email:',
        }