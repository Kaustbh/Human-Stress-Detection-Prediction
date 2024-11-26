from django.db import models
from accounts.models import UserProfileInfo,ConcreteUserProfile
from django.utils import timezone
from django.urls import reverse
 
class Predictions(models.Model):
    profile = models.ForeignKey(ConcreteUserProfile, on_delete=models.CASCADE, related_name='predict')
    sr = models.IntegerField(blank=True, null=True)
    rr = models.IntegerField(blank=True, null=True)
    bt = models.IntegerField(blank=True, null=True)
    lm = models.IntegerField(blank=True, null=True)
    blood_ol = models.IntegerField(blank=True, null=True)
    em = models.IntegerField(blank=True, null=True)
    sh = models.IntegerField(blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('predict:predict', kwargs={'pk': self.profile.pk})
