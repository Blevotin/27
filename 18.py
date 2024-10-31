def add_everything_up(a, b):
    c = 0
    try:
        c = a + b
        return c
    except TypeError as exp:
        a = f"{a}"
        b = f"{b}"
        c = a + b
        return c

print(add_everything_up(2, "retre"))
print(add_everything_up(3,"324"))

