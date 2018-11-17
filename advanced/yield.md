# yield

可以将yield简单类比为return，但是它除了返回一个值，还会记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。yield与retrun语句最大的差别是，return语句之后的代码是不执行的，而yield语句之后的代码依然得到执行。

```python
def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=",i)
        print("yield函数第 %d 次迭代结束"%(i))
    print('yield函数整体结束')

def call(i):
    return i*2
    
#使用for循环获取迭代器中的值
for i in yield_test(5):
    print('yield 函数的返回值是:',i)
```

上述代码的输出结果为：

```bash
yield 函数的返回值是: 0
i= 0
yield函数第 0 次迭代结束
yield 函数的返回值是: 2
i= 1
yield函数第 1 次迭代结束
yield 函数的返回值是: 4
i= 2
yield函数第 2 次迭代结束
yield 函数的返回值是: 6
i= 3
yield函数第 3 次迭代结束
yield 函数的返回值是: 8
i= 4
yield函数第 4 次迭代结束
yield函数整体结束
```

一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 `next()`（在 `for` 循环中会自动调用 `next()`）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。

yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 `next()` 的值，不仅代码简洁，而且执行流程异常清晰。
