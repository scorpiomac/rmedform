from django.contrib import admin

from .views import multistepformexample
from .models import information
from .models import multistepformexample
from .models import Fiche
from .views import createpost




class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name','firstname', 'message','message2', 'email')

admin.site.register(information, RegistrationAdmin)

# Register your models here.
class  RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    #list_display = admin._meta.get_all_field_names()

#admin.site.register(multistepformexample, RegistrationAdmin)


class  RegistrationAdmi(admin.ModelAdmin):
    #
    list_display  = [f.name for f in Fiche._meta.fields]
    # list_display = ('nom','prenom')
    #list_display = RegistrationAdmin._meta.get_all_field_names()


admin.site.register(Fiche, RegistrationAdmi)