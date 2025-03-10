def sum(a,b):
    def mult(a,b):
        result = a*b
        return result
    return mult(a,b) + a + b

print(sum(2,3))