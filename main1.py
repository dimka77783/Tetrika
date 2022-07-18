def task(array):
    for i in array:
        if int(i)==0:
            return array.index(i)

print(task("111111111110000000000000000"))

