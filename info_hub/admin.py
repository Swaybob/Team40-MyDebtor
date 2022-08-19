from django.contrib import admin
from info_hub.models import *
from django.utils.translation import gettext_lazy as _
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['date_created','user', 'content']
    list_editable = ['content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'post', 'user', 'date_created']
 
class ContactAdmin(admin.ModelAdmin):
    exclude = ['date']

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
