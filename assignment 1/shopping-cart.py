# ==========================================
# PART A — Spot the Bug (Explanation)
# ==========================================
"""
Bug Explanation:
In Python, default arguments are evaluated *once* when the function is defined, 
not every time it is called. When you use a mutable object like a list `cart=[]` 
as a default argument, that exact same list object is retained and reused across 
subsequent function calls. 

Expected output of Part A execution:
print(add_item("apple"))            # Output: ['apple']
print(add_item("banana"))           # Output: ['apple', 'banana'] (Shared state!)
print(add_item("milk", cart=["bread"])) # Output: ['bread', 'milk'] (New explicit list passed)
print(add_item("eggs"))             # Output: ['apple', 'banana', 'eggs'] (Back to shared state)
"""

# ==========================================
# PART B — Fix It
# ==========================================
def add_item(item, cart=None):
    """Uses None as a safe, immutable placeholder to create a fresh list every call."""
    if cart is None:
        cart = []
    cart.append(item)
    return cart


# ==========================================
# PART C — Build the Cart
# ==========================================
def create_cart(owner: str, discount: float = 0) -> dict:
    """Creates an independent cart structure using a safe immutable default parameter."""
    return {"owner": owner, "items": [], "discount": discount}

def add_to_cart(cart: dict, name: str, price: float, qty: int = 1) -> None:
    """Appends item dictionary to the cart item list."""
    cart["items"].append({"name": name, "price": price, "qty": qty})

def update_price(price_tuple: tuple, new_price: float):
    """Attempts to mutate an element inside a tuple (Will raise TypeError)."""
    try:
        # Tuples do not support item assignment because they are immutable sequence types.
        price_tuple[0] = new_price 
    except TypeError as e:
        print(f"\n[Caught Expected Error] Cannot modify tuple: {e}")

def calculate_total(cart: dict) -> float:
    """Calculates total gross sum and applies the discount percentage."""
    gross_total = sum(item["price"] * item["qty"] for item in cart["items"])
    discount_amount = gross_total * (cart["discount"] / 100)
    return gross_total - discount_amount


# Demonstration of independent state
if __name__ == "__main__":
    print("--- Demonstrating Part B & C ---")
    
    # 5. Independent Cart Verification
    customer_1 = create_cart("Alice", discount=10)
    customer_2 = create_cart("Bob", discount=0)
    
    add_to_cart(customer_1, "Laptop", 1200.0, 1)
    add_to_cart(customer_2, "Headphones", 150.0, 2)
    
    print(f"{customer_1['owner']}'s Final Total: ${calculate_total(customer_1):.2f}")
    print(f"{customer_2['owner']}'s Final Total: ${calculate_total(customer_2):.2f}")
    
    # 3. Tuple Immutability Verification
    dummy_tuple = (100.0, "USD")
    update_price(dummy_tuple, 95.0)


'''
1. Why is discount=0 safe but cart=[] dangerous?
discount=0 passes an integer, which is immutable. Re-assigning or changing the value 
creates a new object in memory without modifying a shared reference. cart=[] passes a mutable 
list, which means every call shares the exact same memory allocation if an explicit list isn't provided.

2. What is the difference between rebinding and mutating?
Rebinding shifts a variable name to point to a completely different object in memory (e.g., x = [1, 2]).
Mutating alters the internal contents of an existing object in-place without changing its memory address reference (e.g., x.append(3)).

3. Which of these are mutable?
Mutable: list, dict, set
Immutable: tuple, str, int

4. When you pass a list into a function and modify it, do changes reflect outside? Why?
Yes, changes reflect outside. Python uses "Pass-by-assignment" (or Call-by-object-sharing). 
When passing a mutable object like a list, the function parameter receives a copy of the reference 
to the exact same object. Mutating it modifies the source object directly.
'''