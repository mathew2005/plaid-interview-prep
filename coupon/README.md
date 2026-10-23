# Coupon Discount Calculator

## Part 1: Single Coupon

### Problem Description

You are given a coupon and a customer's shopping cart. Your task is to calculate the **final amount the customer will pay** after applying the discount, if applicable.

Each item in the shopping cart has:
- `price`: The price of the item.
- `category`: The category the item belongs to.

### Example Shopping Cart

```python
cart = [
    {'price': 2.00, 'category': 'fruit'},
    {'price': 20.00, 'category': 'toy'},
    {'price': 5.00, 'category': 'clothing'},
    {'price': 8.00, 'category': 'fruit'}
]
```

### Coupon Structure

A coupon provides either:
- A **percentage discount** on items in a specific category.
- A **fixed amount discount** on items in a specific category.

Coupons may also have restrictions:
- `minimum_num_items_required`: Minimum number of items in the category.
- `minimum_amount_required`: Minimum total purchase amount in the category.

Both restrictions are optional and may be `None`.

### Example Coupon

```python
coupon = {
    'category': 'fruit',
    'percent_discount': 15,
    'amount_discount': None,
    'minimum_num_items_required': 2,
    'minimum_amount_required': 10.00
}
```

### Coupon Validation Rules

1. Exactly one of `percent_discount` and `amount_discount` must be non-null.
2. If both discount fields are `None`, raise an error.
3. If both discount fields are populated, raise an error.
4. Discount validation must happen regardless of the contents of the shopping cart.
5. Both minimum requirements can independently be null or non-null.

---

## Part 2: Multiple Coupons

### Problem Description

Extend the calculator from Part 1 to support **multiple coupons**.

Each coupon can now specify one or more categories to which it may apply.

### New Rules

1. Customers can apply multiple coupons to their shopping cart.
2. Each coupon contains a `categories` list instead of a single `category`.
3. If a coupon applies to multiple categories, apply it to the **category that produces the largest discount**.
4. If multiple coupons are applicable to the same category, raise an error.

### Example 1: Valid Coupon Stack

```python
coupons = [
    {
        'categories': ['clothing', 'toy'],
        'percent_discount': None,
        'amount_discount': 6,
        'minimum_num_items_required': None,
        'minimum_amount_required': None
    },
    {
        'categories': ['fruit'],
        'percent_discount': 15,
        'amount_discount': None,
        'minimum_num_items_required': 2,
        'minimum_amount_required': 10.00
    }
]
```

**Why is this valid?**

- The first coupon can apply to either `clothing` or `toy`, whichever produces the largest discount.
- The second coupon applies to `fruit`.
- The coupons do not overlap in their applicable categories.

### Example 2: Invalid Coupon Stack

```python
coupons = [
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
```

**Why is this invalid?**

Both coupons can apply to the `toy` category.

According to the rules, if multiple coupons are applicable to the same category, an **error must be raised**.

---

## Goal

Implement a coupon calculator that:

- **Part 1:** Calculates the final cart total after applying a single valid coupon, respecting its restrictions.
- **Part 2:** Supports multiple coupons, chooses the category with the largest discount for each coupon, and detects conflicting coupons.