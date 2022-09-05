from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse


def view_bag(request):
    """
    A view that renders the bag contents page
    """
    return render(request, 'bag/bag.html')


def update_cart(request):
    """
    View for updating quantity of a product in the cart
    """
    bag = request.session['bag']
    p_id = request.GET['update_id']
    p_qty = int(request.GET['update_qty'])

    if str(p_id) in list(bag.keys()):

        bag[p_id]['qty'] = p_qty
        messages.success(request, f'SKU:{p_id} Updated quantity to {p_qty}.')

    request.session['bag'] = bag

    return JsonResponse({'data': bag})


def delete_cart(request):
    """
    View for deleting a product in the cart
    """
    bag = request.session['bag']
    p_id = str(request.GET['delete_id'])

    if str(p_id) in list(bag.keys()):

        del bag[p_id]
        messages.success(request, f'SKU:{p_id} Deleted product from the bag.')

    request.session['bag'] = bag

    return JsonResponse({'data': bag})
