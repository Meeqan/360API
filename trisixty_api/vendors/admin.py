from django.contrib import admin
from .models import Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'owner')
    list_display_links = ('name',)
    list_filter = ('owner',)
    search_fields = ('name', 'description', 'owner')
    list_per_page = 25

    fieldsets = (
        ('Vendor Info', {
         'fields': ('name', 'location', 'owner', 'logo',
                    'phone', 'email', 'description')}),
    )


# Register your models here.
admin.site.register(Vendor, VendorAdmin)
