def foo():
    print("begin")
    yield 1

    print("middle")
    yield 2

    print("end")
    yield 3

bar = foo()

a = next(bar)
print(a)

print("Back to global")

a = next(bar)
print(a)

a = next(bar)
print(a)