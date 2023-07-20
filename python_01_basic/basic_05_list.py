# List
about_list = ["apple", "banana", "cherry"]
print(about_list)
about_list.remove("apple")
print(about_list)
about_list.insert(len(about_list), 'Apple')
print(about_list)
about_list.insert(len(about_list), 'Apple')
about_list.insert(len(about_list), 'Apple')
about_list.insert(len(about_list), 'Apple')
print(about_list)  # Lists allow duplicate values.
about_list.remove("Apple")
about_list.remove("Apple")
about_list.remove("Apple")
print(about_list)
about_list.insert(len(about_list), 10)
about_list.insert(len(about_list), True)
about_list.insert(len(about_list), 10.11)
print(about_list)  # A list can contain different data types.
print(type(about_list))  # <class 'list'>

# ['banana', 'cherry', 'Apple', 10, True, 10.11]
print(about_list[1])  # cherry
print(about_list[-1])  # 10.11, Negative indexing means start from the end
print(about_list[-2])  # True, Negative indexing means start from the end
print(about_list[2:5])  # ['Apple', 10, True]. It can specify a range of indexes by specifying start and end index.
print(about_list[:2])  # ['banana', 'cherry']. This example returns the items from the beginning to (not include) index.
print(about_list[4:])  # [True, 10.11]. This example returns the items from True to the end.
print(about_list[-3:-1])  # [10, True]. This example returns the items from (-4) to, but NOT including (-1).

# Check if Item Exists
if 'coke' in about_list:
    print("coke in this list")
else:
    print("coke not in this list")
# => coke not in this list

# Change Item Value
about_list[1] = 'coke'
print(about_list)  # ['banana', 'coke', 'Apple', 10, True, 10.11]
