# Time in HH:MM:SS  
s = int(input("Seconds: "))  
print(f"{s//3600:02}:{(s%3600)//60:02}:{s%60:02}")  

print("\n" + "-"*20 + "\n")  






# Area & Circumference  
r = float(input("Radius: "))  
print(f"Area: {3.14159 * r * r:.2f}")  
print(f"Circumference: {2 * 3.14159 * r:.2f}")  
print("\n" + "-"*20 + "\n")  




# Even or Odd  
n = int(input("Number: "))  
print("Even" if n % 2 == 0 else "Odd")  
print("\n" + "-"*20 + "\n")  




# Compare Numbers  
a, b = map(int, input("Two numbers: ").split())  
print("=" if a == b else ">" if a > b else "<")  
print("\n" + "-"*20 + "\n")  






# Quadratic Roots  
import math  
a, b, c = map(float, input("Coefficients a b c: ").split())  
d = b**2 - 4*a*c  
if d > 0:  
    print(f"Roots: {(-b+math.sqrt(d))/(2*a):.2f}, {(-b-math.sqrt(d))/(2*a):.2f}")  
elif d == 0:  
    print(f"Root: {-b / (2*a):.2f}")  
else:  
    print("No real roots")  
print("\n" + "-"*20 + "\n")  







# Right-Angled Triangle  
a, b, c = sorted(map(int, input("Triangle sides: ").split()))  
print("Right-angled" if a**2 + b**2 == c**2 else "Not right-angled")  
print("\n" + "-"*20 + "\n")  









# Quadrant Finder  
x, y = map(int, input("Point (x y): ").split())  
if x > 0 and y > 0: print("Quadrant I")  
elif x < 0 and y > 0: print("Quadrant II")  
elif x < 0 and y < 0: print("Quadrant III")  
elif x > 0 and y < 0: print("Quadrant IV")  
else: print("On Axis")  
print("\n" + "-"*20 + "\n")  







# Sum of Digits  
n = input("Number: ")  
print(sum(int(d) for d in n))  
print("\n" + "-"*20 + "\n")  








# Prime Check  
n = int(input("Number: "))  
print("Prime" if n > 1 and all(n%i for i in range(2, int(n**0.5)+1)) else "Not Prime")  
print("\n" + "-"*20 + "\n")  







# Sum of Even Numbers  
n = int(input("Count: "))  
nums = list(map(int, input("Numbers: ").split()))  
print(sum(x for x in nums if x % 2 == 0))  
print("\n" + "-"*20 + "\n")  







# Sum of Cubes of Even Numbers  
n = int(input("Positive integer: "))  
print(sum(x**3 for x in range(2, n+1, 2)))  
print("\n" + "-"*20 + "\n")  





# Sum & Avg of Positives and Negatives  
nums = list(map(int, input("4 numbers: ").split()))  
pos = [x for x in nums if x > 0]  
neg = [x for x in nums if x < 0]  
print(f"Positive Sum: {sum(pos)}, Average: {sum(pos)/len(pos) if pos else 0:.2f}")  
print(f"Negative Sum: {sum(neg)}, Average: {sum(neg)/len(neg) if neg else 0:.2f}")  





# Reverse a Number
n = input("Number: ")
print(n[::-1])
print("\n" + "-"*20 + "\n")








# First 10 Fibonacci Numbers
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

print("\n" + "-"*20 + "\n")








# Prime Numbers < 1000
primes = [x for x in range(2, 1000) if all(x % i != 0 for i in range(2, int(x**0.5)+1))]
print(*primes)
print("\n" + "-"*20 + "\n")







# Nested Loop Pattern
for i in range(5, 0, -1):
    print(*range(i, 0, -1))

print("\n" + "-"*20 + "\n")







# Multiplication Table (1 to n)
n = int(input("Table up to: "))
for i in range(1, n+1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("-"*10)

print("\n" + "-"*20 + "\n")




# Armstrong Number
n = input("Number: ")
print("Armstrong" if sum(int(d)**len(n) for d in n) == int(n) else "Not Armstrong")
print("\n" + "-"*20 + "\n")





# Count Even & Odd Numbers
nums = list(map(int, input("Numbers: ").split()))
evens = sum(1 for x in nums if x % 2 == 0)
print(f"Evens: {evens}, Odds: {len(nums) - evens}")
print("\n" + "-"*20 + "\n")








# Palindrome Check
s = input("String: ")
print("Palindrome" if s == s[::-1] else "Not Palindrome")
print("\n" + "-"*20 + "\n")









# 2^(2n) + n + 5
n = int(input("Value of n: "))
print(2**(2*n) + n + 5)
print("\n" + "-"*20 + "\n")






# Leap Year Check
y = int(input("Year: "))
print("Leap Year" if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else "Not Leap Year")
print("\n" + "-"*20 + "\n")





# Prime Factors
n = int(input("Number: "))
factors = []
i = 2
while i * i <= n:
    while n % i == 0:
        factors.append(i)
        n //= i
    i += 1
if n > 1:
    factors.append(n)
print(*factors)
print("\n" + "-"*20 + "\n")






# Numbers 100-1000 with sum of digits divisible by 9
print(*[x for x in range(100, 1001) if sum(int(d) for d in str(x)) % 9 == 0])
print("\n" + "-"*20 + "\n")




# Power Calculation (X^Y) Without pow()
x, y = map(int, input("X Y: ").split())
result = 1
for _ in range(y):
    result *= x
print(result)
print("\n" + "-"*20 + "\n")





# Distance Between Two Points
x1, y1, x2, y2 = map(float, input("x1 y1 x2 y2: ").split())
print(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)
print("\n" + "-"*20 + "\n")



# Quadratic Equation Roots
import math
a, b, c = map(float, input("a b c: ").split())
d = b**2 - 4*a*c
if d > 0:
    print(f"Roots: {(-b+math.sqrt(d))/(2*a):.2f}, {(-b-math.sqrt(d))/(2*a):.2f}")
elif d == 0:
    print(f"Root: {-b / (2*a):.2f}")
else:
    print("No real roots")
print("\n" + "-"*20 + "\n")





# Sum of Odd Numbers in Range
l, u = map(int, input("Lower Upper: ").split())
print(sum(x for x in range(l, u+1) if x % 2 == 1))
