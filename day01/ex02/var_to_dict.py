def var_to_dict():
    inputList = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]
    var_dict = dict()
    for name, date in inputList:
        if date in var_dict:
            var_dict[date] = var_dict[date] + " " + name
        else:
            var_dict[date] = name

    for date, name in var_dict.items():
        print(f"{date} : {name}")


if __name__ == '__main__':
    var_to_dict()
