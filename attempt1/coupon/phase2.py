"""
cart = [
    {'price': 2.00, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 5.00, 'category': 'clothing'},
    {'price': 8.00, 'category': 'fruit'}
]
"""

from collections import defaultdict
def multiple_coupons(cart, coupons):
    # coupon validity check
    coupon_categories = set()
    for coupon in coupons:
        for category in coupon["categories"]:
            if category in coupon_categories:
                raise ValueError("Coupon is not valid")
            else:
                coupon_categories.add(category)
    
    # sort cart by categories
    cart_categories = defaultdict(list)
    for i, item in enumerate(cart):
        cart_categories[item["category"]].append(i)

    # match coupon and cart with right category
    for coupon in coupons: 
        maxDiscount = 0
        for category in coupon["categories"]:
            if category not in coupon_categories:
                pass
        # either use the single_coupon (issue with categories being a list and transferring the parameters) or where to apply discounts inside this loop or parent loop? 

cart1 = [
    {'price': 2.00, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 5.00, 'category': 'clothing'},
    {'price': 8.00, 'category': 'fruit'}
]

coupons1 = [
    {
        'categories': ['clothing', 'toy'],
        'percent_discount': None,
        'amount_discount': 6,
        'minimum_num_items_required': None,
        'minimum_amount_required': None
    },
    {
        'categories': ['toy'],
        # Other coupon fields...
    }
]


# valid coupon
cart2 = [
    {'price': 2.00, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 5.00, 'category': 'clothing'},
    {'price': 8.00, 'category': 'fruit'}
]

coupons2 = [
    {
        'categories': ['clothing', 'toy'],
        'percent_discount': None,
        'amount_discount': 6,
        'minimum_num_items_required': None,
        'minimum_amount_required': None
    },
]
# multiple_coupons(cart1, coupons1)
multiple_coupons(cart2, coupons2)