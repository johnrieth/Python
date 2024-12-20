# 3 ways to format strings

# %
# %s converts the object into a string
# %i indicates that I will pass in an integer
name = "Joe"
print("My name is %s" % name)

age = 35
print("You must be %s to continue" % age)

print("Hello %s. You must be %i to continue!" % (name, age))

# this is using named printf-style
print(
    "Hello %(first_name)s. You must be at least %(age)i to continue \n"
    % {"first_name": name, "age": age}
)

# .format()
age1 = 28
name1 = "Jose"

# I am using positional arguments
print("Hello {}. You must be at least {} to continue!".format(name1, age1))

# I am using named arguments
print(
    "Hello {first_name}. You must be at least {age} to continue past this point!".format(
        first_name=name1, age=age1
    )
)

# you cannot pass a dictionary using .format. Using ** means I am passing named parameters to the function
print(
    "Hellow {first_name}. You must be at least {age} to continue up this hill".format(
        **{"first_name": name1, "age": age1}
    )
)

# you can use variables multiple times
first_name = "Harold"
print(
    "\nHello {first_name}. Why do they call you {first_name}?".format(
        first_name=first_name
    )
)

# interpolating values using numbers
print(
    "\nHello {0}. You must be at least {1} to make it past the troll!".format(
        name1, age1
    )
)

greetings = "\nHello {name1}. You must be over the age of {age1} to pass"
print(greetings.format(name1=name1, age1=age1))


# f-strings are evaluated at runtime. This means I can put a Python expression inside the f-string
birth_year = 1980
f"{birth_year+2}"

full_name = "Mike Johns"
f"{full_name.lower()}"

sample_dict = {"name": "Tom", "age": 45}
f"Hello {sample_dict["name"]}. You are {sample_dict['age']} year old."
