from django.db import models

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30, min_length=2)
    last_name = models.CharField(max_length=30, min_length=2)
    age = models.IntegerField(validators=[models.MaxValidator(99)])
    city = models.CharField(max_length=100)
    date_of_joining = models.DateField(validators=[models.DateValidator(min_value='1950-01-01')])

    def clean(self):
        if self.age >= 100:
            raise models.ValidationError("Age must be less than 100.")
        if len(self.first_name) <= 1:
            raise models.ValidationError("First name must be longer than 1 character.")
        if len(self.last_name) <= 1:
            raise models.ValidationError("Last name must be longer than 1 character.")
