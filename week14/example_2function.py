def sum(a,b):
    def mult(a,b):
        result = a*b
        print(result)
        return a, b
    mult(a,b)
    result2 = a + b
    print(result2)


a = sum(4,2)
b = sum(2,2)
# result: 11
# (2*3) + 2 + 3 = 11

print(a)
print(b)