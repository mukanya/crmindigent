from django.contrib import admin

# Register your models here.

from .models import User, Lead , Agent, UserProfile, Category

admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfile)
# admin.site.register(Lead)
admin.site.register(Agent)

class LeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'id_number', 'physical_address', 'postal_address', 'gender', 'agent', 'category')
    search_fields = ('first_name', 'last_name')
    list_filter = ('category', 'gender', 'id_number')
    fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'age',
                'id_number',
                'physical_address',
                'postal_address',
                'gender',
                'agent',
                'category'
            )
        }),
    )
 
admin.site.register(Lead, LeadAdmin)
