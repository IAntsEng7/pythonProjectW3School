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
