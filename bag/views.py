from django.shortcuts import render
from django.http import JsonResponse
from .contexts import bag_contents



# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def update_cart(request):
    """Example."""
    # bag_content = bag_contents(request)
    # bag_items = bag_content['bag_items']

    # p_id = request.GET['id']
    # p_qty = int(request.GET['qty'])

    # data_list = bag_items

    # for dic in data_list:
    #     if str(p_id) == dic['product_id']:
    #         dic['qty_per_product'] = p_qty

    # bag_items = data_list
    # request.session['bag'] = bag_items
  

    # return JsonResponse({'data': bag_items})

    bag = request.session['bag']
    p_id = request.GET['update_id']
    p_qty = int(request.GET['update_qty'])
    # product_spec_id = str(p_id)
    print(p_id)
    print(p_qty)
    bag = request.session.get('bag')

    if str(p_id) in list(bag.keys()):

        bag[p_id]['qty'] = p_qty

    request.session['bag'] = bag
    print(bag)
    
    return JsonResponse({'data': bag})