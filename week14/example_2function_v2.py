def sum(a,b):
    def mult(a,b):
        result = a*b
        print(result)
        return a, b
    mult(a,b)
    result2 = a + b
    print(result2)


sum(4,2)

# result: 11
# (2*3) + 2 + 3 = 11