def list(data):
    total = 0
    for i in data:
        total = total + i
    return total

data = [1,2,3,4,5]
print(list(data))