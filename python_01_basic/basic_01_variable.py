from datetime import datetime

x = "X-Man"
y = 19
z = datetime.now()
print(x)
print(y)
print(z)

a, b, c = "apple", "banana", "cherry"
print(a)
print(b)
print(c)

i = j = k = "tiger"
print(i)
print(j)
print(k)

h = "hello"
w = "wow"


def test_function():
    w = "what"  # what, only in this function
    print("Function H print: " + h)  # Function H print: hello, test_function()
    print("inside wow or what? " + w)  # inside wow or what? what, test_function()


test_function()
print("outside wow or what? " + w)  # outside wow or what? wow


def global_function():
    global g
    g = "global variable"


# print("what is g? " + g)            # NameError: name 'g' is not defined
global_function()
print("after function, what is g? " + g)

k = "Kotlin"


def global_test_2():
    global k
    k = "Kubernetes"


global_test_2()
print("what is k now? " + k)  # what is k now? Kubernetes
