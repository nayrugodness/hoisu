from django.contrib import admin
from .models import City, Establishment
# Register your models here.
class CityAdmin(admin.ModelAdmin):
    class Meta:

        model = City
        fields = '__all__'

class EstablishmentAdmin(admin.ModelAdmin):
    class Meta:

        model = Establishment
        fields = '__all__'

admin.site.register(City, CityAdmin)
admin.site.register(Establishment, EstablishmentAdmin)