from django import forms
from django.contrib.auth import get_user_model
from .models import Contact

User = get_user_model()

class ContactForm(forms.ModelForm):
        name = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        # "class": "form-control", 
                        "placeholder": "Your full name",
                    }
                    )
            )
        email    = forms.EmailField(
       
            widget=forms.EmailInput(
                    attrs={
                        # "class": "form-control", 
                        "placeholder": "Your email"
                    }
                    )
            )
        content  = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class': 'materialize-textarea',
                    "placeholder": "Your message" 
                    }
                )
            )

        class Meta:
                model = Contact
                fields = ('name', 'email', 'content')
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError("Email has to be gmail.com")
    #     return email

    # def clean_content(self):
    #     raise forms.ValidationError("Content is wrong.")