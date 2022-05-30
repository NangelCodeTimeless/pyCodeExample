def num_1(x):
    def num_2(y):
        return x + y
    return num_2


b = num_1(39)
print(b(10))



