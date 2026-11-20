ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# ---  LIST  ---
ft_list[1] = "World!"

# ---  TUPLE  ---
ft_tuple = ft_tuple[:1] + ("France!",)

# ---  SET  ---
ft_set.remove("tutu!")
ft_set.add("Lyon!")

# ---  DICT  ---
ft_dict["Hello"] = '42Lyon!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

#   output
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$
