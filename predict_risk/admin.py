from django.contrib import admin
from predict_risk.models import Predictions
from django import forms

class Prediction(admin.ModelAdmin):
    list_display=('profile','sr','rr','bt','lm','blood_ol','em','sh','hr')
admin.site.register(Predictions,Prediction)
# Register your models here.
