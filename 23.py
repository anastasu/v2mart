def f(a,b):
    if a>b:
        raise ValueError()
    if a == b:
        yield b
    if a+1 <= b:
        yield from f(a+1, b)
    if a + 3 <= b:
        yield from f(a + 3, b)
    if a * 2 <= b:
        yield from f(a * 2, b)
print(len(list(f(3,5))))
print(len(list(f(7,11))))
print(len(list(f(13,16))))