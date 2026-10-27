# input: coupon (percentage or fixed amount discount), shopping cart[price, category]
# are the items supposed to be in the same category, and same with the amount or total

def single_coupon(cart, coupon):
    # discount validation
    if (not coupon["percent_discount"] and  not coupon["amount_discount"]) or (coupon["percent_discount"] and  coupon["amount_discount"]) :
        raise ValueError("Coupon is invalid")


    # applying discount
    coupon_cart = []
    for item in cart:
        if item["category"] == coupon["category"]:
            coupon_cart.append(item)

    # checking if discount applies (min num items required, min amount required)
    total_coupon_cart = sum(item["price"] for item in coupon_cart)
    if len(coupon_cart) < coupon["minimum_num_items_required"] or total_coupon_cart < coupon["minimum_amount_required"]: return cart

    # applying discount
    if coupon["percent_discount"]:
        remaining = max(0, total_coupon_cart - (coupon["percent_discount"] /100) * total_coupon_cart)
    else:
        remaining = max(0, total_coupon_cart - coupon["amount_discount"])

    total = 0
    for item in cart:
        if coupon["category"] != item["category"]:
            total += item["price"]

    total += remaining
    return total

    
# percentage discount
cart1 = [
    {'price': 2.00, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 5.00, 'category': 'clothing'},
    {'price': 8.00, 'category': 'fruit'}
]

coupon1 = {
    'category': 'fruit',
    'percent_discount': 15,
    'amount_discount': None,
    'minimum_num_items_required': 2,
    'minimum_amount_required': 10.00
}

# not valid coupon

cart2 = [
    {'price': 2.00, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 5.00, 'category': 'clothing'},
    {'price': 8.00, 'category': 'fruit'}
]

coupon2 = {
    'category': 'fruit',
    'percent_discount': None,
    'amount_discount': None,
    'minimum_num_items_required': 2,
    'minimum_amount_required': 10.00
}

# not valid coupon

cart3 = [
    {'price': 2.00, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 5.00, 'category': 'clothing'},
    {'price': 8.00, 'category': 'fruit'}
]

coupon3 = {
    'category': 'fruit',
    'percent_discount': 0,
    'amount_discount': 0,
    'minimum_num_items_required': 2,
    'minimum_amount_required': 10.00
}
coupon3 = {
    'category': 'fruit',
    'percent_discount': 0,
    'amount_discount': 0,
    'minimum_num_items_required': 2,
    'minimum_amount_required': 10.00
}



# amount discount
cart4 = [
    {'price': 2.00, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 5.00, 'category': 'clothing'},
    {'price': 8.00, 'category': 'fruit'}
]

coupon4 = {
    'category': 'fruit',
    'percent_discount': 15,
    'amount_discount': None,
    'minimum_num_items_required': 2,
    'minimum_amount_required': 10.00
}


assert single_coupon(cart1, coupon1) == 33.5
# single_coupon(cart2, coupon2)
single_coupon(cart3, coupon3)
