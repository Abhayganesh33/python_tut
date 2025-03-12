# Remove vowels
s = input("String: ")
print("".join(c for c in s if c.lower() not in "aeiou"))
print("\n" + "-"*20 + "\n")





# Remove characters at odd indices
s = input("String: ")
print(s[::2])
print("\n" + "-"*20 + "\n")





# Palindrome without reversing
s = input("String: ")
print("Palindrome" if all(s[i] == s[-(i+1)] for i in range(len(s)//2)) else "Not Palindrome")
print("\n" + "-"*20 + "\n")






# Replace spaces or add $
s = input("String: ")
print(s.replace(" ", "*") if " " in s else f"${s}$")
print("\n" + "-"*20 + "\n")





# Split into odd and even index characters
s = input("String: ")
print(f"Odd: {s[1::2]}, Even: {s[::2]}")
print("\n" + "-"*20 + "\n")





# Remove all occurrences of a substring
s, sub = input("String: "), input("Substring to remove: ")
print(s.replace(sub, ""))
print("\n" + "-"*20 + "\n")






# Convert lowercase to uppercase
s = input("String: ")
print(s.upper())
print("\n" + "-"*20 + "\n")






# Replace occurrences of a substring
s, old, new = input("String: "), input("Old substring: "), input("New substring: ")
print(s.replace(old, new))
print("\n" + "-"*20 + "\n")





# Reverse first and second half separately
s = input("String: ")
mid = len(s) // 2
print(s[:mid][::-1] + s[mid:][::-1])
print("\n" + "-"*20 + "\n")





# Password validation
import re
p = input("Password: ")
if (len(p) >= 6 and re.search("[a-z]", p) and re.search("[A-Z]", p) and 
    re.search("[0-9]", p) and re.search("[$#@]", p)):
    print("Valid Password")
else:
    print("Invalid Password")
print("\n" + "-"*20 + "\n")





# Decimal to Binary
n = int(input("Decimal Number: "))
print(bin(n)[2:])
print("\n" + "-"*20 + "\n")





# Binary to Decimal
b = input("Binary Number: ")
print(int(b, 2))
print("\n" + "-"*20 + "\n")




# Area of a circle
def area_circle(r): return 3.1416 * r * r
r = float(input("Radius: "))
print(area_circle(r))
print("\n" + "-"*20 + "\n")




# Compute nCr using factorial
def fact(n): return 1 if n == 0 else n * fact(n-1)
n, r = map(int, input("n r: ").split())
print(fact(n) // (fact(r) * fact(n-r)))




# Remove vowels from a string
s = input("Enter string: ")
print("".join(c for c in s if c.lower() not in "aeiou"))



# Remove characters at odd index positions
s = input("Enter string: ")
print("".join(s[i] for i in range(len(s)) if i % 2 == 0))



# Check palindrome without reversing
s = input("Enter string: ")
is_palindrome = all(s[i] == s[-(i+1)] for i in range(len(s)//2))
print("Palindrome" if is_palindrome else "Not a palindrome")



# Replace spaces with * or add $
s = input("Enter string: ")
print(s.replace(" ", "*") if " " in s else f"${s}$")


# Separate odd and even indexed characters
s = input("Enter string: ")
print(f"Odd index: {s[1::2]}, Even index: {s[0::2]}")


# Remove all occurrences of a substring
s = input("Enter string: ")
sub = input("Enter substring: ")
print(s.replace(sub, ""))




# Convert lowercase to uppercase
s = input("Enter string: ")
print(s.upper())


# Replace substring with new substring
s = input("Enter string: ")
old = input("Substring to replace: ")
new = input("New substring: ")
print(s.replace(old, new))


# Reverse first and second half separately
s = input("Enter string: ")
mid = len(s) // 2
print(s[:mid][::-1] + s[mid:][::-1])




# Validate password
import re
p = input("Enter password: ")
if (len(p) >= 6 and re.search(r'[a-z]', p) and re.search(r'[A-Z]', p) and
        re.search(r'\d', p) and re.search(r'[$#@]', p)):
    print("Valid password")
else:
    print("Invalid password")


# Convert decimal to binary
print(bin(int(input("Enter decimal: ")))[2:])




# Convert binary to decimal
print(int(input("Enter binary: "), 2))




# Area of a circle
r = float(input("Enter radius: "))
print(f"Area: {3.1416 * r * r}")




# Compute nCr using factorial
import math
n, r = map(int, input("Enter n and r: ").split())
print(math.comb(n, r))




# Menu-driven program
def even_odd(n): return "Even" if n % 2 == 0 else "Odd"

def pos_neg_zero(n): return "Positive" if n > 0 else "Negative" if n < 0 else "Zero"

def factors(n): return [i for i in range(1, n+1) if n % i == 0]

while True:
    print("\n1. Even/Odd\n2. Positive/Negative/Zero\n3. Factors\n4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 4: break
    n = int(input("Enter number: "))
    print([even_odd(n), pos_neg_zero(n), factors(n)][choice-1])




# Compute sin(x) using series expansion
x, n = float(input("Enter x (radians): ")), int(input("Terms: "))
print(sum(((-1)**i * x**(2*i+1) / math.factorial(2*i+1)) for i in range(n)))


# Factorial using recursion
def fact(n): return 1 if n == 0 else n * fact(n-1)
print(fact(int(input("Enter number: "))))




# N'th Fibonacci using recursion
def fib(n): return n if n <= 1 else fib(n-1) + fib(n-2)
print(fib(int(input("Enter n: "))))



# Sort list of names
print(sorted(input("Enter names: ").split(",")))


# Sum of even numbers from input
nums = list(map(int, input("Enter numbers: ").split()))
print(sum(n for n in nums if n % 2 == 0))


# Remove given words from string
s, word = input("Enter string: "), input("Word to remove: ")
print(s.replace(word, ""))


# Find median of a list
nums = sorted(map(int, input("Enter numbers: ").split()))
mid = len(nums) // 2
print((nums[mid] + nums[mid-1]) / 2 if len(nums) % 2 == 0 else nums[mid])


# Find mode (most frequent number)
nums = list(map(int, input("Enter numbers: ").split()))
print(max(set(nums), key=nums.count))


# Remove duplicates from a list
nums = list(map(int, input("Enter numbers: ").split()))
print(list(set(nums)))


# Separate integers, floats, and strings
lst = input("Enter elements: ").split()
ints, floats, strs = [], [], []
for i in lst:
    if i.replace('.', '', 1).isdigit():
        floats.append(float(i)) if '.' in i else ints.append(int(i))
    else:
        strs.append(i)
print(f"Integers: {ints}, Floats: {floats}, Strings: {strs}")


# Separate prime and composite numbers
nums = list(map(int, input("Enter numbers: ").split()))
primes, composites = [], []
for n in nums:
    if n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)):
        primes.append(n)
    else:
        composites.append(n)
print(f"Primes: {primes}, Composites: {composites}")


# Sort list without built-in functions
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
nums = list(map(int, input("Enter numbers: ").split()))
bubble_sort(nums)
print(nums)


# Basic set operations
A = set(map(int, input("Set A: ").split()))
B = set(map(int, input("Set B: ").split()))
print(f"Union: {A | B}, Intersection: {A & B}, Difference: {A - B}")


# Completely remove duplicates (no copies left)
nums = list(map(int, input("Enter numbers: ").split()))
print([n for n in nums if nums.count(n) == 1])
