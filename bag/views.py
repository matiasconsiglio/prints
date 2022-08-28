from django.shortcuts import render
from django.http import JsonResponse
from .contexts import bag_contents



# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def update_cart(request):
    """Example."""
    bag = request.session['bag']
    p_id = request.GET['update_id']
    p_qty = int(request.GET['update_qty'])
    # bag = request.session.get('bag')

    if str(p_id) in list(bag.keys()):

        bag[p_id]['qty'] = p_qty

    request.session['bag'] = bag

    return JsonResponse({'data': bag})

def delete_cart(request):
    """Example."""
    bag = request.session['bag']
    p_id = str(request.GET['delete_id'])

    if str(p_id) in list(bag.keys()):

        del bag[p_id]

    request.session['bag'] = bag

    return JsonResponse({'data': bag})