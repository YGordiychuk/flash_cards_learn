from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs=
                                   {'class':'form-control',
                                    'placeholder':'Enter title of card'
                                    }),
            "description": Textarea(attrs=
                                    {'class':'form-control',
                                    'placeholder':'Enter description of card'
                                    }),
            }