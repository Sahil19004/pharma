from django.contrib import admin
from .models import Banner,Category,Product,ServiceCategory,Service,Gallery,Contact,Client,PolicyPage
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

