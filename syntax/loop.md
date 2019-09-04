# 循环

Python 只有两种循环：for 循环和 while 循环。

## for 循环

for 循环语法：

```python
for i in iterable_object:
   # do something
```

所有在 for 循环或者 while 循环中的声明，必须使用相同的缩进值。否则会出现语法错误。

我们看下面这段代码：

```python
mylist = [1, 2, 3, 4]

for i in mylist:
    print(i)
```

在第一次循环时，值 1 被传递给 i，第二次循环时，值 2 被传递给 i。循环一直到列表变量 mylist 没有更多元素时停止。运行结果为：

```python
1
2
3
4
```

## 范围循环

range() 函数能够指定循环的起始值和结束值，从而让循环体在指定的范围内循环。例如：

```python
for i in range(10):
    print(i)                    # 0-9
for i in range(1,10):
    print(i)                    # 1-9
for i in range(1,10,2):
    print(i)                    # 1,3,5,7
```

range() 函数只有 1 个参数时，表示从 0 开始循环；两个参数时，第一个参数是起始值，第二个参数是结束值；三个参数时，第三个参数表示循环步长。

## while 循环

语法：

```python
while condition:
    # do something
```

While 循环会一直执行循环体内部的声明，直到条件变成 false。每次循环都会检查判断条件，如果为真，就继续循环。例如：

```python
count = 0

while count < 10:
    print(count)
    count += 1
```

这段代码将会打印出 0-9，直到 count 等于 10。

## 中断循环

使用 break 语句，可以中断循环，例如：

```python
count = 0

while count < 10:
    count += 1
    if count == 5:
        break
    print("inside loop", count)

print("out of while loop")
```

运行结果为：

```python
inside loop 1
inside loop 2
inside loop 3
inside loop 4
out of while loop
```

## 继续循环

当循环体内部出现 continue 声明时，会结束本次循环，跳转到循环体开始位置，开始下一次循环。例如：

```python
count = 0

while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
```

运行结果将打印出 1，3，5，7，9。
