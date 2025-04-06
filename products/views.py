from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def get_playtime_range(playtime_filter):
    """
    Returns a tuple of playtime range based on the filter
    """
    ranges = {
        'quick': (0, 30),
        'medium': (31, 60),
        'long': (61, 120),
    }
    return ranges.get(playtime_filter, (None, None))


def get_player_count_range(player_count_filter):
    """
    Returns a tuple of player count range based on the filter
    """
    ranges = {
        'solo': (1, 1),
        'duo': (2, 2),
        'trio': (3, 6),
        'penta': (5, 99),
    }

    return ranges.get(player_count_filter, (0, 99))


def get_age_range(age_filter):
    """
    Returns a tuple of age range based on the filter
    """
    ranges = {
        'kids': (0, 7),
        'children': (8, 12),
        'teens': (13, 17),
        'adult': (18, 99),
    }
    return ranges.get(age_filter, (0, 99))


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """
    products = Product.objects.all()
    query = None
    categories = None
    playtime = None
    playercount = None
    age = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'age' in request.GET:
            age = request.GET['age']
            min_age, max_age = get_age_range(age)
            products = products.filter(
                min_age__gte=min_age, min_age__lte=max_age
            )

        if 'playercount' in request.GET:
            playercount = request.GET['playercount']
            min_playercount, max_playercount = get_player_count_range(
                playercount)
            products = products.filter(
                Q(min_players__lte=max_playercount) &
                Q(max_players__gte=min_playercount)
            )

        if 'playtime' in request.GET:
            playtime = request.GET['playtime']
            min_playtime, max_playtime = get_playtime_range(playtime)
            products = products.filter(
                playing_time__gte=min_playtime, playing_time__lte=max_playtime
            )

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didnt enter any search criteria!")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """
    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
