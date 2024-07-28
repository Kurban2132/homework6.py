my_dict = {"Kurban": 1973, "Andrey": 1998, "Helen": 1991}
print(my_dict)
my_dict["Kurban"] = 1973
print(my_dict["Kurban"])
my_dict["Kurban"] = 1968
print(my_dict['Kurban'])
my_dict["Maxim"] = 1982
print(my_dict["Maxim"])
my_dict.update({"Alex": 1979, "Sergey": 1975})
print(my_dict)
del my_dict["Alex"]
print(my_dict)
set_ = {1, 2, 3, 4, 5, 6, 3, 5, "Anton", "Sergey", (4, 3, 1, 2)}
print(set_)
set_.update([7, 8, 9])
print(set_)
set_.remove(1)
print(set_)