## 数字类型

Python 3 支持3种不同类型的数字类型。

1. [int] 整型数字，比如2015。
1. [float] 浮点型数字，比如3.14。
1. [complex] 复数，比如3+2j。

### 查看变量类型

Python 使用内置函数 type()来查看变量的类型。在Python中，内置了一些高效强大的对象类型，使得开发人员不用从零开始进行编程。实际上，Python中的每样东西都是对象。虽然Python中没有类型声明，但表达式的语法决定了创建和使用的对象的类型。一旦创建了一个对象，它就和操作集合绑定了，这就是所谓的动态类型和强类型语言。即Python自动根据表达式创建类型，一旦创建成功，只能对一个对象进行适合该类型的有效操作。

``` python
>>> x = 12
>>> type(x)
 <class 'int'>
```

### 整型

整型（int）字面量在Python中属于int类。

``` python
>>> i = 100
>>> i
100
```

数字可以进行各种运算，如：

``` python
123 + 345
```

还可以使用数学模块进行更高级的运算，如产生随机数等等：

``` python
import random
print(random.random())
```

import表示引入模块，import random就是引入随机数模块。

### 浮点类型

浮点数（float）是指有小数点的数字。

``` python
>>> f = 12.3
>>> type(f)
<class 'float'>
```

### 复数

复数（Complex number）由实数和虚数两部分构成，虚数用j表示。我们可以这样定义一个复数：

``` python
>>> x = 2+3j
>>> type(x)
<class 'complex'>
```
