1.已知一个列表，求列表中心元素  
```python
list = [1,2,3,5,'dad']
if not len(list) % 2:
    num = [list[int(len(list)/2)],list[int(len(list)/2-1)]]
else:
    num = [list[int(len(list)/2)]]

print(num)
```
2.已知一个列表，求所有元素和 
```python
list = [1,4,5,5,6]
s = 0
for x in list:
    s += x
print(s)
```
3.已知一个列表，输出所有下标是奇数的元素
```python
list = ['ad',34,54,57,'hahd','老大',32]
print(list[1::2])
```
4.已知一个列表，输出所有元素中，值为奇数的元素。
```python
list = [43,5,38,54,3,56]
for x in list:
    if x % 2:
        print(x)
```
5.已知一个列表，将所有的元素乘以2。
```python
list = [34,354,2,'a',21,3]
for x in list:
    str = x * 2
    print(str)
```
6.已知一个列表，将所有元素加到第一个元素中。
```python
list = [42,53,346,'sf','sfg']
a = str(list[0])
for x in list[1:]:
    b = str(x)
    a += b
print(a)
```
7.已知一个列表A，将奇数位置元素存到B列表中，偶数元素存到C列表中。
```python
A = [32,42,5,324,'23s','sfs']
B = []
C = []
for x in A[1::2]:
    B.append(x)
print(B)
for y in A[0::2]:
    C.append(y)
print(C)
```
8.把A列表的前5个元素复制到B列表中。
```python
A = [24,'dfs',423,4,[42,45],'sdf']
B = []
for x in A[0:5]:
    B.append(x)
print(B)
```
9. 有一个长度是10的列表，按递增排列，用户输入一个数，插入适当位置。
```python
list = [1,2,3,4,5,6,7,8,9,10]
num = 5

for x in range(10):
        if int(list[x]) > num:
                list.insert(x,num)
                break
print(list)
```
10. 自己实现列表的count方法的功能。
```python
list = [23,234,56,'345']
a = 23
count = 0
for x in list:
    if x == a :
        count += 1
print(count)
```
11.自己实现列表的extend方法的功能。
```python
list = [1,'3s',23,34]
list1 = [2,3]
for x in list1:
    list.append(x)
print(list)
```
12.自己实现列表的index方法
```python
list = [1,5,3,3,634,53]
a = 3
b = 0
for x in list:
    if a == x:
        print(b)
        break
    b += 1
```





