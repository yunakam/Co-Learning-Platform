from django.forms import ModelForm, Textarea, CharField, ValidationError
from .models import Question, Answer
from django.core.exceptions import ValidationError


class PostQuestion(ModelForm):
    class Meta:
        model = Question
        fields = ('text',)
        labels = {'text': 'Make sure your question requires a formative response.',}
        widgets = {
            'text': Textarea(attrs={
                'class': "form-control",
                # 'style': 'max-width: 300px;',
                'rows':2, 'cols':15,
                'placeholder': 'Add your original question'
                }),
        }

    def clean_text(self, *args, **kwargs):
        text = self.cleaned_data.get("text")
        if len(text) < 10:
            if text.startswith("Define" or "What is"):
                return text
            else:
                raise ValidationError('Question is too short')
        else:
            return text
            # self.is_valid = True


class PostAnswer(ModelForm):
    class Meta:
        model = Answer
        fields = ('text',)
        labels = {'text': '',}
        widgets = {
            'text': Textarea(attrs={
            'class': "form-control",
            'rows':4,
            'placeholder': 'Your answer here'
            }),
        }

    def clean_text(self, *args, **kwargs):
        text = self.cleaned_data.get("text")
        if len(text) < 15:
            raise ValidationError('Your answer is too short')
        else:
            # self.is_valid
            return text
 
