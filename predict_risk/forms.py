from django import forms
from predict_risk.models import Predictions

class Predict_Form(forms.ModelForm):
    class Meta:
        model = Predictions
        fields = ('sr','rr','bt','lm','blood_ol','em','sh','hr')
        widgets = {'sr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter snoring rate'}),
                   'rr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Respiratory rate'}),
                   'bt': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter  Body temperature'}),
                   'lm':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Limb movement'}),
                   'blood_ol':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Blood oxygen level'}),
                   'em':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Eye movement'}),
                   'sh':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Sleep Hours'}),
                   'hr':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Heart rate'}),
                   }
