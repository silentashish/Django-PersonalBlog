from django.contrib import admin

# Register your models here.
from testadmin.models import customer,movie

class MovieAdmin(admin.ModelAdmin):
    fields= ['length','title','releaseYear']
    search_fields=['title','releaseYear']
    list_filter=['length','title','releaseYear']
    list_display=['title','releaseYear','length',]
    list_editable=['releaseYear']

class customerAdmin(admin.ModelAdmin):
    fields=['first_name','phone','last_name']

admin.site.register(customer,customerAdmin)
admin.site.register(movie,MovieAdmin)
