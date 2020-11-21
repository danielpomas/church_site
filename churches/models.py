from django.conf import settings
from django.db import models

from django_countries.fields import CountryField


class ChurchQuerySet(models.query.QuerySet):
    def is_member(self, user):
        return self.filter(members=user)


class ChurchManager(models.Manager):
    def get_queryset(self):
        return ChurchQuerySet(self.model, using=self._db)

    def get_member_churches(self, user):
        return self.filter(members=user)


class Church(models.Model):
    name = models.CharField(max_length=200, unique=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province_state = models.CharField(max_length=50)
    country = CountryField()

    mixlr_url = models.URLField(null=True, blank=True)

    objects = ChurchManager()

    @property
    def slug(self):
        return self.name.replace(' ', '-')

    class Meta:
        ordering = ('country', 'name')

    def __str__(self):
        return self.name


class Person(models.Model):

    class Gender(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    class MaritalStatus(models.IntegerChoices):
        SINGLE = 1, 'Single'
        MARRIED = 2, 'Married'
        WIDOWED = 3, 'Widowed'
        DIVORCED = 4, 'Divorced'

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=100)
    second_last_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    date_of_birth = models.DateField(blank=True, null=True)
    contact_number = models.CharField(max_length=30, null=True, blank=True)
    marital_status = models.IntegerField(MaritalStatus.choices)
    is_speaker = models.BooleanField(default=False)  # Will person appear in speaker list
    # Address
    street_address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50)
    Country = CountryField()

    child_of = models.ForeignKey('Family', on_delete=models.PROTECT, related_name='children', blank=True, null=True)
    user_account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='person',
                                        blank=True, null=True)
    # TODO: need to add sermon connection
    # TODO: need to add stream connection

    def __str__(self):
        if self.second_last_name:
            return f"{self.first_name} {self.last_name} {self.second_last_name}"
        else:
            return f"{self.first_name} {self.last_name}"


class Family(models.Model):
    father = models.OneToOneField('Person', on_delete=models.PROTECT, related_name='father_of')
    mother = models.OneToOneField('Person', on_delete=models.PROTECT, related_name='mother_of')

    def __str__(self):
        return f"{self.father.first_name} & {self.mother.first_name} {self.father.last_name}"


class Membership(models.Model):
    member = models.ForeignKey('Person', on_delete=models.PROTECT, related_name='membership')
    church = models.ForeignKey('Church', on_delete=models.PROTECT, related_name='memberships')
    start_date = models.DateField(null=True, blank=True)
    reason_for_joining = models.TextField(null=True, blank=True)
    biblical_verse = models.TextField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    reason_for_leaving = models.TextField(null=True, blank=True)
    is_member = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.church} - {self.member}"
