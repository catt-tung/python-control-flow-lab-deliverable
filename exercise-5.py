# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
#create a function that will push values into a list
# iterate over the list printing index and number

fib = [0, 1]

def fib_seq(list):
  count = 0
  n0 = 0
  n1 = 1
  while count < 49:
    n = n0 + n1
    list.append(n)
    n0 = n1
    n1 = n
    count += 1

fib_seq(fib)

for n in range(51):
  print(f"term: {n} / number {fib[n]}")