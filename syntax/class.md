# Python 对象和类

## 创建类

Python 一门面向对象的语言。在 Python 中所有的东西都是对象，比如之前学习的整型、字符串等等，甚至模块、函数也都是对象。

面向对象编程时使用对象创建程序，使用对象存储数据和行为。

在 Python 中，使用关键字 class 定义类。类通常包括数据区域，用以存数数据和方法的定义。Python 中的所有类，都包含一个特殊的方法，叫作初始化（initializer），或者叫作构造方法。构造方法会在使用类创建新的对象时自动执行。例如：

```python
class Person:

      # 构造函数
      def __init__(self, name):
            self.name = name

      # 定义方法
     def whoami(self):
           return "You are " + self.name
```

上述代码中，我们创建了一个名叫 Person 的类，这个类中包含数据字段 name 和方法 whoami()。

Python 中的所有方法，包括构造方法，首个参数都是 self。这个参数指向对象本身。当我们创建一个新的对象时候，self 参数就会自动指向新创建的对象。

### __str__ 和 __init__

`__str__`方法和`__init__`方法，是两个非常有用的内置方法，`__str__`用来返回对象的字符串表达式，`__init__`用来初始化对象。

如果不用`__str__`方法，使用`print`方法打印一个对象时，会显示类似与`<main.Person object at 0x10c941890>`之类的信息，不便于理解和调试。而用`__str__`方法后，则会将对象的内容用字符串的形式返回。

例如，下面是一个时间对象的 str 方法：

```python
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
```

当你用 print 打印输出的时候，Python 会调用它的 str 方法，如下：

```bash
>>> time = Time(9, 45)
>>> print time
09:45:23
```

在我们编写一个新的 Python 类的时候，通常会在最开始位置写一个初始化方法`__init__`，以便初始化对象，然后会写一个`__str__`方法，方面我们调试程序。

## 从类中创建对象

使用类名就可创建对象。当我们调用方法时，不需要传递 self 参数，Python 会自动传递。例如：

```python
p1 = Person('tom')
print(p1.whoami())
print(p1.name)
```

输出结果为：

```python
You are tom
tom
```

我们还可以改变数据字段的值：

```python
p1.name = 'jerry'
print(p1.name)
```

输出结果为 jerry。然而，像这样从类的外部获取数据字段，属于不太好的操作方式，下面我们看如何阻止这种操作。

## 隐藏数据字段

为了隐藏数据字段，我们需要定义私有数据字段。在 Python 中，使用两个前置下划线，就可定义私有数据字段和私有方法。比如：

```python
class BankAccount:

     # 构造函数
    def __init__(self, name, money):
        self.__name = name  # 定义私有数据字段
        self.__balance = money  # 定义私有数据字段

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Insufficient funds"

    def checkbalance(self):
        return self.__balance

b1 = BankAccount('tim', 400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.checkbalance())
print(b1.withdraw(800))
print(b1.checkbalance())
```

在上述代码中，我们定义了 BankAccout 类，这个类有两个数据字段，但都是私有字段。代码运行结果为：

```python
Insufficient funds
900
800
100
```

现在，让我们尝试访问私有数据字段：

```python
print(b1.__balance)
```

结果显示：

```python
AttributeError: 'BankAccount' object has no attribute '__balance'
```

这就表明，设置为私有的数据字段，无法在类的外部访问。
