
# Bank Routing Number Mapping

## Problem Description

Banks have multiple properties used for identification.

Within Plaid, each bank has:

- A unique integer **bank ID**.
- One or more **routing numbers**, which are sequences of digits.
- One or more **names**, which are strings without an established standard format.

We are given two databases that represent these relationships.

---

## Part 1: Routing Number Mapping

### Input

**Database 1: Routing Number to Bank Name**

```python
rn_to_name = {
    "123": "Wells Fargo",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
}
```

**Database 2: Bank Name to Bank ID**

```python
name_to_bank_id = [
    # There are multiple common ways to write the name of this bank
    ("Wells Fargo", 1),
    ("Wells", 1),
    ("Chase", 2),
    ("Capital One", 3),
    ("Bank of America", 4),

    # These are two different banks with the same name
    ("First State Bank", 5),
    ("First State Bank", 6),
]
```

### Task

Implement `create_routing_number_mapping(rn_to_name, name_to_bank_id)`, which returns a map with:

- **Keys:** Routing numbers.
- **Values:** Lists of related bank IDs.

---

## Part 2: Follow-Up - Multiple Data Providers

The `rn_to_name` database may be incorrect, so we want to get more information by assembling multiple `rn_to_name` databases from different providers.

However, these databases may disagree with each other.

### Task

Decide on an algorithm to make the **best guess** of what bank each routing number routes to.

### Input

```python
rn_to_name_list = [
    {
        "123": "Wells Fargo",
        "456": "Chase",
        "555": "First State Bank",
        "556": "First State Bank",
    },
    {
        "123": "Wells",
        "789": "Capital One",
        "456": "Bank of America",
        "555": "Bank of America",
        "556": "First State Bank",
    },
    {
        "123": "Bank of America",
        "456": "Chase",
    },
]
```
