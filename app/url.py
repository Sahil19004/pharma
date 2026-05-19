from django.urls import path
from . import views
urlpatterns = [
	path('', views.indexpage, name='indexpage'),
	path('about/', views.about, name='about'),
	path('gallery/', views.gallery, name='gallery'),
	path('products/<slug:slug>/', views.products, name='products'),
	path('contact/', views.contact, name='contact'),
	path('services/', views.services, name='services'),
	path('services/<slug:slug>/', views.service_detail, name='service_detail'),
	path('service-detail-info/<int:service_id>/', views.service_detail_info, name='service_detail_info'),
	path('product-detail/<str:product_name>/', views.product_detail, name='product_detail'),
]
