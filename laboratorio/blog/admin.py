from django.contrib import admin
from .models import Category, Publi

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields  = ('created', 'updated')




class PubliAdmin(admin.ModelAdmin):
    readonly_fields  = ('created', 'updated')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Publi, PubliAdmin)


