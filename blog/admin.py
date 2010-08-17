from blogtest.blog.models import Post
from django.contrib.auth.models import User
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        
        obj.last_updated_by = request.user
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs["initial"] = User.objects.get(pk=request.user.id).id
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Post, PostAdmin)
