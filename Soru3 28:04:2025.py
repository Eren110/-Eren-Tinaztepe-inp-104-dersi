my_tuple = (0, 1, 2, "hi", 4, 5)
yeni_tuple = my_tuple[:3] + (3,) + my_tuple[4:]
print("Yeni Tuple:", yeni_tuple)