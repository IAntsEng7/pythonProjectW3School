# # 數值型別: int(整數), float(浮點數), complex(複數)
int_x = 1
float_x = 1.11
complex_x = 4 - 1j
# 創建一個複數
complex_y = complex(2, 4)  # 1是實部，2是虛部
complex_z = 1 + 3j  # 或可用更簡潔的語法來創建複數
# 獲取複數的實部和虛部
complex_y_real_part = complex_y.real  # 結果為 2.0
complex_y_imaginary_part = complex_y.imag  # 結果為 4.0
# 複雜一點的計算
complex_count_plus = complex_x + complex_z
print(complex_count_plus)  # (5+2j)
# print("complex_y.real = " + complex_y_real_part)  # TypeError: can only concatenate str (not "float") to str
# print("complex_y.imag = " + complex_y_imaginary_part)  # TypeError: can only concatenate str (not "float") to str
# 在 Python 中，字符串前面的 'f' 或者 'F' 代表著 "formatted string literals"，常被簡稱為 f-string。
# 在 f-string 中，你可以在字符串裡面用大括號 {} 包住變數名或者表達式。當該字符串被評估的時候，大括號內的內容會被評估並替換成其結果。
print("complex_y.real = " + str(complex_y_real_part))  # complex_y.real = 2.0
print(f"complex_y.imag = {complex_y_imaginary_part}")  # complex_y.imag = 4.0
print("complex_z.real = " + str(complex_z.real))  # complex_z.real = 1.0
print(f"complex_z.imag = {complex_z.imag}")  # complex_z.imag = 3.0
print(f"complex_x - complex_z = {complex_x - complex_z}")

# # 序列型別: str(字串), list(列表), tuple(元組)
str_x = "string"
list_x_int = [1, 2, 3]
list_x_str = ['apple', 'banana', 'cherry']
tuple_x_int = (1, 2, 3)
tuple_x_str = ('what', 'where', 'when', 'what', 'what')

# # 映射型別: dict(字典)
dict_x = {'name': 'Caerus', 'age': 99}
list_dict_x = [{'name': 'Caerus', 'age': 18}, {'name': 'Kairos', 'age': 36}]

# # 集合型別: set(集合-可變), frozenset(凍結的集合-不可變)
set_x = {1, 2, 3}
frozenset_x = frozenset([1, 2, 3, 4, 5, 1])
# frozenset的每個元素必須是唯一的, 其元素則是無序的, hashable(可哈希), 不可變資料型別
print(frozenset_x)  # frozenset({1, 2, 3, 4, 5}),

# # 布林型別: bool(布林)
bool_x = True

# # None型別: None(沒有值, 空值)
none_x = None

# # 範圍型別: range
# 在 Python 中，range 是一種內建的範圍型別，通常用於在 for 迴圈中進行特定次數的迭代。
# range 函數接受一到三個參數（都應為整數）並返回一個 range 對象。
# 提供一個參數，則該參數被視為終點，起始點為 0，增量為 1。
# 提供兩個參數，則它們分別被視為起始點和終點，增量為 1。
# 提供三個參數，則它們分別被視為起始點和終點，增量為第三個參數。
# range with one argument (stop)
range_r1 = range(5)
print(list(range_r1))  # prints: [0, 1, 2, 3, 4]
# range with two arguments (start, stop)
range_r2 = range(5, 10)
print(list(range_r2))  # prints: [5, 6, 7, 8, 9]
# range with three arguments (start, stop, step)
range_r3 = range(0, 10, 2)
print(list(range_r3))  # prints: [0, 2, 4, 6, 8]

# # 位元組和位元組陣列型別: bytes(不可變), bytearray(可變)
# 使用一個整數創建 bytes
bytes_b1 = bytes(10)
print(bytes_b1)  # 輸出：b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# 使用一個字串和一個編碼方式創建 bytes
bytes_b2 = bytes("Hello, world!", "utf-8")
print(bytes_b2)  # 輸出：b'Hello, world!'
# 使用一個可迭代對象創建 bytes
bytes_b3 = bytes([65, 66, 67])
print(bytes_b3)  # 輸出：b'ABC'
# 使用一個整數創建 bytearray
# (需要注意的是，雖然 bytearray 是可變的，但其中的每個位元組仍然必須是 0-255（包含 0 和 255）範圍內的整數。
#  如果嘗試添加一個超出這個範圍的整數，Python 將引發異常。)
bytearray_b1 = bytearray(10)
print(bytearray_b1)  # 輸出：bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
# 使用一個字串和一個編碼方式創建 bytearray
bytearray_b2 = bytearray("Hello, world!", "utf-8")
print(bytearray_b2)  # 輸出：bytearray(b'Hello, world!')
# 使用一個可迭代對象創建 bytearray
bytearray_b3 = bytearray([65, 66, 67])
print(bytearray_b3)  # 輸出：bytearray(b'ABC')
# 但可以像操作列表一樣操作 bytearray 對象，例如修改、刪除或者新增元素：
# 修改第一個元素
bytearray_b3[0] = 68
print(bytearray_b3)  # 輸出：bytearray(b'DBC')
# 刪除第一個元素
del bytearray_b3[0]
print(bytearray_b3)  # 輸出：bytearray(b'BC')
# 新增一個元素
bytearray_b3.append(65)
print(bytearray_b3)  # 輸出：bytearray(b'BCA')

# # 記憶體檢視型別: memoryview
# 在 Python 中，memoryview 是一種內置型別，用於安全地操作其他物件的內存（buffers）。
# memoryview 物件可以讓在不複製內容的情況下訪問其他物件的內部資料。
# 這可以更有效地處理大型資料結構，例如位元組陣列、陣列模塊或 numpy 陣列等。
# 要創建 memoryview 物件，可以使用 memoryview() 函數，並將一個支援 buffer 協議（如位元組，位元組陣列等）的物件作為參數。

# 創建一個位元組陣列
byte_array = bytearray('XYZ', 'utf-8')
# 創建一個 memoryview 物件
mv = memoryview(byte_array)
# 存取 memoryview 物件的內容
# 在範例中，mv[0] 和 mv[-1] 會直接訪問 byte_array 的內存，而不會複製任何資料。數字 88 和 90 是字元 'X' 和 'Z' 的 ASCII 值。
print(mv[0])  # 輸出：88
print(mv[-1])  # 輸出：90
# 也可以使用 memoryview 物件來修改支援寫操作的 buffer 物件（如位元組陣列）的內容：
# 修改 memoryview 物件的內容
# 修改 mv 物件的內容也會修改 byte_array 物件的內容，因為他們共享同一塊內存。
# 需要注意的是，memoryview 物件本身並不擁有它所訪問的記憶體。
# 當原始物件被刪除或被回收時，任何指向該物件的 memoryview 都將變得無效。
mv[0] = 65
mv[-1] = 66
print(byte_array)  # 輸出：bytearray(b'AYB')

#
#
#
#
#
# Python 包含多種內置（built-in）資料型別，可以分為以下幾個大類：
#     數值型別：
#         int：整數型別，例如 10、3、15 等。
#         float：浮點數型別，例如 3.14、0.01、-15.22 等。
#         complex：複數型別，例如 3+4j、1-2j 等。
#     序列型別：
#         str：字串型別，例如 "hello"、"world" 等。
#         list：列表型別，例如 [1, 2, 3]、['a', 'b', 'c'] 等。
#         tuple：元組型別，例如 (1, 2, 3)、('a', 'b', 'c') 等。
#     映射型別：
#         dict：字典型別，例如 {'name': 'John', 'age': 30} 等。
#     集合型別：
#         set：集合型別，例如 {1, 2, 3}、{'a', 'b', 'c'} 等。
#         frozenset：凍結集合型別，例如 frozenset([1, 2, 3])、frozenset('abc') 等。
#     位元組和位元組陣列型別：
#         bytes：位元組型別，例如 b'hello'、b'\x01\x02\x03' 等。
#         bytearray：位元組陣列型別，例如 bytearray(b'hello')、bytearray([1, 2, 3]) 等。
#     其他型別：
#         bool：布林型別，例如 True、False。
#         range：範圍型別，例如 range(10)、range(1, 11)、range(0, 30, 5) 等。
#         memoryview：記憶體檢視型別。
# 此外，Python 還包含一些特殊的型別，例如 NoneType（None 物件的型別）、function（函數的型別）、generator（產生器的型別）等。
