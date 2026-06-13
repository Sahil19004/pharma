from django.shortcuts import render, get_object_or_404
from .models import Banner, Category, Client, Product, ServiceCategory, Service, Gallery, Contact, Client, PolicyPage
# Create your views here.
def indexpage(request):
    banner = Banner.objects.all()
    gallery_items = Gallery.objects.all()[0:5]
    service_categories = ServiceCategory.objects.all()
    categories = Category.objects.all()
    clients = Client.objects.all()  # ✅ Fetch clients for marquee

    # Latest 6 products
    products = Product.objects.order_by('-id')[:6]
    # Latest 6 services
    services = Service.objects.order_by('-id')[:6]

    return render(
        request,
        'index.html',
        {
            'banner': banner,
            'gallery_items': gallery_items,
            'service_categories': service_categories,
            'products': products,
            'categories': categories,   
            'services': services,
            'clients': clients,
        }
    )


def about(request):
    service_categories = ServiceCategory.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'about.html',
        {'service_categories': service_categories, 'categories': categories}
    )


def gallery(request):
    service_categories = ServiceCategory.objects.all()
    categories = Category.objects.all()
    gallery=Gallery.objects.all()
    return render(
        request,
        'gallery.html',
        {'service_categories': service_categories, 'categories': categories, 'gallery': gallery}
    )


def products(request, slug):
    service_categories = ServiceCategory.objects.all()
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(
        request,
        'products.html',
        {
            'service_categories': service_categories,
            'categories': categories,
            'category': category,
            'products': products,
        }
    )


def contact(request):
    service_categories = ServiceCategory.objects.all()
    categories = Category.objects.all()
    success = False
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST.get('name', '').strip(),
            company_name=request.POST.get('company', '').strip(),
            email=request.POST.get('email', '').strip(),
            phone=request.POST.get('phone', '').strip(),
            subject=request.POST.get('subject', '').strip(),
            message=request.POST.get('message', '').strip(),
        )
        success = True
    return render(
        request,
        'contact.html',
        {'service_categories': service_categories, 'categories': categories, 'success': success}
    )


def services(request):
    service_categories = ServiceCategory.objects.all()
    services = Service.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'services.html',
        {'service_categories': service_categories, 'categories': categories, 'services': services}
    )


def service_detail(request, slug):
    services = Service.objects.filter(category__slug=slug)
    service_categories = ServiceCategory.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'services.html',
        {'services': services, 'service_categories': service_categories, 'categories': categories}
    )


def service_detail_info(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service_categories = ServiceCategory.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'servicedetail.html',
        {'service': service, 'service_categories': service_categories, 'categories': categories}
    )
def product_detail(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    service_categories = ServiceCategory.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'productdetail.html',
        {'product': product, 'service_categories': service_categories, 'categories': categories}
    )


def policy_page(request, slug):
    page = get_object_or_404(PolicyPage, slug=slug)
    service_categories = ServiceCategory.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'policy_page.html',
        {'page': page, 'service_categories': service_categories, 'categories': categories}
    )