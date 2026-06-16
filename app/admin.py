from django.contrib import admin
from .models import Banner,Category,Product,ServiceCategory,Service,Gallery,Contact,Client,PolicyPage,Blog
# Register your models here.
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(Gallery)
admin.site.register(Contact) 
admin.site.register(Client)


@admin.register(PolicyPage)
class PolicyPageAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug')
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'category', 'is_published', 'published_date')
	list_filter = ('is_published', 'category')
	search_fields = ('title', 'excerpt', 'content')
	prepopulated_fields = {'slug': ('title',)}

