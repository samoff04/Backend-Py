from models.cart_model import get_cart
from models.product_model import get_products
from models.order_model import create_order

def checkout():
    cart = get_cart()
    products = get_products()
    product_map = {}
    for p in products:
        product_map[p["id"]] = p["price"]
    total = 0

    for item in cart:
        total += (
            product_map[item["product_id"]]
            * item["quantity"]
        )
    create_order(total)
    return total