def my_var():
    i = 42
    print(f"{i} est de type {type(i)}")
    i = "42"
    print(f"{i} est de type {type(i)}")
    i = "quarante-deux"
    print(f"{i} est de type {type(i)}")
    i = 42.0
    print(f"{i} est de type {type(i)}")
    i = True
    print(f"{i} est de type {type(i)}")
    i = [42]
    print(f"{i} est de type {type(i)}")
    i = {42: 42}
    print(f"{i} est de type {type(i)}")
    i = (42,)
    print(f"{i} est de type {type(i)}")
    i = set()
    print(f"{i} est de type {type(i)}")

if __name__ == '__main__':
    my_var()