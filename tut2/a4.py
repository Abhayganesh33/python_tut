
# Replace spaces or add $
s = input("String: ")
print(s.replace(" ", "*") if " " in s else f"${s}$")
print("\n" + "-"*20 + "\n")