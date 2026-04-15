def product_of_tuple(t):
  """Calculates the product of numbers in a tuple."""
  product = 1
  for num in t:
    product *= num
  return product

# Example
my_tuple = (2, 3, 4)
result = product_of_tuple(my_tuple)
print("The product is:", result)