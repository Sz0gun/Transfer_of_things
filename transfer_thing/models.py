from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

TYPE_CHOISES = (
    (1, 'fundacja'),
    (2, 'organizacja pozarowa'),
    (3, 'zbiórka lokalna')
)


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOISES, default=1)
    categories = models.ManyToManyField(Category, related_name='category')

    def get_categories(self):
        return ', '.join([c.name for c in self.categories.all()])
    

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='donation_category')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    street = models.TextField()
    phone = PhoneNumberField()
    city = models.CharField(_("city"), max_length=64)
    zip_code = models.CharField(_("zip_code"), max_length=5)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, default=None)
        # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
        #                              message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        # phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)