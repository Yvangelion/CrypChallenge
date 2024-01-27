# calculate the modular inverse of x (mod n)
def inverse(x, n):
    g, inv, skip = gcd(x, n)
    if g != 1:
        print(f"No modular inverse for {x} (mod {n})")
    else:
        return inv % n

# calculate the gcd using the EA 
def gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        z, x, y = gcd(b%a, a)
        return z, y - (b//a) * x, x

# prompt user for input
x = int(input("Input x: "))
n = int(input("Input n: "))

# call method
result = inverse(x, n)

# print only if there is inverse
if result:
    print(f"The modular inverse of {x} (mod {n}) is: {result}")

