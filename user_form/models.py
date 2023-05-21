from django.core.exceptions import ValidationError
from django.db import models
import re

def validate_phone_number(value):
    pattern = r"^(?:(?:\+|0{0,2})91(\s*[-]\s*)?|[0]?)?[6789]\d{9}$"  # Modify the pattern to match your desired phone number format
    if not re.match(pattern, value):
        raise ValidationError('Invalid phone number.')

class UserForm(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, validators=[validate_phone_number] ,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
