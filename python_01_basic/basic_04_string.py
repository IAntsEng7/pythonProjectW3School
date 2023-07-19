# 'hello' is the same as "hello". (three double quotes equals three single quotes.)
print(type('hello'))
print(type("hello"))

# Assign String to a Variable
str_a = 'hello'
print("what is str_a? " + str_a)

# Multiline Strings(three double quotes equals three single quotes.)
str_b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print("what is str_b? " + str_b)

# Strings are Arrays
str_c = "Hello, World!"
print("what is str_c[1]? " + str_c[1])

# Looping Through a String
str_d = "hysteria"
for x in str_d:
    print(x)

# String Length
str_e = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
print(f"Length of pneumonoultramicroscopicsilicovolcanoconiosis = {len(str_e)}")

# Check String
check_str = "The best things in life are free!"
# Check String - in
print("free" in check_str)  # True
# Check String - in - and use it in an if statement:
if "free" in check_str:
    print("Yes, 'free' is present.")  # Yes, 'free' is present.
# Check String - not in
print("expensive" not in check_str)  # True
# Check String - not in - and use it in an if statement:
if "expensive" not in check_str:
    print("No, 'expensive' is NOT present.")  # No, 'expensive' is NOT present.

# Slicing Strings
slicing_str = "Hello, World!"
print(slicing_str[2:5])  # "llo". Get the characters from position 2 to position 5 (not included).
# Slice From the Start
print(slicing_str[:5])  # "Hello". Get the characters from the start to position 5 (not included).
# Slice To the End
print(slicing_str[2:])  # "llo, World!". Get the characters from position 2, and all the way to the end.
# Negative Indexing
print(slicing_str[-5:-2])  # "orl". From: "o" in "World!" (-5). To(but not included): "d" in "World!" (-2).

# Modify Strings
modify_str = '  Hello, world ! '
# to uppercase
print(modify_str.upper())  # "  HELLO, WORLD ! "
# to lowercase
print(modify_str.lower())  # "  hello, world ! "
# remove whitespace
print(modify_str.strip())  # "Hello, world !"
# replace string
print(modify_str.replace("H", "J"))  # "  Jello, world ! "
# split string
print(modify_str.split(','))  # ['  Hello', ' world ! ']

# String Concatenation
concat_str_a = 'Hello'
concat_str_b = 'World'
concat_str_c = concat_str_a + concat_str_b
print(concat_str_c)  # "HelloWorld"
concat_str_d = concat_str_a + " " + concat_str_b
print(concat_str_d)  # "Hello World"

# Format Strings
age_int = 36
# txt_str1 = "My name is John, I am " + age_int  # TypeError: can only concatenate str (not "int") to str
# print(txt_str1)  # TypeError: can only concatenate str (not "int") to str
txt_str2 = "My name is John, and I am {}"
print(txt_str2.format(age_int))  # My name is John, and I am 36
# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
item_no = 567
price = 49.95
my_order_1 = "I want {} pieces of item {} for {} dollars."
print(my_order_1.format(quantity, item_no, price))  # I want 3 pieces of item 567 for 49.95 dollars.
# Also can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
my_order_2 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(my_order_2.format(quantity, item_no, price))  # I want to pay 49.95 dollars for 3 pieces of item 567.

# Escape Characters
# It will get an error if it uses double quotes inside a string that is surrounded by double quotes
# error_txt = "We are the so-called "Vikings" from the north."
# The escape character allows to use double quotes when it normally would not be allowed
escape_txt = "We are the so-called \"Vikings\" from the north."
print(escape_txt)  # We are the so-called "Vikings" from the north.
