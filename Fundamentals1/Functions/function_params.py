
def pet_names(cat_name, dog_name):
    return "I have a cat named {} and a dog named {}".format(cat_name, dog_name)

print(pet_names("bob", "cat"))


def pet_names(cat_name, dog_name):
    return "I have a cat named {} and a dog named {}.".format(cat_name, dog_name)

# no keyword arguments - order matters!
pet_names("Mittens", "Fido") # "I have a cat named Mittens and a dog named Fido."

pet_names("Fido", "Mittens") # "I have a cat named Fido and a dog named Mittens." -- uh oh, the names are the opposite of what we want, because we passed them to the function in the wrong order.

# keyword arguments
pet_names(cat_name="Mittens", dog_name="Fido")
# "I have a cat named Mittens and a dog named Fido."

# keyword arguments - order doesn't matter!
pet_names(dog_name="Fido", cat_name="Mittens")
# "I have a cat named Mittens and a dog named Fido."
