from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin class for OrderLineItem to be used in the Order
    admin interface.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Order admin class to manage the Order model in the admin interface.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'order_total',
                       'delivery_cost', 'grand_total', 'original_bag',
                       'stripe_pid')

    fields = (
        'order_number', 'user_profile' 'date', 'full_name', 'email', 
        'phone_number', 'country', 'postcode', 'town_or_city', 
        'street_address1', 'street_address2', 'county', 'delivery_cost',
        'order_total', 'grand_total', 'original_bag', 'stripe_pid',
    )
    list_display = (
        'order_number', 'date', 'full_name', 'order_total',
        'delivery_cost', 'grand_total'
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
