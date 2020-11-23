from django.db.models import TextChoices, IntegerChoices


class Gender(TextChoices):
    MALE = 'male', 'Male'
    FEMALE = 'female', 'Female'


class MaritalStatus(IntegerChoices):
    SINGLE = 1, 'Single'
    MARRIED = 2, 'Married'
    WIDOWED = 3, 'Widowed'
    DIVORCED = 4, 'Divorced'