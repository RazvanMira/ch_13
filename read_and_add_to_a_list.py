list_ = []

while True:
    number = int(input("Please type in a number: "))
    if number == 0:
        break
    list_ = list_ + [number]

print(list_)
print(min(list_))
print(max(list_))