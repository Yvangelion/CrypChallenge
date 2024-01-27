# loop through b until b == 0, then return value of a after iterating and updating a and b
def euc(a, b):
    while b != 0:
        a,b = b, a%b
    return a

# prompt user for values
a = int(input("Input x: ")) 
b = int(input("Input n: "))

# method for euc
result = euc(a, b)

#print result
print(f"GCD: {result}")
