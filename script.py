import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# Inspect visits
print(visits.head())

# Inspect cart
print(cart.head())

# Inspect checkout
print(checkout.head())

# Inspect purchase
print(purchase.head())

# Combine visits and cart using a left merge and assign it to visits_cart
visits_cart = pd.merge(
  visits,
  cart,
  how = 'left'
)

# Display visits_cart
print(visits_cart)

# Variable visits_cart_rows to hold the length of visits_cart
visits_cart_rows = len(visits_cart)

# Display the length of visits_cart_rows
print(visits_cart_rows)

# Variable null_cart_times to hold the number of timestamps that are null for the column cart_time
null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])

# Display null_cart_times
print(null_cart_times)

# Percentage of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart
print(float(null_cart_times) / visits_cart_rows)

# Combine cart and checkout using a left merge and assign it to cart_checkout
cart_checkout = pd.merge(
  cart,
  checkout,
  how = 'left'
)

# Display cart_checkout
print(cart_checkout)

# Variable cart_checkout_rows to hold the length of cart_checkout
cart_checkout_rows = len(cart_checkout)

# Display the length of cart_checkout_rows
print(cart_checkout_rows)

# Variable null_checkout_times to hold the number of timestamps that are null for the column checkout_time
null_checkout_times = len(cart_checkout[cart_checkout.checkout_time.isnull()])

# Display null_checkout_times
print(null_checkout_times)

# Percentage of users who put items in thier cart, but did not proceed to checkout
print(float(null_checkout_times) / cart_checkout_rows)


# Combine checkout and purchase using a left merge and assign it to checkout_purchase
checkout_purchase = pd.merge(
  checkout,
  purchase,
  how = 'left'
)

# Display checkout_purchase
print(checkout_purchase)

# Variable checkout_purchase_rows to hold the length of checkout_purchase
checkout_purchase_rows = len(checkout_purchase)

# Display the length of checkout_purchase_rows
print(checkout_purchase_rows)

# Variable null_purchase_times to hold the number of timestamps that are null for the column purchase_time
null_purchase_times = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])

# Display null_purchase_times
print(null_purchase_times)

# Percentage of items that is a time in checkout_time, but not in purchase_time
print(float(null_purchase_times) / checkout_purchase_rows)

# Merge visits, cart, checkout and purchase DataFrames together using a series of left merges and assign it to the variable all_data
all_data = visits.merge(cart, how = 'left')\
                 .merge(checkout, how = 'left')\
                 .merge(purchase, how = 'left')

# Adding columns to all_data
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

# Examine all_data using print and head
#print(all_data.head())

# Examine the time_to_purchase column from all_data
print(all_data.time_to_purchase)

# Calculate the average time to purchase
print(all_data.time_to_purchase.mean())