def sum(a,b):
    def mult(a,b):
        result = a*b
        print(result)
        return a, b
    mult(a,b)
    result2 = a + b
    print(result2)


sum(2,3)

# result: 6 and 5

# using only for decorator, it is not usual because it is not a good practice!

