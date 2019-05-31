from django import forms

from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'type': 'email',
            'class': "form-control",
            'placeholder': "Enter email...",
            'aria-label': "Enter email...",
            'aria-describedby':"basic-addon",
        }),
        label=""
    )
    class Meta:
        model = Subscription
        fields = ('email', )