from django.contrib import admin

from churches.models import Church, Person, Family, Membership


admin.site.register(Church)
admin.site.register(Person)
admin.site.register(Family)
admin.site.register(Membership)
