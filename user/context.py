from .models import Wishlist

def user_info(request):
    if 'wishlist' in request.session:
        wishlist = request.session['wishlist']
        return {'wishlist':wishlist}

    if 'cart' in request.session:
        cart = request.session['cart']
        total_items = len(cart)
        return {'total_items':total_items,'cart':cart}

    return {}

def notification(request):
    if notification in request.session:
        notif=request.session['notification']
        return {'notification':notif}
    return {}