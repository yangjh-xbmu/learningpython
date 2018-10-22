# 异常处理

异常是指程序中的例外，违例情况。异常机制是指程序出现错误后，程序的处理方法。当出现错误后，程序的执行流程发生改变，程序的控制权转移到异常处理。

## 捕获异常

异常处理可以使开发人员能以优雅的方式处理错误。

### try-except

Python使用try-except语句处理异常。语法如下：

```python
try:
    # write some code
    # that might throw exception
except <ExceptionType>:
    # Exception handler, alert the user
```

在try语句块中，我们写入可能会产生异常的代码，当异常发生时，try语句块中的代码会被忽略，转而进入except语句块中处理异常。例如：

```python
try:
    f = open('somefile.txt', 'r')
    print(f.read())
    f.close()
except IOError:
    print('file not found')
```

上述代码的执行流程如下：

27. 先执行介于try和except之间的语句。
28. 如果没有异常，则except语句块中的代码会被跳过。
29. 如果文件不存在，则产生异常，在try语句块中的其他代码会被跳过。
30. 当异常发生时，如果异常类型和except关键字后的异常名称匹配，就执行except分支中的代码。上述代码中只能处理IOError异常，如要处理其他类型的异常，还需要添加更多的except分支。

### 多个except

try声明可以有多个except分支，它还可以选择else和finally分支。语法如下：

```python
try:
    <body>
except <ExceptionType1>:
    <handler1>
except <ExceptionTypeN>:
    <handlerN>
except:
    <handlerExcept>
else:
    <process_else>
finally:
    <process_finally>
```

except分支类似于elif。当异常发生时，将检查except分支是否和异常类型匹配。如果匹配，就执行对应except分支中的代码。在最后一个except分支中，异常类型是被忽略了的。如果异常发生，但没有匹配到最后一个except之前的分支，则最后的except分支中的代码会被执行。如果没有任何异常发生，则执行else语句中的代码。finally分支中的代码，无论是否有异常发生，都会被执行。例如：

```python
try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")
```

eval()函数允许在Python程序内部运行Python代码，了解更多关于eval()的信息，请访问<http://stackoverflow.com/questions/9383740/what-does-pythons-eval-do>

### 自定义异常

使用关键字raise，可以在方法中自定义异常。语法为：

```python
raise ExceptionClass("Your argument")
```

例如：

```python
def enterage(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")

    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")

try:
    num = int(input("Enter your age: "))
    enterage(num)

except ValueError:
    print("Only positive integers are allowed")
except:
    print("something is wrong")
```
当用户输入的年龄小于0时，程序显示结果为：

```python
only positive integers are allowed
```

