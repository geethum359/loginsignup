from bookapp.models import book
from django.forms import ModelForm

class bookform(ModelForm):
    class Meta:
        model=book
        fields='__all__'