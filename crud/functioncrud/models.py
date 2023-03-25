from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

from django.contrib.auth.models import User

class Food(models.Model):
    person = models.ForeignKey(User, verbose_name=_("Person"), on_delete=models.CASCADE)
    food_name = models.CharField(_("Food"), max_length=100)
    quantity = models.PositiveIntegerField(_("Quantity"))
    calories = models.DecimalField(_("Calories"), max_digits=5, decimal_places=2)
    image = models.ImageField(_("Food Image"), upload_to='food/images', height_field=100, width_field=100, max_length=None)

    @property
    def total_calories(self):
        return self.calories * self.quantity