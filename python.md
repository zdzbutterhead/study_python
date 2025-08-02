## 01.初识Python

|    类型     |     核心逻辑     | 实现难度 |          典型场景           |
| :---------: | :--------------: | :------: | :-------------------------: |
| 向下/后兼容 | 新版本兼容旧内容 |   较易   | 新 Word 打开旧版`.doc`文件  |
| 向上/前兼容 | 旧版本兼容新内容 |   较难   | 旧 Word 打开新版`.docx`文件 |

> **说明**：大多数软件的版本号一般分为三段，形如A.B.C，其中A表示大版本号，当软件整体重写升级或出现不向后兼容的改变时，才会增加A；B表示功能更新，出现新功能时增加B；C表示小的改动（例如：修复了某个Bug），只要有修改就增加C。

Python 最主要的缺点是**执行效率低**（解释型语言的通病），如果更看重代码的执行效率，C、C++ 或 Go 可能是你更好的选择。

Python 的包管理工具 pip，可以帮助我们安装三方库和三方工具。

> **说明**：如果python安装过程报错或提示安装失败，很有可能是你的 Windows 系统缺失了一些动态链接库文件或缺少必要的构建工具导致的。可以在[微软官网](https://visualstudio.microsoft.com/zh-hans/downloads/)下载“Visual Studio 2022 生成工具”进行修复，如下图所示。如果不方便在微软官网下载的，也可以使用下面的百度云盘链接来获取修复工具，链接: https://pan.baidu.com/s/1iNDnU5UVdDX5sKFqsiDg5Q 提取码: cjs3。
>
> ![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day01-20/res/day01/vs_build_tools_download.png)
>
> 上面下载的“Visual Studio 2022 生成工具”需要联网才能运行，运行后会出现如下图所示的画面，大家可以参考下图勾选对应的选项进行修复。修复过程需要联网下载对应的软件包，这个过程可能会比较耗时间，修复成功后可能会要求重启你的操作系统。
>
> ![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day01-20/res/day01/vs_build_tools_install.png)

## 02.第一个Python程序

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day01-20/res/day02/using_pycharm_5.png)

在 Python 开发中，虚拟环境（Virtual Environment）是一种隔离项目依赖的机制，它允许你在同一台机器上为不同项目创建独立的 Python 运行环境，避免包版本冲突，确保项目依赖的一致性。

- **依赖冲突**：不同项目可能依赖同一包的不同版本（例如，项目 A 需要 Flask 1.0，项目 B 需要 Flask 2.0）。
- **全局污染**：直接在系统 Python 环境中安装包会导致全局环境混乱，难以管理。
- **可复现性**：虚拟环境可以记录项目依赖，便于在其他环境（如测试服务器、生产环境）中复现相同的依赖配置。

> **提示**：如果路径比较长，不愿意手动输入，我们可以通过拖拽的方式将文件直接拖到“命令提示符”或“终端”中，这样会自动输入完整的文件路径。

1. 单行注释：以`#`和空格开头，可以注释掉从`#`开始后面一整行的内容。
2. 多行注释：三个引号（通常用双引号）开头，三个引号结尾，通常用于添加多行说明性内容。

## 03.Python语言中的变量

计算机的硬件系统通常由五大部件构成，包括：**运算器**、**控制器**、**存储器**、**输入设备**和**输出设备**。

变量是数据的载体，变量的值可以被读取和修改

### 变量类型

```python
#整型(int)
print(0b100)  # 二进制整数
print(0o100)  # 八进制整数
print(100)    # 十进制整数
print(0x100)  # 十六进制整数
```

```python
#浮点型(float)
print(123.456)    # 数学写法
print(1.23456e2)  # 科学计数法
```

字符串型（`str`）：字符串是以单引号或双引号包裹起来的任意文本，比如`'hello'`和`"hello"`

布尔型（`bool`）：布尔型只有`True`、`False`两种值，要么是`True`，要么是`False`

### 变量命名

- 规则部分：
  - 规则1：变量名由**字母**、**数字**和**下划线**构成，数字不能开头。需要说明的是，这里说的字母指的是 Unicode 字符，Unicode 称为万国码，囊括了世界上大部分的文字系统，这也就意味着中文、日文、希腊字母等都可以作为变量名中的字符，但是一些特殊字符（如：`！`、`@`、`#`等）是不能出现在变量名中的。我们强烈建议大家把这里说的字母理解为**尽可能只使用英文字母**。
  - 规则2：Python 是**大小写敏感**的编程语言，简单的说就是大写的`A`和小写的`a`是两个不同的变量，这一条其实并不算规则，而是需要大家注意的地方。
  - 规则3：变量名**不要跟 Python 的关键字重名**，**尽可能避开 Python 的保留字**。这里的关键字是指在 Python 程序中有特殊含义的单词（如：`is`、`if`、`else`、`for`、`while`、`True`、`False`等），保留字主要指 Python 语言内置函数、内置模块等的名字（如：`int`、`print`、`input`、`str`、`math`、`os`等）。
- 惯例部分：
  - 惯例1：变量名通常使用**小写英文字母**，**多个单词用下划线进行连接**。
  - 惯例2：受保护的变量用单个下划线_开头。
  - 惯例3：私有的变量用两个下划线__开头。

### 变量的使用

在 Python 中可以使用`type`函数对变量的类型进行检查。

常用的和变量类型相关的函数

- `int()`：将一个数值或字符串转换成整数，可以指定进制。
- `float()`：将一个字符串（在可能的情况下）转换成浮点数。
- `str()`：将指定的对象转换成字符串形式，可以指定编码方式。
- `chr()`：将整数（字符编码）转换成对应的（一个字符的）字符串。
- `ord()`：将（一个字符的）字符串转换成对应的整数（字符编码）。

```python
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(c))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出123.45
print(bool(f))          # str类型的'hello, world'转成bool，输出True
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd'
print(ord('d'))         # str类型的'd'转成int，输出100
```

> **说明**：`str`类型转`int`类型时可以通过`base`参数来指定进制，可以将字符串视为对应进制的整数进行转换。`str`类型转成`bool`类型时，只要字符串有内容，不是`''`或`""`，对应的布尔值都是`True`。`bool`类型转`int`类型时，`True`会变成`1`，`False`会变成`0`。在 ASCII 字符集和 Unicode 字符集中， 字符`'d'`对应的编码都是`100`。

## 04.Python语言中的运算符

下面的表格按照运算符的优先级从高到低

| 运算符                                                       | 描述                           |
| ------------------------------------------------------------ | ------------------------------ |
| `[]`、`[:]`                                                  | 索引、切片                     |
| `**`                                                         | 幂                             |
| `~`、`+`、`-`                                                | 按位取反、正号、负号           |
| `*`、`/`、`%`、`//`                                          | 乘、除、模、整除               |
| `+`、`-`                                                     | 加、减                         |
| `>>`、`<<`                                                   | 右移、左移                     |
| `&`                                                          | 按位与                         |
| `^`                                                          | 按位异或                       |
| `<=`、`<`、`>`、`>=`                                         | 小于等于、小于、大于、大于等于 |
| `==`、`!=`                                                   | 等于、不等于                   |
| `is`、`is not`                                               | 身份运算符                     |
| `in`、`not in`                                               | 成员运算符                     |
| `not`、`or`、`and`                                           | 逻辑运算符                     |
| `=`、`+=`、`-=`、`*=`、`/=`、`%=`、`//=`、`**=`、`&=`、`|=`、`^=`、`>>=`、`<<=` | 赋值运算符                     |

赋值运算构成的表达式本身不产生任何值，也就是说，如果你把一个赋值表达式放到`print`函数中试图输出表达式的值，将会产生语法错误。为了解决这个问题，Python 3.8 中引入了一个新的赋值运算符`:=`，我们称之为海象运算符，大家可以猜一猜它为什么叫这个名字。海象运算符也是将运算符右侧的值赋值给左边的变量，与赋值运算符不同的是，运算符右侧的值也是整个表达式的值，看看下面的代码大家就明白了。

```python
#print((a = 10))
print((a := 10))  # 10
print(a)          # 10
```

> **提示**：上面第1行代码如果不注释掉，运行代码会看到`SyntaxError: invalid syntax`错误信息，注意，这行代码中我们给`a = 10`加上了圆括号，如果不小心写成了`print(a = 10)`，会看到`TypeError: 'a' is an invalid keyword argument for print()`错误信息，后面讲到函数的时候，大家就会明白这个错误提示是什么意思了。

比较运算符也称为关系运算符（左右比较什么都行），包括`==`、`!=`、`<`、`>`、`<=`、`>=`。

逻辑运算符（左右只能比较布尔值）有三个，分别是`and`、`or`和`not`。如果`and`运算符左边的布尔值是`False`，不管右边的布尔值是什么，最终的结果都是`False`，这时运算符右边的布尔值会被跳过（专业的说法叫短路处理，如果`and`右边是一个表达式，那么这个表达式不会执行）。`or`运算符也是有短路功能的。`not`运算符的后面可以跟一个布尔值。

```python
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
```

上面代码中的`input`函数用于从键盘接收用户输入，由于输入的都是字符串，如果想处理成浮点小数来做后续的运算，可以用我们上一课讲解的类型转换的方法，用`float`函数将`str`类型处理成`float`类型。

上面的代码中，我们对`print`函数输出的内容进行了格式化处理，`print`输出的字符串中有两个`%.1f`占位符，这两个占位符会被`%`之后的`(f, c)`中的两个`float`类型的变量值给替换掉，浮点数小数点后保留1位有效数字。如果字符串中有`%d`占位符，那么我们会用`int`类型的值替换掉它，如果字符串中有`%s`占位符，那么它会被`str`类型的值替换掉。

除了上面格式化输出的方式外，Python 中还可以用下面的办法来格式化输出，我们给出一个带占位符的字符串，字符串前面的`f`表示这个字符串是需要格式化处理的，其中的`{f:.1f}`和`{c:.1f}`可以先看成是`{f}`和`{c}`，表示输出时会用变量`f`和变量`c`的值替换掉这两个占位符，后面的`:.1f`表示这是一个浮点数，小数点后保留1位有效数字。

```python
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print(f'{f:.1f}') #输出f的“值”，对格式有要求才用冒号，直接用{f}也可以，会直接输出f的值
print(f'{f=:.1f}') #输出“f=值”
```

Python 中有一个名为`math` 的内置模块，该模块中定义了名为`pi`的变量，它的值就是圆周率。`import math`表示导入`math`模块，导入该模块以后，才能用`math.pi`得到圆周率的值。

## 05.分支结构

### 使用if和else构造分支结构

需要说明的是，不同于 C、C++、Java 等编程语言，Python 中没有用花括号来构造代码块而是**使用缩进的方式来表示代码的层次结构**，如果`if`条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了。换句话说，若干行连续的语句如果保持了相同的缩进，那么它们就属于同一个**代码块**，相当于是一个执行的整体。缩进可以使用任意数量的空格，但**通常使用4个空格**，强烈建议大家**不要使用制表键（Tab键）来缩进代码**，如果你已经习惯了这么做，可以设置你的代码编辑器自动将 1 个制表键变成 4 个空格，很多代码编辑器都支持这项功能，PyCharm 中默认也是这样设定的。还有一点，在 C、C++、Java 等编程语言中，`18.5 <= bmi < 24`要写成两个条件`bmi >= 18.5`和`bmi < 24`，然后把两个条件用与运算符连接起来，Python 中也可以这么做，例如刚才的`if`语句也可以写成`if bmi >= 18.5 and bmi < 24:`，但是没有必要，难道`if 18.5 <= bmi < 24:`这个写法它不香吗？

```python
height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18.5:
    print('你的体重过轻！')
elif bmi < 24:
    print('你的身材很棒！')
elif bmi < 27:
    print('你的体重过重！')
elif bmi < 30:
    print('你已轻度肥胖！')
elif bmi < 35:
    print('你已中度肥胖！')
else:
    print('你已重度肥胖！')
```

### 使用match和case构造分支结构

```python
status_code = int(input('响应状态码: '))
if status_code == 400:
    description = 'Bad Request'
elif status_code == 401:
    description = 'Unauthorized'
elif status_code == 403:
    description = 'Forbidden'
elif status_code == 404:
    description = 'Not Found'
elif status_code == 405:
    description = 'Method Not Allowed'
elif status_code == 418:
    description = 'I am a teapot'
elif status_code == 429:
    description = 'Too many requests'
else:
    description = 'Unknown status Code'
print('状态码描述:', description)

#以下代码和上述代码功能相同
status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
```

> **说明**：带有`_`的`case`语句在代码中起到通配符的作用，如果前面的分支都没有匹配上，代码就会来到`case _`。`case _`的是可选的，并非每种分支结构都要给出通配符选项。如果分支中出现了`case _`，它只能放在分支结构的最后面，如果它的后面还有其他的分支，那么这些分支将是不可达的。

计算三角形面积的公式叫做海伦公式，假设有一个三角形，边长分别为 a 、 b 、 c ，那么三角的面积 A 可以由公式 A=根号下s(s−a)(s−b)(s−c) 得到，其中， s=（a+b+c）/2 表示半周长。

## 06.循环结构

### for-in循环

```python
"""
每隔1秒输出一次“hello, world”，持续1小时
"""
import time

for _ in range(3600):
    print('hello, world')
    time.sleep(1)
```

- `range(101)`：可以用来产生`0`到`100`范围的整数，需要注意的是取不到`101`。
- `range(1, 101)`：可以用来产生`1`到`100`范围的整数，相当于是左闭右开的设定，即`[1, 101)`。
- `range(1, 101, 2)`：可以用来产生`1`到`100`的奇数，其中`2`是步长（跨度），即每次递增的值，`101`取不到。
- `range(100, 0, -2)`：可以用来产生`100`到`1`的偶数，其中`-2`是步长（跨度），即每次递减的值，`0`取不到。

代码的输出操作和休眠操作都没有用到循环变量`i`，对于不需要用到循环变量的`for-in`循环结构，按照 Python 的编程惯例，我们通常把循环变量命名为`_`，修改后的代码如下所示。虽然结果没什么变化，但是这样写显得你更加专业，逼格瞬间拉满。

### while循环

### break和continue

`break`只能终止它所在的那个循环，这一点在使用嵌套循环结构时需要引起注意，后面我们会讲到什么是嵌套的循环结构。除了`break`之外，还有另一个在循环结构中可以使用的关键字`continue`，它可以用来放弃本次循环后续的代码直接让循环进入下一轮

### 嵌套的循环结构

```python
"""
打印乘法口诀表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}×{j}={i * j}', end='\t')
    print()
```

```python
"""
输入两个正整数求它们的最大公约数
"""
x = int(input('x = '))
y = int(input('y = '))
while y % x != 0:
    x, y = y % x, x
print(f'最大公约数: {x}')
```

`x, y = y % x, x`语句表示将`y % x`的值赋给`x`，将`x` 原来的值赋给`y`。

欧几里得算法（Euclidean algorithm），也称为辗转相除法，是一种用于计算两个非负整数的最大公约数（GCD, Greatest Common Divisor）的高效算法。其核心思想是通过不断用较小数去除较大数，直到余数为零，此时的除数即为最大公约数。

Python 标准库的`random`模块，该模块的`randrange(1,101)`函数帮助我们生成了 1 到 100 范围的随机数（不包括 100）。

## 07.分支和循环结构实战

将一个不知道有多少位的正整数进行反转，例如将 12389 变成 98321

```python
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
```

百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？翻译成现代文是：公鸡 5 元一只，母鸡 3 元一只，小鸡 1 元三只，用 100 块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

```python
for x in range(0, 21):
    for y in range(0, 34):
        for z in range(0, 100, 3):
            if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
                print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')
```

上面使用的方法叫做**穷举法**，也称为**暴力搜索法**，这种方法通过一项一项的列举备选解决方案中所有可能的候选项，并检查每个候选项是否符合问题的描述，最终得到问题的解。上面的代码中，我们使用了嵌套的循环结构，假设公鸡有`x`只，显然`x`的取值范围是 0 到 20，假设母鸡有`y`只，它的取值范围是 0 到 33，假设小鸡有`z`只，它的取值范围是 0 到 99 且取值是 3 的倍数。这样，我们设置好 100 只鸡的条件`x + y + z == 100`，设置好 100 块钱的条件`5 * x + 3 * y + z // 3 == 100`，当两个条件同时满足时，就是问题的正确答案，我们用`print`函数输出它。这种方法看起来比较笨拙，但对于运算能力非常强大的计算机来说，通常都是一个可行的甚至是不错的选择，只要问题的解存在就能够找到它。

事实上，上面的代码还有更好的写法，既然我们已经假设公鸡有`x`只，母鸡有`y`只，那么小鸡的数量就应该是`100 - x - y`，这样减少一个条件，我们就可以把上面三层嵌套的`for-in`循环改写为两层嵌套的`for-in`循环。循环次数减少了，代码的执行效率就有了显著的提升，如下所示。

```python
for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')
```

## 08.常用的数据结构之列表

### 创建列表

在 Python 中，**列表是由一系元素按特定顺序构成的数据序列**，这就意味着如果我们定义一个列表类型的变量，**可以用它来保存多个数据**。在 Python 中，可以使用`[]`字面量语法来定义列表，列表中的多个元素用逗号进行分隔

```python
items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]
print(items1)  # [35, 12, 99, 68, 55, 35, 87]
print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # [100, 12.3, 'Python', True]
```

> **说明**：列表中可以有重复元素，例如`items1`中的`35`；列表中可以有不同类型的元素，例如`items3`中有`int`类型、`float`类型、`str`类型和`bool`类型的元素，但是我们通常并不建议将不同类型的元素放在同一个列表中，主要是操作起来极为不便。

列表类型的变量起名字时，变量名通常用复数形式的单词。

通过 Python 内置的`list`函数将其他序列变成列表。准确的说，`list`并不是一个普通的函数，它是创建列表对象的构造器，后面的课程会为大家介绍对象和构造器这些概念。

```python
items4 = list(range(1, 10))
items5 = list('hello')
print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(items5)  # ['h', 'e', 'l', 'l', 'o']
```

### 列表的运算

使用`+`运算符实现两个列表的拼接，拼接运算会将两个列表中的元素连接起来放到一个列表中

使用`*`运算符实现列表的重复运算，`*`运算符会将列表元素重复指定的次数

使用`in`或`not in`运算符判断一个元素在不在列表中

```python
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
items5 += items6
print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']
print(29 in items6)  # True
print(99 in items6)  # False
print('C++' not in items7)     # True
print('Python' not in items7)  # False
```

当我们想操作列表中的某个元素时，可以使用`[]`运算符，通过在`[]`中指定元素的位置来访问该元素，这种运算称为索引运算。需要说明的是，`[]`的元素位置可以是`0`到`N - 1`的整数，也可以是`-1`到`-N`的整数，分别称为正向索引和反向索引，其中`N`代表列表元素的个数。对于正向索引，`[0]`可以访问列表中的第一个元素，`[N - 1]`可以访问最后一个元素；对于反向索引，`[-1]`可以访问列表中的最后一个元素，`[-N]`可以访问第一个元素

```python
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])   # apple
print(items8[2])   # pitaya
print(items8[4])   # watermelon
items8[2] = 'durian'
print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
print(items8[-5])  # 'apple'
print(items8[-4])  # 'waxberry'
print(items8[-1])  # watermelon
items8[-4] = 'strawberry'
print(items8)      # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']
```

如果希望一次性访问列表中的多个元素，我们可以使用切片运算。切片运算是形如`[start:end:stride]`的运算符，其中`start`代表访问列表元素的起始位置，`end`代表访问列表元素的终止位置（终止位置的元素无法访问），而`stride`则代表了跨度，简单的说就是位置的增量，比如我们访问的第一个元素在`start`位置，那么第二个元素就在`start + stride`位置，当然`start + stride`要小于`end`。

```python
print(items8[1:3:1])     # ['strawberry', 'durian']
print(items8[0:3:1])     # ['apple', 'strawberry', 'durian']
print(items8[0:5:2])     # ['apple', 'durian', 'watermelon']
print(items8[-4:-2:1])   # ['strawberry', 'durian']
print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']
```

如果`start`值等于`0`，那么在使用切片运算符时可以将其省略；如果`end`值等于`N`，`N`代表列表元素的个数，那么在使用切片运算符时可以将其省略；如果`stride`值等于`1`，那么在使用切片运算符时也可以将其省略。所以，下面的代码跟上面的代码作用完全相同。

```python
print(items8[1:3])     # ['strawberry', 'durian']
print(items8[:3:1])    # ['apple', 'strawberry', 'durian']
print(items8[::2])     # ['apple', 'durian', 'watermelon']
print(items8[-4:-2])   # ['strawberry', 'durian']
print(items8[-2::-1])  # ['peach', 'durian', 'strawberry', 'apple']
```

事实上，我们还可以通过切片操作修改列表中的元素

```python
items8[1:3] = ['x', 'o']
print(items8)  # ['apple', 'x', 'o', 'peach', 'watermelon']
```

两个列表还可以做关系运算，我们可以比较两个列表是否相等，也可以给两个列表比大小

```python
nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
nums3 = [3, 2, 1]
print(nums1 == nums2)  # True
print(nums1 != nums2)  # False
print(nums1 <= nums3)  # True
print(nums2 >= nums3)  # False
```

> **说明**：上面的`nums1`和`nums2`对应元素完全相同，所以`==`运算的结果是`True`。`nums2`和`nums3`的比较，由于`nums2`的第一个元素`1`小于`nums3`的第一个元素`3`，所以`nums2 >= nums3`比较的结果是`False`。两个列表的关系运算在实际工作并不那么常用，如果实在不理解就跳过吧，不用纠结。

默认情况下，Python 列表比较会逐个检查所有元素，而非只比较第一个元素。比较规则类似于字典序（lexicographical order），从左到右依次比较，直到找到差异或确定相等。

### 元素的遍历

```python
# 方法一：在循环结构中通过索引运算，遍历列表元素。
languages = ['Python', 'Java', 'C++', 'Kotlin']
for index in range(len(languages)):
    print(languages[index])


# 方法二：直接对列表做循环，循环变量就是列表元素的代表。
languages = ['Python', 'Java', 'C++', 'Kotlin']
for language in languages:
    print(language)
```

### 列表的方法

列表类型的变量拥有很多方法可以帮助我们操作一个列表，假设我们有名为`foos`的列表，列表有名为`bar`的方法，那么使用列表方法的语法是：`foos.bar()`，这是一种通过对象引用调用对象方法的语法。后面我们讲面向对象编程的时候，还会对这种语法进行详细的讲解，这种语法也称为给对象发消息。

#### 添加和删除元素

列表是一种可变容器，可变容器指的是我们可以向容器中添加元素、可以从容器移除元素，也可以修改现有容器中的元素。我们可以使用列表的`append`方法向列表中追加元素，使用`insert`方法向列表中插入元素。追加指的是将元素添加到列表的末尾，而插入则是在指定的位置添加新元素

```python
languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')
print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
languages.insert(1, 'SQL')
print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
```

我们可以用列表的`remove`方法从列表中删除指定元素，需要注意的是，如果要删除的元素并不在列表中，会引发`ValueError`错误导致程序崩溃，所以建议大家在删除元素时，先用之前讲过的成员运算做一个判断。我们还可以使用`pop`方法从列表中删除元素，`pop`方法默认删除列表中的最后一个元素，当然也可以给一个位置，删除指定位置的元素。在使用`pop`方法删除元素时，如果索引的值超出了范围，会引发`IndexError`异常，导致程序崩溃。除此之外，列表还有一个`clear`方法，可以清空列表中的元素，代码如下所示。

```python
languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
languages.pop()
temp = languages.pop(1)
print(temp)       # SQL
languages.append(temp)
print(languages)  # ['Python', C++', 'SQL']
languages.clear()
print(languages)  # []
```

> **说明**：`pop`方法删除元素时会得到被删除的元素，上面的代码中，我们将`pop`方法删除的元素赋值给了名为`temp`的变量。当然如果你愿意，还可以把这个元素再次加入到列表中，正如上面的代码`languages.append(temp)`所做的那样。

`remove()` 方法**只会删除第一个匹配的元素**，而非删除所有匹配项（如果列表中有重复值，只删除第一个）。

从列表中删除元素其实还有一种方式，就是使用 Python 中的`del`关键字后面跟要删除的元素，这种做法跟使用`pop`方法指定索引删除元素没有实质性的区别，但后者会返回删除的元素，前者在性能上略优，因为`del`对应的底层字节码指令是`DELETE_SUBSCR`，而`pop`对应的底层字节码指令是`CALL_METHOD`和`POP_TOP`，如果不理解就不用管它了。

```python
items = ['Python', 'Java', 'C++']
del items[1]
print(items)  # ['Python', 'C++']
```

remove()传入的是要删除的值，而del和pop()传入的是索引值(从0开始)

#### 元素位置和频次

列表的`index`方法可以查找某个元素在列表中的索引位置，如果找不到指定的元素，`index`方法会引发`ValueError`错误；列表的`count`方法可以统计一个元素在列表中出现的次数

```python
items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))     # 0
# 从索引位置1开始查找'Python'
print(items.index('Python', 1))  # 5
print(items.count('Python'))     # 2
print(items.count('Kotlin'))     # 1
print(items.count('Swfit'))      # 0
# 从索引位置3开始查找'Java'
print(items.index('Java', 3))    # ValueError: 'Java' is not in list
```

#### 元素排序和反转

列表的`sort`操作可以实现列表元素的排序，而`reverse`操作可以实现元素的反转

```python
items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items.sort()
print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
items.reverse()
print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']
```

### 列表生成式

```python
# 场景一：创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。
items = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)
# 使用列表生成式做同样的事情
items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)
```

```python
# 场景二：有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    nums2.append(num ** 2)
print(nums2)
# 使用列表生成式做同样的事情
nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)
```

使用列表生成式创建列表不仅代码简单优雅，而且性能上也优于使用`for-in`循环和`append`方法向空列表中追加元素的方式。为什么说生成式有更好的性能呢，那是因为 Python 解释器的字节码指令中有专门针对生成式的指令（`LIST_APPEND`指令）；而`for`循环是通过方法调用（`LOAD_METHOD`和`CALL_METHOD`指令）的方式为列表添加元素，方法调用本身就是一个相对比较耗时的操作。对这一点不理解也没有关系，记住“**强烈建议用生成式语法来创建列表**”这个结论就可以了。

### 嵌套列表

Python 语言没有限定列表中的元素必须是相同的数据类型，也就是说一个列表中的元素可以任意的数据类型，当然也包括列表本身。如果列表中的元素也是列表，那么我们可以称之为嵌套的列表。嵌套的列表可以用来表示表格或数学上的矩阵，例如：我们想保存5个学生3门课程的成绩，可以用如下所示的列表。

```python
scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
print(scores[0])
print(scores[0][1])
```

如果想通过键盘输入的方式来录入5个学生3门课程的成绩并保存在列表中

```python
scores = []
for _ in range(5):
    temp = []
    for _ in range(3):
        score = int(input('请输入: '))
        temp.append(score)
    scores.append(temp)
print(scores)
```

如果想通过产生随机数的方式来生成5个学生3门课程的成绩并保存在列表中，我们可以使用列表生成式

```python
import random

scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)
```

> **说明**：上面的代码`[random.randrange(60, 101) for _ in range(3)] `可以产生由3个随机整数构成的列表，我们把这段代码又放在了另一个列表生成式中作为列表的元素，这样的元素一共生成5个，最终得到了一个嵌套列表。

### 列表的应用

下面我们通过一个双色球随机选号的例子为大家讲解列表的应用。双色球是由中国福利彩票发行管理中心发售的乐透型彩票，每注投注号码由`6`个红色球和`1`个蓝色球组成。红色球号码从`1`到`33`中选择，蓝色球号码从`1`到`16`中选择。每注需要选择`6`个红色球号码和`1`个蓝色球号码

```python
import random

red_balls = list(range(1, 34))
selected_balls = []
# 添加6个红色球到选中列表
for _ in range(6):
    # 生成随机整数代表选中的红色球的索引位置
    index = random.randrange(len(red_balls))
    # 将选中的球从红色球列表中移除并添加到选中列表
    selected_balls.append(red_balls.pop(index))
# 对选中的红色球排序
selected_balls.sort()
# 输出选中的红色球
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# 随机选择1个蓝色球
blue_ball = random.randrange(1, 17)
# 输出选中的蓝色球
print(f'\033[034m{blue_ball:0>2d}\033[0m')
```

> **说明**：上面代码中`print(f'\033[0m...\033[0m')`是为了控制输出内容的颜色，红色球输出成红色，蓝色球输出成蓝色。其中省略号代表我们要输出的内容，`\033[0m`是一个控制码，表示关闭所有属性，也就是说之前的控制码将会失效，你也可以将其简单的理解为一个定界符，`m`前面的`0`表示控制台的显示方式为默认值，`0`可以省略，`1`表示高亮，`5`表示闪烁，`7`表示反显等。在`0`和`m`的中间，我们可以写上代表颜色的数字，比如`30`代表黑色，`31`代表红色，`32`代表绿色，`33`代表黄色，`34`代表蓝色等。
>
> 0>2d中，0指定用 `0` 填充宽度不足的部分。若改为其他字符（如 `*`），则用该字符填充。>右对齐，即数值靠右放置，左侧用填充字符补足宽度。2为输出字符串的最小宽度。d表示将数值作为十进制整数处理。

**`random.choice()`：随机选择单个元素**,从**非空序列**（如列表、元组、字符串）中随机选择一个元素。若序列为空，会抛出 `IndexError`。

**`random.sample()`：随机选择多个不重复元素**,从**总体序列或集合**中随机选择指定数量的**唯一元素**（不重复），返回一个新列表。若采样数量超过总体大小，会抛出 `ValueError`。

Python 中的列表底层是一个可以动态扩容的数组，列表元素在计算机内存中是连续存储的，所以可以实现随机访问（通过一个有效的索引获取对应的元素且操作时间与列表元素个数无关）。

```python
import random

from rich.console import Console
from rich.table import Table

# 创建控制台
console = Console()

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    # 向表格中添加行（序号，红色球，蓝色球）
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

# 通过控制台输出表格
console.print(table)
```

`" ".join([...])`是将列表中的多个字符串用空格拼接成一个完整的字符串

## 09.常用数据结构之元组

### 元组的定义和运算

在 Python 语言中，元组也是多个元素按照一定顺序构成的序列。元组和列表的不同之处在于，**元组是不可变类型**，这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能修改。如果试图修改元组中的元素，将引发`TypeError`错误，导致程序崩溃。定义元组通常使用形如`(x, y, z)`的字面量语法，元组类型支持的运算符跟列表是一样的，我们可以看看下面的代码。

```python
# 定义一个三元组
t1 = (35, 12, 98)
# 定义一个四元组
t2 = ('骆昊', 45, True, '四川成都')

# 查看变量的类型
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>

# 查看元组中元素的数量
print(len(t1))  # 3
print(len(t2))  # 4

# 索引运算
print(t1[0])    # 35
print(t1[2])    # 98
print(t2[-1])   # 四川成都

# 切片运算
print(t2[:2])   # ('骆昊', 43)
print(t2[::3])  # ('骆昊', '四川成都')

# 循环遍历元组中的元素
for elem in t1:
    print(elem)

# 成员运算
print(12 in t1)         # True
print(99 in t1)         # False
print('Hao' not in t2)  # True

# 拼接运算
t3 = t1 + t2
print(t3)  # (35, 12, 98, '骆昊', 43, True, '四川成都')

# 比较运算
print(t1 == t3)            # False
print(t1 >= t3)            # False
print(t1 <= (35, 11, 99))  # False
```

一个元组中如果有两个元素，我们就称之为二元组；一个元组中如果五个元素，我们就称之为五元组。需要提醒大家注意的是，`()`表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则`()`就不是代表元组的字面量语法，而是改变运算优先级的圆括号，所以`('hello', )`和`(100, )`才是一元组，而`('hello')`和`(100)`只是字符串和整数。

```python
a = ()
print(type(a))  # <class 'tuple'>
b = ('hello')
print(type(b))  # <class 'str'>
c = (100)
print(type(c))  # <class 'int'>
d = ('hello', )
print(type(d))  # <class 'tuple'>
e = (100, )
print(type(e))  # <class 'tuple'>
```

当我们把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型；当我们把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量

```python
# 打包操作
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
print(a)        # (1, 10, 100)
# 解包操作
i, j, k = a
print(i, j, k)  # 1 10 100
```

在解包时，如果解包出来的元素个数和变量个数不对应，会引发`ValueError`异常，错误信息为：`too many values to unpack`（解包的值太多）或`not enough values to unpack`（解包的值不足）。

```python
a = 1, 10, 100, 1000
# i, j, k = a             # ValueError: too many values to unpack (expected 3)
# i, j, k, l, m, n = a    # ValueError: not enough values to unpack (expected 6, got 4)
```

有一种解决变量个数少于元素的个数方法，就是使用星号表达式。通过星号表达式，我们可以让一个变量接收多个值，代码如下所示。需要注意两点：首先，用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素；其次，在解包语法中，星号表达式只能出现一次。

```python
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)        # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)        # 1 [10, 100] 1000
*i, j, k = a
print(i, j, k)        # [1, 10] 100 1000
*i, j = a
print(i, j)           # [1, 10, 100] 1000
i, *j = a
print(i, j)           # 1 [10, 100, 1000]
i, j, k, *l = a
print(i, j, k, l)     # 1 10 100 [1000]
i, j, k, l, *m = a
print(i, j, k, l, m)  # 1 10 100 1000 []
```

需要说明一点，解包语法对所有的序列都成立，这就意味着我们之前讲的列表、`range`函数构造的范围序列甚至字符串都可以使用解包语法。大家可以尝试运行下面的代码，看看会出现怎样的结果。

```python
a, b, *c = range(1, 10)
print(a, b, c)             # 1 2 [3, 4, 5, 6, 7, 8, 9]
a, b, c = [1, 10, 100]
print(a, b, c)             # 1 10 100
a, *b, c = 'hello'
print(a, b, c)             # h ['e', 'l', 'l'] o
```

### 交换变量的值

交换变量的值是写代码时经常用到的一个操作，但是在很多编程语言中，交换两个变量的值都需要借助一个中间变量才能做到，如果不用中间变量就需要使用比较晦涩的位运算来实现。在 Python 中，交换两个变量`a`和`b`的值只需要使用如下所示的代码。

```python
a, b = b, a
```

同理，如果要将三个变量`a`、`b`、`c`的值互换，即`b`的值赋给`a`，`c`的值赋给`b`，`a`的值赋给`c`，也可以如法炮制。

```python
a, b, c = b, c, a
```

需要说明的是，上面的操作并没有用到打包和解包语法，Python 的字节码指令中有`ROT_TWO`和`ROT_THREE`这样的指令可以直接实现这个操作，效率是非常高的。**但是如果有多于三个变量的值要依次互换，这个时候是没有直接可用的字节码指令的**，需要通过打包解包的方式来完成变量之间值的交换。

### 元组和列表的比较

1. 元组是不可变类型，**不可变类型更适合多线程环境**，因为它降低了并发访问变量的同步化开销。关于这一点，我们会在后面讲解并发编程的时候跟大家一起探讨。
2. 元组是不可变类型，通常**不可变类型在创建时间上优于对应的可变类型**。我们可以使用`timeit`模块的`timeit`函数来看看创建保存相同元素的元组和列表各自花费的时间，`timeit`函数的`number`参数表示代码执行的次数。下面的代码中，我们分别创建了保存`1`到`9`的整数的列表和元组，每个操作执行`10000000`次，统计运行时间。

```python
import timeit

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))
```

Python 中的元组和列表类型是可以相互转换的，我们可以通过下面的代码来完成该操作。

```python
infos = ('骆昊', 43, True, '四川成都')
# 将元组转换成列表
print(list(infos))  # ['骆昊', 43, True, '四川成都']

frts = ['apple', 'banana', 'orange']
# 将列表转换成元组
print(tuple(frts))  # ('apple', 'banana', 'orange')
```

## 10.常用数据结构之字符串

### 字符串的定义

所谓**字符串**，就是**由零个或多个字符组成的有限序列**，一般记为：s=a1a2⋯an,,,,,(0≤n≤∞)

在 Python 程序中，我们把单个或多个字符用单引号或者双引号包围起来，就可以表示一个字符串。字符串中的字符可以是特殊符号、英文字母、中文字符、日文的平假名或片假名、希腊字母、Emoji 字符（如：💩、🐷、🀄️）等。

#### 转义字符

我们可以在字符串中使用`\`（反斜杠）来表示转义，也就是说`\`后面的字符不再是它原来的意义，例如：`\n`不是代表字符`\`和字符`n`，而是表示换行；`\t`也不是代表字符`\`和字符`t`，而是表示制表符。所以如果字符串本身又包含了`'`、`"`、`\`这些特殊的字符，必须要通过`\`进行转义处理。

#### 原始字符串

Python 中有一种以`r`或`R`（raw的缩写）开头的字符串，这种字符串被称为原始字符串，意思是字符串中的每个字符都是它本来的含义，没有所谓的转义字符。例如，在字符串`'hello\n'`中，`\n`表示换行；而在`r'hello\n'`中，`\n`不再表示换行，就是字符`\`和字符`n`。

#### 字符的特殊表示

Python 中还允许在`\`后面还可以跟一个八进制或者十六进制数来表示字符，例如`\141`和`\x61`都代表小写字母`a`，前者是八进制的表示法，后者是十六进制的表示法。另外一种表示字符的方式是在`\u`后面跟 Unicode 字符编码，例如`\u9a86\u660a`代表的是中文“骆昊”。

```python
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1)
print(s2)
```

### 字符串的运算

Python 语言为字符串类型提供了非常丰富的运算符，有很多运算符跟列表类型的运算符作用类似。例如，我们可以使用`+`运算符来实现字符串的拼接，可以使用`*`运算符来重复一个字符串的内容，可以使用`in`和`not in`来判断一个字符串是否包含另外一个字符串，我们也可以用`[]`和`[:]`运算符从字符串取出某个字符或某些字符。

#### 拼接和重复

```python
s1 = 'hello' + ', ' + 'world'
print(s1)    # hello, world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2
print(s1)    # hello, world!!!
s1 *= 2
print(s1)    # hello, world!!!hello, world!!!
```

#### 比较运算

对于两个字符串类型的变量，可以直接使用比较运算符来判断两个字符串的相等性或比较大小。需要说明的是，因为字符串在计算机内存中也是以二进制形式存在的，那么字符串的大小比较比的是每个字符对应的编码的大小。例如`A`的编码是`65`， 而`a`的编码是`97`，所以`'A' < 'a'`的结果相当于就是`65 < 97`的结果，这里很显然是`True`；而`'boy' < 'bad'`，因为第一个字符都是`'b'`比不出大小，所以实际比较的是第二个字符的大小，显然`'o' < 'a'`的结果是`False`，所以`'boy' < 'bad'`的结果是`False`。如果不清楚两个字符对应的编码到底是多少，可以使用`ord`函数来获得，之前我们有提到过这个函数。例如`ord('A')`的值是`65`，而`ord('昊')`的值是`26122`。下面的代码展示了字符串的比较运算，请大家仔细看看。

```python
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)             # False
print(s1 < s2)              # True
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
s3 = '骆昊'
print(ord('骆'))            # 39558
print(ord('昊'))            # 26122
s4 = '王大锤'
print(ord('王'))            # 29579
print(ord('大'))            # 22823
print(ord('锤'))            # 38180
print(s3 >= s4)             # True
print(s3 != s4)             # True
```

#### 成员运算

Python 中可以用`in`和`not in`判断一个字符串中是否包含另外一个字符或字符串，跟列表类型一样，`in`和`not in`称为成员运算符，会产生布尔值`True`或`False`

#### 获取字符串长度

获取字符串长度跟获取列表元素个数一样，使用内置函数`len`

#### 索引和切片

字符串的索引和切片操作跟列表、元组几乎没有区别，因为字符串也是一种有序序列，可以通过正向或反向的整数索引访问其中的元素。但是有一点需要注意，因为**字符串是不可变类型**，所以**不能通过索引运算修改字符串中的字符**。

### 字符的遍历

如果希望遍历字符串中的每个字符，可以使用`for-in`循环，有如下所示的两种方式

```python
# 方法一
s = 'hello'
for i in range(len(s)):
    print(s[i])
```

```python
# 方法二
s = 'hello'
for elem in s:
    print(elem)
```

### 字符串的方法

在 Python 中，我们可以通过字符串类型自带的方法对字符串进行操作和处理，假设我们有名为`foo`的字符串，字符串有名为`bar`的方法，那么使用字符串方法的语法是：`foo.bar()`，这是一种通过对象引用调用对象方法的语法，跟前面使用列表方法的语法是一样的。

#### 大小写相关操作

```python
s1 = 'hello, world!'
# 字符串首字母大写
print(s1.capitalize())  # Hello, world!
# 字符串每个单词首字母大写
print(s1.title())       # Hello, World!
# 字符串变大写
print(s1.upper())       # HELLO, WORLD!
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())       # goodbye
# 检查s1和s2的值
print(s1)               # hello, world
print(s2)               # GOODBYE
```

> **说明**：由于字符串是不可变类型，使用字符串的方法对字符串进行操作会产生新的字符串，但是原来变量的值并没有发生变化。所以上面的代码中，当我们最后检查`s1`和`s2`两个变量的值时，`s1`和`s2` 的值并没有发生变化。

#### 查找操作

如果想在一个字符串中从前向后查找有没有另外一个字符串，可以使用字符串的`find`或`index`方法。在使用`find`和`index`方法时还可以通过方法的参数来指定查找的范围，也就是查找不必从索引为`0`的位置开始。

```python
s = 'hello, world!'
print(s.find('or'))      # 8
print(s.find('or', 9))   # -1
print(s.find('of'))      # -1
print(s.index('or'))     # 8
print(s.index('or', 9))  # ValueError: substring not found
```

> **说明**：`find`方法找不到指定的字符串会返回`-1`，`index`方法找不到指定的字符串会引发`ValueError`错误。

`find`和`index`方法还有逆向查找（从后向前查找）的版本，分别是`rfind`和`rindex`，代码如下所示。

```python
s = 'hello world!'
print(s.find('o'))       # 4
print(s.rfind('orl'))      # 7(返回的是首字母的索引)
print(s.rfind('o'))      # 7
print(s.rindex('o'))     # 7
# print(s.rindex('o', 8))  # ValueError: substring not found
```

#### 性质判断

可以通过字符串的`startswith`、`endswith`来判断字符串是否以某个字符串开头和结尾；还可以用`is`开头的方法判断字符串的特征，这些方法都返回布尔值，代码如下所示。

```python
s1 = 'hello, world!'
print(s1.startswith('He'))   # False
print(s1.startswith('hel'))  # True
print(s1.endswith('!'))      # True
s2 = 'abc123456'
print(s2.isdigit())  # False
print(s2.isalpha())  # False
print(s2.isalnum())  # True
```

> **说明**：上面的`isdigit`用来判断字符串是不是完全由数字构成的，`isalpha`用来判断字符串是不是完全由字母构成的，这里的字母指的是 Unicode 字符但不包含 Emoji 字符，`isalnum`用来判断字符串是不是由字母和数字构成的。

#### 格式化

在 Python 中，字符串类型可以通过`center`、`ljust`、`rjust`方法做居中、左对齐和右对齐的处理。如果要在字符串的左侧补零，也可以使用`zfill`方法。

```python
s = 'hello, world'
print(s.center(20, '*'))  # ****hello, world****
print(s.rjust(20))        #         hello, world
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
print('33'.zfill(5))      # 00033
print('-33'.zfill(5))     # -0033
```

我们之前讲过，在用`print`函数输出字符串时，可以用下面的方式对字符串进行格式化。

```python
a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
```

当然，我们也可以用字符串的`format`方法来完成字符串的格式，代码如下所示。

```python
a = 321
b = 123
print('{0} * {1} = {2}'.format(a, b, a * b))
```

从 Python 3.6 开始，格式化字符串还有更为简洁的书写方式，就是在字符串前加上`f`来格式化字符串，在这种以`f`打头的字符串中，`{变量名}`是一个占位符，会被变量对应的值将其替换掉，代码如下所示。

```python
a = 321
b = 123
print(f'{a} * {b} = {a * b}')
```

如果需要进一步控制格式化语法中变量值的形式，可以参照下面的表格来进行字符串格式化操作。

| 变量值      | 占位符     | 格式化结果      | 说明                         |
| ----------- | ---------- | --------------- | ---------------------------- |
| `3.1415926` | `{:.2f}`   | `'3.14'`        | 保留小数点后两位             |
| `3.1415926` | `{:+.2f}`  | `'+3.14'`       | 带符号保留小数点后两位       |
| `-1`        | `{:+.2f}`  | `'-1.00'`       | 带符号保留小数点后两位       |
| `3.1415926` | `{:.0f}`   | `'3'`           | 不带小数                     |
| `123`       | `{:0>10d}` | `'0000000123'`  | 左边补`0`，补够10位          |
| `123`       | `{:x<10d}` | `'123xxxxxxx'`  | 右边补`x` ，补够10位         |
| `123`       | `{:>10d}`  | `'       123'`  | 左边补空格，补够10位         |
| `123`       | `{:<10d}`  | `'123       '`  | 右边补空格，补够10位         |
| `123456789` | `{:,}`     | `'123,456,789'` | 逗号分隔格式                 |
| `0.123`     | `{:.2%}`   | `'12.30%'`      | 百分比格式                   |
| `123456789` | `{:.2e}`   | `'1.23e+08'`    | 科学计数法格式(保留两位小数) |

#### 修剪操作

字符串的`strip`方法可以帮我们获得将原字符串修剪掉左右两端指定字符之后的字符串，默认是修剪空格字符。这个方法非常有实用价值，可以用来将用户输入时不小心键入的头尾空格等去掉，`strip`方法还有`lstrip`和`rstrip`两个版本，相信从名字大家已经猜出来这两个方法是做什么用的。

```python
s1 = '   jackfrued@126.com  '
print(s1.strip())      # jackfrued@126.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  # 你好，世界~
print(s2.rstrip('~'))  # ~你好，世界
```

#### 替换操作

如果希望用新的内容替换字符串中指定的内容，可以使用`replace`方法，代码如下所示。`replace`方法的第一个参数是被替换的内容，第二个参数是替换后的内容，还可以通过第三个参数指定替换的次数。

```python
s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 1))  # hell@, good world
```

#### 拆分与合并

可以使用字符串的`split`方法将一个字符串拆分为多个字符串（放在一个列表中），也可以使用字符串的`join`方法将列表中的多个字符串连接成一个字符串，代码如下所示。

```python
s = 'I love you'
words = s.split()       # 不指定分隔符时，默认按空白字符（空格、制表符、换行等）分隔，也可指定分隔符，如s.split("!")
print(words)            # ['I', 'love', 'you']
print('~'.join(words))  # I~love~you
```

需要说明的是，`split`方法默认使用空格进行拆分，我们也可以指定其他的字符来拆分字符串，而且还可以指定最大拆分次数来控制拆分的效果，代码如下所示。

```python
s = 'I#love#you#so#much'
words = s.split('#')
print(words)  # ['I', 'love', 'you', 'so', 'much']
words = s.split('#', 2)
print(words)  # ['I', 'love', 'you#so#much']
```

#### 编码和解码

Python 中除了字符串`str`类型外，还有一种表示二进制数据的字节串类型（`bytes`）。所谓字节串，就是**由零个或多个字节组成的有限序列**。通过字符串的`encode`方法，我们可以按照某种编码方式将字符串编码为字节串，我们也可以使用字节串的`decode`方法，将字节串解码为字符串，代码如下所示。

```python
a = '骆昊'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                  # b'\xe9\xaa\x86\xe6\x98\x8a'
print(c)                  # b'\xc2\xe6\xea\xbb'
print(b.decode('utf-8'))  # 骆昊
print(c.decode('gbk'))    # 骆昊
```

注意，如果编码和解码的方式不一致，会导致乱码问题（无法再现原始的内容）或引发`UnicodeDecodeError`错误，导致程序崩溃。

#### 其他方法

对于字符串类型来说，还有一个常用的操作是对字符串进行匹配检查，即检查字符串是否满足某种特定的模式。例如，一个网站对用户注册信息中用户名和邮箱的检查，就属于模式匹配检查。实现模式匹配检查的工具叫做正则表达式，Python 语言通过标准库中的`re`模块提供了对正则表达式的支持，我们会在后续的课程中为大家讲解这个知识点。

## 11.常用数据结构之集合

如果我们**把一定范围的、确定的、可以区别的事物当作一个整体来看待**，那么这个整体就是集合，集合中的各个事物称为集合的**元素**。通常，集合需要满足以下要求：

1. **无序性**：一个集合中，每个元素的地位都是相同的，元素之间是无序的。
2. **互异性**：一个集合中，任何两个元素都是不相同的，即元素在集合中只能出现一次。
3. **确定性**：给定一个集合和一个任意元素，该元素要么属这个集合，要么不属于这个集合，二者必居其一，不允许有模棱两可的情况出现。

无序性说明集合中的元素并不像列中的元素那样存在某种次序，可以通过索引运算就能访问任意元素，**集合并不支持索引运算**。另外，集合的互异性决定了**集合中不能有重复元素**，这一点也是集合区别于列表的地方，我们无法将重复的元素添加到一个集合中。集合类型必然是支持`in`和`not in`成员运算的，这样就可以确定一个元素是否属于集合，也就是上面所说的集合的确定性。**集合的成员运算在性能上要优于列表的成员运算**，这是集合的底层存储特性决定的，此处我们暂时不做讨论，大家记住这个结论即可。

> **说明**：集合底层使用了哈希存储（散列存储），对哈希存储不了解的读者可以先看看“Hello 算法”网站对[哈希表](https://www.hello-algo.com/chapter_hashing/)的讲解，感谢作者的开源精神。

### 创建集合

在 Python 中，创建集合可以使用`{}`字面量语法，`{}`中需要至少有一个元素，因为没有元素的`{}`并不是空集合而是一个空字典，字典类型我们会在下一节课中为大家介绍。当然，也可以使用 Python 内置函数`set`来创建一个集合，准确的说`set`并不是一个函数，而是创建集合对象的构造器，这个知识点会在后面讲解面向对象编程的地方为大家介绍。我们可以使用`set`函数创建一个空集合，也可以用它将其他序列转换成集合，例如：`set('hello')`会得到一个包含了`4`个字符的集合（重复的字符`l`只会在集合中出现一次）。除了这两种方式，还可以使用生成式语法来创建集合，就像我们之前用生成式语法创建列表那样。

```python
set1 = {1, 2, 3, 3, 3, 2}
print(set1)

set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
print(set2)

set3 = set('hello')
print(set3)

set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)

set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)
```

需要提醒大家，集合中的元素必须是`hashable`类型，所谓`hashable`类型指的是能够计算出哈希码的数据类型，**通常不可变类型**都是`hashable`类型，如整数（`int`）、浮点小数（`float`）、布尔值（`bool`）、字符串（`str`）、元组（`tuple`）等。可变类型都不是`hashable`类型，因为可变类型无法计算出确定的哈希码，所以它们不能放到集合中。例如：我们不能将列表作为集合中的元素；同理，由于集合本身也是可变类型，所以集合也不能作为集合中的元素。我们可以创建出嵌套列表（列表的元素也是列表），但是我们不能创建出嵌套的集合，这一点在使用集合的时候一定要引起注意。

### 元素的遍历

我们可以通过`len`函数来获得集合中有多少个元素，但是我们不能通过索引运算来遍历集合中的元素，因为集合元素并没有特定的顺序。当然，要实现对集合元素的遍历，我们仍然可以使用`for-in`循环，代码如下所示。

```python
set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
for elem in set1:
    print(elem)
```

> **提示**：大家看看上面代码的运行结果，通过单词输出的顺序体会一下集合的无序性（每次输出的顺序都不一样）。

### 集合的运算

#### 成员运算

可以通过成员运算`in`和`not in `检查元素是否在集合中，代码如下所示。

```python
set1 = {11, 12, 13, 14, 15}
print(10 in set1)      # False 
print(15 in set1)      # True
set2 = {'Python', 'Java', 'C++', 'Swift'}
print('Ruby' in set2)  # False
print('Java' in set2)  # True
```

#### 二元运算

集合的二元运算主要指集合的交集、并集、差集、对称差等运算，这些运算可以通过运算符来实现，也可以通过集合类型的方法来实现

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day01-20/res/day12/set_operations.png)

```python
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1 & set2)                      # {2, 4, 6}
print(set1.intersection(set2))          # {2, 4, 6}

# 并集
print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
print(set1 - set2)                      # {1, 3, 5, 7}
print(set1.difference(set2))            # {1, 3, 5, 7}

# 对称差
print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}
```

通过上面的代码可以看出，对两个集合求交集，`&`运算符和`intersection`方法的作用是完全相同的，使用运算符的方式显然更直观且代码也更简短。需要说明的是，集合的二元运算还可以跟赋值运算一起构成复合赋值运算，例如：`set1 |= set2`相当于`set1 = set1 | set2`，跟`|=`作用相同的方法是`update`；`set1 &= set2`相当于`set1 = set1 & set2`，跟`&=`作用相同的方法是`intersection_update`，代码如下所示。

```python
set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2
# set1.update(set2)
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
set3 = {3, 6, 9}
set1 &= set3
# set1.intersection_update(set3)
print(set1)  # {3, 6}
set2 -= set1
# set2.difference_update(set1)
print(set2)  # {2, 4}
```

#### 比较运算

两个集合可以用`==`和`!=`进行相等性判断，如果两个集合中的元素完全相同，那么`==`比较的结果就是`True`，否则就是`False`。如果集合`A`的任意一个元素都是集合`B`的元素，那么集合`A`称为集合`B`的子集，即对于 ∀a∈A ，均有 a∈B ，则 A⊆B ，`A`是`B`的子集，反过来也可以称`B`是`A`的超集。如果`A`是`B`的子集且`A`不等于`B`，那么`A`就是`B`的真子集。Python 为集合类型提供了判断子集和超集的运算符，其实就是我们非常熟悉的`<`、`<=`、`>`、`>=`这些运算符。当然，我们也可以通过集合类型的方法`issubset`和`issuperset`来判断集合之间的关系，代码如下所示。

```python
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}

print(set1 < set2)   # True
print(set1 <= set2)  # True
print(set2 < set3)   # False
print(set2 <= set3)  # True
print(set2 > set1)   # True
print(set2 == set3)  # True

print(set1.issubset(set2))    # True
print(set2.issuperset(set1))  # True
```

> **说明**：上面的代码中，`set1 < set2`判断`set1`是不是`set2`的真子集，`set1 <= set2`判断`set1`是不是`set2`的子集，`set2 > set1`判断`set2`是不是`set1`的超集。当然，我们也可以通过`set1.issubset(set2)`判断`set1`是不是`set2`的子集；通过`set2.issuperset(set1)`判断`set2`是不是`set1`的超集。

### 集合的方法

```python
set1 = {1, 10, 100}

# 添加元素
set1.add(1000)
set1.add(10000)
print(set1)  # {1, 100, 1000, 10, 10000}

# 删除元素
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)  # {1, 1000, 10000}

# 清空元素
set1.clear()
print(set1)  # set()
```

> **说明**：删除元素的`remove`方法在元素不存在时会引发`KeyError`错误，所以上面的代码中我们先通过成员运算判断元素是否在集合中。集合类型还有一个`pop`方法可以从集合中随机删除一个元素，该方法在删除元素的同时会返回（获得）被删除的元素，而`remove`和`discard`方法仅仅是删除元素，不会返回（获得）被删除的元素。

集合类型还有一个名为`isdisjoint`的方法可以判断两个集合有没有相同的元素，如果没有相同元素，该方法返回`True`，否则该方法返回`False`，代码如下所示。

```python
set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True
```

### 不可变集合

Python 中还有一种不可变类型的集合，名字叫`frozenset`。`set`跟`frozenset`的区别就如同`list`跟`tuple`的区别，`frozenset`由于是不可变类型，能够计算出哈希码，因此它可以作为`set`中的元素。除了不能添加和删除元素，`frozenset`在其他方面跟`set`是一样的，下面的代码简单的展示了`frozenset`的用法。

```python
fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False
```

## 12.常用数据结构之字典

### 创建和使用字典

Python 中创建字典可以使用`{}`字面量语法，这一点跟上一节课讲的集合是一样的。但是字典的`{}`中的元素是以键值对的形式存在的，每个元素由`:`分隔的两个值构成，`:`前面是键，`:`后面是值，代码如下所示。

```python
xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101', 
    'tel': '13122334455',
    'emergence contact': '13800998877'
}
print(person)
```

我们也可以使用内置函数`dict`或者是字典的生成式语法来创建字典

```python
# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')
print(person)  # {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

# 可以通过Python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

# 用字典生成式语法创建字典
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```

想知道字典中一共有多少组键值对，仍然是使用`len`函数；如果想对字典进行遍历，可以用`for`循环，但是需要注意，`for`循环只是对字典的键进行了遍历，不过没关系，在学习了字典的索引运算后，我们可以通过字典的键访问它对应的值。

```python
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101'
}
print(len(person))  # 5
for key in person:
    print(key)
```

### 字典的运算

对于字典类型来说，成员运算和索引运算肯定是很重要的，前者可以判定指定的键在不在字典中，后者可以通过键访问对应的值或者向字典中添加新的键值对。值得注意的是，字典的索引不同于列表的索引，列表中的元素因为有属于自己有序号，所以列表的索引是一个整数；字典中因为保存的是键值对，所以字典需要用键去索引对应的值。需要**特别提醒**大家注意的是，**字典中的键必须是不可变类型**，例如整数（`int`）、浮点数（`float`）、字符串（`str`）、元组（`tuple`）等类型，这一点跟集合类型对元素的要求是一样的；很显然，之前我们讲的列表（`list`）和集合（`set`）不能作为字典中的键，字典类型本身也不能再作为字典中的键，因为字典也是可变类型，但是列表、集合、字典都可以作为字典中的值，例如：

```python
person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print(person)
```

大家可以看看下面的代码，了解一下字典的成员运算和索引运算。

```python
person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

# 成员运算
print('name' in person)  # True
print('tel' in person)   # False

# 索引运算
print(person['name'])
print(person['addr'])
person['age'] = 25
person['height'] = 178
person['tel'] = '13122334455'
person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
print(person)

# 循环遍历
for key in person:
    print(f'{key}:\t{person[key]}')
```

需要注意，在通过索引运算获取字典中的值时，如指定的键没有在字典中，将会引发`KeyError`异常。

### 字典的方法

字典类型的方法基本上都跟字典的键值对操作相关，其中`get`方法可以通过键来获取对应的值。跟索引运算不同的是，`get`方法在字典中没有指定的键时不会产生异常，而是返回`None`或指定的默认值，代码如下所示。

```python
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.get('name'))       # 王大锤
print(person.get('sex'))        # None
print(person.get('sex', True))  # True
```

如果需要获取字典中所有的键，可以使用`keys`方法；如果需要获取字典中所有的值，可以使用`values`方法。字典还有一个名为`items`的方法，它会将键和值组装成二元组，通过该方法来遍历字典中的元素也是非常方便的。

```python
person = {'name': '王大锤', 'age': 25, 'height': 178}
print(person.keys())    # dict_keys(['name', 'age', 'height'])
print(person.values())  # dict_values(['王大锤', 25, 178])
print(person.items())   # dict_items([('name', '王大锤'), ('age', 25), ('height', 178)])
for key, value in person.items():
    print(f'{key}:\t{value}')
```

字典的`update`方法实现两个字典的合并操作。例如，有两个字典`x`和`y`，当执行`x.update(y)`操作时，`x`跟`y`相同的键对应的值会被`y`中的值更新，而`y`中有但`x`中没有的键值对会直接添加到`x`中

```python
person1 = {'name': '王大锤', 'age': 55, 'height': 178}
person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
person1.update(person2)
print(person1)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
# 如果使用 Python 3.9 及以上的版本，也可以使用|运算符来完成同样的操作
person1 |= person2
print(person1)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
```

可以通过`pop`或`popitem`方法从字典中删除元素，前者会返回（获得）键对应的值，但是如果字典中不存在指定的键，会引发`KeyError`错误；后者在删除元素时，会返回（获得）键和值组成的二元组。字典的`clear`方法会清空字典中所有的键值对

```python
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.pop('age'))  # 25
print(person)             # {'name': '王大锤', 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.popitem())   # ('addr', '成都市武侯区科华北路62号1栋101')
print(person)             # {'name': '王大锤', 'height': 178}
person.clear()
print(person)             # {}
```

跟列表一样，从字典中删除元素也可以使用`del`关键字，在删除元素的时候如果指定的键索引不到对应的值，一样会引发`KeyError`错误

```python
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
del person['age']
del person['addr']
print(person)  # {'name': '王大锤', 'height': 178}
```

### 字典的应用

输入一段话，统计每个英文字母出现的次数，按出现次数从高到低输出。

```python
sentence = input('请输入一段话: ')
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1
sorted_keys = sorted(counter, key=counter.get, reverse=True)
for key in sorted_keys:
    print(f'{key} 出现了 {counter[key]} 次.')
```

在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。

```python
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)
```

## 13.函数和模块

### 定义函数

Python 中可以使用`def`关键字来定义函数，和变量一样每个函数也应该有一个漂亮的名字，命名规则跟变量的命名规则是一样的（大家赶紧想想我们之前讲过的变量的命名规则）。在函数名后面的圆括号中可以设置函数的参数，也就是我们刚才说的函数的自变量，而函数执行完成后，我们会通过`return`关键字来返回函数的执行结果，这就是我们刚才说的函数的因变量。如果函数中没有`return`语句，那么函数会返回代表空值的`None`。另外，函数也可以没有自变量（参数），但是函数名后面的圆括号是必须有的。一个函数要做的事情（要执行的代码），是通过代码缩进的方式放到函数定义行之后，跟之前分支和循环结构的代码块类似，如下图所示。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day01-20/res/day14/function_definition.png)

**所谓重构，是在不影响代码执行结果的前提下对代码的结构进行调整**

Python 标准库的`math`模块中，已经有一个名为`factorial`的函数实现了求阶乘的功能，我们可以直接用`import math`导入`math`模块，然后使用`math.factorial`来调用求阶乘的函数；我们也可以通过`from math import factorial`直接导入`factorial`函数来使用它

将来我们使用的函数，要么是自定义的函数，要么是 Python 标准库或者三方库中提供的函数，如果已经有现成的可用的函数，我们就没有必要自己去定义，“**重复发明轮子**”是一件非常糟糕的事情。对于上面的代码，如果你觉得`factorial`这个名字太长，书写代码的时候不是特别方便，我们在导入函数的时候还可以通过`as`关键字为其别名。在调用函数的时候，我们可以用函数的别名，而不再使用它之前的名字

### 函数的参数

#### 位置参数和关键字参数

```python
def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
```

上面`make_judgement`函数有三个参数，这种参数叫做位置参数，在调用函数时通常按照从左到右的顺序依次传入，而且传入参数的数量必须和定义函数时参数的数量相同

```python
print(make_judgement(1, 2, 3))  # False
print(make_judgement(4, 5, 6))  # True
```

如果不想按照从左到右的顺序依次给出`a`、`b`、`c` 三个参数的值，也可以使用关键字参数，通过“参数名=参数值”的形式为函数传入参数

```python
print(make_judgement(b=2, c=3, a=1))  # False
print(make_judgement(c=6, b=4, a=5))  # True
```

在定义函数时，我们可以在参数列表中用`/`设置**强制位置参数**（*positional-only arguments*），用`*`设置**命名关键字参数**。所谓强制位置参数，就是调用函数时只能按照参数位置来接收参数值的参数；而命名关键字参数只能通过“参数名=参数值”的方式来传递和接收参数

```python
# /前面的参数是强制位置参数
def make_judgement(a, b, c, /):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b


# 下面的代码会产生TypeError错误，错误信息提示“强制位置参数是不允许给出参数名的”
# TypeError: make_judgement() got some positional-only arguments passed as keyword arguments
# print(make_judgement(b=2, c=3, a=1))
```

```python
# *后面的参数是命名关键字参数
def make_judgement(*, a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b


# 下面的代码会产生TypeError错误，错误信息提示“函数没有位置参数但却给了3个位置参数”
# TypeError: make_judgement() takes 0 positional arguments but 3 were given
# print(make_judgement(1, 2, 3))
```

#### 参数的默认值

Python 中允许函数的参数拥有默认值，我们可以把之前讲过的一个例子“CRAPS赌博游戏”（《第07课：分支和循环结构的应用》）中摇色子获得点数的功能封装到函数中

```python
from random import randrange


# 定义摇色子的函数
# 函数的自变量（参数）n表示色子的个数，默认值为2
# 函数的因变量（返回值）表示摇n颗色子得到的点数
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randrange(1, 7)
    return total


# 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
print(roll_dice())
# 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
print(roll_dice(3))
```

```python
def add(a=0, b=0, c=0):
    """三个数相加求和"""
    return a + b + c


# 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add())         # 0
# 调用add函数，传入一个参数，该参数赋值给变量a, 变量b和c使用默认值0
print(add(1))        # 1
# 调用add函数，传入两个参数，分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2))     # 3
# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(1, 2, 3))  # 6
```

需要注意的是，**带默认值的参数必须放在不带默认值的参数之后**，否则将产生`SyntaxError`错误，错误消息是：`non-default argument follows default argument`，翻译成中文的意思是“没有默认值的参数放在了带默认值的参数后面”。

#### 可变参数

Python 语言中可以通过星号表达式语法让函数支持可变参数。所谓可变参数指的是在调用函数时，可以向函数传入`0`个或任意多个参数。将来我们以团队协作的方式开发商业项目时，很有可能要设计函数给其他人使用，但有的时候我们并不知道函数的调用者会向该函数传入多少个参数，这个时候可变参数就能派上用场。

```python
# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total = 0
    # 对保存可变参数的元组进行循环遍历
    for val in args:
        # 对参数进行了类型检查（数值型的才能求和）
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())         # 0
print(add(1))        # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, 'hello', 3.45, 6))  # 12.45
```

如果我们希望通过“参数名=参数值”的形式传入若干个参数，具体有多少个参数也是不确定的，我们还可以给函数添加可变关键字参数，把传入的关键字参数组装到一个字典中

```python
# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)

# 输出
(3, 2.1, True)
{'name': '骆昊', 'age': 43, 'gpa': 4.95}
```

### 用模块管理函数

不管用什么样的编程语言来写代码，给变量、函数起名字都是一个让人头疼的问题，因为我们会遇到**命名冲突**这种尴尬的情况。最简单的场景就是在同一个`.py`文件中定义了两个同名的函数

```python
def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')

    
foo()  # 大家猜猜调用foo函数会输出什么
```

在 Python 中，**同一个文件中定义了两个同名函数时，后定义的函数会覆盖先定义的函数**。因此，调用该函数时会执行**后定义的版本**

当然上面的这种情况我们很容易就能避免，但是如果项目是团队协作多人开发的时候，团队中可能有多个程序员都定义了名为`foo`的函数，这种情况下怎么解决命名冲突呢？答案其实很简单，Python 中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，在使用函数的时候，我们通过`import`关键字导入指定的模块再使用**完全限定名**（`模块名.函数名`）的调用方式，就可以区分到底要使用的是哪个模块中的`foo`函数

```python
# module1.py
def foo():
    print('hello, world!')
```

```python
# module2.py
def foo():
    print('goodbye, world!')
```

```python
# test.py
# 在导入模块时，还可以使用as关键字对模块进行别名，这样我们可以使用更为简短的完全限定名。
import module1 as m1
import module2 as m2

m1.foo()  # hello, world!
m2.foo()  # goodbye, world!
```

上面两段代码，我们导入的是定义函数的模块，我们也可以使用`from...import...`语法从模块中直接导入需要使用的函数

```python
from module1 import foo

foo()  # hello, world!

from module2 import foo

foo()  # goodbye, world!
```

但是，如果我们如果从两个不同的模块中导入了同名的函数，后面导入的函数会替换掉之前的导入，就像下面的代码，调用`foo`会输出`goodbye, world!`，因为我们先导入了`module1`的`foo`，后导入了`module2`的`foo` 。如果两个`from...import...`反过来写，那就是另外一番光景了。

```python
from module1 import foo
from module2 import foo

foo()  # goodbye, world!
```

如果想在上面的代码中同时使用来自两个模块的`foo`函数还是有办法的，大家可能已经猜到了，还是用`as`关键字对导入的函数进行别名

```python
from module1 import foo as f1
from module2 import foo as f2

f1()  # hello, world!
f2()  # goodbye, world!
```

### 标准库中的模块和函数

Python 标准库中提供了大量的模块和函数来简化我们的开发工作，我们之前用过的`random`模块就为我们提供了生成随机数和进行随机抽样的函数；而`time`模块则提供了和时间操作相关的函数；我们之前用到过的`math`模块中还包括了计算正弦、余弦、指数、对数等一系列的数学函数。

Python 标准库中还有一类函数是不需要`import`就能够直接使用的，我们将其称之为**内置函数**，这些内置函数不仅有用而且还很常用，下面的表格列出了一部分的内置函数。

| 函数    | 说明                                                         |
| ------- | ------------------------------------------------------------ |
| `abs`   | 返回一个数的绝对值，例如：`abs(-1.3)`会返回`1.3`。           |
| `bin`   | 把一个整数转换成以`'0b'`开头的二进制字符串，例如：`bin(123)`会返回`'0b1111011'`。 |
| `chr`   | 将Unicode编码转换成对应的字符，例如：`chr(8364)`会返回`'€'`。 |
| `hex`   | 将一个整数转换成以`'0x'`开头的十六进制字符串，例如：`hex(123)`会返回`'0x7b'`。 |
| `input` | 从输入中读取一行，返回读到的字符串。                         |
| `len`   | 获取字符串、列表等的长度。                                   |
| `max`   | 返回多个参数或一个可迭代对象中的最大值，例如：`max(12, 95, 37)`会返回`95`。 |
| `min`   | 返回多个参数或一个可迭代对象中的最小值，例如：`min(12, 95, 37)`会返回`12`。 |
| `oct`   | 把一个整数转换成以`'0o'`开头的八进制字符串，例如：`oct(123)`会返回`'0o173'`。 |
| `open`  | 打开一个文件并返回文件对象。                                 |
| `ord`   | 将字符转换成对应的Unicode编码，例如：`ord('€')`会返回`8364`。 |
| `pow`   | 求幂运算，例如：`pow(2, 3)`会返回`8`；`pow(2, 0.5)`会返回`1.4142135623730951`。 |
| `print` | 打印输出。                                                   |
| `range` | 构造一个范围序列，例如：`range(100)`会产生`0`到`99`的整数序列。 |
| `round` | 按照指定的精度对数值进行四舍五入，例如：`round(1.23456, 4)`会返回`1.2346`。 |
| `sum`   | 对一个序列中的项从左到右进行求和运算，例如：`sum(range(1, 101))`会返回`5050`。 |
| `type`  | 返回对象的类型，例如：`type(10)`会返回`int`；而` type('hello')`会返回`str`。 |

在 Python 中，**可迭代对象（Iterable）** 是指**可以被遍历（迭代）的对象**，即能够提供一个迭代器（Iterator）来逐个访问其元素的对象。简单来说，任何可以用在 `for` 循环中的对象，都是可迭代对象。

## 14.函数应用实战

### 随机验证码

设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。

```python
# 自写代码
import random

def generate_code(n = 4):
    # 小写字母
    lalp = [chr(i) for i in range(ord('a'), ord('z')+1)]
    # 大写字母
    salp = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    # 合并为所有字母
    alp = lalp + salp
    # 数字
    num = [str(i) for i in range(10)]
    
    # 随机生成n个字母
    anum = random.randint(0,n)
    # 剩余的数字个数
    nnum = n - anum

    # 随机生成验证码
    code = random.sample(alp,anum)
    code += random.sample(num,nnum)

    # 利用集合的无序性来打乱验证码
    set_code = set(code)
    # 输出打乱后的验证码
    for i in set_code:
        print(i, end='')


for i in range(5):
    generate_code(5)
    print()
    
    
# 答案
import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(*, code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))
```

> **说明1**：`string`模块的`digits`代表0到9的数字构成的字符串`'0123456789'`，`string`模块的`ascii_letters`代表大小写英文字母构成的字符串`'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`。
>
> **说明2**：`random`模块的`sample`和`choices`函数都可以实现随机抽样，`sample`实现无放回抽样，这意味着抽样取出的元素是不重复的；`choices`实现有放回抽样，这意味着可能会重复选中某些元素。这两个函数的第一个参数代表抽样的总体，而参数`k`代表样本容量，需要说明的是`choices`函数的参数`k`是一个命名关键字参数，在传参时必须指定参数名。
>
> **说明**：我们设计的`generate_code`函数的参数是命名关键字参数，由于它有默认值，可以不给它传值，使用默认值4。如果需要给函数传入参数，必须指定参数名`code_len`。

设计一个判断给定的大于1的正整数是不是质数的函数。质数是只能被1和自身整除的正整数（大于1），如果一个大于 1 的正整数 N 是质数，那就意味着在 2 到 N−1 之间都没有它的因子。

### 判断素数

设计一个判断给定的大于1的正整数是不是质数的函数。质数是只能被1和自身整除的正整数（大于1），如果一个大于 1 的正整数 N 是质数，那就意味着在 2 到 N−1 之间都没有它的因子。

```python
# 自己代码
def prime(n):
    if n <2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


# 答案
def is_prime(num: int) -> bool:
    """
    判断一个正整数是不是质数
    :param num: 大于1的正整数
    :return: 如果num是质数返回True，否则返回False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```

> **说明1**：上面`is_prime`函数的参数`num`后面的`: int`用来标注参数的类型，虽然它对代码的执行结果不产生任何影响，但是很好的增强了代码的可读性。同理，参数列表后面的`-> bool`用来标注函数返回值的类型，它也不会对代码的执行结果产生影响，但是却让我们清楚的知道，调用函数会得到一个布尔值，要么是`True`，要么是`False`。

### 最大公约数和最小公倍数

设计计算两个正整数最大公约数和最小公倍数的函数。 x 和 y 的最大公约数是能够同时整除 x 和 y 的最大整数，如果 x 和 y 互质，那么它们的最大公约数为 1； x 和 y 的最小公倍数是能够同时被 x 和 y 整除的最小正整数，如果 x 和 y 互质，那么它们的最小公倍数为 x×y 。需要提醒大家注意的是，计算最大公约数和最小公倍数是两个不同的功能，应该设计成两个函数，而不是把两个功能放到同一个函数中。

```python
# 敲
def greatest_common_divisor(a: int, b: int):
    if a < b:
        while b % a != 0:
            a, b = b % a, a
        return a
    else:
        while a % b != 0:
            a, b = b, a % b
        return b

def least_common_multiple(a: int, b: int):
    return a * b // greatest_common_divisor(a, b)
    
   
# 答案
def lcm(x: int, y: int) -> int:
    """求最小公倍数"""
    return x * y // gcd(x, y)


def gcd(x: int, y: int) -> int:
    """求最大公约数"""
    while y % x != 0:
        x, y = y % x, x
    return x
```

### 数据统计

假设样本数据保存一个列表中，设计计算样本数据描述性统计信息的函数。描述性统计信息通常包括：算术平均值、中位数、极差（最大值和最小值的差）、方差、标准差、变异系数等，计算公式如下所示。

样本均值（sample mean）：
$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$
样本方差（sample variance）：
$$
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$
样本标准差（sample standard deviation）：
$$
s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
$$
变异系数（coefficient of sample variation）：
$$
CV = \frac{s}{\bar{x}} \times 100\%
$$

```python
# 敲
def sample_mean(data):
    return sum(data)/len(data)

def median(data):
    data.sort()
    if len(data) % 2 == 0:
        return (data[len(data)//2] + data[len(data)//2 - 1])/2
    else:
        return data[len(data)//2]

def ptp(data):
    return max(data) - min(data)

def sample_variance(data):
    return sum((x - sample_mean(data))**2 for x in data)/(len(data)-1)

def sample_standard_deviation(data):
    return pow(sample_variance(data),0.5)

def coefficient_of_sample_variation(data):
    return sample_standard_deviation(data)/sample_mean(data)
    
    
# 答案
def ptp(data):
    """极差（全距）"""
    return max(data) - min(data)


def mean(data):
    """算术平均"""
    return sum(data) / len(data)


def median(data):
    """中位数"""
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return mean(temp[size // 2 - 1:size // 2 + 1])


def var(data, ddof=1):
    """方差"""
    x_bar = mean(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(temp) - ddof)


def std(data, ddof=1):
    """标准差"""
    return var(data, ddof) ** 0.5


def cv(data, ddof=1):
    """变异系数"""
    return std(data, ddof) / mean(data)


def describe(data):
    """输出描述性统计信息"""
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')
```

> **说明1**：中位数是将数据按照升序或降序排列后位于中间的数，它描述了数据的中等水平。中位数的计算分两种情况：当数据体量$n$为奇数时，中位数是位于 (n+1)/2 位置的元素；当数据体量 n 为偶数时，中位数是位于 n/2 和 n/2+1 两个位置元素的均值。
>
> **说明2**：计算方差和标准差的函数中有一个名为`ddof`的参数，它代表了可以调整的自由度，默认值为 1。在计算样本方差和样本标准差时，需要进行自由度校正；如果要计算总体方差和总体标准差，可以将`ddof`参数赋值为 0，即不需要进行自由度校正。
>
> **说明3**：`describe`函数将上面封装好的统计函数组装到一起，用于输出数据的描述性统计信息。事实上，Python 标准库中有一个名为`statistics`的模块，它已经把获取描述性统计信息的函数封装好了，有兴趣的读者可以自行了解。

#### **1. 集中趋势度量**

| 函数                  | 说明                         | 示例                               |
| --------------------- | ---------------------------- | ---------------------------------- |
| `mean(data)`          | 计算算术平均数（均值）       | `mean([1, 2, 3, 4]) → 2.5`         |
| `median(data)`        | 计算中位数（中间值）         | `median([1, 3, 2]) → 2`            |
| `mode(data)`          | 计算众数（出现次数最多的值） | `mode([1, 2, 2, 3]) → 2`           |
| `harmonic_mean(data)` | 计算调和平均数               | `harmonic_mean([1, 2, 4]) → 1.714` |

#### **2. 离散程度度量**

| 函数              | 说明           | 示例                           |
| ----------------- | -------------- | ------------------------------ |
| `pstdev(data)`    | 计算总体标准差 | `pstdev([1, 2, 3]) → 0.816`    |
| `pvariance(data)` | 计算总体方差   | `pvariance([1, 2, 3]) → 0.667` |
| `stdev(data)`     | 计算样本标准差 | `stdev([1, 2, 3]) → 1.0`       |
| `variance(data)`  | 计算样本方差   | `variance([1, 2, 3]) → 1.0`    |

调和平均数（Harmonic Mean）是一种特殊的平均数，主要用于计算**速率的平均值**或**处理具有比率性质的数据**。它的计算方式与算术平均数和几何平均数不同，尤其适用于 “时间 - 速度”“距离 - 效率” 等问题。

对于 *n* 个正数 *x*1,*x*2,…,*xn*，调和平均数 *H* 的计算公式为：
$$
H = \frac{n}{\sum_{i=1}^{n} \frac{1}{x_i}}
$$
**文字描述**：调和平均数等于数据个数除以各数据倒数之和。

### 双色球随机选号

我们用函数重构之前讲过的双色球随机选号的例子（《第09课：常用数据结构之列表-2》），将生成随机号码和输出一组号码的功能分别封装到两个函数中，然后通过调用函数实现机选`N`注号码的功能。

```python
"""
双色球随机选号程序

Author: 骆昊
Version: 1.3
"""
import random

RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]


def choose():
    """
    生成一组随机号码
    :return: 保存随机号码的列表
    """
    selected_balls = random.sample(RED_BALLS, 6)
    selected_balls.sort()
    selected_balls.append(random.choice(BLUE_BALLS))
    return selected_balls


def display(balls):
    """
    格式输出一组号码
    :param balls: 保存随机号码的列表
    """
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')


n = int(input('生成几注号码: '))
for _ in range(n):
    display(choose())
```

## 15.函数使用进阶

**Python 中的函数是“一等函数”**，所谓“一等函数”指的就是函数可以赋值给变量，函数可以作为函数的参数，函数也可以作为函数的返回值。把一个函数作为其他函数的参数或返回值的用法，我们通常称之为“高阶函数”。

### 高阶函数

我们回到之前讲过的一个例子，设计一个函数，传入任意多个参数，对其中`int`类型或`float`类型的元素实现求和操作。

```python
def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result
```

如果我们希望上面的`calc`函数不仅仅可以做多个参数的求和，还可以实现更多的甚至是自定义的二元运算，我们该怎么做呢？上面的代码只能求和是因为函数中使用了`+=`运算符，这使得函数跟加法运算形成了耦合关系，如果能解除这种耦合关系，函数的通用性和灵活性就会更好。解除耦合的办法就是将`+`运算符变成函数调用，并将其设计为函数的参数

```python
def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result
```

注意，上面的函数增加了两个参数，其中`init_value`代表运算的初始值，`op_func`代表二元运算函数，为了调用修改后的函数，我们先定义做加法和乘法运算的函数

```python
def add(x, y):
    return x + y


def mul(x, y):
    return x * y

print(calc(0, add, 1, 2, 3, 4, 5))  # 15
print(calc(1, mul, 1, 2, 3, 4, 5))  # 120 
```

上面的`calc`函数通过将运算符变成函数的参数，实现了跟加法运算耦合，这是一种非常高明和实用的编程技巧，但对于最初学者来说可能会觉得难以理解，建议大家细品一下。需要注意上面的代码中，将函数作为参数传入其他函数和直接调用函数是有显著的区别的，**调用函数需要在函数名后面跟上圆括号，而把函数作为参数时只需要函数名即可**。

如果我们没有提前定义好`add`和`mul`函数，也可以使用 Python 标准库中的`operator`模块提供的`add`和`mul`函数，它们分别代表了做加法和做乘法的二元运算，我们拿过来直接使用即可，代码如下所示。

```python
import operator

print(calc(0, operator.add, 1, 2, 3, 4, 5))  # 15
print(calc(1, operator.mul, 1, 2, 3, 4, 5))  # 120
```

Python 内置函数中有不少高阶函数，我们前面提到过的`filter`和`map`函数就是高阶函数，前者可以实现对序列中元素的过滤，后者可以实现对序列中元素的映射，例如我们要去掉一个整数列表中的奇数，并对所有的偶数求平方得到一个新的列表，就可以直接使用这两个函数来做到

```python
def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num):
    """求平方"""
    return num ** 2


old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(square, filter(is_even, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]
```

filter()函数过滤可迭代对象中的元素，返回满足条件的元素组成的迭代器。

```python
filter(function, iterable)
```

- **`function`**：判断函数，返回布尔值（`True` 或 `False`）。
- **`iterable`**：待过滤的可迭代对象（如列表、元组）。

map()函数对可迭代对象中的每个元素应用指定函数，返回处理后的元素组成的迭代器。

```python
map(function, iterable)
```

- **`function`**：处理函数，接收一个参数并返回处理结果。
- **`iterable`**：待处理的可迭代对象。

在 Python 中，**迭代器（Iterator）** 是一种实现了迭代协议的对象，用于逐个访问集合中的元素，而无需暴露集合的内部结构。它是 Python 迭代机制的核心，支持 `for` 循环、`next()` 函数等迭代操作。

迭代器的核心特征

- 惰性计算 **：迭代器不会一次性加载所有元素到内存，而是在需要时（通过 `next()` 调用）才生成下一个元素，适合处理海量数据或无限序列。**
- 单向访问 **：元素只能从前往后依次访问，无法回退或重置（除非重新创建迭代器）。**
- 迭代协议 ：必须实现两个特殊方法：
  - `__iter__()`：返回迭代器自身（使迭代器可用于 `for` 循环）。
  - `__next__()`：返回下一个元素，当没有元素时触发 `StopIteration` 异常。

迭代器与可迭代对象的区别

可迭代对象（Iterable）：**能被 `for` 循环遍历的对象（如列表、字符串、字典等），实现了 `__iter__()` 方法，可通过 `iter()` 函数转换为迭代器。**

迭代器（Iterator）：是可迭代对象的一种，但额外实现了 `__next__()` 方法，是 “正在迭代中” 的状态对象。

**关系**：所有迭代器都是可迭代对象，但并非所有可迭代对象都是迭代器。

当然，要完成上面代码的功能，也可以使用列表生成式，列表生成式的做法更为简单优雅。

```python
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = [num ** 2 for num in old_nums if num % 2 == 0]
print(new_nums)  # [144, 64, 3600, 2704]
```

我们再来讨论一个内置函数`sorted`，它可以实现对容器型数据类型（如：列表、字典等）元素的排序。我们之前讲过`list`类型的`sort`方法，它实现了对列表元素的排序，`sorted`函数从功能上来讲跟列表的`sort`方法没有区别，但它会返回排序后的列表对象，而不是直接修改原来的列表，这一点我们称为**函数的无副作用设计**，也就是说调用函数除了产生返回值以外，不会对程序的状态或外部环境产生任何其他的影响。使用`sorted`函数排序时，可以通过高阶函数的形式自定义排序的规则

```python
old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings)
print(new_strings)  # ['apple', 'in', 'pear', waxberry', 'zoo']
```

上面的代码对大家来说并不陌生，但是如果希望根据字符串的长度而不是字母表顺序对列表元素排序，我们可以向`sorted`函数传入一个名为`key`的参数，将`key`参数赋值为获取字符串长度的函数`len`

```python
old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings, key=len)
print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']
```

> **说明**：列表类型的`sort`方法也有同样的`key`参数，有兴趣的读者可以自行尝试。

### Lambda函数

在使用高阶函数的时候，如果作为参数或者返回值的函数本身非常简单，一行代码就能够完成，也不需要考虑对函数的复用，那么我们可以使用 lambda 函数。Python 中的 lambda 函数是没有的名字函数，所以很多人也把它叫做**匿名函数**，lambda 函数只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值。之前的代码中，我们写的`is_even`和`square`函数都只有一行代码，我们可以考虑用 lambda 函数来替换掉它们

```python
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]
```

通过上面的代码可以看出，定义 lambda 函数的关键字是`lambda`，后面跟函数的参数，如果有多个参数用逗号进行分隔；冒号后面的部分就是函数的执行体，通常是一个表达式，表达式的运算结果就是 lambda 函数的返回值，不需要写`return` 关键字。

前面我们说过，Python 中的函数是“一等函数”，函数是可以直接赋值给变量的。在学习了 lambda 函数之后，前面我们写过的一些函数就可以用一行代码来实现它们了

```python
import functools
import operator

# 用一行代码实现计算阶乘的函数
fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)

# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# 调用Lambda函数
print(fac(6))        # 720
print(is_prime(37))  # True
```

> **提示1**：上面使用的`reduce`函数是 Python 标准库`functools`模块中的函数，它可以实现对一组数据的归约操作，类似于我们之前定义的`calc`函数，第一个参数是代表运算的函数，第二个参数是运算的数据，第三个参数是运算的初始值。很显然，`reduce`函数也是高阶函数，它和`filter`函数、`map`函数一起构成了处理数据中非常关键的三个动作：**过滤**、**映射**和**归约**。
>
> 在 Python 中，**归约操作（Reduction）** 是一种将可迭代对象（如列表、元组）通过某种规则逐步合并，最终得到单个结果的操作。它的核心是 “将多个元素缩减为一个值”，是函数式编程中的重要概念。
>
> **提示2**：上面判断素数的 lambda 函数通过`range`函数构造了从 2 到 x 的范围，检查这个范围有没有`x`的因子。`all`函数也是 Python 内置函数，如果传入的序列中所有的布尔值都是`True`，`all`函数返回`True`，否则`all`函数返回`False`。

### 偏函数

偏函数是指固定函数的某些参数，生成一个新的函数，这样就无需在每次调用函数时都传递相同的参数。在 Python 语言中，我们可以使用`functools`模块的`partial`函数来创建偏函数。例如，`int`函数在默认情况下可以将字符串视为十进制整数进行类型转换，如果我们修修改它的`base`参数，就可以定义出三个新函数，分别用于将二进制、八进制、十六进制字符串转换为整数

```python
import functools

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int('1001'))    # 1001

print(int2('1001'))   # 9
print(int8('1001'))   # 513
print(int16('1001'))  # 4097
```

不知大家是否注意到，`partial`函数的第一个参数和返回值都是函数，它将传入的函数处理成一个新的函数返回。通过构造偏函数，我们可以结合实际的使用场景将原函数变成使用起来更为便捷的新函数，不知道大家有没有觉得这波操作很有意思。

## 16.函数高级应用

### 装饰器

Python 语言中，装饰器是“**用一个函数装饰另外一个函数并为其提供额外的能力**”的语法现象。装饰器本身是一个函数，它的参数是被装饰的函数，它的返回值是一个带有装饰功能的函数。通过前面的描述，相信大家已经听出来了，装饰器是一个高阶函数，它的参数和返回值都是函数。但是，装饰器的概念对编程语言的初学者来说，还是让人头疼的，下面我们先通过一个简单的例子来说明装饰器的作用。假设有名为`downlaod`和`upload`的两个函数，分别用于文件的上传和下载

```python
import random
import time


def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

    
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

    
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
```

> **说明**：上面的代码用休眠一段随机时间的方式模拟了下载和上传文件需要花费一定的时间，并没有真正的联网上传下载文件。用 Python 语言实现联网上传下载文件也非常简单，后面我们会讲到相关的知识。

现在有一个新的需求，我们希望知道调用`download`和`upload`函数上传下载文件到底用了多少时间，这应该如何实现呢？相信很多小伙伴已经想到了，我们可以在函数开始执行的时候记录一个时间，在函数调用结束后记录一个时间，两个时间相减就可以计算出下载或上传的时间，代码如下所示。

```python
start = time.time()
download('MySQL从删库到跑路.avi')
end = time.time()
print(f'花费时间: {end - start:.2f}秒')
start = time.time()
upload('Python从入门到住院.pdf')
end = time.time()
print(f'花费时间: {end - start:.2f}秒')
```

通过上面的代码，我们可以在下载和上传文件时记录下耗费的时间，但不知道大家是否注意到，上面记录时间、计算和显示执行时间的代码都是重复代码。有编程经验的人都知道，**重复的代码是万恶之源**，那么有没有办法在不写重复代码的前提下，用一种简单优雅的方式记录下函数的执行时间呢？在 Python 语言中，装饰器就是解决这类问题的最佳选择。通过装饰器语法，我们可以把跟原来的业务（上传和下载）没有关系计时功能的代码封装到一个函数中，如果`upload`和`download`函数需要记录时间，我们直接把装饰器作用到这两个函数上即可。既然上面提到了，装饰器是一个高阶函数，它的参数和返回值都是函数，我们将记录时间的装饰器姑且命名为`record_time`，那么它的整体结构应该如下面的代码所示。

```python
def record_time(func):
    
    def wrapper(*args, **kwargs):
        
        result = func(*args, **kwargs)
        
        return result
    
    return wrapper
```

相信大家注意到了，`record_time`函数的参数`func`代表了一个被装饰的函数，函数里面定义的`wrapper`函数是带有装饰功能的函数，它会执行被装饰的函数`func`，它还需要返回在最后产生函数执行的返回值。不知大家是否留意到，上面的代码我在第4行和第6行留下了两个空行，这意味着我们可以这些地方添加代码来实现额外的功能。`record_time`函数最终会返回这个带有装饰功能的函数`wrapper`并通过它替代原函数`func`，当原函数`func`被`record_time`函数装饰后，我们调用它时其实调用的是`wrapper`函数，所以才获得了额外的能力。`wrapper`函数的参数比较特殊，由于我们要用`wrapper`替代原函数`func`，但是我们又不清楚原函数`func`会接受哪些参数，所以我们就通过可变参数和关键字参数照单全收，然后在调用`func`的时候，原封不动的全部给它。这里还要强调一下，Python 语言支持函数的嵌套定义，就像上面，我们可以在`record_time`函数中定义`wrapper`函数，这个操作在很多编程语言中并不被支持。

看懂这个结构后，我们就可以把记录时间的功能写到这个装饰器中

```python
import time


def record_time(func):

    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        # 返回被装饰函数的返回值
        return result
    
    return wrapper
```

写装饰器虽然颇费周折，但是这是个一劳永逸的骚操作，将来再有记录函数执行时间的需求时，我们只需要添加上面的装饰器即可。使用上面的装饰器函数有两种方式，第一种方式就是直接调用装饰器函数，传入被装饰的函数并获得返回值，我们可以用这个返回值直接替代原来的函数，那么在调用时就已经获得了装饰器提供的额外的能力（记录执行时间），大家试试下面的代码就明白了。

```python
download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
```

在 Python 中，使用装饰器有更为便捷的**语法糖**（编程语言中添加的某种语法，这种语法对语言的功能没有影响，但是使用更加方便，代码的可读性也更强，我们将其称之为“语法糖”或“糖衣语法”），可以用`@装饰器函数`将装饰器函数直接放在被装饰的函数上，效果跟上面的代码相同。我们把完整的代码为大家罗列出来，大家可以再看看我们是如何定义和使用装饰器的。

```python
import random
import time


def record_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result

    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
```

上面的代码，我们通过装饰器语法糖为`download`和`upload`函数添加了装饰器，被装饰后的`download`和`upload`函数其实就是我们在装饰器中返回的`wrapper`函数，调用它们其实就是在调用`wrapper`函数，所以才有了记录函数执行时间的功能。

如果在代码的某些地方，我们想去掉装饰器的作用执行原函数，那么在定义装饰器函数的时候，需要做一点点额外的工作。Python 标准库`functools`模块的`wraps`函数也是一个装饰器，我们将它放在`wrapper`函数上，这个装饰器可以帮我们保留被装饰之前的函数，这样在需要取消装饰器时，可以通过被装饰函数的`__wrapped__`属性获得被装饰之前的函数。

```python
import random
import time

from functools import wraps


def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result

    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


# 调用装饰后的函数会记录执行时间
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
# 取消装饰器的作用不记录执行时间
download.__wrapped__('MySQL必知必会.pdf')
upload.__wrapped__('Python从新手到大师.pdf')
```

**装饰器函数本身也可以参数化**，简单的说就是装饰器也是可以通过调用者传入的参数来进行定制的，这个知识点我们在后面用到的时候再为大家讲解。

### 递归调用

Python 中允许函数嵌套定义，也允许函数之间相互调用，而且一个函数还可以直接或间接的调用自身。函数自己调用自己称为递归调用，那么递归调用有什么用处呢？现实中，有很多问题的定义本身就是一个递归定义，例如我们之前讲到的阶乘，非负整数`N`的阶乘是`N`乘以`N-1`的阶乘，即 N!=N×(N−1)! ，定义的左边和右边都出现了阶乘的概念，所以这是一个递归定义。既然如此，我们可以使用递归调用的方式来写一个求阶乘的函数，代码如下所示。

```python
def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)
```

上面的代码中，`fac`函数中又调用了`fac`函数，这就是所谓的递归调用。代码第2行的`if`条件叫做递归的收敛条件，简单的说就是什么时候要结束函数的递归调用，在计算阶乘时，如果计算到`0`或`1`的阶乘，就停止递归调用，直接返回`1`；代码第4行的`num * fac(num - 1)`是递归公式，也就是阶乘的递归定义。下面，我们简单的分析下，如果用`fac(5)`计算`5`的阶乘，整个过程会是怎样的。

```python
# 递归调用函数入栈
# 5 * fac(4)
# 5 * (4 * fac(3))
# 5 * (4 * (3 * fac(2)))
# 5 * (4 * (3 * (2 * fac(1))))
# 停止递归函数出栈
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120
print(fac(5))    # 120
```

注意，函数调用会通过内存中称为“栈”（stack）的数据结构来保存当前代码的执行现场，函数调用结束后会通过这个栈结构恢复之前的执行现场。栈是一种先进后出的数据结构，这也就意味着最早入栈的函数最后才会返回，而最后入栈的函数会最先返回。例如调用一个名为`a`的函数，函数`a`的执行体中又调用了函数`b`，函数`b`的执行体中又调用了函数`c`，那么最先入栈的函数是`a`，最先出栈的函数是`c`。每进入一个函数调用，栈就会增加一层栈帧（stack frame），栈帧就是我们刚才提到的保存当前代码执行现场的结构；每当函数调用结束后，栈就会减少一层栈帧。通常，内存中的栈空间很小，因此递归调用的次数如果太多，会导致栈溢出（stack overflow），所以**递归调用一定要确保能够快速收敛**。我们可以尝试执行`fac(5000)`，看看是不是会提示`RecursionError`错误，错误消息为：`maximum recursion depth exceeded in comparison`（超出最大递归深度），其实就是发生了栈溢出。

如果我们使用官方的 Python 解释器（CPython），默认将函数调用的栈结构最大深度设置为`1000`层。如果超出这个深度，就会发生上面说的`RecursionError`。当然，我们可以使用`sys`模块的`setrecursionlimit`函数来改变递归调用的最大深度，但是我们不建议这样做，因为让递归快速收敛才是我们应该做的事情，否则就应该考虑使用循环递推而不是递归。

再举一个之前讲过的生成斐波那契数列的例子，因为斐波那契数列前两个数都是`1`，从第三个数开始，每个数是前两个数相加的和，可以记为`f(n) = f(n - 1) + f(n - 2)`，很显然这又是一个递归的定义，所以我们可以用下面的递归调用函数来计算第`n`个斐波那契数。

```python
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 21):
    print(fib1(i))
```

需要提醒大家，上面计算斐波那契数的代码虽然看起来非常简单明了，但执行性能是比较糟糕的。大家可以试一试，把上面代码`for`循环中`range`函数的第二个参数修改为`51`，即输出前50个斐波那契数，看看需要多长时间，也欢迎大家在评论区留下你的代码执行时间。至于为什么这么慢，大家可以自己思考一下原因。很显然，直接使用循环递推的方式获得斐波那契数列是更好的选择，代码如下所示。

```python
def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

除此以外，我们还可以使用 Python 标准库中`functools`模块的`lru_cache`函数来优化上面的递归代码。`lru_cache`函数是一个装饰器函数，我们将其置于上面的函数`fib1`之上，它可以缓存该函数的执行结果从而避免在递归调用的过程中产生大量的重复运算，这样代码的执行性能就有“飞一般”的提升。大家可以尝试输出前50个斐波那契数，看看加上装饰器以后代码需要执行多长时间，评论区见！

```python
from functools import lru_cache


@lru_cache()
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 51):
    print(i, fib1(i))
```

> **提示**：`lru_cache`函数是一个带参数的装饰器，所以上面第4行代码使用装饰器语法糖时，`lru_cache`后面要跟上圆括号。`lru_cache`函数有一个非常重要的参数叫`maxsize`，它可以用来定义缓存空间的大小，默认值是128。

在 Python 中，装饰器语法糖是否需要加括号取决于**装饰器的实现方式**：是否需要接收额外参数。

核心区别：装饰器是否需要参数

**1. 无参数装饰器（不加括号）**

- **本质**：装饰器是一个**单参数函数**，直接接收被装饰的函数。
- **语法**：`@decorator` 等价于 `func = decorator(func)`。

```python
def timer(func):  # 接收被装饰的函数
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"耗时: {time.time() - start}秒")
        return result
    return wrapper

@timer  # 等价于：add = timer(add)
def add(a, b):
    return a + b
```

**2. 带参数装饰器（加括号）**

- 本质：装饰器是一个返回真正装饰器的函数（即 “装饰器工厂”）。
  - 外层函数接收装饰器参数（如 `n`），返回内层函数。
  - 内层函数接收被装饰的函数（如 `func`），返回包装函数。
- **语法**：`@decorator(arg)` 等价于 `func = decorator(arg)(func)`。

```python
def repeat(n):  # 外层：接收装饰器参数
    def decorator(func):  # 内层：接收被装饰的函数
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)  # 等价于：greet = repeat(3)(greet)
def greet():
    print("Hello!")
```

**如何实现既支持参数又支持无参数的装饰器？**

通过**参数默认值**和**判断参数类型**实现：

```python
def flexible_decorator(func=None, *, n=1):  # 注意：必须使用关键字参数
    def decorator(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = f(*args, **kwargs)
            return result
        return wrapper
    
    if func is None:
        return decorator  # 带参数调用，如 @flexible_decorator(n=3)
    else:
        return decorator(func)  # 无参数调用，如 @flexible_decorator

@flexible_decorator  # 无参数
def f1():
    pass

@flexible_decorator(n=3)  # 带参数
def f2():
    pass
```

| **场景**               | **装饰器结构**                         | **语法糖写法**                    | **等价展开**                  |
| ---------------------- | -------------------------------------- | --------------------------------- | ----------------------------- |
| 无参数装饰器           | 单函数（接收被装饰函数）               | `@decorator`                      | `func = decorator(func)`      |
| 带参数装饰器           | 函数嵌套（外层接收参数，内层接收函数） | `@decorator(arg)`                 | `func = decorator(arg)(func)` |
| 灵活装饰器（可选参数） | 通过参数判断实现两种调用方式           | `@decorator` 或 `@decorator(arg)` | 需特殊实现逻辑                |

- 若装饰器本身直接接收函数（如 `timer(func)`），则不加括号。
- 若装饰器需要先接收其他参数（如 `repeat(n)`），则必须加括号。

## 17.面向对象编程入门

面向对象编程是一种非常流行的**编程范式**（programming paradigm），所谓编程范式就是**程序设计的方法论**，简单的说就是程序员对程序的认知和理解以及他们编写代码的方式。

在前面的课程中，我们说过“**程序是指令的集合**”，运行程序时，程序中的语句会变成一条或多条指令，然后由CPU（中央处理器）去执行。为了简化程序的设计，我们又讲到了函数，**把相对独立且经常重复使用的代码放置到函数中**，在需要使用这些代码的时候调用函数即可。如果一个函数的功能过于复杂和臃肿，我们又可以进一步**将函数进一步拆分为多个子函数**来降低系统的复杂性。

随着软件复杂性的增加，编写正确可靠的代码会变成了一项极为艰巨的任务，这也是很多人都坚信“软件开发是人类改造世界所有活动中最为复杂的活动”的原因。如何用程序描述复杂系统和解决复杂问题，就成为了所有程序员必须要思考和直面的问题。诞生于上世纪70年代的 Smalltalk 语言让软件开发者看到了希望，因为它引入了一种新的编程范式叫面向对象编程。在面向对象编程的世界里，程序中的**数据和操作数据的函数是一个逻辑上的整体**，我们称之为**对象**，**对象可以接收消息**，解决问题的方法就是**创建对象并向对象发出各种各样的消息**；通过消息传递，程序中的多个对象可以协同工作，这样就能构造出复杂的系统并解决现实中的问题。当然，面向对象编程的雏形还可以向前追溯到更早期的Simula语言，但这不是我们要讨论的重点。

> **说明：** 今天我们使用的很多高级程序设计语言都支持面向对象编程，但是面向对象编程也不是解决软件开发中所有问题的“银弹”，或者说在软件开发这个行业目前还没有所谓的“银弹”。关于这个问题，大家可以参考 IBM360 系统之父弗雷德里克·布鲁克斯所发表的论文《没有银弹：软件工程的本质性与附属性工作》或软件工程的经典著作《人月神话》一书。

### 类和对象

如果要用一句话来概括面向对象编程，我认为下面的说法是相当精辟和准确的。

> **面向对象编程**：把一组数据和处理数据的方法组成**对象**，把行为相同的对象归纳为**类**，通过**封装**隐藏对象的内部细节，通过**继承**实现类的特化和泛化，通过**多态**实现基于对象类型的动态分派。

我们先说说类和对象这两个词。在面向对象编程中，**类是一个抽象的概念，对象是一个具体的概念**。我们把同一类对象的共同特征抽取出来就是一个类，比如我们经常说的人类，这是一个抽象概念，而我们每个人就是人类的这个抽象概念下的实实在在的存在，也就是一个对象。简而言之，**类是对象的蓝图和模板，对象是类的实例，是可以接受消息的实体**。

在面向对象编程的世界中，**一切皆为对象**，**对象都有属性和行为**，**每个对象都是独一无二的**，而且**对象一定属于某个类**。对象的属性是对象的静态特征，对象的行为是对象的动态特征。按照上面的说法，如果我们把拥有共同特征的对象的属性和行为都抽取出来，就可以定义出一个类。

### 定义类

在 Python 语言中，我们可以使用`class`关键字加上类名来定义类，通过缩进我们可以确定类的代码块，就如同定义函数那样。在类的代码块中，我们需要写一些函数，我们说过类是一个抽象概念，那么这些函数就是我们对一类对象共同的动态特征的提取。写在类里面的函数我们通常称之为**方法**，方法就是对象的行为，也就是对象可以接收的消息。方法的第一个参数通常都是`self`，它代表了接收这个消息的对象本身。

```python
class Student:

    def study(self, course_name):
        print(f'学生正在学习{course_name}.')

    def play(self):
        print(f'学生正在玩游戏.')
```

### 创建和使用对象

在我们定义好一个类之后，可以使用构造器语法来创建对象

```python
stu1 = Student()
stu2 = Student()
print(stu1)    # <__main__.Student object at 0x10ad5ac50>
print(stu2)    # <__main__.Student object at 0x10ad5acd0> 
print(hex(id(stu1)), hex(id(stu2)))    # 0x10ad5ac50 0x10ad5acd0
```

在类的名字后跟上圆括号就是所谓的构造器语法，上面的代码创建了两个学生对象，一个赋值给变量`stu1`，一个赋值给变量`stu2`。当我们用`print`函数打印`stu1`和`stu2`两个变量时，我们会看到输出了对象在内存中的地址（十六进制形式），跟我们用`id`函数查看对象标识获得的值是相同的。现在我们可以告诉大家，我们定义的变量其实保存的是一个对象在内存中的逻辑地址（位置），通过这个逻辑地址，我们就可以在内存中找到这个对象。所以`stu3 = stu2`这样的赋值语句并没有创建新的对象，只是用一个新的变量保存了已有对象的地址。

接下来，我们尝试给对象发消息，即调用对象的方法。刚才的`Student`类中我们定义了`study`和`play`两个方法，两个方法的第一个参数`self`代表了接收消息的学生对象，`study`方法的第二个参数是学习的课程名称。Python中，给对象发消息有两种方式

```python
# 通过“类.方法”调用方法
# 第一个参数是接收消息的对象
# 第二个参数是学习的课程名称
Student.study(stu1, 'Python程序设计')    # 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法
# 点前面的对象就是接收消息的对象
# 只需要传入第二个参数课程名称
stu1.study('Python程序设计')             # 学生正在学习Python程序设计.

Student.play(stu2)                      # 学生正在玩游戏.
stu2.play()                             # 学生正在玩游戏. 
```

### 初始化方法

大家可能已经注意到了，刚才我们创建的学生对象只有行为没有属性，如果要给学生对象定义属性，我们可以修改`Student`类，为其添加一个名为`__init__`的方法。在我们调用`Student`类的构造器创建对象时，首先会在内存中获得保存学生对象所需的内存空间，然后通过自动执行`__init__`方法，完成对内存的初始化操作，也就是把数据放到内存空间中。所以我们可以通过给`Student`类添加`__init__`方法的方式为学生对象指定属性，同时完成对属性赋初始值的操作，正因如此，`__init__`方法通常也被称为初始化方法。

```python
class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')
```

修改刚才创建对象和给对象发消息的代码，重新执行一次，看看程序的执行结果有什么变化。

```python
# 调用Student类的构造器创建对象并传入初始化参数
stu1 = Student('骆昊', 44)
stu2 = Student('王大锤', 25)
stu1.study('Python程序设计')    # 骆昊正在学习Python程序设计.
stu2.play()                    # 王大锤正在玩游戏.
```

### 面向对象的支柱

面向对象编程有三大支柱，就是我们之前给大家划重点的时候圈出的三个词：**封装**、**继承**和**多态**。后面两个概念在下一节课中会详细说明，这里我们先说一下什么是封装。我自己对封装的理解是：**隐藏一切可以隐藏的实现细节，只向外界暴露简单的调用接口**。我们在类中定义的对象方法其实就是一种封装，这种封装可以让我们在创建对象之后，只需要给对象发送一个消息就可以执行方法中的代码，也就是说我们在只知道方法的名字和参数（方法的外部视图），不知道方法内部实现细节（方法的内部视图）的情况下就完成了对方法的使用。

### 面向对象案例

时钟 ：定义一个类描述数字时钟，提供走字和显示时间的功能。

```python
import time


# 定义时钟类
class Clock:
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        """走字"""
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """显示时间"""
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'


# 创建时钟对象
clock = Clock(23, 59, 58)
while True:
    # 给时钟对象发消息读取时间
    print(clock.show())
    # 休眠1秒钟
    time.sleep(1)
    # 给时钟对象发消息使其走字
    clock.run()
```

平面上的点：定义一个类描述平面上的点，提供计算到另一个点距离的方法。

```python
class Point:
    """平面上的点"""

    def __init__(self, x=0, y=0):
        """初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x, self.y = x, y

    def distance_to(self, other):
        """计算与另一个点的距离
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** 0.5

    def __str__(self):
        return f'({self.x}, {self.y})'


p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1)  # 调用对象的__str__魔法方法
print(p2)
print(p1.distance_to(p2))
```

在 Python 中，`print(p1)` 能够直接输出 `Point` 类实例的坐标值，是因为 **`Point` 类重写了 `__str__` 特殊方法**。这个方法决定了对象在被转换为字符串时的表现形式。

## 18.面向对象编程进阶

### 可见性和属性装饰器

在很多面向对象编程语言中，对象的属性通常会被设置为私有（private）或受保护（protected）的成员，简单的说就是不允许直接访问这些属性；对象的方法通常都是公开的（public），因为公开的方法是对象能够接受的消息，也是对象暴露给外界的调用接口，这就是所谓的访问可见性。在 Python 中，可以通过给对象属性名添加前缀下划线的方式来说明属性的访问可见性，例如，可以用`__name`表示一个私有属性，`_name`表示一个受保护属性

```python
class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


stu = Student('王大锤', 20)
stu.study('Python程序设计')
print(stu.__name)  # AttributeError: 'Student' object has no attribute '__name'
```

上面代码的最后一行会引发`AttributeError`（属性错误）异常，异常消息为：`'Student' object has no attribute '__name'`。由此可见，以`__`开头的属性`__name`相当于是私有的，在类的外面无法直接访问，但是类里面的`study`方法中可以通过`self.__name`访问该属性。需要说明的是，大多数使用 Python 语言的人在定义类时，通常不会选择让对象的属性私有或受保护，正如有一句名言说的：“**We are all consenting adults here**”（大家都是成年人），成年人可以为自己的行为负责，而不需要通过 Python 语言本身来限制访问可见性。事实上，大多数的程序员都认为**开放比封闭要好**，把对象的属性私有化并非必不可少的东西，所以 Python 语言并没有从语义上做出最严格的限定，也就是说上面的代码如果你愿意，用`stu._Student__name`的方式仍然可以访问到私有属性`__name`，有兴趣的读者可以自己试一试。

### 动态属性

Python 语言属于动态语言，维基百科对动态语言的解释是：“在运行时可以改变其结构的语言，例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化”。动态语言非常灵活，目前流行的 Python 和 JavaScript 都是动态语言，除此之外，诸如 PHP、Ruby 等也都属于动态语言，而 C、C++ 等语言则不属于动态语言。

在 Python 中，我们可以动态为对象添加属性，这是 Python 作为动态类型语言的一项特权，代码如下所示。需要提醒大家的是，对象的方法其实本质上也是对象的属性，如果给对象发送一个无法接收的消息，引发的异常仍然是`AttributeError`。

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
stu.sex = '男'  # 给学生对象动态添加sex属性
```

如果不希望在使用对象时动态的为对象添加属性，可以使用 Python 语言中的`__slots__`魔法。对于`Student`类来说，可以在类中指定`__slots__ = ('name', 'age')`，这样`Student`类的对象只能有`name`和`age`属性，如果想动态添加其他属性将会引发异常，代码如下所示。

```python
class Student:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
stu.sex = '男'
```

### 静态方法和类方法

之前我们在类中定义的方法都是对象方法，换句话说这些方法都是对象可以接收的消息。除了对象方法之外，类中还可以有静态方法和类方法，这两类方法是发给类的消息，二者并没有实质性的区别。在面向对象的世界里，一切皆为对象，我们定义的每一个类其实也是一个对象，而静态方法和类方法就是发送给类对象的消息。那么，什么样的消息会直接发送给类对象呢？

举一个例子，定义一个三角形类，通过传入三条边的长度来构造三角形，并提供计算周长和面积的方法。计算周长和面积肯定是三角形对象的方法，这一点毫无疑问。但是在创建三角形对象时，传入的三条边长未必能构造出三角形，为此我们可以先写一个方法来验证给定的三条边长是否可以构成三角形，这种方法很显然就不是对象方法，因为在调用这个方法时三角形对象还没有创建出来。我们可以把这类方法设计为静态方法或类方法，也就是说这类方法不是发送给三角形对象的消息，而是发送给三角形类的消息，代码如下所示。

```python
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
```

上面的代码使用`staticmethod`装饰器声明了`is_valid`方法是`Triangle`类的静态方法，如果要声明类方法，可以使用`classmethod`装饰器（如上面的代码15~18行所示）。可以直接使用`类名.方法名`的方式来调用静态方法和类方法，二者的区别在于，类方法的第一个参数是类对象本身，而静态方法则没有这个参数。简单的总结一下，**对象方法、类方法、静态方法都可以通过“类名.方法名”的方式来调用，区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象**。静态方法通常也可以直接写成一个独立的函数，因为它并没有跟特定的对象绑定。

在 Python 中，类定义时类名后面的括号 `()` 主要用于指定**父类**（基类），表示该类继承自哪些类。这里的 `object` 是 Python 中所有类的基类（也称为 “根类”）。在 Python 3 中，**即使不显式继承 `object`，类也会自动继承它**

这里做一个补充说明，我们可以给上面计算三角形周长和面积的方法添加一个`property`装饰器（Python 内置类型），这样三角形类的`perimeter`和`area`就变成了两个属性，不再通过调用方法的方式来访问，而是用对象访问属性的方式直接获得，修改后的代码如下所示。

```python
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


t = Triangle(3, 4, 5)
print(f'周长: {t.perimeter}')
print(f'面积: {t.area}')
```

### 继承和多态

面向对象的编程语言支持在已有类的基础上创建新类，从而减少重复代码的编写。提供继承信息的类叫做父类（超类、基类），得到继承信息的类叫做子类（派生类、衍生类）。例如，我们定义一个学生类和一个老师类，我们会发现他们有大量的重复代码，而这些重复代码都是老师和学生作为人的公共属性和行为，所以在这种情况下，我们应该先定义人类，再通过继承，从人类派生出老师类和学生类，代码如下所示。

```python
class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name}正在吃饭.')
    
    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生"""
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
    
    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')



stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')
```

继承的语法是在定义类的时候，在类名后的圆括号中指定当前类的父类。如果定义一个类的时候没有指定它的父类是谁，那么默认的父类是`object`类。`object`类是 Python 中的顶级类，这也就意味着所有的类都是它的子类，要么直接继承它，要么间接继承它。Python 语言允许多重继承，也就是说一个类可以有一个或多个父类，关于多重继承的问题我们在后面会有更为详细的讨论。在子类的初始化方法中，我们可以通过`super().__init__()`来调用父类初始化方法，`super`函数是 Python 内置函数中专门为获取当前对象的父类对象而设计的。从上面的代码可以看出，子类除了可以通过继承得到父类提供的属性和方法外，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力。在实际开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，也叫做“里氏替换原则”（Liskov Substitution Principle）。

子类继承父类的方法后，还可以对方法进行重写（重新实现该方法），不同的子类可以对父类的同一个方法给出不同的实现版本，这样的方法在程序运行时就会表现出多态行为（调用相同的方法，做了不同的事情）。多态是面向对象编程中最精髓的部分，当然也是对初学者来说最难以理解和灵活运用的部分，我们会在下一个章节用专门的例子来讲解这个知识点。

## 19.面向对象编程应用

### 扑克游戏

> **说明**：简单起见，我们的扑克只有52张牌（没有大小王），游戏需要将 52 张牌发到 4 个玩家的手上，每个玩家手上有 13 张牌，按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能。

使用面向对象编程方法，首先需要从问题的需求中找到对象并抽象出对应的类，此外还要找到对象的属性和行为。当然，这件事情并不是特别困难，我们可以从需求的描述中找出名词和动词，名词通常就是对象或者是对象的属性，而动词通常是对象的行为。扑克游戏中至少应该有三类对象，分别是牌、扑克和玩家，牌、扑克、玩家三个类也并不是孤立的。类和类之间的关系可以粗略的分为 **is-a关系（继承）**、**has-a关系（关联）**和 **use-a关系（依赖）**。很显然扑克和牌是 has-a 关系，因为一副扑克有（has-a）52 张牌；玩家和牌之间不仅有关联关系还有依赖关系，因为玩家手上有（has-a）牌而且玩家使用了（use-a）牌。

牌的属性显而易见，有花色和点数。我们可以用 0 到 3 的四个数字来代表四种不同的花色，但是这样的代码可读性会非常糟糕，因为我们并不知道黑桃、红心、草花、方块跟 0 到 3 的数字的对应关系。如果一个变量的取值只有有限多个选项，我们可以使用枚举。与 C、Java 等语言不同的是，Python 中没有声明枚举类型的关键字，但是可以通过继承`enum`模块的`Enum`类来创建枚举类型，代码如下所示。

```python
from enum import Enum


class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)
```

上面的代码可以看出，定义枚举类型其实就是定义符号常量，如`SPADE`、`HEART`等。每个符号常量都有与之对应的值，这样表示黑桃就可以不用数字 0，而是用`Suite.SPADE`；同理，表示方块可以不用数字 3， 而是用`Suite.DIAMOND`。注意，使用符号常量肯定是优于使用字面常量的，因为能够读懂英文就能理解符号常量的含义，代码的可读性会提升很多。Python 中的枚举类型是可迭代类型，简单的说就是可以将枚举类型放到`for-in`循环中，依次取出每一个符号常量及其对应的值，如下所示。

```python
for suite in Suite:
    print(f'{suite}: {suite.value}')
```

在 Python 的枚举（`enum` 模块）中，`value` 属性返回成员对应的值，这是枚举类的**核心特性**。所以通过.value可以获得花色对应的数值。

接下来我们可以定义牌类。

```python
class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'  # 返回牌的花色和点数
```

可以通过下面的代码来测试下`Card`类。

```python
card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1)  # ♠5 
print(card2)  # ♥K
```

接下来我们定义扑克类。

```python
import random


class Poker:
    """扑克"""

    def __init__(self):
        self.cards = [Card(suite, face) 
                      for suite in Suite
                      for face in range(1, 14)]  # 52张牌构成的列表
        self.current = 0  # 记录发牌位置的属性

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)  # 通过random模块的shuffle函数实现随机乱序，它通过原地修改的方式直接改变原序列，不会返回新的序列。

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)
```

嵌套列表推导式（Nested List Comprehension）是 Python 中一种强大且简洁的语法，用于从现有可迭代对象（如列表、元组、集合等）创建新的列表。它允许在一个列表推导式中嵌套另一个列表推导式，从而实现更复杂的数据处理和组合。嵌套列表推导式的核心结构是**多层循环嵌套**，语法格式通常为:

```python
new_list = [expression for outer_item in outer_iterable for inner_item in inner_iterable]

# 等价于以下普通循环结构：
new_list = []
for outer_item in outer_iterable:
    for inner_item in inner_iterable:
        new_list.append(expression)
        
# 目标：创建一个3x3的矩阵，每个元素是行索引和列索引的乘积
matrix = [[i * j for j in range(3)] for i in range(3)]

# 展开后的普通循环写法
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * j)
    matrix.append(row)

print(matrix)  # 输出：[[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# 扑克牌嵌套列表推导式等价写法
self.cards = []
for suite in Suite:  # 遍历每种花色
    for face in range(1, 14):  # 遍历每个点数（1-13）
        self.cards.append(Card(suite, face))  # 创建一张牌并添加到列表
```

```python
poker = Poker()
print(poker.cards)  # 洗牌前的牌
poker.shuffle()
print(poker.cards)  # 洗牌后的牌
```

定义玩家类。

```python
class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []  # 玩家手上的牌

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        """整理手上的牌"""
        self.cards.sort()
```

执行上面的代码会在`player.arrange()`那里出现异常，因为`Player`的`arrange`方法使用了列表的`sort`对玩家手上的牌进行排序，排序需要比较两个`Card`对象的大小，而`<`运算符又不能直接作用于`Card`类型，所以就出现了`TypeError`异常，异常消息为：`'<' not supported between instances of 'Card' and 'Card'`。

为了解决这个问题，我们可以对`Card`类的代码稍作修改，使得两个`Card`对象可以直接用`<`进行大小的比较。这里用到技术叫**运算符重载**，Python 中要实现对`<`运算符的重载，需要在类中添加一个名为`__lt__`的魔术方法。很显然，魔术方法`__lt__`中的`lt`是英文单词“less than”的缩写，以此类推，魔术方法`__gt__`对应`>`运算符，魔术方法`__le__`对应`<=`运算符，`__ge__`对应`>=`运算符，`__eq__`对应`==`运算符，`__ne__`对应`!=`运算符。

修改后的`Card`类代码如下所示。

```python
class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'
    
    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face   # 花色相同比较点数的大小
        return self.suite.value < other.suite.value   # 花色不同比较花色对应的值
```

### 工资结算系统

> **要求**：某公司有三种类型的员工，分别是部门经理、程序员和销售员。需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。其中，部门经理的月薪是固定 15000 元；程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。

通过对上述需求的分析，可以看出部门经理、程序员、销售员都是员工，有相同的属性和行为，那么我们可以先设计一个名为`Employee`的父类，再通过继承的方式从这个父类派生出部门经理、程序员和销售员三个子类。很显然，后续的代码不会创建`Employee` 类的对象，因为我们需要的是具体的员工对象，所以这个类可以设计成专门用于继承的抽象类。Python 语言中没有定义抽象类的关键字，但是可以通过`abc`模块中名为`ABCMeta` 的元类来定义抽象类。关于元类的概念此处不展开讲解，当然大家不用纠结，照做即可。

```python
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪"""
        pass
```

在上面的员工类中，有一个名为`get_salary`的方法用于结算月薪，但是由于还没有确定是哪一类员工，所以结算月薪虽然是员工的公共行为但这里却没有办法实现。对于暂时无法实现的方法，我们可以使用`abstractmethod`装饰器将其声明为抽象方法，所谓**抽象方法就是只有声明没有实现的方法**，**声明这个方法是为了让子类去重写这个方法**。接下来的代码展示了如何从员工类派生出部门经理、程序员、销售员这三个子类以及子类如何重写父类的抽象方法。

```python
class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05
```

上面的`Manager`、`Programmer`、`Salesman`三个类都继承自`Employee`，三个类都分别重写了`get_salary`方法。**重写就是子类对父类已有的方法重新做出实现**。相信大家已经注意到了，三个子类中的`get_salary`各不相同，所以这个方法在程序运行时会产生**多态行为**，多态简单的说就是**调用相同的方法**，**不同的子类对象做不同的事情**。

我们通过下面的代码来完成这个工资结算系统，由于程序员和销售员需要分别录入本月的工作时间和销售额，所以在下面的代码中我们使用了 Python 内置的`isinstance`函数来判断员工对象的类型。我们之前讲过的`type`函数也能识别对象的类型，但是`isinstance`函数更加强大，因为它可以判断出一个对象是不是某个继承结构下的子类型，你可以简单的理解为`type`函数是对对象类型的精准匹配，而`isinstance`函数是对对象类型的模糊匹配。

```python
emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')
```

## 20.文件读写和异常处理

实际开发中常常会遇到对数据进行持久化的场景，所谓持久化是指将数据从无法长久保存数据的存储介质（通常是内存）转移到可以长久保存数据的存储介质（通常是硬盘）中。实现数据持久化最直接简单的方式就是通过**文件系统**将数据保存到**文件**中。

计算机的**文件系统**是一种存储和组织计算机数据的方法，它使得对数据的访问和查找变得容易，文件系统使用**文件**和**树形目录**的抽象逻辑概念代替了硬盘、光盘、闪存等物理设备的数据块概念，用户使用文件系统来保存数据时，不必关心数据实际保存在硬盘的哪个数据块上，只需要记住这个文件的路径和文件名。在写入新数据之前，用户不必关心硬盘上的哪个数据块没有被使用，硬盘上的存储空间管理（分配和释放）功能由文件系统自动完成，用户只需要记住数据被写入到了哪个文件中。

### 打开和关闭文件

有了文件系统，我们可以非常方便的通过文件来读写数据；在Python中要实现文件操作是非常简单的。我们可以使用Python内置的`open`函数来打开文件，在使用`open`函数时，我们可以通过函数的参数指定**文件名**、**操作模式**和**字符编码**等信息，接下来就可以对文件进行读写操作了。这里所说的操作模式是指要打开什么样的文件（字符文件或二进制文件）以及做什么样的操作（读、写或追加），具体如下表所示。

| 操作模式 | 具体含义                         |
| -------- | -------------------------------- |
| `'r'`    | 读取 （默认）                    |
| `'w'`    | 写入（会覆盖之前的内容）         |
| `'x'`    | 写入，如果文件已经存在会产生异常 |
| `'a'`    | 追加，将内容写入到已有文件的末尾 |
| `'b'`    | 二进制模式                       |
| `'t'`    | 文本模式（默认）                 |
| `'+'`    | 更新（既可以读又可以写）         |

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210803201644.png)

在使用`open`函数时，如果打开的文件是字符文件（文本文件），可以通过`encoding`参数来指定读写文件使用的字符编码。如果对字符编码和字符集这些概念不了解，可以看看[《字符集和字符编码》](https://www.cnblogs.com/skynet/archive/2011/05/03/2035105.html)一文，此处不再进行赘述。

使用`open`函数打开文件成功后会返回一个文件对象，通过这个对象，我们就可以实现对文件的读写操作；如果打开文件失败，`open`函数会引发异常，稍后会对此加以说明。如果要关闭打开的文件，可以使用文件对象的`close`方法，这样可以在结束文件操作时释放掉这个文件。

### 读写文本文件

用`open`函数打开文本文件时，需要指定文件名并将文件的操作模式设置为`'r'`，如果不指定，默认值也是`'r'`；如果需要指定字符编码，可以传入`encoding`参数，如果不指定，默认值是None，那么在读取文件时使用的是操作系统默认的编码。需要提醒大家，如果不能保证保存文件时使用的编码方式与`encoding`参数指定的编码方式是一致的，那么就可能因无法解码字符而导致读取文件失败。

下面的例子演示了如何读取一个纯文本文件（一般指只有字符原生编码构成的文件，与富文本相比，纯文本不包含字符样式的控制元素，能够被最简单的文本编辑器直接读取）。

```python
file = open('致橡树.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
```

除了使用文件对象的`read`方法读取文件之外，还可以使用`for-in`循环逐行读取或者用`readlines`方法将文件按行读取到一个列表容器中，代码如下所示。

```python
file = open('致橡树.txt', 'r', encoding='utf-8')
for line in file:
    print(line, end='')
file.close()

file = open('致橡树.txt', 'r', encoding='utf-8')
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()
```

`end=''` 是为了**避免重复换行**。文本文件中的每一行末尾通常包含一个换行符（如 `\n`）。Python 的 `print()` 函数默认会在输出内容后**自动添加一个换行符**。如果不添加`end=''`会导致重复换行

如果要向文件中写入内容，可以在打开文件时使用`w`或者`a`作为操作模式，前者会截断之前的文本内容写入新的内容，后者是在原来内容的尾部追加新的内容。

```python
file = open('致橡树.txt', 'a', encoding='utf-8')
file.write('\n标题：《致橡树》')
file.write('\n作者：舒婷')
file.write('\n时间：1977年3月')
file.close()
```

### 异常处理机制

请注意上面的代码，如果`open`函数指定的文件并不存在或者无法打开，那么将引发异常状况导致程序崩溃。为了让代码具有健壮性和容错性，我们可以**使用Python的异常机制对可能在运行时发生状况的代码进行适当的处理**。Python中和异常相关的关键字有五个，分别是`try`、`except`、`else`、`finally`和`raise`，我们先看看下面的代码，再来为大家介绍这些关键字的用法。

```python
file = None
try:
    file = open('致橡树.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
finally:
    if file:
        file.close()
```

在Python中，我们可以将运行时会出现状况的代码放在`try`代码块中，在`try`后面可以跟上一个或多个`except`块来捕获异常并进行相应的处理。例如，在上面的代码中，文件找不到会引发`FileNotFoundError`，指定了未知的编码会引发`LookupError`，而如果读取文件时无法按指定编码方式解码文件会引发`UnicodeDecodeError`，所以我们在`try`后面跟上了三个`except`分别处理这三种不同的异常状况。在`except`后面，我们还可以加上`else`代码块，这是`try` 中的代码没有出现异常时会执行的代码，而且`else`中的代码不会再进行异常捕获，也就是说如果遇到异常状况，程序会因异常而终止并报告异常信息。最后我们使用`finally`代码块来关闭打开的文件，释放掉程序中获取的外部资源。由于`finally`块的代码不论程序正常还是异常都会执行，甚至是调用了`sys`模块的`exit`函数终止Python程序，`finally`块中的代码仍然会被执行（因为`exit`函数的本质是引发了`SystemExit`异常），因此我们把`finally`代码块称为“总是执行代码块”，它最适合用来做释放外部资源的操作。

Python中内置了大量的异常类型，除了上面代码中用到的异常类型以及之前的课程中遇到过的异常类型外，还有许多的异常类型，其继承结构如下所示。

```python
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

从上面的继承结构可以看出，Python中所有的异常都是`BaseException`的子类型，它有四个直接的子类，分别是：`SystemExit`、`KeyboardInterrupt`、`GeneratorExit`和`Exception`。其中，`SystemExit`表示解释器请求退出，`KeyboardInterrupt`是用户中断程序执行（按下`Ctrl+c`），`GeneratorExit`表示生成器发生异常通知退出，不理解这些异常没有关系，继续学习就好了。值得一提的是`Exception`类，它是常规异常类型的父类型，很多的异常都是直接或间接的继承自`Exception`类。如果Python内置的异常类型不能满足应用程序的需要，我们可以自定义异常类型，而自定义的异常类型也应该直接或间接继承自`Exception`类，当然还可以根据需要重写或添加方法。

在Python中，可以使用`raise`关键字来引发异常（抛出异常对象），而调用者可以通过`try...except...`结构来捕获并处理异常。例如在函数中，当函数的执行条件不满足时，可以使用抛出异常的方式来告知调用者问题的所在，而调用者可以通过捕获处理异常来使得代码从异常中恢复，定义异常和抛出异常的代码如下所示。

```python
class InputError(ValueError):
    """自定义异常类型"""
    pass


def fac(num):
    """求阶乘"""
    if num < 0:
        raise InputError('只能计算非负整数的阶乘')
    if num in (0, 1):
        return 1
    return num * fac(num - 1)
```

调用求阶乘的函数`fac`，通过`try...except...`结构捕获输入错误的异常并打印异常对象（显示异常信息），如果输入正确就计算阶乘并结束程序。

```python
flag = True
while flag:
    num = int(input('n = '))
    try:
        print(f'{num}! = {fac(num)}')
        flag = False
    except InputError as err:
        print(err)
```

### 上下文管理器语法

对于`open`函数返回的文件对象，还可以使用`with`上下文管理器语法在文件操作完成后自动执行文件对象的`close`方法，这样可以让代码变得更加简单优雅，因为不需要再写`finally`代码块来执行关闭文件释放资源的操作。需要提醒大家的是，并不是所有的对象都可以放在`with`上下文语法中，只有符合**上下文管理器协议**（有`__enter__`和`__exit__`魔术方法）的对象才能使用这种语法，Python标准库中的`contextlib`模块也提供了对`with`上下文语法的支持，后面再为大家进行讲解。

用`with`上下文语法改写后的代码如下所示。

```python
try:
    with open('致橡树.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
```

### 读写二进制文件

读写二进制文件跟读写文本文件的操作类似，但是需要注意，在使用`open`函数打开文件时，如果要进行读操作，操作模式是`'rb'`，如果要进行写操作，操作模式是`'wb'`。还有一点，读写文本文件时，`read`方法的返回值以及`write`方法的参数是`str`对象（字符串），而读写二进制文件时，`read`方法的返回值以及`write`方法的参数是`bytes-like`对象（字节串）。下面的代码实现了将当前路径下名为`guido.jpg`的图片文件复制到`吉多.jpg`文件中的操作。

```
try:
    with open('guido.jpg', 'rb') as file1:
        data = file1.read()
    with open('吉多.jpg', 'wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')
```

如果要复制的图片文件很大，一次将文件内容直接读入内存中可能会造成非常大的内存开销，为了减少对内存的占用，可以为`read`方法传入`size`参数来指定每次读取的字节数，通过循环读取和写入的方式来完成上面的操作，代码如下所示。

```
try:
    with open('guido.jpg', 'rb') as file1, open('吉多.jpg', 'wb') as file2:
        data = file1.read(512)
        while data:
            file2.write(data)
            data = file1.read()
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')
```

通过读写文件的操作，我们可以实现数据持久化。在Python中可以通过`open`函数来获得文件对象，可以通过文件对象的`read`和`write`方法实现文件读写操作。程序在运行时可能遭遇无法预料的异常状况，可以使用Python的异常机制来处理这些状况。Python的异常机制主要包括`try`、`except`、`else`、`finally`和`raise`这五个核心关键字。`try`后面的`except`语句不是必须的，`finally`语句也不是必须的，但是二者必须要有一个；`except`语句可以有一个或多个，多个`except`会按照书写的顺序依次匹配指定的异常，如果异常已经处理就不会再进入后续的`except`语句；`except`语句中还可以通过元组同时指定多个异常类型进行捕获；`except`语句后面如果不指定异常类型，则默认捕获所有异常；捕获异常后可以使用`raise`要再次抛出，但是不建议捕获并抛出同一个异常；不建议在不清楚逻辑的情况下捕获所有异常，这可能会掩盖程序中严重的问题。最后强调一点，**不要使用异常机制来处理正常业务逻辑或控制程序流程**，简单的说就是不要滥用异常机制，这是初学者常犯的错误。

## 21.对象的序列化和反序列化

### JSON概述

通过上面的讲解，我们已经知道如何将文本数据和二进制数据保存到文件中，那么这里还有一个问题，如果希望把一个列表或者一个字典中的数据保存到文件中又该怎么做呢？在Python中，我们可以将程序中的数据以JSON格式进行保存。JSON是“JavaScript Object Notation”的缩写，它本来是JavaScript语言中创建对象的一种字面量语法，现在已经被广泛的应用于跨语言跨平台的数据交换。使用JSON的原因非常简单，因为它结构紧凑而且是纯文本，任何操作系统和编程语言都能处理纯文本，这就是**实现跨语言跨平台数据交换**的前提条件。目前JSON基本上已经取代了XML（可扩展标记语言）作为**异构系统间交换数据的事实标准**。可以在[JSON的官方网站](https://www.json.org/json-zh.html)找到更多关于JSON的知识，这个网站还提供了每种语言处理JSON数据格式可以使用的工具或三方库。

```python
{
    name: "骆昊",
    age: 40,
    friends: ["王大锤", "白元芳"],
    cars: [
        {"brand": "BMW", "max_speed": 240},
        {"brand": "Benz", "max_speed": 280},
        {"brand": "Audi", "max_speed": 280}
    ]
}
```

上面是JSON的一个简单例子，大家可能已经注意到了，它跟Python中的字典非常类似而且支持嵌套结构，就好比Python字典中的值可以是另一个字典。我们可以尝试把下面的代码输入浏览器的控制台（对于Chrome浏览器，可以通过“更多工具”菜单找到“开发者工具”子菜单，就可以打开浏览器的控制台），浏览器的控制台提供了一个运行JavaScript代码的交互式环境（类似于Python的交互式环境），下面的代码会帮我们创建出一个JavaScript的对象，我们将其赋值给名为`obj`的变量。

```python
let obj = {
    name: "骆昊",
    age: 40,
    friends: ["王大锤", "白元芳"],
    cars: [
        {"brand": "BMW", "max_speed": 240},
        {"brand": "Benz", "max_speed": 280},
        {"brand": "Audi", "max_speed": 280}
    ]
}
```

![image-20210820143756353](https://github.com/jackfrued/mypic/raw/master/20210820143803.png)

上面的`obj`就是JavaScript中的一个对象，我们可以通过`obj.name`或`obj["name"]`两种方式获取到`name`对应的值，如下图所示。可以注意到，`obj["name"]`这种获取数据的方式跟Python字典通过键获取值的索引操作是完全一致的，而Python中也通过名为`json`的模块提供了字典与JSON双向转换的支持。

![img](https://github.com/jackfrued/mypic/raw/master/20210820144411.png)

我们在JSON中使用的数据类型（JavaScript数据类型）和Python中的数据类型也是很容易找到对应关系的，大家可以看看下面的两张表。

表1：JavaScript数据类型（值）对应的Python数据类型（值）

| JSON                         | Python                    |
| ---------------------------- | ------------------------- |
| `object`                     | `dict`                    |
| `array`                      | `list`                    |
| `string`                     | `str`                     |
| `number `                    | `int` / `float`           |
| `number` (real)              | `float`                   |
| `boolean` (`true` / `false`) | `bool` (`True` / `False`) |
| `null`                       | `None`                    |

表2：Python数据类型（值）对应的JavaScript数据类型（值）

| Python                      | JSON                         |
| --------------------------- | ---------------------------- |
| `dict`                      | `object`                     |
| `list` / `tuple`            | `array`                      |
| `str`                       | `string`                     |
| `int` / `float`             | `number`                     |
| `bool` （`True` / `False`） | `boolean` (`true` / `false`) |
| `None`                      | `null`                       |

### 读写JSON格式的数据

在Python中，如果要将字典处理成JSON格式（以字符串形式存在），可以使用`json`模块的`dumps`函数

```python
import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))
```

运行上面的代码，输出如下所示，可以注意到中文字符都是用Unicode编码显示的。

```python
{"name": "\u9a86\u660a", "age": 40, "friends": ["\u738b\u5927\u9524", "\u767d\u5143\u82b3"], "cars": [{"brand": "BMW", "max_speed": 240}, {"brand": "Audi", "max_speed": 280}, {"brand": "Benz", "max_speed": 280}]}
```

如果要将字典处理成JSON格式并写入文本文件，只需要将`dumps`函数换成`dump`函数并传入文件对象即可，代码如下所示。

```python
import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
with open('data.json', 'w') as file:
    json.dump(my_dict, file)
```

执行上面的代码，会创建`data.json`文件，文件的内容跟上面代码的输出是一样的。

`json`模块有四个比较重要的函数，分别是：

- `dump` - 将Python对象按照JSON格式序列化到文件中
- `dumps` - 将Python对象处理成JSON格式的字符串
- `load` - 将文件中的JSON数据反序列化成对象
- `loads` - 将字符串的内容反序列化成Python对象

这里出现了两个概念，一个叫序列化，一个叫反序列化，[维基百科](https://zh.wikipedia.org/)上的解释是：“序列化（serialization）在计算机科学的数据处理中，是指将数据结构或对象状态转换为可以存储或传输的形式，这样在需要的时候能够恢复到原先的状态，而且通过序列化的数据重新获取字节时，可以利用这些字节来产生原始对象的副本（拷贝）。与这个过程相反的动作，即从一系列字节中提取数据结构的操作，就是反序列化（deserialization）”。

我们可以通过下面的代码，读取上面创建的`data.json`文件，将JSON格式的数据还原成Python中的字典。

```python
import json

with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)
```

### 包管理工具pip

Python标准库中的`json`模块在数据序列化和反序列化时性能并不是非常理想，为了解决这个问题，可以使用三方库`ujson`来替换`json`。所谓三方库，是指非公司内部开发和使用的，也不是来自于官方标准库的Python模块，这些模块通常由其他公司、组织或个人开发，所以被称为三方库。虽然Python语言的标准库虽然已经提供了诸多模块来方便我们的开发，但是对于一个强大的语言来说，它的生态圈一定也是非常繁荣的。

之前安装Python解释器时，默认情况下已经勾选了安装pip，大家可以在命令提示符或终端中通过`pip --version`来确定是否已经拥有了pip。pip是Python的包管理工具，通过pip可以查找、安装、卸载、更新Python的三方库或工具，macOS和Linux系统应该使用pip3。例如要安装替代`json`模块的`ujson`，可以使用下面的命令。

```python
pip install ujson
```

在默认情况下，pip会访问`https://pypi.org/simple/`来获得三方库相关的数据，但是国内访问这个网站的速度并不是十分理想，因此国内用户可以使用豆瓣网提供的镜像来替代这个默认的下载源，操作如下所示。

```python
pip install ujson
```

可以通过`pip search`命令根据名字查找需要的三方库，可以通过`pip list`命令来查看已经安装过的三方库。如果想更新某个三方库，可以使用`pip install -U`或`pip install --upgrade`；如果要删除某个三方库，可以使用`pip uninstall`命令。

搜索`ujson`三方库。

```python
pip search ujson

micropython-cpython-ujson (0.2)  - MicroPython module ujson ported to CPython
pycopy-cpython-ujson (0.2)       - Pycopy module ujson ported to CPython
ujson (3.0.0)                    - Ultra fast JSON encoder and decoder for Python
ujson-bedframe (1.33.0)          - Ultra fast JSON encoder and decoder for Python
ujson-segfault (2.1.57)          - Ultra fast JSON encoder and decoder for Python. Continuing 
                                   development.
ujson-ia (2.1.1)                 - Ultra fast JSON encoder and decoder for Python (Internet 
                                   Archive fork)
ujson-x (1.37)                   - Ultra fast JSON encoder and decoder for Python
ujson-x-legacy (1.35.1)          - Ultra fast JSON encoder and decoder for Python
drf_ujson (1.2)                  - Django Rest Framework UJSON Renderer
drf-ujson2 (1.6.1)               - Django Rest Framework UJSON Renderer
ujsonDB (0.1.0)                  - A lightweight and simple database using ujson.
fast-json (0.3.2)                - Combines best parts of json and ujson for fast serialization
decimal-monkeypatch (0.4.3)      - Python 2 performance patches: decimal to cdecimal, json to 
                                   ujson for psycopg2
```

查看已经安装的三方库。

```python
pip list

Package                       Version
----------------------------- ----------
aiohttp                       3.5.4
alipay                        0.7.4
altgraph                      0.16.1
amqp                          2.4.2
...							  ...
```

更新`ujson`三方库。

```python
pip install -U ujson
```

删除`ujson`三方库。

```python
pip uninstall -y ujson
```

> **提示**：如果要更新`pip`自身，对于macOS系统来说，可以使用命令`pip install -U pip`。在Windows系统上，可以将命令替换为`python -m pip install -U --user pip`。

### 使用网络API获取数据

如果想在我们自己的程序中显示天气、路况、航班等信息，这些信息我们自己没有能力提供，所以必须使用网络数据服务。目前绝大多数的网络数据服务（或称之为网络API）都是基于[HTTP](https://zh.wikipedia.org/wiki/超文本传输协议)或HTTPS提供JSON格式的数据，我们可以通过Python程序发送HTTP请求给指定的URL（统一资源定位符），这个URL就是所谓的网络API，如果请求成功，它会返回HTTP响应，而HTTP响应的消息体中就有我们需要的JSON格式的数据。关于HTTP的相关知识，可以看看阮一峰的[《HTTP协议入门》](http://www.ruanyifeng.com/blog/2016/08/http.html)一文。

国内有很多提供网络API接口的网站，例如[聚合数据](https://www.juhe.cn/)、[阿凡达数据](http://www.avatardata.cn/)等，这些网站上有免费的和付费的数据接口，国外的[{API}Search](http://apis.io/)网站也提供了类似的功能，有兴趣的可以自行研究。下面的例子演示了如何使用[`requests`](http://docs.python-requests.org/zh_CN/latest/)库（基于HTTP进行网络资源访问的三方库）访问网络API获取国内新闻并显示新闻标题和链接。在这个例子中，我们使用了名为[天行数据](https://www.tianapi.com/)的网站提供的国内新闻数据接口，其中的APIKey需要自己到网站上注册申请。在天行数据网站注册账号后会自动分配APIKey，但是要访问接口获取数据，需要绑定验证邮箱或手机，然后还要申请需要使用的接口，如下图所示。

![image-20210820151134034](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210820151134.png)

Python通过URL接入网络，我们推荐大家使用`requests`三方库，它简单且强大，但需要自行安装。

```python
pip install requests
```

获取国内新闻并显示新闻标题和链接。

```python
import requests

resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
if resp.status_code == 200:
    data_model = resp.json()
    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)
```

上面的代码通过`requests`模块的`get`函数向天行数据的国内新闻接口发起了一次请求，如果请求过程没有出现问题，`get`函数会返回一个`Response`对象，通过该对象的`status_code`属性表示HTTP响应状态码，如果不理解没关系，你只需要关注它的值，如果值等于`200`或者其他`2`字头的值，那么我们的请求是成功的。通过`Response`对象的`json()`方法可以将返回的JSON格式的数据直接处理成Python字典，非常方便。天行数据国内新闻接口返回的JSON格式的数据（部分）如下图所示。

![img](https://github.com/jackfrued/mypic/raw/master/20210820154455.png)

> **提示**：上面代码中的APIKey需要换成自己在天行数据网站申请的APIKey。天行数据网站上还有提供了很多非常有意思的API接口，例如：垃圾分类、周公解梦等，大家可以仿照上面的代码来调用这些接口。每个接口都有对应的接口文档，文档中有关于如何使用接口的详细说明。

Python中实现序列化和反序列化除了使用`json`模块之外，还可以使用`pickle`和`shelve`模块，但是这两个模块是使用特有的序列化协议来序列化数据，因此序列化后的数据只能被Python识别，关于这两个模块的相关知识，有兴趣的读者可以自己查找网络上的资料。处理JSON格式的数据很显然是程序员必须掌握的一项技能，因为不管是访问网络API接口还是提供网络API接口给他人使用，都需要具备处理JSON格式数据的相关知识。

## 22.Python读写CSV文件

### CSV文件介绍

CSV（Comma Separated Values）全称逗号分隔值文件是一种简单、通用的文件格式，被广泛的应用于应用程序（数据库、电子表格等）数据的导入和导出以及异构系统之间的数据交换。因为CSV是纯文本文件，不管是什么操作系统和编程语言都是可以处理纯文本的，而且很多编程语言中都提供了对读写CSV文件的支持，因此CSV格式在数据处理和数据科学中被广泛应用。

CSV文件有以下特点：

1. 纯文本，使用某种字符集（如[ASCII](https://zh.wikipedia.org/wiki/ASCII)、[Unicode](https://zh.wikipedia.org/wiki/Unicode)、[GB2312](https://zh.wikipedia.org/wiki/GB2312)）等）；
2. 由一条条的记录组成（典型的是每行一条记录）；
3. 每条记录被分隔符（如逗号、分号、制表符等）分隔为字段（列）；
4. 每条记录都有同样的字段序列。

CSV文件可以使用文本编辑器或类似于Excel电子表格这类工具打开和编辑，当使用Excel这类电子表格打开CSV文件时，你甚至感觉不到CSV和Excel文件的区别。很多数据库系统都支持将数据导出到CSV文件中，当然也支持从CSV文件中读入数据保存到数据库中，这些内容并不是现在要讨论的重点。

### 将数据写入CSV文件

现有五个学生三门课程的考试成绩需要保存到一个CSV文件中，要达成这个目标，可以使用Python标准库中的`csv`模块，该模块的`writer`函数会返回一个`csvwriter`对象，通过该对象的`writerow`或`writerows`方法就可以将数据写入到CSV文件中，具体的代码如下所示。

```python
import csv
import random

with open('scores.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)
        
'''        
生成的CSV文件的内容。
姓名,语文,数学,英语
关羽,98,86,61
张飞,86,58,80
赵云,95,73,70
马超,83,97,55
黄忠,61,54,87
'''
```

需要说明的是上面的`writer`函数，除了传入要写入数据的文件对象外，还可以`dialect`参数，它表示CSV文件的方言，默认值是`excel`。除此之外，还可以通过`delimiter`、`quotechar`、`quoting`参数来指定分隔符（默认是逗号）、包围值的字符（默认是双引号）以及包围的方式。其中，包围值的字符主要用于当字段中有特殊符号时，通过添加包围值的字符可以避免二义性。大家可以尝试将上面第5行代码修改为下面的代码，然后查看生成的CSV文件。

```python
writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)

'''
生成的CSV文件的内容。
"姓名"|"语文"|"数学"|"英语"
"关羽"|"88"|"64"|"65"
"张飞"|"76"|"93"|"79"
"赵云"|"78"|"55"|"76"
"马超"|"72"|"77"|"68"
"黄忠"|"70"|"72"|"51"
'''
```

### 从CSV文件读取数据

如果要读取刚才创建的CSV文件，可以使用下面的代码，通过`csv`模块的`reader`函数可以创建出`csvreader`对象，该对象是一个迭代器，可以通过`next`函数或`for-in`循环读取到文件中的数据。

```python
import csv

with open('scores.csv', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for data_list in reader:
        print(reader.line_num, end='\t')
        for elem in data_list:
            print(elem, end='\t')
        print()
```

上面的代码对`csvreader`对象做`for`循环时，每次会取出一个列表对象，该列表对象包含了一行中所有的字段。

将来如果大家使用Python做数据分析，很有可能会用到名为`pandas`的三方库，它是Python数据分析的神器之一。`pandas`中封装了名为`read_csv`和`to_csv`的函数用来读写CSV文件，其中`read_CSV`会将读取到的数据变成一个`DataFrame`对象，而`DataFrame`就是`pandas`库中最重要的类型，它封装了一系列用于数据处理的方法（清洗、转换、聚合等）；而`to_csv`会将`DataFrame`对象中的数据写入CSV文件，完成数据的持久化。`read_csv`函数和`to_csv`函数远远比原生的`csvreader`和`csvwriter`强大。

## 23.Python读写Excel文件

### Excel简介

Excel 是 Microsoft（微软）为使用 Windows 和 macOS 操作系统开发的一款电子表格软件。Excel 凭借其直观的界面、出色的计算功能和图表工具，再加上成功的市场营销，一直以来都是最为流行的个人计算机数据处理软件。当然，Excel 也有很多竞品，例如 Google Sheets、LibreOffice Calc、Numbers 等，这些竞品基本上也能够兼容 Excel，至少能够读写较新版本的 Excel 文件，当然这些不是我们讨论的重点。掌握用 Python 程序操作 Excel 文件，可以让日常办公自动化的工作更加轻松愉快，而且在很多商业项目中，导入导出 Excel 文件都是特别常见的功能。

Python 操作 Excel 需要三方库的支持，如果要兼容 Excel 2007 以前的版本，也就是`xls`格式的 Excel 文件，可以使用三方库`xlrd`和`xlwt`，前者用于读 Excel 文件，后者用于写 Excel 文件。如果使用较新版本的 Excel，即`xlsx`格式的 Excel 文件，可以使用`openpyxl`库，当然这个库不仅仅可以操作Excel，还可以操作其他基于 Office Open XML 的电子表格文件。

本章我们先讲解基于`xlwt`和`xlrd`操作 Excel 文件，大家可以先使用下面的命令安装这两个三方库以及配合使用的工具模块`xlutils`。

```python
pip install xlwt xlrd xlutils
```

XLS 和 XLSX 都是 Microsoft Excel 电子表格应用程序中的文件格式，XLS 是 Excel 早期版本使用的文件格式，而 XLSX 则是 Excel 2007 及以后版本中主要使用的文件格式。它们的区别主要如下：

- **文件结构**：XLS 文件是以二进制格式存储的，数据都以二进制代码的形式存储，不易被其他程序识别和处理。XLSX 文件则是基于开放文档标准（Open XML）的 XML 文件格式，数据以分层结构存储，可被其他软件解读和编辑。
- **文件大小**：由于 XLS 文件以二进制格式存储，文件体积相对较大。XLSX 文件采用了更高效的压缩算法，在相同数据量的情况下，文件大小通常比 XLS 格式小得多。
- **兼容性与互操作性**：XLS 格式的文件在不同电子表格应用程序之间的互操作性较差，因为该格式是专有的，其他软件可能无法正确读取其中的数据。XLSX 格式则相对更易于在不同软件之间共享和传输，因为它是基于开放文档标准的。
- **功能支持**：XLSX 格式提供了更多的功能和可扩展性。与 XLS 文件格式相比，XLSX 支持更多的行和列数，能够在一个工作表中存储更多的数据。此外，XLSX 还支持更多的数据类型、图表类型和外部链接，提供了更丰富的数据处理和展示功能。

### 读Excel文件

例如在当前文件夹下有一个名为“阿里巴巴2020年股票数据.xls”的 Excel 文件，如果想读取并显示该文件的内容，可以通过如下所示的代码来完成。

```python
import xlrd

# 使用xlrd模块的open_workbook函数打开指定Excel文件并获得Book对象（工作簿）
wb = xlrd.open_workbook('阿里巴巴2020年股票数据.xls')
# 通过Book对象的sheet_names方法可以获取所有表单名称
sheetnames = wb.sheet_names()
print(sheetnames)
# 通过指定的表单名称获取Sheet对象（工作表）
sheet = wb.sheet_by_name(sheetnames[0])
# 通过Sheet对象的nrows和ncols属性获取表单的行数和列数
print(sheet.nrows, sheet.ncols)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        # 通过Sheet对象的cell方法获取指定Cell对象（单元格）
        # 通过Cell对象的value属性获取单元格中的值
        value = sheet.cell(row, col).value
        # 对除首行外的其他行进行数据格式化处理
        if row > 0:
            # 第1列的xldate类型先转成元组再格式化为“年月日”的格式
            if col == 0:
                # xldate_as_tuple函数用于将 Excel 日期数值转换为 Python 元组,返回值：包含 6 个元素的元组 (year, month, day, hour, minute, second)第二个参数只有0和1两个取值
                # 其中0代表以1900-01-01为基准的日期，1代表以1904-01-01为基准的日期
                value = xlrd.xldate_as_tuple(value, 0)
                value = f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'
            # 其他列的number类型处理成小数点后保留两位有效数字的浮点数
            else:
                value = f'{value:.2f}'
        print(value, end='\t')
    print()
# 获取最后一个单元格的数据类型
# 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols - 1)
print(last_cell_type)
# 获取第一行的值（列表）
print(sheet.row_values(0))
# 获取指定行指定列范围的数据（列表）
# 第一个参数代表行索引，第二个和第三个参数代表列的开始（含）和结束（不含）索引
print(sheet.row_slice(3, 0, 5))
```

> **提示**：上面代码中使用的Excel文件“阿里巴巴2020年股票数据.xls”可以通过后面的百度云盘地址进行获取。链接:https://pan.baidu.com/s/1rQujl5RQn9R7PadB2Z5g_g 提取码:e7b4。

相信通过上面的代码，大家已经了解到了如何读取一个 Excel 文件，如果想知道更多关于`xlrd`模块的知识，可以阅读它的[官方文档](https://xlrd.readthedocs.io/en/latest/)。

### 写Excel文件

写入 Excel 文件可以通过`xlwt` 模块的`Workbook`类创建工作簿对象，通过工作簿对象的`add_sheet`方法可以添加工作表，通过工作表对象的`write`方法可以向指定单元格中写入数据，最后通过工作簿对象的`save`方法将工作簿写入到指定的文件或内存中。下面的代码实现了将5 个学生 3 门课程的考试成绩写入 Excel 文件的操作。

```python
import random

import xlwt

student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
scores = [[random.randrange(50, 101) for _ in range(3)] for _ in range(5)]
# 创建工作簿对象（Workbook）
wb = xlwt.Workbook()
# 创建工作表对象（Worksheet）
sheet = wb.add_sheet('一年级二班')
# 添加表头数据
titles = ('姓名', '语文', '数学', '英语')
# enumerate 是一个内置函数，用于在遍历可迭代对象（如列表、元组、字符串）时同时获取元素的索引和值。它将可迭代对象转换为一个枚举对象，返回包含索引和元素的元组，从而简化循环时对索引的处理。
# 0：代表行索引，这里是首行（行索引从 0 起）。
# index：是列索引，会随着循环递增，从而实现横向写入。
for index, title in enumerate(titles):
    sheet.write(0, index, title)
# 将学生姓名和考试成绩写入单元格
# 在 Python 中，对二维列表（即列表的列表）调用 len() 函数会返回外层列表的长度，也就是二维列表的行数。
for row in range(len(scores)):
    sheet.write(row + 1, 0, student_names[row])
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1, scores[row][col])
# 保存Excel工作簿
wb.save('考试成绩表.xls')
```

### 调整单元格样式

在写Excel文件时，我们还可以为单元格设置样式，主要包括字体（Font）、对齐方式（Alignment）、边框（Border）和背景（Background）的设置，`xlwt`对这几项设置都封装了对应的类来支持。要设置单元格样式需要首先创建一个`XFStyle`对象，再通过该对象的属性对字体、对齐方式、边框等进行设定，例如在上面的例子中，如果希望将表头单元格的背景色修改为黄色，可以按照如下的方式进行操作。

```python
header_style = xlwt.XFStyle()
# 创建一个填充模式对象
pattern = xlwt.Pattern()
# 设置为实心填充模式
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# 0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色
pattern.pattern_fore_colour = 5
header_style.pattern = pattern
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    sheet.write(0, index, title, header_style)
```

如果希望为表头设置指定的字体，可以使用`Font`类并添加如下所示的代码。

```python
font = xlwt.Font()
# 字体名称
font.name = '华文楷体'
# 字体大小（20是基准单位，18表示18px）
font.height = 20 * 18
# 是否使用粗体
font.bold = True
# 是否使用斜体
font.italic = False
# 字体颜色
font.colour_index = 1
header_style.font = font
```

> **注意**：上面代码中指定的字体名（`font.name`）应当是本地系统有的字体，例如在我的电脑上有名为“华文楷体”的字体。

如果希望表头垂直居中对齐，可以使用下面的代码进行设置。

```python
align = xlwt.Alignment()
# 垂直方向的对齐方式
align.vert = xlwt.Alignment.VERT_CENTER
# 水平方向的对齐方式
align.horz = xlwt.Alignment.HORZ_CENTER
header_style.alignment = align
```

如果希望给表头加上黄色的虚线边框，可以使用下面的代码来设置。

```python
borders = xlwt.Borders()
props = (
    ('top', 'top_colour'), ('right', 'right_colour'),
    ('bottom', 'bottom_colour'), ('left', 'left_colour')
)
# 通过循环对四个方向的边框样式及颜色进行设定
for position, color in props:
    # 使用setattr内置函数动态给对象指定的属性赋值
    # 设置边框线型为虚线
    setattr(borders, position, xlwt.Borders.DASHED)
    # 设置边框颜色为黄色
    setattr(borders, color, 5)
header_style.borders = borders
```

如果要调整单元格的宽度（列宽）和表头的高度（行高），可以按照下面的代码进行操作。

```python
# 设置行高为40px
sheet.row(0).set_style(xlwt.easyxf(f'font:height {20 * 40}'))
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    # 设置列宽为200px
    sheet.col(index).width = 20 * 200
    # 设置单元格的数据和样式
    sheet.write(0, index, title, header_style)
```

### 公式计算

对于前面打开的“阿里巴巴2020年股票数据.xls”文件，如果要统计全年收盘价（Close字段）的平均值以及全年交易量（Volume字段）的总和，可以使用Excel的公式计算即可。我们可以先使用`xlrd`读取Excel文件夹，然后通过`xlutils`三方库提供的`copy`函数将读取到的Excel文件转成`Workbook`对象进行写操作，在调用`write`方法时，可以将一个`Formula`对象写入单元格。

实现公式计算的代码如下所示。

```
import xlrd
import xlwt
from xlutils.copy import copy

# 打开文件用于读取
wb_for_read = xlrd.open_workbook('阿里巴巴2020年股票数据.xls')
sheet1 = wb_for_read.sheet_by_index(0)
nrows, ncols = sheet1.nrows, sheet1.ncols  # 获取行列数

# 复制工作簿用于写入
wb_for_write = copy(wb_for_read)
sheet2 = wb_for_write.get_sheet(0)

# 在最后一行下方添加公式
sheet2.write(nrows, 4, xlwt.Formula(f'average(E2:E{nrows})'))  # E列添加平均值
sheet2.write(nrows, 5, xlwt.Formula(f'sum(F2:F{nrows})'))      # F列添加总和

# 保存为新文件
wb_for_write.save('阿里巴巴2020年股票数据汇总.xls')
```

掌握了 Python 程序操作 Excel 的方法，可以解决日常办公中很多繁琐的处理 Excel 电子表格工作，最常见就是将多个数据格式相同的 Excel 文件合并到一个文件以及从多个 Excel 文件或表单中提取指定的数据。当然，如果要对表格数据进行处理，使用 Python 数据分析神器之一的 pandas 库可能更为方便。

讲解基于另一个三方库`openpyxl`如何进行 Excel 文件操作，首先需要先安装它。

```python
pip install openpyxl
```

`openpyxl`的优点在于，当我们打开一个 Excel 文件后，既可以对它进行读操作，又可以对它进行写操作，而且在操作的便捷性上是优于`xlwt`和`xlrd`的。此外，如果要进行样式编辑和公式计算，使用`openpyxl`也远比上一个章节我们讲解的方式更为简单，而且`openpyxl`还支持数据透视和插入图表等操作，功能非常强大。有一点需要再次强调，`openpyxl`并不支持操作 Office 2007 以前版本的 Excel 文件。

### 读取Excel文件

例如在当前文件夹下有一个名为“阿里巴巴2020年股票数据.xlsx”的 Excel 文件，如果想读取并显示该文件的内容，可以通过如下所示的代码来完成。

```python
import datetime

import openpyxl

# 加载一个工作簿 ---> Workbook
wb = openpyxl.load_workbook('阿里巴巴2020年股票数据.xlsx')
# 获取工作表的名字
print(wb.sheetnames)
# 获取工作表 ---> Worksheet
sheet = wb.worksheets[0]
# 获得单元格的范围
print(sheet.dimensions)
# 获得行数和列数
print(sheet.max_row, sheet.max_column)

# 获取指定单元格的值
print(sheet.cell(3, 3).value)
print(sheet['C3'].value)
print(sheet['G255'].value)

# 获取多个单元格（嵌套元组）
print(sheet['A2:C5'])

# 读取所有单元格的数据
for row_ch in range(2, sheet.max_row + 1):
    for col_ch in 'ABCDEFG':
        value = sheet[f'{col_ch}{row_ch}'].value
        if type(value) == datetime.datetime:
            print(value.strftime('%Y年%m月%d日'), end='\t')
        elif type(value) == int:
            print(f'{value:<10d}', end='\t')
        elif type(value) == float:
            print(f'{value:.4f}', end='\t')
        else:
            print(value, end='\t')
    print()
```

需要提醒大家一点，`openpyxl`获取指定的单元格有两种方式，一种是通过`cell`方法，需要注意，该方法的行索引和列索引都是从`1`开始的，这是为了照顾用惯了 Excel 的人的习惯；另一种是通过索引运算，通过指定单元格的坐标，例如`C3`、`G255`，也可以取得对应的单元格，再通过单元格对象的`value`属性，就可以获取到单元格的值。通过上面的代码，相信大家还注意到了，可以通过类似`sheet['A2:C5']`或`sheet['A2':'C5']`这样的切片操作获取多个单元格，该操作将返回嵌套的元组，相当于获取到了多行多列。

### 写Excel文件

下面我们使用`openpyxl`来进行写 Excel 操作。

```python
import random

import openpyxl

# 第一步：创建工作簿（Workbook）
wb = openpyxl.Workbook()

# 第二步：添加工作表（Worksheet）
sheet = wb.active
sheet.title = '期末成绩'

titles = ('姓名', '语文', '数学', '英语')
for col_index, title in enumerate(titles):
    sheet.cell(1, col_index + 1, title)

names = ('关羽', '张飞', '赵云', '马超', '黄忠')
for row_index, name in enumerate(names):
    sheet.cell(row_index + 2, 1, name)
    for col_index in range(2, 5):
        sheet.cell(row_index + 2, col_index, random.randrange(50, 101))

# 第四步：保存工作簿
wb.save('考试成绩表.xlsx')
```

### 调整样式和公式计算

在使用`openpyxl`操作 Excel 时，如果要调整单元格的样式，可以直接通过单元格对象（`Cell`对象）的属性进行操作。单元格对象的属性包括字体（`font`）、对齐（`alignment`）、边框（`border`）等，具体的可以参考`openpyxl`的[官方文档](https://openpyxl.readthedocs.io/en/stable/index.html)。在使用`openpyxl`时，如果需要做公式计算，可以完全按照 Excel 中的操作方式来进行，具体的代码如下所示。

```python
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side

# 对齐方式
alignment = Alignment(horizontal='center', vertical='center')
# 边框线条
side = Side(color='ff7f50', style='mediumDashed')

wb = openpyxl.load_workbook('考试成绩表.xlsx')
sheet = wb.worksheets[0]

# 调整行高和列宽
sheet.row_dimensions[1].height = 30
sheet.column_dimensions['E'].width = 120

sheet['E1'] = '平均分'
# 设置字体
sheet.cell(1, 5).font = Font(size=18, bold=True, color='ff1493', name='华文楷体')
# 设置对齐方式
sheet.cell(1, 5).alignment = alignment
# 设置单元格边框
sheet.cell(1, 5).border = Border(left=side, top=side, right=side, bottom=side)
for i in range(2, 7):
    # 公式计算每个学生的平均分
    sheet[f'E{i}'] = f'=average(B{i}:D{i})'
    sheet.cell(i, 5).font = Font(size=12, color='4169e1', italic=True)
    sheet.cell(i, 5).alignment = alignment

wb.save('考试成绩表.xlsx')
```

### 生成统计图表

通过`openpyxl`库，可以直接向 Excel 中插入统计图表，具体的做法跟在 Excel 中插入图表大体一致。我们可以创建指定类型的图表对象，然后通过该对象的属性对图表进行设置。当然，最为重要的是为图表绑定数据，即横轴代表什么，纵轴代表什么，具体的数值是多少。最后，可以将图表对象添加到表单中，具体的代码如下所示。

```python
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook(write_only=True)
sheet = wb.create_sheet()

rows = [
    ('类别', '销售A组', '销售B组'),
    ('手机', 40, 30),
    ('平板', 50, 60),
    ('笔记本', 80, 70),
    ('外围设备', 20, 10),
]

# 向表单中添加行
for row in rows:
    sheet.append(row)

# 创建图表对象
chart = BarChart()
chart.type = 'col'
chart.style = 10
# 设置图表的标题
chart.title = '销售统计图'
# 设置图表纵轴的标题
chart.y_axis.title = '销量'
# 设置图表横轴的标题
chart.x_axis.title = '商品类别'
# 设置数据的范围
data = Reference(sheet, min_col=2, min_row=1, max_row=5, max_col=3)
# 设置分类的范围
cats = Reference(sheet, min_col=1, min_row=2, max_row=5)
# 给图表添加数据
chart.add_data(data, titles_from_data=True)
# 给图表设置分类
chart.set_categories(cats)
chart.shape = 4
# 将图表添加到表单指定的单元格中
sheet.add_chart(chart, 'A10')

wb.save('demo.xlsx')
```

运行上面的代码，打开生成的 Excel 文件，效果如下图所示。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210819235009.png)

## 24.Python操作Word和PowerPoint文件

在日常工作中，有很多简单重复的劳动其实完全可以交给 Python 程序，比如根据样板文件（模板文件）批量的生成很多个 Word 文件或 PowerPoint 文件。Word 是微软公司开发的文字处理程序，相信大家都不陌生，日常办公中很多正式的文档都是用 Word 进行撰写和编辑的，目前使用的 Word 文件后缀名一般为`.docx`。PowerPoint 是微软公司开发的演示文稿程序，是微软的 Office 系列软件中的一员，被商业人士、教师、学生等群体广泛使用，通常也将其称之为“幻灯片”。在 Python 中，可以使用名为`python-docx` 的三方库来操作 Word，可以使用名为`python-pptx`的三方库来生成 PowerPoint。

### 操作Word文档

我们可以先通过下面的命令来安装`python-docx`三方库。

```python
pip install python-docx
```

按照[官方文档](https://python-docx.readthedocs.io/en/latest/)的介绍，我们可以使用如下所示的代码来生成一个简单的 Word 文档。

```python
from docx import Document
from docx.shared import Cm, Pt

from docx.document import Document as Doc

# 创建代表Word文档的Doc对象
document = Document()  # type: Doc
# 添加大标题，第二个参数是标题级别，范围是 0-9，0级是最高级标题
document.add_heading('快快乐乐学Python', 0)
# 添加段落，add_run继续向本段落添加内容，还能设置文本格式（如加粗、斜体、颜色等）
p = document.add_paragraph('Python是一门非常流行的编程语言，它')
run = p.add_run('简单')
run.bold = True
run.font.size = Pt(18)
p.add_run('而且')
run = p.add_run('优雅')
run.font.size = Pt(18)
run.underline = True
p.add_run('。')

# 添加一级标题
document.add_heading('Heading, level 1', level=1)
# 添加带样式的段落
document.add_paragraph('Intense quote', style='Intense Quote')
# 添加无序列表
document.add_paragraph(
    'first item in unordered list', style='List Bullet'
)
document.add_paragraph(
    'second item in ordered list', style='List Bullet'
)
# 添加有序列表
document.add_paragraph(
    'first item in ordered list', style='List Number'
)
document.add_paragraph(
    'second item in ordered list', style='List Number'
)

# 添加图片（注意路径和图片必须要存在）
document.add_picture('resources/guido.jpg', width=Cm(5.2))

# 添加分节符
document.add_section()

records = (
    ('骆昊', '男', '1995-5-5'),
    ('孙美丽', '女', '1992-2-2')
)
# 添加表格
table = document.add_table(rows=1, cols=3)
table.style = 'Dark List'
hdr_cells = table.rows[0].cells
hdr_cells[0].text = '姓名'
hdr_cells[1].text = '性别'
hdr_cells[2].text = '出生日期'
# 为表格添加行
for name, sex, birthday in records:
    row_cells = table.add_row().cells
    row_cells[0].text = name
    row_cells[1].text = sex
    row_cells[2].text = birthday

# 添加分页符
document.add_page_break()

# 保存文档
document.save('demo.docx')
```

> **提示**：上面代码第7行中的注释`# type: Doc`是为了在PyCharm中获得代码补全提示，因为如果不清楚对象具体的数据类型，PyCharm 无法在后续代码中给出`Doc`对象的代码补全提示。
>
> from docx import Document和from docx.document import Document as Doc并不是 “引入同一个包两次”，而是**对同一个模块中的不同对象进行有针对性的导入**，主要是为了在代码中更清晰地区分 “文档类” 和 “文档实例类型注解”，属于 Python 类型提示（Type Hints）的常用技巧。
>
> 1. `from docx import Document`
>    导入的是 `docx` 模块中用于创建 Word 文档的**类**（`Document` 类），后续可以通过 `document = Document()` 来实例化一个具体的文档对象。
> 2. `from docx.document import Document as Doc`
>    导入的是 `docx.document` 模块中定义的 `Document` 类（与上面的类本质上是同一个，但从不同路径导入），并通过 `as Doc` 给它起了一个别名。
>    这个别名通常用于**类型注解**，明确指定变量的类型

执行上面的代码，打开生成的 Word 文档，效果如下图所示。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210820002742.png)

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210820002843.png)

对于一个已经存在的 Word 文件，我们可以通过下面的代码去遍历它所有的段落并获取对应的内容。

```python
from docx import Document
from docx.document import Document as Doc

doc = Document('resources/离职证明.docx')  # type: Doc
# enumerate() 函数用于遍历列表时同时获取每个元素的索引（序号） 和元素本身，这里 no 是段落序号（从 0 开始），p 是每个段落的对象（Paragraph 实例）。
for no, p in enumerate(doc.paragraphs):
    print(no, p.text)
```

读取到的内容如下所示。

```
0 
1 离 职 证 明
2 
3 兹证明 王大锤 ，身份证号码： 100200199512120001 ，于 2018 年 8 月 7 日至 2020 年 6 月 28 日在我单位  开发部 部门担任 Java开发工程师 职务，在职期间无不良表现。因 个人 原因，于 2020 年 6 月 28 日起终止解除劳动合同。现已结清财务相关费用，办理完解除劳动关系相关手续，双方不存在任何劳动争议。
4 
5 特此证明！
6 
7 
8 公司名称（盖章）:成都风车车科技有限公司
9    			2020 年 6 月 28 日
```

讲到这里，相信很多读者已经想到了，我们可以把上面的离职证明制作成一个模板文件，把姓名、身份证号、入职和离职日期等信息用占位符代替，这样通过对占位符的替换，就可以根据实际需要写入对应的信息，这样就可以批量的生成 Word 文档。

按照上面的思路，我们首先编辑一个离职证明的模板文件，如下图所示。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210820004223.png)

接下来我们读取该文件，将占位符替换为真实信息，就可以生成一个新的 Word 文档，如下所示。

```python
from docx import Document
from docx.document import Document as Doc

# 将真实信息用字典的方式保存在列表中
employees = [
    {
        'name': '骆昊',
        'id': '100200198011280001',
        'sdate': '2008年3月1日',
        'edate': '2012年2月29日',
        'department': '产品研发',
        'position': '架构师',
        'company': '成都华为技术有限公司'
    },
    {
        'name': '王大锤',
        'id': '510210199012125566',
        'sdate': '2019年1月1日',
        'edate': '2021年4月30日',
        'department': '产品研发',
        'position': 'Python开发工程师',
        'company': '成都谷道科技有限公司'
    },
    {
        'name': '李元芳',
        'id': '2102101995103221599',
        'sdate': '2020年5月10日',
        'edate': '2021年3月5日',
        'department': '产品研发',
        'position': 'Java开发工程师',
        'company': '同城企业管理集团有限公司'
    },
]
# 对列表进行循环遍历，批量生成Word文档 
for emp_dict in employees:
    # 读取离职证明模板文件
    doc = Document('resources/离职证明模板.docx')  # type: Doc
    # 循环遍历所有段落寻找占位符
    for p in doc.paragraphs:
        if '{' not in p.text:
            continue
        # 不能直接修改段落内容，否则会丢失样式
        # 所以需要对段落中的元素进行遍历并进行查找替换
        for run in p.runs:
            if '{' not in run.text:
                continue
            # 将占位符换成实际内容
            start, end = run.text.find('{'), run.text.find('}')
            # key：提取括号内的内容（去掉括号），作为字典的键。例如 (name) 会提取出 name。
			# place_holder：提取包含括号的完整占位符（如 (name)），用于后续替换。
            key, place_holder = run.text[start + 1:end], run.text[start:end + 1]
            run.text = run.text.replace(place_holder, emp_dict[key])
    # 每个人对应保存一个Word文档
    doc.save(f'{emp_dict["name"]}离职证明.docx')
```

在 `python-docx` 中，`Run`（文本片段）的划分依据是**格式是否一致**，而不是句子是否以句号结尾。因此，一个句子（即使以句号结尾）可能是一个 `Run`，也可能被拆分成多个 `Run`，完全取决于文本的格式变化。

执行上面的代码，会在当前路径下生成三个 Word 文档，如下图所示。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210820004825.png)

### 生成PowerPoint

首先我们需要安装名为`python-pptx`的三方库，命令如下所示。

```python
pip install python-pptx
```

用 Python 操作 PowerPoint 的内容，因为实际应用场景不算很多，我不打算在这里进行赘述，有兴趣的读者可以自行阅读`python-pptx`的[官方文档](https://python-pptx.readthedocs.io/en/latest/)，下面仅展示一段来自于官方文档的代码。

```python
from pptx import Presentation

# 创建幻灯片对象
pres = Presentation()

# 选择母版添加一页
title_slide_layout = pres.slide_layouts[0]
slide = pres.slides.add_slide(title_slide_layout)
# 获取标题栏和副标题栏
title = slide.shapes.title
subtitle = slide.placeholders[1]
# 编辑标题和副标题
title.text = "Welcome to Python"
subtitle.text = "Life is short, I use Python"

# 选择母版添加一页
bullet_slide_layout = pres.slide_layouts[1]
slide = pres.slides.add_slide(bullet_slide_layout)
# 获取页面上所有形状
shapes = slide.shapes
# 获取标题和主体
title_shape = shapes.title
body_shape = shapes.placeholders[1]
# 编辑标题
title_shape.text = 'Introduction'
# 编辑主体内容
tf = body_shape.text_frame
tf.text = 'History of Python'
# 添加一个一级段落
p = tf.add_paragraph()
p.text = 'X\'max 1989'
p.level = 1
# 添加一个二级段落
p = tf.add_paragraph()
p.text = 'Guido began to write interpreter for Python.'
p.level = 2

# 保存幻灯片
pres.save('test.pptx')
```

运行上面的代码，生成的 PowerPoint 文件如下图所示。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210820010306.png)

## 25.Python操作PDF文件

PDF 是 Portable Document Format 的缩写，这类文件通常使用`.pdf`作为其扩展名。在日常开发工作中，最容易遇到的就是从 PDF 中读取文本内容以及用已有的内容生成PDF文档这两个任务。

### 从PDF中提取文本

在 Python 中，可以使用名为`PyPDF2`的三方库来读取 PDF 文件，可以使用下面的命令来安装它。

```python
pip install PyPDF2
```

`PyPDF2`没有办法从 PDF 文档中提取图像、图表或其他媒体，但它可以提取文本，并将其返回为 Python 字符串。

```python
import PyPDF2

reader = PyPDF2.PdfReader('test.pdf')
for page in reader.pages:
    print(page.extract_text())
```

当然，`PyPDF2`并不是什么样的 PDF 文档都能提取出文字来，这个问题就我所知并没有什么特别好的解决方法，尤其是在提取中文的时候。网上也有很多讲解从 PDF 中提取文字的文章，推荐大家自行阅读[《三大神器助力Python提取pdf文档信息》](https://cloud.tencent.com/developer/article/1395339)一文进行了解。

```pyth
pip install pdfminer.six
pdf2text.py test.pdf
```

### 旋转和叠加页面

上面的代码中通过创建`PdfFileReader`对象的方式来读取 PDF 文档，该对象的`getPage`方法可以获得PDF文档的指定页并得到一个`PageObject`对象，通过`PageObject`对象的`rotateClockwise`和`rotateCounterClockwise`方法可以实现页面的顺时针和逆时针方向旋转，通过`PageObject`对象的`addBlankPage`方法可以添加一个新的空白页，代码如下所示。

```python
reader = PyPDF2.PdfReader('XGBoost.pdf')
writer = PyPDF2.PdfWriter()

for no, page in enumerate(reader.pages):
    if no % 2 == 0:
        new_page = page.rotate(-90)
    else:
        new_page = page.rotate(90)
    writer.add_page(new_page)

# 将 PDF 写入器（writer）中的内容保存到本地文件
with open('temp.pdf', 'wb') as file_obj:
    writer.write(file_obj)
```

### 加密PDF文件

使用`PyPDF2`中的`PdfFileWrite`对象可以为PDF文档加密，如果需要给一系列的PDF文档设置统一的访问口令，使用Python程序来处理就会非常的方便。

```python
import PyPDF2

reader = PyPDF2.PdfReader('XGBoost.pdf')
writer = PyPDF2.PdfWriter()

for page in reader.pages:
    writer.add_page(page)
    
writer.encrypt('foobared')

with open('temp.pdf', 'wb') as file_obj:
    writer.write(file_obj)
```

### 批量添加水印

上面提到的`PageObject`对象还有一个名为`mergePage`的方法，可以两个 PDF 页面进行叠加，通过这个操作，我们很容易实现给PDF文件添加水印的功能。例如要给上面的“XGBoost.pdf”文件添加一个水印，我们可以先准备好一个提供水印页面的 PDF 文件，然后将包含水印的`PageObject`读取出来，然后再循环遍历“XGBoost.pdf”文件的每个页，获取到`PageObject`对象，然后通过`mergePage`方法实现水印页和原始页的合并，代码如下所示。

```python
reader1 = PyPDF2.PdfReader('XGBoost.pdf')
reader2 = PyPDF2.PdfReader('watermark.pdf')
writer = PyPDF2.PdfWriter()
watermark_page = reader2.pages[0]

for page in reader1.pages:
    page.merge_page(watermark_page)
    writer.add_page(page)

with open('temp.pdf', 'wb') as file_obj:
    writer.write(file_obj)
```

### 创建PDF文件

创建 PDF 文档需要三方库`reportlab`的支持，安装的方法如下所示。

```python
pip install reportlab
```

下面通过一个例子为大家展示`reportlab`的用法。

```python
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

pdf_canvas = canvas.Canvas('resources/demo.pdf', pagesize=A4)
width, height = A4

# 绘图
image = canvas.ImageReader('resources/guido.jpg')
# 第2，3个参数为xy坐标，最后两个参数为图片宽和高
pdf_canvas.drawImage(image, 20, height - 395, 250, 375)

# 显示当前页
pdf_canvas.showPage()

# 注册字体文件
pdfmetrics.registerFont(TTFont('Font1', 'resources/fonts/Vera.ttf'))
pdfmetrics.registerFont(TTFont('Font2', 'resources/fonts/青呱石头体.ttf'))

# 写字
pdf_canvas.setFont('Font2', 40)
# 参数分别代表RGB和透明度
pdf_canvas.setFillColorRGB(0.9, 0.5, 0.3, 1)
pdf_canvas.drawString(width // 2 - 120, height // 2, '你好，世界！')
pdf_canvas.setFont('Font1', 40)
pdf_canvas.setFillColorRGB(0, 1, 0, 0.5)
pdf_canvas.rotate(18)
pdf_canvas.drawString(250, 250, 'hello, world!')

# 保存
pdf_canvas.save()
```

上面的代码如果不太理解也没有关系，等真正需要用 Python 创建 PDF 文档的时候，再好好研读一下`reportlab`的[官方文档](https://www.reportlab.com/docs/reportlab-userguide.pdf)就可以了。

## 26.Python处理图像

### 入门知识

1. 颜色。如果你有使用颜料画画的经历，那么一定知道混合红、黄、蓝三种颜料可以得到其他的颜色，事实上这三种颜色就是美术中的三原色，它们是不能再分解的基本颜色。在计算机中，我们可以将红、绿、蓝三种色光以不同的比例叠加来组合成其他的颜色，因此这三种颜色就是色光三原色。在计算机系统中，我们通常会将一个颜色表示为一个 RGB 值或 RGBA 值（其中的 A 表示 Alpha 通道，它决定了透过这个图像的像素，也就是透明度）。

   | 名称        | RGB值           | 名称         | RGB值         |
   | ----------- | --------------- | ------------ | ------------- |
   | White（白） | (255, 255, 255) | Red（红）    | (255, 0, 0)   |
   | Green（绿） | (0, 255, 0)     | Blue（蓝）   | (0, 0, 255)   |
   | Gray（灰）  | (128, 128, 128) | Yellow（黄） | (255, 255, 0) |
   | Black（黑） | (0, 0, 0)       | Purple（紫） | (128, 0, 128) |

2. 像素。对于一个由数字序列表示的图像来说，最小的单位就是图像上单一颜色的小方格，这些小方块都有一个明确的位置和被分配的色彩数值，而这些一小方格的颜色和位置决定了该图像最终呈现出来的样子，它们是不可分割的单位，我们通常称之为像素（pixel）。每一个图像都包含了一定量的像素，这些像素决定图像在屏幕上所呈现的大小，大家如果爱好拍照或者自拍，对像素这个词就不会陌生。

### 用Pillow处理图像

Pillow 是由从著名的 Python 图像处理库 PIL 发展出来的一个分支，通过 Pillow 可以实现图像压缩和图像处理等各种操作。可以使用下面的命令来安装 Pillow。

```python
pip install pillow
```

Pillow 中最为重要的是`Image`类，可以通过`Image`模块的`open`函数来读取图像并获得`Image`类型的对象。

1. 读取和显示图像

   ```python
   from PIL import Image
   
   # 读取图像获得Image对象
   image = Image.open('guido.jpg')
   # 通过Image对象的format属性获得图像的格式
   print(image.format) # JPEG
   # 通过Image对象的size属性获得图像的尺寸
   print(image.size)   # (500, 750)
   # 通过Image对象的mode属性获取图像的模式
   print(image.mode)   # RGB
   # 通过Image对象的show方法显示图像
   image.show()
   ```

   ![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210803202628.png)

2. 剪裁图像

   ```python
   # 通过Image对象的crop方法指定剪裁区域剪裁图像，参数列表为左上角的xy坐标，右下角的xy坐标
   image.crop((80, 20, 310, 360)).show()
   ```

   ![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210803202701.png)

3. 生成缩略图

   ```python
   # 通过Image对象的thumbnail方法生成指定尺寸的缩略图
   image.thumbnail((128, 128))
   image.show()
   ```

   ![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210803202722.png)

4. 缩放和粘贴图像

   ```python
   # 读取骆昊的照片获得Image对象
   luohao_image = Image.open('luohao.png')
   # 读取吉多的照片获得Image对象
   guido_image = Image.open('guido.jpg')
   # 从吉多的照片上剪裁出吉多的头
   guido_head = guido_image.crop((80, 20, 310, 360))
   width, height = guido_head.size
   # 使用Image对象的resize方法修改图像的尺寸
   # 使用Image对象的paste方法将吉多的头粘贴到骆昊的照片上
   luohao_image.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
   luohao_image.show()
   ```

   ![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210803202749.png)

5. 旋转和翻转

   ```python
   image = Image.open('guido.jpg')
   # 使用Image对象的rotate方法实现图像的旋转
   image.rotate(45).show()
   # 使用Image对象的transpose方法实现图像翻转
   # Image.FLIP_LEFT_RIGHT - 水平翻转
   # Image.FLIP_TOP_BOTTOM - 垂直翻转
   image.transpose(Image.FLIP_TOP_BOTTOM).show()
   ```

   ![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210803202829.png)

6. 操作像素

   ```python
   for x in range(80, 310):
       for y in range(20, 360):
           # 通过Image对象的putpixel方法修改图像指定像素点
           image.putpixel((x, y), (128, 128, 128))
   image.show()
   ```

   ![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210803202932.png)

7. 滤镜效果

   ```python
   from PIL import ImageFilter
   
   # 使用Image对象的filter方法对图像进行滤镜处理
   # ImageFilter模块包含了诸多预设的滤镜也可以自定义滤镜
   image.filter(ImageFilter.CONTOUR).show()
   ```

   ![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210803202953.png)

### 使用Pillow绘图

Pillow 中有一个名为`ImageDraw`的模块，该模块的`Draw`函数会返回一个`ImageDraw`对象，通过`ImageDraw`对象的`arc`、`line`、`rectangle`、`ellipse`、`polygon`等方法，可以在图像上绘制出圆弧、线条、矩形、椭圆、多边形等形状，也可以通过该对象的`text`方法在图像上添加文字。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210803203016.png)

要绘制如上图所示的图像，完整的代码如下所示。

```python
import random

from PIL import Image, ImageDraw, ImageFont


def random_color():
    """生成随机颜色"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


width, height = 800, 600
# 创建一个800*600的图像，背景色为白色
image = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
# 创建一个ImageDraw对象
drawer = ImageDraw.Draw(image)
# 通过指定字体和大小获得ImageFont对象
font = ImageFont.truetype('Kongxin.ttf', 32)
# 通过ImageDraw对象的text方法绘制文字
drawer.text((300, 50), 'Hello, world!', fill=(255, 0, 0), font=font)
# 通过ImageDraw对象的line方法绘制两条对角直线
drawer.line((0, 0, width, height), fill=(0, 0, 255), width=2)
drawer.line((width, 0, 0, height), fill=(0, 0, 255), width=2)
xy = width // 2 - 60, height // 2 - 60, width // 2 + 60, height // 2 + 60
# 通过ImageDraw对象的rectangle方法绘制矩形
drawer.rectangle(xy, outline=(255, 0, 0), width=2)
# 通过ImageDraw对象的ellipse方法绘制椭圆
for i in range(4):
    left, top, right, bottom = 150 + i * 120, 220, 310 + i * 120, 380
    drawer.ellipse((left, top, right, bottom), outline=random_color(), width=8)
# 显示图像
image.show()
# 保存图像
image.save('result.png')
```

> **注意**：上面代码中使用的字体文件需要根据自己准备，可以选择自己喜欢的字体文件并放置在代码目录下。

使用 Python 语言做开发，除了可以用 Pillow 来处理图像外，还可以使用更为强大的 OpenCV 库来完成图形图像的处理，OpenCV（**Open** Source **C**omputer **V**ision Library）是一个跨平台的计算机视觉库，可以用来开发实时图像处理、计算机视觉和模式识别程序。在我们的日常工作中，有很多繁琐乏味的任务其实都可以通过 Python 程序来处理，编程的目的就是让计算机帮助我们解决问题，减少重复乏味的劳动。通过本章节的学习，相信大家已经感受到了使用 Python 程序绘图改图的乐趣，其实 Python 能做的事情还远不止这些，继续你的学习吧。

## 27.Python发送邮件和短信

在前面的课程中，我们已经教会大家如何用 Python 程序自动的生成 Excel、Word、PDF 文档，接下来我们还可以更进一步，就是通过邮件将生成好的文档发送给指定的收件人，然后用短信告知对方我们发出了邮件。这些事情利用 Python 程序也可以轻松愉快的解决。

### 发送电子邮件

在即时通信软件如此发达的今天，电子邮件仍然是互联网上使用最为广泛的应用之一，公司向应聘者发出录用通知、网站向用户发送一个激活账号的链接、银行向客户推广它们的理财产品等几乎都是通过电子邮件来完成的，而这些任务应该都是由程序自动完成的。

我们可以用HTTP（超文本传输协议）来访问网站资源，HTTP 是一个应用级协议，它建立在 TCP（传输控制协议）之上，TCP 为很多应用级协议提供了可靠的数据传输服务。如果要发送电子邮件，需要使用 SMTP（简单邮件传输协议），它也是建立在 TCP 之上的应用级协议，规定了邮件的发送者如何跟邮件服务器进行通信的细节。Python 通过名为`smtplib`的模块将这些操作简化成了`SMTP_SSL`对象，通过该对象的`login`和`send_mail`方法，就能够完成发送邮件的操作。

我们先尝试一下发送一封极为简单的邮件，该邮件不包含附件、图片以及其他超文本内容。发送邮件首先需要接入邮件服务器，我们可以自己架设邮件服务器，这件事情对新手并不友好，但是我们可以选择使用第三方提供的邮件服务。例如，我在<[www.126.com>已经注册了账号，登录成功之后，就可以在设置中开启](http://www.126.xn--com>,,-sd0mtjjwx9ac6uc0dcsgsdur2tz56brqyfnid4fu4bl34ay37d49vcs86bxwdwp2jg2i/) SMTP 服务，这样就相当于获得了邮件服务器，具体的操作如下所示。

![image-20210820190306861](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210820190307.png)

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210820190816.png)

用手机扫码上面的二维码可以通过发送短信的方式来获取授权码，短信发送成功后，点击“我已发送”就可以获得授权码。授权码需要妥善保管，因为一旦泄露就会被其他人冒用你的身份来发送邮件。接下来，我们就可以编写发送邮件的代码了，如下所示。

```python
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 创建邮件主体对象
email = MIMEMultipart()
# 设置发件人、收件人和主题
email['From'] = 'xxxxxxxxx@126.com'
email['To'] = 'yyyyyy@qq.com;zzzzzz@1000phone.com'
email['Subject'] = Header('上半年工作情况汇报', 'utf-8')
# 添加邮件正文内容
content = """据德国媒体报道，当地时间9日，德国火车司机工会成员进行了投票，
定于当地时间10日起进行全国性罢工，货运交通方面的罢工已于当地时间10日19时开始。
此后，从11日凌晨2时到13日凌晨2时，德国全国范围内的客运和铁路基础设施将进行48小时的罢工。"""
email.attach(MIMEText(content, 'plain', 'utf-8'))

# 创建SMTP_SSL对象（连接邮件服务器）
smtp_obj = smtplib.SMTP_SSL('smtp.126.com', 465)
# 通过用户名和授权码进行登录
smtp_obj.login('xxxxxxxxx@126.com', '邮件服务器的授权码')
# 发送邮件（发件人、收件人、邮件内容（字符串））
smtp_obj.sendmail(
    'xxxxxxxxx@126.com',
    ['yyyyyy@qq.com', 'zzzzzz@1000phone.com'],
    email.as_string()
)
```

如果要发送带有附件的邮件，只需要将附件的内容处理成 BASE64 编码，那么它就和普通的文本内容几乎没有什么区别。BASE64 是一种基于 64 个可打印字符来表示二进制数据的表示方法，常用于某些需要表示、传输、存储二进制数据的场合，电子邮件就是其中之一。对这种编码方式不理解的同学，推荐阅读[《Base64笔记》](http://www.ruanyifeng.com/blog/2008/06/base64.html)一文。在之前的内容中，我们也提到过，Python 标准库的`base64`模块提供了对 BASE64 编解码的支持。

下面的代码演示了如何发送带附件的邮件。

```python
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

# 创建邮件主体对象
email = MIMEMultipart()
# 设置发件人、收件人和主题
email['From'] = 'xxxxxxxxx@126.com'
email['To'] = 'zzzzzzzz@1000phone.com'
email['Subject'] = Header('请查收离职证明文件', 'utf-8')
# 添加邮件正文内容（带HTML标签排版的内容）
content = """<p>亲爱的前同事：</p>
<p>你需要的离职证明在附件中，请查收！</p>
<br>
<p>祝，好！</p>
<hr>
<p>孙美丽 即日</p>"""
email.attach(MIMEText(content, 'html', 'utf-8'))
# 读取作为附件的文件
with open(f'resources/王大锤离职证明.docx', 'rb') as file:
    attachment = MIMEText(file.read(), 'base64', 'utf-8')
    # 指定内容类型
    attachment['content-type'] = 'application/octet-stream'
    # 将中文文件名处理成百分号编码
    filename = quote('王大锤离职证明.docx')
    # 指定如何处置内容
    attachment['content-disposition'] = f'attachment; filename="{filename}"'

# 创建SMTP_SSL对象（连接邮件服务器）
smtp_obj = smtplib.SMTP_SSL('smtp.126.com', 465)
# 通过用户名和授权码进行登录
smtp_obj.login('xxxxxxxxx@126.com', '邮件服务器的授权码')
# 发送邮件（发件人、收件人、邮件内容（字符串））
smtp_obj.sendmail(
    'xxxxxxxxx@126.com',
    'zzzzzzzz@1000phone.com',
    email.as_string()
)
```

为了方便大家用 Python 实现邮件发送，我将上面的代码封装成了函数，使用的时候大家只需要调整邮件服务器域名、端口、用户名和授权码就可以了。

```python
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

# 邮件服务器域名（自行修改）
EMAIL_HOST = 'smtp.126.com'
# 邮件服务端口（通常是465）
EMAIL_PORT = 465
# 登录邮件服务器的账号（自行修改）
EMAIL_USER = 'xxxxxxxxx@126.com'
# 开通SMTP服务的授权码（自行修改）
EMAIL_AUTH = '邮件服务器的授权码'


def send_email(*, from_user, to_users, subject='', content='', filenames=[]):
    """发送邮件
    
    :param from_user: 发件人
    :param to_users: 收件人，多个收件人用英文分号进行分隔
    :param subject: 邮件的主题
    :param content: 邮件正文内容
    :param filenames: 附件要发送的文件路径
    """
    email = MIMEMultipart()
    email['From'] = from_user
    email['To'] = to_users
    email['Subject'] = subject

    message = MIMEText(content, 'plain', 'utf-8')
    email.attach(message)
    for filename in filenames:
        with open(filename, 'rb') as file:
            pos = filename.rfind('/')
            display_filename = filename[pos + 1:] if pos >= 0 else filename
            display_filename = quote(display_filename)
            attachment = MIMEText(file.read(), 'base64', 'utf-8')
            attachment['content-type'] = 'application/octet-stream'
            attachment['content-disposition'] = f'attachment; filename="{display_filename}"'
            email.attach(attachment)

    smtp = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
    smtp.login(EMAIL_USER, EMAIL_AUTH)
    smtp.sendmail(from_user, to_users.split(';'), email.as_string())
```

### 发送短信

发送短信也是项目中常见的功能，网站的注册码、验证码、营销信息基本上都是通过短信来发送给用户的。发送短信需要三方平台的支持，下面我们以[螺丝帽平台](https://luosimao.com/)为例，为大家介绍如何用 Python 程序发送短信。注册账号和购买短信服务的细节我们不在这里进行赘述，大家可以咨询平台的客服。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210820194421.png)

接下来，我们可以通过`requests`库向平台提供的短信网关发起一个 HTTP 请求，通过将接收短信的手机号和短信内容作为参数，就可以发送短信，代码如下所示。

```python
import random

import requests


def send_message_by_luosimao(tel, message):
    """发送短信（调用螺丝帽短信网关）"""
    resp = requests.post(
        url='http://sms-api.luosimao.com/v1/send.json',
        auth=('api', 'key-注册成功后平台分配的KEY'),
        data={
            'mobile': tel,
            'message': message
        },
        timeout=10,
        verify=False
    )
    return resp.json()


def gen_mobile_code(length=6):
    """生成指定长度的手机验证码"""
    return ''.join(random.choices('0123456789', k=length))


def main():
    code = gen_mobile_code()
    message = f'您的短信验证码是{code}，打死也不能告诉别人哟！【Python小课】'
    print(send_message_by_luosimao('13500112233', message))


if __name__ == '__main__':
    main()
```

上面请求螺丝帽的短信网关`http://sms-api.luosimao.com/v1/send.json`会返回JSON格式的数据，如果返回`{'error': 0, 'msg': 'OK'}`就说明短信已经发送成功了，如果`error`的值不是`0`，可以通过查看官方的[开发文档](https://luosimao.com/docs/api/)了解到底哪个环节出了问题。螺丝帽平台常见的错误类型如下图所示。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210820195505.png)

目前，大多数短信平台都会要求短信内容必须附上签名，下图是我在螺丝帽平台配置的短信签名“【Python小课】”。有些涉及到敏感内容的短信，还需要提前配置短信模板，有兴趣的读者可以自行研究。一般情况下，平台为了防范短信被盗用，还会要求设置“IP 白名单”，不清楚如何配置的可以咨询平台客服。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210820194653.png)

当然国内的短信平台很多，读者可以根据自己的需要进行选择（通常会考虑费用预算、短信达到率、使用的难易程度等指标），如果需要在商业项目中使用短信服务建议购买短信平台提供的套餐服务。

其实，发送邮件和发送短信一样，也可以通过调用三方服务来完成，在实际的商业项目中，建议自己架设邮件服务器或购买三方服务来发送邮件，这个才是比较靠谱的选择。

## 28.正则表达式的应用

### 正则表达式相关知识

在编写处理字符串的程序时，经常会遇到在一段文本中查找符合某些规则的字符串的需求，正则表达式就是用于描述这些规则的工具，换句话说，我们可以使用正则表达式来定义字符串的匹配模式，即如何检查一个字符串是否有跟某种模式匹配的部分或者从一个字符串中将与模式匹配的部分提取出来或者替换掉。

举一个简单的例子，如果你在 Windows 操作系统中使用过文件查找并且在指定文件名时使用过通配符（`*`和`?`），那么正则表达式也是与之类似的用 来进行文本匹配的工具，只不过比起通配符正则表达式更强大，它能更精确地描述你的需求，当然你付出的代价是书写一个正则表达式比使用通配符要复杂得多，因为任何给你带来好处的东西都需要你付出对应的代价。

再举一个例子，我们从某个地方（可能是一个文本文件，也可能是网络上的一则新闻）获得了一个字符串，希望在字符串中找出手机号和座机号。当然我们可以设定手机号是 11 位的数字（注意并不是随机的 11 位数字，因为你没有见过“25012345678”这样的手机号），而座机号则是类似于“区号-号码”这样的模式，如果不使用正则表达式要完成这个任务就会比较麻烦。最初计算机是为了做数学运算而诞生的，处理的信息基本上都是数值，而今天我们在日常工作中处理的信息很多都是文本数据，我们希望计算机能够识别和处理符合某些模式的文本，正则表达式就显得非常重要了。今天几乎所有的编程语言都提供了对正则表达式操作的支持，Python 通过标准库中的`re`模块来支持正则表达式操作。

关于正则表达式的相关知识，大家可以阅读一篇非常有名的博文叫[《正则表达式30分钟入门教程》](https://deerchao.net/tutorials/regex/regex.htm)，读完这篇文章后你就可以看懂下面的表格，这是我们对正则表达式中的一些基本符号进行的扼要总结。

| 符号           | 解释                             | 示例               | 说明                                                         |
| -------------- | -------------------------------- | ------------------ | ------------------------------------------------------------ |
| `.`            | 匹配任意字符                     | `b.t`              | 可以匹配bat / but / b#t / b1t等                              |
| `\w`           | 匹配字母/数字/下划线             | `b\wt`             | 可以匹配bat / b1t / b_t等 但不能匹配b#t                      |
| `\s`           | 匹配空白字符（包括\r、\n、\t等） | `love\syou`        | 可以匹配love you                                             |
| `\d`           | 匹配数字                         | `\d\d`             | 可以匹配01 / 23 / 99等                                       |
| `\b`           | 匹配单词的边界                   | `\bThe\b`          |                                                              |
| `^`            | 匹配字符串的开始                 | `^The`             | 可以匹配The开头的字符串                                      |
| `$`            | 匹配字符串的结束                 | `.exe$`            | 可以匹配.exe结尾的字符串                                     |
| `\W`           | 匹配非字母/数字/下划线           | `b\Wt`             | 可以匹配b#t / b@t等 但不能匹配but / b1t / b_t等              |
| `\S`           | 匹配非空白字符                   | `love\Syou`        | 可以匹配love#you等 但不能匹配love you                        |
| `\D`           | 匹配非数字                       | `\d\D`             | 可以匹配9a / 3# / 0F等                                       |
| `\B`           | 匹配非单词边界                   | `\Bio\B`           |                                                              |
| `[]`           | 匹配来自字符集的任意单一字符     | `[aeiou]`          | 可以匹配任一元音字母字符                                     |
| `[^]`          | 匹配不在字符集中的任意单一字符   | `[^aeiou]`         | 可以匹配任一非元音字母字符                                   |
| `*`            | 匹配0次或多次                    | `\w*`              |                                                              |
| `+`            | 匹配1次或多次                    | `\w+`              |                                                              |
| `?`            | 匹配0次或1次                     | `\w?`              |                                                              |
| `{N}`          | 匹配N次                          | `\w{3}`            |                                                              |
| `{M,}`         | 匹配至少M次                      | `\w{3,}`           |                                                              |
| `{M,N}`        | 匹配至少M次至多N次               | `\w{3,6}`          |                                                              |
| `|`            | 分支                             | `foo|bar`          | 可以匹配foo或者bar                                           |
| `(?#)`         | 注释                             |                    |                                                              |
| `(exp)`        | 匹配exp并捕获到自动命名的组中    |                    |                                                              |
| `(?<name>exp)` | 匹配exp并捕获到名为name的组中    |                    |                                                              |
| `(?:exp)`      | 匹配exp但是不捕获匹配的文本      |                    |                                                              |
| `(?=exp)`      | 匹配exp前面的位置                | `\b\w+(?=ing)`     | 可以匹配I'm dancing中的danc                                  |
| `(?<=exp)`     | 匹配exp后面的位置                | `(?<=\bdanc)\w+\b` | 可以匹配I love dancing and reading中的第一个ing              |
| `(?!exp)`      | 匹配后面不是exp的位置            |                    |                                                              |
| `(?<!exp)`     | 匹配前面不是exp的位置            |                    |                                                              |
| `*?`           | 重复任意次，但尽可能少重复       | `a.*b` `a.*?b`     | 将正则表达式应用于aabab，前者会匹配整个字符串aabab，后者会匹配aab和ab两个字符串 |
| `+?`           | 重复1次或多次，但尽可能少重复    |                    |                                                              |
| `??`           | 重复0次或1次，但尽可能少重复     |                    |                                                              |
| `{M,N}?`       | 重复M到N次，但尽可能少重复       |                    |                                                              |
| `{M,}?`        | 重复M次以上，但尽可能少重复      |                    |                                                              |

> **说明：** 如果需要匹配的字符是正则表达式中的特殊字符，那么可以使用`\`进行转义处理，例如想匹配小数点可以写成`\.`就可以了，因为直接写`.`会匹配任意字符；同理，想匹配圆括号必须写成`\(`和`\)`，否则圆括号被视为正则表达式中的分组。

### Python对正则表达式的支持

Python 提供了`re`模块来支持正则表达式相关操作，下面是`re`模块中的核心函数。

| 函数                                           | 说明                                                         |
| ---------------------------------------------- | ------------------------------------------------------------ |
| `compile(pattern, flags=0)`                    | 编译正则表达式返回正则表达式对象                             |
| `match(pattern, string, flags=0)`              | 用正则表达式匹配字符串 成功返回匹配对象 否则返回`None`       |
| `search(pattern, string, flags=0)`             | 搜索字符串中第一次出现正则表达式的模式 成功返回匹配对象 否则返回`None` |
| `split(pattern, string, maxsplit=0, flags=0)`  | 用正则表达式指定的模式分隔符拆分字符串 返回列表              |
| `sub(pattern, repl, string, count=0, flags=0)` | 用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用`count`指定替换的次数 |
| `fullmatch(pattern, string, flags=0)`          | `match`函数的完全匹配（从字符串开头到结尾）版本              |
| `findall(pattern, string, flags=0)`            | 查找字符串所有与正则表达式匹配的模式 返回字符串的列表        |
| `finditer(pattern, string, flags=0)`           | 查找字符串所有与正则表达式匹配的模式 返回一个迭代器          |
| `purge()`                                      | 清除隐式编译的正则表达式的缓存                               |
| `re.I` / `re.IGNORECASE`                       | 忽略大小写匹配标记                                           |
| `re.M` / `re.MULTILINE`                        | 多行匹配标记                                                 |

> **说明：** 上面提到的`re`模块中的这些函数，实际开发中也可以用正则表达式对象（`Pattern`对象）的方法替代对这些函数的使用，如果一个正则表达式需要重复的使用，那么先通过`compile`函数编译正则表达式并创建出正则表达式对象无疑是更为明智的选择。

下面我们通过一系列的例子来告诉大家在Python中如何使用正则表达式。

例子1：验证输入用户名和QQ号是否有效并给出对应的提示信息。

```python
"""
要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re

username = input('请输入用户名: ')
qq = input('请输入QQ号: ')
# match函数的第一个参数是正则表达式字符串或正则表达式对象
# match函数的第二个参数是要跟正则表达式做匹配的字符串对象
m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
if not m1:
    print('请输入有效的用户名.')
# fullmatch函数要求字符串和正则表达式完全匹配
# 所以正则表达式没有写起始符和结束符
m2 = re.fullmatch(r'[1-9]\d{4,11}', qq)
if not m2:
    print('请输入有效的QQ号.')
if m1 and m2:
    print('你输入的信息是有效的!')
```

> **提示：** 上面在书写正则表达式时使用了“原始字符串”的写法（在字符串前面加上了`r`），所谓“原始字符串”就是字符串中的每个字符都是它原始的意义，说得更直接一点就是字符串中没有所谓的转义字符啦。因为正则表达式中有很多元字符和需要进行转义的地方，如果不使用原始字符串就需要将反斜杠写作`\\`，例如表示数字的`\d`得书写成`\\d`，这样不仅写起来不方便，阅读的时候也会很吃力。

例子2：从一段文字中提取出国内手机号码。

下面这张图是截止到 2017 年底，国内三家运营商推出的手机号段。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day21-30/res/20210803203134.png)

```python
import re

# 创建正则表达式对象，使用了前瞻和回顾来保证手机号前后不应该再出现数字
pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也不是110或119，王大锤的手机号才是15600998765。'''
# 方法一：查找所有匹配并保存到一个列表中
tels_list = re.findall(pattern, sentence)
for tel in tels_list:
    print(tel)
print('--------华丽的分隔线--------')

# 方法二：通过迭代器取出匹配对象并获得匹配的内容
for temp in pattern.finditer(sentence):
    print(temp.group())
print('--------华丽的分隔线--------')

# 方法三：通过search函数指定搜索位置找出所有匹配
m = pattern.search(sentence)
while m:
    print(m.group())
    m = pattern.search(sentence, m.end())
```

> **说明：** 上面匹配国内手机号的正则表达式并不够好，因为像 14 开头的号码只有 145 或 147，而上面的正则表达式并没有考虑这种情况，要匹配国内手机号，更好的正则表达式的写法是：`(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)`，国内好像已经有 19 和 16 开头的手机号了，但是这个暂时不在我们考虑之列。

例子3：替换字符串中的不良内容

```python
import re

sentence = 'Oh, shit! 你是傻逼吗? Fuck you.'
purified = re.sub('fuck|shit|[傻煞沙][比笔逼叉缺吊碉雕]',
                  '*', sentence, flags=re.IGNORECASE)
print(purified)  # Oh, *! 你是*吗? * you.
```

> **说明：**` re`模块的正则表达式相关函数中都有一个`flags`参数，它代表了正则表达式的匹配标记，可以通过该标记来指定匹配时是否忽略大小写、是否进行多行匹配、是否显示调试信息等。如果需要为`flags`参数指定多个值，可以使用[按位或运算符](http://www.runoob.com/python/python-operators.html#ysf5)进行叠加，如`flags=re.I | re.M`。

例子4：拆分长字符串

```python
import re

poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentences_list = re.split(r'[，。]', poem)
# 这是一个列表推导式，用于过滤掉上一步拆分结果中的空字符串（''）
sentences_list = [sentence for sentence in sentences_list if sentence]
for sentence in sentences_list:
    print(sentence)
```

正则表达式在字符串的处理和匹配上真的非常强大，通过上面的例子相信大家已经感受到了正则表达式的魅力，当然写一个正则表达式对新手来说并不是那么容易，但是很多事情都是熟能生巧，大胆的去尝试就行了，有一个在线的[正则表达式测试工具](https://c.runoob.com/front-end/854)相信能够在一定程度上帮到大家。

## 29.Python语言进阶

### 重要知识点

- 生成式（推导式）的用法

  ```python
  prices = {
      'AAPL': 191.88,
      'GOOG': 1186.96,
      'IBM': 149.24,
      'ORCL': 48.44,
      'ACN': 166.89,
      'FB': 208.09,
      'SYMC': 21.29
  }
  # 用股票价格大于100元的股票构造一个新的字典
  prices2 = {key: value for key, value in prices.items() if value > 100}
  print(prices2)
  ```

  > 说明：生成式（推导式）可以用来生成列表、集合和字典。

- 嵌套的列表的坑

  ```python
  names = ['关羽', '张飞', '赵云', '马超', '黄忠']
  courses = ['语文', '数学', '英语']
  # 录入五个学生三门课程的成绩
  # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
  # scores = [[None] * len(courses)] * len(names)
  # 它创建的是一个包含多个指向同一列表的引用的列表，而不是多个独立的列表。具体来说，[None] * len(courses) 会创建一个初始列表（比如 [None, None, None]），但当你用 * len(names) 复制这个列表时，并没有创建新的独立列表，而是复制了对同一个列表的引用。这意味着：当你修改 scores 中的任何一个子列表时，所有子列表都会跟着变化（因为它们本质上是同一个列表）。
  scores = [[None] * len(courses) for _ in range(len(names))]
  for row, name in enumerate(names):
      for col, course in enumerate(courses):
          scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
          print(scores)
  ```

  > 以上内容参考笔记algorithm4.5的Q&A的最后三个问题

  [Python Tutor](http://pythontutor.com/) - VISUALIZE CODE AND GET LIVE HELP

- `heapq`模块（堆排序）是 Python 标准库中用于实现**堆（heap）数据结构**的模块，主要提供了基于最小堆（min-heap）的一系列操作函数，可高效实现优先级队列、Top N 元素查找等功能。

  ```python
  """
  从列表中找出最大的或最小的N个元素
  堆结构(大根堆/小根堆)
  """
  import heapq
  
  list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
  list2 = [
      {'name': 'IBM', 'shares': 100, 'price': 91.1},
      {'name': 'AAPL', 'shares': 50, 'price': 543.22},
      {'name': 'FB', 'shares': 200, 'price': 21.09},
      {'name': 'HPQ', 'shares': 35, 'price': 31.75},
      {'name': 'YHOO', 'shares': 45, 'price': 16.35},
      {'name': 'ACME', 'shares': 75, 'price': 115.65}
  ]
  print(heapq.nlargest(3, list1))
  print(heapq.nsmallest(3, list1))
  print(heapq.nlargest(2, list2, key=lambda x: x['price']))
  print(heapq.nlargest(2, list2, key=lambda x: x['shares']))
  
  # 1. 创建堆（将列表转换为最小堆）
  nums = [3, 1, 4, 1, 5, 9, 2, 6]
  heapq.heapify(nums)  # 原地转换，不返回新列表
  print("最小堆:", nums)  # 输出：[1, 1, 2, 3, 5, 9, 4, 6]（堆结构的列表表示）
  
  # 2. 弹出堆顶元素（最小元素）
  smallest = heapq.heappop(nums)
  print("弹出的最小元素:", smallest)  # 输出：1
  print("弹出后堆:", nums)  # 输出：[1, 3, 2, 6, 5, 9, 4]
  
  # 3. 插入元素
  heapq.heappush(nums, 0)
  print("插入0后堆:", nums)  # 输出：[0, 1, 2, 6, 5, 9, 4, 3]
  
  # 4. 获取最大的n个元素
  largest3 = heapq.nlargest(3, nums)
  print("最大的3个元素:", largest3)  # 输出：[9, 6, 5]
  
  # 5. 获取最小的n个元素
  smallest2 = heapq.nsmallest(2, nums)
  print("最小的2个元素:", smallest2)  # 输出：[0, 1]
  
  # 6. 实现最大堆（通过插入负值模拟）
  max_heap = []
  for num in [3, 1, 4]:
      heapq.heappush(max_heap, -num)  # 插入负值
  print("最大堆的堆顶（原最大值）:", -max_heap[0])  # 输出：4
  ```

  **典型应用**

  1. 优先级队列：堆可高效实现优先级队列，每次弹出优先级最高（或最低）的元素。例如任务调度中，优先处理紧急任务：

     ```python
     # 优先级队列示例（元组中第一个元素为优先级，值越小优先级越高）
     tasks = []
     heapq.heappush(tasks, (2, '任务B'))  # 优先级2
     heapq.heappush(tasks, (1, '任务A'))  # 优先级1（更高）
     heapq.heappush(tasks, (3, '任务C'))  # 优先级3
     
     while tasks:
         priority, task = heapq.heappop(tasks)
         print(f"处理任务: {task}（优先级 {priority}）")
     # 输出：
     # 处理任务: 任务A（优先级 1）
     # 处理任务: 任务B（优先级 2）
     # 处理任务: 任务C（优先级 3）
     ```

  2. top n问题

  3. 堆排序：利用堆的特性实现排序（时间复杂度 O (n log n)），但实际中 Python 的 `sorted()` 更优，堆排序多用于特定场景（如部分排序）。

  > 注意
  >
  > - `heapq` 仅实现**最小堆**，若需最大堆，可通过插入元素的负值（如 `-num`）间接实现。
  > - 堆的底层是列表，但列表的索引顺序不直接对应排序后的顺序，仅保证堆顶是最小元素
  > - 对于已排序的列表，`heapify` 转换后的堆结构可能与原列表顺序不同（堆是完全二叉树的层序遍历结果）。

- `itertools`模块是 Python 标准库中用于创建和操作**迭代器**的模块，提供了一系列高效的工具函数，可用于生成复杂的迭代器、组合数据、处理序列等。这些工具的特点是**惰性计算**（仅在需要时生成元素），节省内存且适合处理大数据流。

  ```python
  """
  迭代工具模块
  """
  import itertools
  
  # 产生ABCD的全排列
  itertools.permutations('ABCD')
  # 产生ABCDE的五选三组合
  itertools.combinations('ABCDE', 3)
  # 产生ABCD和123的笛卡尔积
  itertools.product('ABCD', '123')
  # 产生ABC的无限循环序列
  itertools.cycle(('A', 'B', 'C'))
  ```

  1. **无限迭代器（Infinite Iterators）**

  生成无限序列，需配合 `break` 或切片使用，避免无限循环。

  | 函数                 | 功能描述                                   | 示例                             |
  | -------------------- | ------------------------------------------ | -------------------------------- |
  | `count(start, step)` | 从 `start` 开始，以 `step` 为步长无限计数  | `count(10, 2)` → 10, 12, 14, ... |
  | `cycle(iterable)`    | 无限循环迭代 `iterable` 中的元素           | `cycle([1,2])` → 1, 2, 1, 2, ... |
  | `repeat(value, n)`   | 重复 `value` 最多 `n` 次（`n` 省略则无限） | `repeat('a', 3)` → 'a', 'a', 'a' |

  2. **迭代器组合（Combinatoric Iterators）**

  用于生成数据的排列、组合、笛卡尔积等。

  | 函数                                         | 功能描述                              | 示例                                                         |
  | -------------------------------------------- | ------------------------------------- | ------------------------------------------------------------ |
  | `product(*iterables)`                        | 计算多个可迭代对象的笛卡尔积          | `product([1,2], ['a'])` → (1,'a'), (2,'a')                   |
  | `permutations(iterable, r)`                  | 生成长度为 `r` 的排列（有序）         | `permutations([1,2,3], 2)` → (1,2), (1,3), (2,1), ...        |
  | `combinations(iterable, r)`                  | 生成长度为 `r` 的组合（无序，不重复） | `combinations([1,2,3], 2)` → (1,2), (1,3), (2,3)             |
  | `combinations_with_replacement(iterable, r)` | 生成允许重复元素的组合                | `combinations_with_replacement([1,2], 2)` → (1,1), (1,2), (2,2) |

  3. **序列处理（Iterators for Sequence Handling）**

  用于过滤、分组、合并迭代器。

  | 函数                                  | 功能描述                                                  | 示例                                                         |
  | ------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
  | `chain(*iterables)`                   | 将多个迭代器 “链” 成一个连续迭代器                        | `chain([1,2], [3,4])` → 1,2,3,4                              |
  | `filterfalse(predicate, iterable)`    | 保留 `predicate` 为 `False` 的元素                        | `filterfalse(lambda x: x%2==0, [1,2,3])` → 1,3               |
  | `groupby(iterable, key)`              | 按 `key` 分组，返回 `(key, group)` 对                     | 对 `[('a',1), ('a',2), ('b',3)]` 按第一个元素分组 → ('a', 迭代器), ('b', 迭代器) |
  | `islice(iterable, start, stop, step)` | 对迭代器进行切片（类似列表切片）                          | `islice(count(), 2, 5)` → 2,3,4                              |
  | `zip_longest(*iterables, fillvalue)`  | 类似 `zip`，但以最长的迭代器为准，缺省用 `fillvalue` 填充 | `zip_longest([1,2], [3], fillvalue=0)` → (1,3), (2,0)        |

  **典型应用**

  - 生成测试用例的所有组合（笛卡尔积）；
  - 处理大数据流的分组、过滤（如日志分析）；
  - 实现排列组合问题（如密码破解、数据分析）；
  - 合并或拆分迭代器（如多文件内容合并）。

- `collections`模块

  常用的工具类：

  - `namedtuple`：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。它结合了元组的不可变性和字典的字段访问特性，既保留了元组的轻量性，又能通过名称访问元素，提高代码的可读性和可维护性。

    ```python
    from collections import namedtuple
    
    # 1. 定义 namedtuple 类（第一个参数是类名，第二个参数是字段名列表）
    Person = namedtuple('Person', ['name', 'age', 'gender'])
    
    # 2. 创建实例（参数顺序需与字段名一致）
    p1 = Person('Alice', 30, 'female')
    p2 = Person(name='Bob', age=25, gender='male')  # 也支持关键字参数
    
    # 3. 访问字段（两种方式）
    print(p1.name)   # 通过字段名访问（推荐）
    print(p1[1])     # 通过索引访问（兼容元组）
    
    # 4. 不可变性（尝试修改会报错）
    # p1.age = 31  # 报错：AttributeError: can't set attribute
    
    # 5. 转换为字典
    print(p1._asdict())  # 输出：{'name': 'Alice', 'age': 30, 'gender': 'female'}
    
    # 6. 替换字段值（返回新实例，原实例不变）
    p3 = p1._replace(age=31)
    print(p3)  # 输出：Person(name='Alice', age=31, gender='female')
    ```

  - `deque`：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表，是处理 “两端操作” 的最优选择，尤其在数据量大或需要频繁头部操作时，性能远优于列表。但如果需要频繁随机访问元素（如通过索引读写），则列表更合适。

    ```python
    from collections import deque
    
    # 1. 创建deque（可初始化，也可指定maxlen）
    dq = deque([1, 2, 3])  # 从列表初始化
    dq_max = deque(maxlen=3)  # 限制最大长度为3
    
    # 2. 尾部操作（类似列表）
    dq.append(4)  # 右侧添加：deque([1, 2, 3, 4])
    dq.pop()      # 右侧删除：返回4，结果 deque([1, 2, 3])
    
    # 3. 头部操作（deque的优势）
    dq.appendleft(0)  # 左侧添加：deque([0, 1, 2, 3])
    dq.popleft()      # 左侧删除：返回0，结果 deque([1, 2, 3])
    
    # 4. 限制长度的特性（超过maxlen时自动移除旧元素）
    for i in range(5):
        dq_max.append(i)
    print(dq_max)  # 输出：deque([2, 3, 4], maxlen=3)（前两个元素被自动移除）
    
    # 5. 其他常用方法
    dq.extend([4, 5])      # 尾部扩展：deque([1, 2, 3, 4, 5])
    dq.extendleft([0, -1]) # 左侧扩展（注意顺序会反转）：deque([-1, 0, 1, 2, 3, 4, 5])
    dq.reverse()           # 反转：deque([5, 4, 3, 2, 1, 0, -1])
    dq.rotate(2)           # 向右旋转2步：deque([0, -1, 5, 4, 3, 2, 1])
    ```

  - `Counter`：`dict`的子类，键是元素，值是元素的计数，专门用于**计数可哈希对象**，是处理频率统计问题的高效工具。它的`most_common()`方法可以帮助我们获取出现频率最高的元素。`Counter`和`dict`的继承关系我认为是值得商榷的，按照CARP原则，`Counter`跟`dict`的关系应该设计为关联关系更为合理。

    ```python
    from collections import Counter
    
    # 1. 基本计数（统计列表元素出现次数）
    fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    fruit_counts = Counter(fruits)
    print(fruit_counts)
    # 输出：Counter({'apple': 3, 'banana': 2, 'orange': 1})
    
    # 2. 统计字符串中字符出现次数
    word = 'hello world'
    char_counts = Counter(word)
    print(char_counts)
    # 输出：Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    
    # 3. 访问元素计数（类似字典）
    print(fruit_counts['apple'])  # 输出：3
    print(fruit_counts.get('grape', 0))  # 输出：0（不存在的元素默认返回0）
    
    # 4. 获取最常见的元素（前n名）
    top2 = fruit_counts.most_common(2)
    print(top2)  # 输出：[('apple', 3), ('banana', 2)]
    
    # 5. 元素计数的更新（增加或减少）
    fruit_counts.update(['apple', 'grape'])  # 增加计数
    print(fruit_counts)  # 输出：Counter({'apple': 4, 'banana': 2, 'orange': 1, 'grape': 1})
    
    fruit_counts.subtract(['banana', 'apple'])  # 减少计数
    print(fruit_counts)  # 输出：Counter({'apple': 3, 'banana': 1, 'orange': 1, 'grape': 1})
    
    # 6. 转换为普通字典或列表
    print(dict(fruit_counts))  # 输出：{'apple': 3, 'banana': 1, 'orange': 1, 'grape': 1}
    print(list(fruit_counts.elements()))  # 输出：['apple', 'apple', 'apple', 'banana', 'orange', 'grape']
    
    ```

  - `OrderedDict`：`dict`的子类，它记录了键值对插入的顺序（在 Python 3.7 之前，普通字典不保证插入顺序），看起来既有字典的行为，也有链表的行为。

    ```python
  from collections import OrderedDict
    # 1. 创建OrderedDict并插入元素（保留插入顺序）
    
      od = OrderedDict()
      od['a'] = 1
      od['b'] = 2
      od['c'] = 3
    
      # 迭代时按插入顺序返回
    
      for key, value in od.items():
          print(key, value)
    
      # 输出：
    
      # a 1
    
      # b 2
    
      # c 3
    
      # 2. 特有方法：移动元素到末尾（move_to_end）
    
      od.move_to_end('a')  # 将键'a'移到最后
    print(list(od.keys()))  # 输出：['b', 'c', 'a']
    
      # 3. 特有方法：移动元素到开头（last=False）
    
      od.move_to_end('c', last=False)  # 将键'c'移到最前
      print(list(od.keys()))  # 输出：['c', 'b', 'a']
    
      # 4. 特有方法：弹出第一个元素（popitem）
    
      first_item = od.popitem(last=False)  # last=False表示弹出第一个元素
      print("弹出的第一个元素:", first_item)  # 输出：('c', 3)
      print("剩余元素:", list(od.items()))  # 输出：[('b', 2), ('a', 1)]
    
      # 5. 顺序敏感的相等性判断
    
      od1 = OrderedDict(a=1, b=2)
      od2 = OrderedDict(b=2, a=1)
      print(od1 == od2)  # 输出：False（普通字典会返回True）
    ```
    
  -  `defaultdict`：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的`setdefault()`方法，这种做法更加高效。处理 “需要自动初始化键值” 场景的高效工具，尤其适合分组、计数、去重收集等场景。它通过消除冗余的判断逻辑，让代码更简洁、可读性更高，是 Python 中简化字典操作的重要工具。
  
    ```python
    from collections import defaultdict
      
      # 1. 以list为默认工厂（自动初始化列表）
      # 场景：将列表元素按首字母分组
      words = ['apple', 'banana', 'ant', 'cat', 'book']
      grouped_by_first = defaultdict(list)  # 键不存在时默认值为[]
      
      for word in words:
          first_char = word[0]
          grouped_by_first[first_char].append(word)  # 无需判断键是否存在
      
      print("按首字母分组:", dict(grouped_by_first))
      # 输出：{'a': ['apple', 'ant'], 'b': ['banana', 'book'], 'c': ['cat']}
      
      # 2. 以int为默认工厂（自动初始化0，适合计数）
      # 场景：统计元素出现次数
      nums = [1, 2, 3, 2, 1, 3, 3, 4]
      counts = defaultdict(int)  # 键不存在时默认值为0
      
      for num in nums:
          counts[num] += 1  # 直接累加，无需初始化
      
      print("元素计数:", dict(counts))
      # 输出：{1: 2, 2: 2, 3: 3, 4: 1}
      
      # 3. 以set为默认工厂（自动初始化空集合，适合去重）
      # 场景：收集不重复的关联元素
      pairs = [('a', 1), ('b', 2), ('a', 3), ('b', 2)]
      unique_pairs = defaultdict(set)  # 键不存在时默认值为set()
      
      for key, value in pairs:
          unique_pairs[key].add(value)  # 自动去重
      
      print("去重后的关联元素:", dict(unique_pairs))
      # 输出：{'a': {1, 3}, 'b': {2}}
    ```

### 数据结构和算法

- 算法：解决问题的方法和步骤
- 评价算法的好坏：渐近时间复杂度和渐近空间复杂度。
- 渐近时间复杂度的大O标记：
  - $O(c)$ - 常量时间复杂度 - 布隆过滤器 / 哈希存储
  - $O(log_2 n)$对数时间复杂度 - 折半查找（二分查找）
  - $O(n)$ - 线性时间复杂度 - 顺序查找 / 计数排序
  - $O(n*log_2 n)$ - 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
  - $O(n^2)$ - 平方时间复杂度 - 简单排序算法（选择排序、插入排序、冒泡排序）
  - $O(n^3)$ - 立方时间复杂度 - Floyd算法 / 矩阵乘法运算
  - $O(2^n)$ - 几何级数时间复杂度 - 汉诺塔
  - $O(n!)$ - 阶乘时间复杂度 - 旅行经销商问题 - NPC

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day31-35/res/algorithm_complexity_1.png)

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day31-35/res/algorithm_complexity_2.png)

- 排序算法（选择、冒泡和归并）和查找算法（顺序和折半）

  ```python
  def select_sort(items, comp=lambda x, y: x < y):
      """简单选择排序"""
      # 创建列表 items 的一个浅拷贝（shallow copy），并将新列表重新赋值给变量 items
      items = items[:]
      for i in range(len(items) - 1):
          min_index = i
          for j in range(i + 1, len(items)):
              if comp(items[j], items[min_index]):
                  min_index = j
          items[i], items[min_index] = items[min_index], items[i]
      return items
  ```

  ```python
  def bubble_sort(items, comp=lambda x, y: x > y):
      """冒泡排序"""
      items = items[:]
      for i in range(len(items) - 1):
          swapped = False
          for j in range(len(items) - 1 - i):
              if comp(items[j], items[j + 1]):
                  items[j], items[j + 1] = items[j + 1], items[j]
                  swapped = True
          if not swapped:
              break
      return items
  ```

  ```python
  def bubble_sort(items, comp=lambda x, y: x > y):
      """搅拌排序(冒泡排序升级版)"""
      items = items[:]
      for i in range(len(items) - 1):
          swapped = False
          for j in range(len(items) - 1 - i):
              if comp(items[j], items[j + 1]):
                  items[j], items[j + 1] = items[j + 1], items[j]
                  swapped = True
          if swapped:
              swapped = False
              for j in range(len(items) - 2 - i, i, -1):
                  if comp(items[j - 1], items[j]):
                      items[j], items[j - 1] = items[j - 1], items[j]
                      swapped = True
          if not swapped:
              break
      return items
  ```
  
  ```python
  def merge(items1, items2, comp=lambda x, y: x < y):
      """合并(将两个有序的列表合并成一个有序的列表)"""
      items = []
      index1, index2 = 0, 0
      while index1 < len(items1) and index2 < len(items2):
          if comp(items1[index1], items2[index2]):
              items.append(items1[index1])
              index1 += 1
          else:
              items.append(items2[index2])
              index2 += 1
      items += items1[index1:]
      items += items2[index2:]
      return items
  
  # 这种写法是合理且必要的，它通过职责分离提升了代码的可读性、易用性和安全性，符合高质量代码的设计原则
  def merge_sort(items, comp=lambda x, y: x < y):
      return _merge_sort(list(items), comp)
  
  
  def _merge_sort(items, comp):
      """归并排序"""
      if len(items) < 2:
          return items
      mid = len(items) // 2
      left = _merge_sort(items[:mid], comp)
      right = _merge_sort(items[mid:], comp)
      return merge(left, right, comp)
  ```
  
  ```python
  def seq_search(items, key):
      """顺序查找"""
      for index, item in enumerate(items):
          if item == key:
              return index
      return -1
  ```
  
  ```python
  def bin_search(items, key):
      """折半查找"""
      start, end = 0, len(items) - 1
      while start <= end:
          mid = (start + end) // 2
          if key > items[mid]:
              start = mid + 1
          elif key < items[mid]:
              end = mid - 1
          else:
              return mid
      return -1
  ```
  
- 常用算法

  - 穷举法 - 又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案。
  - 贪婪法 - 在对问题求解时，总是做出在当前看来最好的选择，不追求最优解，快速找到满意解。
  - 分治法 - 把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解。
  - 回溯法 - 回溯法又称为试探法，按选优条件向前搜索，当搜索到某一步发现原先选择并不优或达不到目标时，就退回一步重新选择。
  - 动态规划 - 基本思想也是将待求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算。

  穷举法例子：百钱百鸡和五人分鱼。

  ```python
  # 公鸡5元一只 母鸡3元一只 小鸡1元三只
  # 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
  for x in range(20):
      for y in range(33):
          z = 100 - x - y
          if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
              print(x, y, z)
  
  # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
  # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
  # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
  # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
  fish = 6
  while True:
      total = fish
      enough = True
      for _ in range(5):
          if (total - 1) % 5 == 0:
              total = (total - 1) // 5 * 4
          else:
              enough = False
              break
      if enough:
          print(fish)
          break
      fish += 5
  ```

  贪婪法例子：假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。
  
  | 名称   | 价格（美元） | 重量（kg） |
  | ------ | ------------ | ---------- |
  | 电脑   | 200          | 20         |
  | 收音机 | 20           | 4          |
  | 钟     | 175          | 10         |
  | 花瓶   | 50           | 2          |
  | 书     | 10           | 1          |
  | 油画   | 90           | 9          |
  
  ```python
  """
  贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
  输入：
  20 6
  电脑 200 20
  收音机 20 4
  钟 175 10
  花瓶 50 2
  书 10 1
  油画 90 9
  """
  class Thing(object):
      """物品"""
  
      def __init__(self, name, price, weight):
          self.name = name
          self.price = price
          self.weight = weight
  
      @property
      def value(self):
          """价格重量比"""
          return self.price / self.weight
  
  
  def input_thing():
      """输入物品信息"""
      name_str, price_str, weight_str = input().split()
      return name_str, int(price_str), int(weight_str)
  
  
  def main():
      """主函数"""
      # map() 是 Python 内置函数，用于将一个函数应用到可迭代对象（如列表、元组、字符串等）的每个元素上，并返回一个包含结果的迭代器（map 对象）。
      max_weight, num_of_things = map(int, input().split())
      all_things = []
      for _ in range(num_of_things):
          # * 运算符：这里是解包操作，将 input_thing() 返回的元组拆分成三个独立的参数。
          # 不能直接写 all_things.append(Thing(input_thing()))，是因为 input_thing() 返回的是一个元组（(name, price, weight)），而 Thing 类的构造函数需要三个独立的参数，直接传递元组会导致参数不匹配。
          # 也可以手动拆分
          # name, price, weight = input_thing()
          # all_things.append(Thing(name, price, weight))
          all_things.append(Thing(*input_thing()))
      all_things.sort(key=lambda x: x.value, reverse=True)
      total_weight = 0
      total_price = 0
      for thing in all_things:
          if total_weight + thing.weight <= max_weight:
              print(f'小偷拿走了{thing.name}')
              total_weight += thing.weight
              total_price += thing.price
      print(f'总价值: {total_price}美元')
  
  
  if __name__ == '__main__':
      main()
  ```
  
  分治法例子：[快速排序](https://zh.wikipedia.org/zh/快速排序)。
  
  ```python
  """
  快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
  """
  def quick_sort(items, comp=lambda x, y: x <= y):
  	# 这种写法其实是冗余的，因为 list(items) 和 [:] 都能独立完成浅拷贝：
      # items = list(items)
      # items = items[:]
      items = list(items)[:]
      _quick_sort(items, 0, len(items) - 1, comp)
      return items
  
  
  def _quick_sort(items, start, end, comp):
      if start < end:
          pos = _partition(items, start, end, comp)
          _quick_sort(items, start, pos - 1, comp)
          _quick_sort(items, pos + 1, end, comp)
  
  
  def _partition(items, start, end, comp):
      pivot = items[end]
      i = start - 1
      for j in range(start, end):
          if comp(items[j], pivot):
              i += 1
              items[i], items[j] = items[j], items[i]
      items[i + 1], items[end] = items[end], items[i + 1]
      return i + 1
  ```
  
  回溯法例子：[骑士巡逻](https://zh.wikipedia.org/zh/骑士巡逻)。
  
  ```python
  """
  递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
  """
  import sys
  import time
  
  SIZE = 5
  total = 0
  
  
  def print_board(board):
      for row in board:
          for col in row:
              print(str(col).center(4), end='')
          print()
  
  
  def patrol(board, row, col, step=1):
      if row >= 0 and row < SIZE and \
          col >= 0 and col < SIZE and \
          board[row][col] == 0:
          board[row][col] = step
          if step == SIZE * SIZE:
              global total
              total += 1
              print(f'第{total}种走法: ')
              print_board(board)
          patrol(board, row - 2, col - 1, step + 1)
          patrol(board, row - 1, col - 2, step + 1)
          patrol(board, row + 1, col - 2, step + 1)
          patrol(board, row + 2, col - 1, step + 1)
          patrol(board, row + 2, col + 1, step + 1)
          patrol(board, row + 1, col + 2, step + 1)
          patrol(board, row - 1, col + 2, step + 1)
          patrol(board, row - 2, col + 1, step + 1)
          board[row][col] = 0
  
  
  def main():
      board = [[0] * SIZE for _ in range(SIZE)]
      patrol(board, SIZE - 1, SIZE - 1)
  
  
  if __name__ == '__main__':
      main()
  ```
  
  动态规划例子：子列表元素之和的最大值。
  
  > 说明：子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值，例如：
  >
  > 输入：1 -2 3 5 -3 2
  >
  > 输出：8
  >
  > 输入：0 -2 3 5 -1 2
  >
  > 输出：9
  >
  > 输入：-9 -2 -3 -5 -3
  >
  > 输出：-2
  
  ```python
  '''
  动态规划的核心是通过定义状态和推导状态转移方程，将问题分解为重叠子问题并高效求解。以下是具体思路：
  1. 定义状态（关键）
  设 dp[i] 表示 “以列表中第 i 个元素结尾的最大子数组和”。
  
  这里的 “以第 i 个元素结尾” 是关键限制，确保子数组的连续性（因为子数组必须连续，所以第 i 个元素必须包含在子数组中）。
  例如：对于列表 [-2, 1, -3, 4]，dp[3]（假设索引从 0 开始）表示以 4 结尾的最大子数组和，即 4（子数组 [4]）。
  2. 推导状态转移方程
  对于第 i 个元素，有两种选择：
  
  选择 1：将第 i 个元素加入 “以上一个元素（i-1）结尾的最大子数组”，形成新的子数组（[... , i-1, i]）。此时和为 dp[i-1] + nums[i]。
  选择 2：从第 i 个元素开始，单独作为一个子数组（[i]）。此时和为 nums[i]。
  dp[i] 取两种选择中的最大值，即：dp[i] = max(nums[i], dp[i-1] + nums[i])
  '''
  def main():
      items = list(map(int, input().split()))
      overall = partial = items[0]
      for i in range(1, len(items)):
          partial = max(items[i], partial + items[i])
          overall = max(partial, overall)
      print(overall)
  
  
  if __name__ == '__main__':
      main()
  ```
  
  > **说明**：这个题目最容易想到的解法是使用二重循环，但是代码的时间性能将会变得非常的糟糕。使用动态规划的思想，仅仅是多用了两个变量，就将原来$O(N^2)$复杂度的问题变成了$O(N)$。

### 函数的使用方式

- 将函数视为“一等公民”
  - 函数可以赋值给变量
  - 函数可以作为函数的参数
  - 函数可以作为函数的返回值

- 高阶函数的用法（`filter`、`map`以及它们的替代品）

  ```python
  items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
  items2 = [x ** 2 for x in range(1, 10) if x % 2]
  ```

- 位置参数、可变参数、关键字参数、命名关键字参数

- 参数的元信息（代码可读性问题）

- 匿名函数和内联函数的用法（`lambda`函数）

- 闭包和作用域问题

  - Python搜索变量的LEGB顺序（Local >>> Embedded >>> Global >>> Built-in）

  - `global`和`nonlocal`关键字的作用

  - `global`：声明或定义全局变量（要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域）。

    `nonlocal`：声明使用嵌套作用域的变量（嵌套作用域必须存在该变量，否则报错）。

- 装饰器函数（使用装饰器和取消装饰器）

  例子：输出函数执行时间的装饰器。

  ```python
  def record_time(func):
      """自定义装饰函数的装饰器"""
      
      @wraps(func)
      def wrapper(*args, **kwargs):
          start = time()
          result = func(*args, **kwargs)
          print(f'{func.__name__}: {time() - start}秒')
          return result
          
      return wrapper
  ```

  如果装饰器不希望跟`print`函数耦合，可以编写可以参数化的装饰器。

  ```python
  from functools import wraps
  from time import time
  
  
  def record(output):
      """可以参数化的装饰器"""
  	
  	def decorate(func):
  		
  		@wraps(func)
  		def wrapper(*args, **kwargs):
  			start = time()
  			result = func(*args, **kwargs)
  			output(func.__name__, time() - start)
  			return result
              
  		return wrapper
  	
  	return decorate
  ```

  ```python
  from functools import wraps
  from time import time
  
  
  class Record():
      """通过定义类的方式定义装饰器"""
  
      def __init__(self, output):
          self.output = output
  
      def __call__(self, func):
  
          @wraps(func)
          def wrapper(*args, **kwargs):
              start = time()
              result = func(*args, **kwargs)
              self.output(func.__name__, time() - start)
              return result
  
          return wrapper
  ```

  > **说明**：由于对带装饰功能的函数添加了@wraps装饰器，可以通过`func.__wrapped__`方式获得被装饰之前的函数或类来取消装饰器的作用。

  例子：用装饰器来实现单例模式(用于保证被装饰的类在程序运行过程中**只会创建一个实例对象**，无论尝试实例化多少次，都返回同一个对象)。

  ```python
  from functools import wraps
  
  
  def singleton(cls):
      """装饰类的装饰器"""
      # 定义一个字典，用于缓存已经创建的类实例。键是类本身（cls），值是该类的唯一实例。
      instances = {}
  
      # 由于这个字典定义在装饰器函数内部，形成了一个 “闭包”，其生命周期会伴随整个程序，确保实例不会被销毁。
      @wraps(cls)
      def wrapper(*args, **kwargs):
          if cls not in instances:
              instances[cls] = cls(*args, **kwargs)
          return instances[cls]
  
      return wrapper
  
  
  @singleton
  class President:
      """总统(单例类)"""
      pass
  ```

  > **提示**：上面的代码中用到了闭包（closure），不知道你是否已经意识到了。还有一个小问题就是，上面的代码并没有实现线程安全的单例，如果要实现线程安全的单例应该怎么做呢？
  >
  > 闭包（Closure）是 Python 中一种特殊的函数现象，指的是**一个嵌套函数能够记住并访问其外部（非全局）作用域中的变量，即使外部函数已经执行完毕**。简单来说，闭包就是 “**携带状态的函数**”，它将函数与其依赖的外部变量 “捆绑” 在一起。
  >
  > 闭包的构成条件
  >
  > 要形成闭包，需要满足三个条件：
  >
  > 1. **存在嵌套函数**：一个函数（内层函数）定义在另一个函数（外层函数）的内部。
  > 2. **内层函数引用了外层函数的变量**：内层函数使用了外层函数中定义的非全局变量。
  > 3. **外层函数返回内层函数**：外层函数执行后，将内层函数作为返回值返回。
  >
  > ```python
  > def outer_func(message):
  >     # 外层函数的变量（非全局）
  >     msg = message
  >     
  >     # 内层函数（嵌套函数）
  >     def inner_func():
  >         # 引用外层函数的变量msg
  >         print(msg)
  >     
  >     # 返回内层函数
  >     return inner_func
  > 
  > # 调用外层函数，得到内层函数的引用
  > closure = outer_func("Hello, Closure!")
  > 
  > # 执行内层函数（此时外层函数已执行完毕）
  > closure()  # 输出：Hello, Closure!
  > ```
  >
  > 关键观察：
  >
  > - 外层函数 `outer_func` 执行完毕后，理论上其内部变量 `msg` 应该被销毁。
  > - 但实际调用 `closure()` 时，`inner_func` 仍然能访问 `msg` 的值 —— 这就是闭包的作用：**内层函数 “记住” 了外层函数的变量**。

  线程安全的单例装饰器。

  ```python
  from functools import wraps
  from threading import RLock
  
  
  def singleton(cls):
      """线程安全的单例装饰器"""
      instances = {}
      locker = RLock()
  
      @wraps(cls)
      def wrapper(*args, **kwargs):
          if cls not in instances:
              # with 语句会自动获取锁（locker.acquire()）并在代码块执行完毕后释放锁（locker.release()），无需手动管理，避免遗漏释放导致的死锁。
              # 当多个线程同时执行到 with locker 时，只有一个线程能获取锁进入临界区，其他线程会阻塞等待，直到锁被释放。
              with locker:
                  if cls not in instances:
                      instances[cls] = cls(*args, **kwargs)
          return instances[cls]
  
    return wrapper
  ```
  
  > **提示**：上面的代码用到了`with`上下文语法来进行锁操作，因为锁对象本身就是上下文管理器对象（支持`__enter__`和`__exit__`魔术方法）。在`wrapper`函数中，我们先做了一次不带锁的检查，然后再做带锁的检查，这样做比直接加锁检查性能要更好，如果对象已经创建就没有必须再去加锁而是直接返回该对象就可以了。

### 面向对象相关知识

- 三大支柱：封装、继承、多态

  例子：工资结算系统。

  ```python
  """
  月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
  """
  from abc import ABCMeta, abstractmethod
  
  
  class Employee(metaclass=ABCMeta):
      """员工(抽象类)"""
  
      def __init__(self, name):
          self.name = name
  	# 被标记的方法必须在子类中被重写（实现具体逻辑），否则子类无法实例化（会报错）。
      @abstractmethod
      def get_salary(self):
          """结算月薪(抽象方法)"""
          pass
  
  
  class Manager(Employee):
      """部门经理"""
  
      def get_salary(self):
          return 15000.0
  
  
  class Programmer(Employee):
      """程序员"""
  
      def __init__(self, name, working_hour=0):
          self.working_hour = working_hour
          super().__init__(name)
  
      def get_salary(self):
          return 200.0 * self.working_hour
  
  
  class Salesman(Employee):
      """销售员"""
  
      def __init__(self, name, sales=0.0):
          self.sales = sales
          super().__init__(name)
  
      def get_salary(self):
          return 1800.0 + self.sales * 0.05
  
  
  class EmployeeFactory:
      """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""
  
      @staticmethod
      def create(emp_type, *args, **kwargs):
          """创建员工"""
          all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
          # 将输入的 emp_type 转换为大写
          cls = all_emp_types[emp_type.upper()]
          # 用获取到的类（cls）创建实例，传入 *args, **kwargs 作为构造参数（如 Manager(name, salary)）。
          return cls(*args, **kwargs) if cls else None
  
  
  def main():
      """主函数"""
      emps = [
          EmployeeFactory.create('M', '曹操'), 
          EmployeeFactory.create('P', '荀彧', 120),
          EmployeeFactory.create('P', '郭嘉', 85), 
          EmployeeFactory.create('S', '典韦', 123000),
      ]
      for emp in emps:
          print(f'{emp.name}: {emp.get_salary():.2f}元')
  
  
  if __name__ == '__main__':
      main()
  ```

- 类与类之间的关系

  - is-a关系：继承
  - has-a关系：关联 / 聚合 / 合成
  - use-a关系：依赖

  例子：扑克游戏。

  ```python
  """
  经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
  """
  from enum import Enum, unique
  
  import random
  
  # enum 模块提供的装饰器，用于确保枚举类中所有成员的值都是唯一的。如果出现值重复的成员，会抛出 ValueError 异常，避免定义时的逻辑错误。
  @unique
  class Suite(Enum):
      """花色"""
  
      SPADE, HEART, CLUB, DIAMOND = range(4)
  
      def __lt__(self, other):
          return self.value < other.value
  
  
  class Card:
      """牌"""
  
      def __init__(self, suite, face):
          """初始化方法"""
          self.suite = suite
          self.face = face
  
      def show(self):
          """显示牌面"""
          suites = ['♠︎', '♥︎', '♣︎', '♦︎']
          faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
          return f'{suites[self.suite.value]}{faces[self.face]}'
  
      def __repr__(self):
          return self.show()
  
  
  class Poker:
      """扑克"""
  
      def __init__(self):
          self.index = 0
          self.cards = [Card(suite, face)
                        for suite in Suite
                        for face in range(1, 14)]
  
      def shuffle(self):
          """洗牌（随机乱序）"""
          random.shuffle(self.cards)
          self.index = 0
  
      def deal(self):
          """发牌"""
          card = self.cards[self.index]
          self.index += 1
          return card
  
      @property
      def has_more(self):
          return self.index < len(self.cards)
  
  
  class Player:
      """玩家"""
  
      def __init__(self, name):
          self.name = name
          self.cards = []
  
      def get_one(self, card):
          """摸一张牌"""
          self.cards.append(card)
  
      def sort(self, comp=lambda card: (card.suite, card.face)):
          """整理手上的牌"""
          self.cards.sort(key=comp)
  
  
  def main():
      """主函数"""
      poker = Poker()
      poker.shuffle()
      players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
      while poker.has_more:
          for player in players:
                  player.get_one(poker.deal())
      for player in players:
          player.sort()
          print(player.name, end=': ')
          print(player.cards)
  
  
  if __name__ == '__main__':
      main()
  ```

  > **说明**：上面的代码中使用了Emoji字符来表示扑克牌的四种花色，在某些不支持Emoji字符的系统上可能无法显示。

- 对象的复制（深复制/深拷贝/深度克隆和浅复制/浅拷贝/影子克隆）

- 垃圾回收、循环引用和弱引用

  Python使用了自动化内存管理，这种管理机制以**引用计数**为基础，同时也引入了**标记-清除**和**分代收集**两种机制为辅的策略。

  ```c
  typedef struct _object {
      /* 引用计数 */
      /* 记录当前对象被引用的次数（引用计数机制），是 Python 内存管理的核心。 */
      /*  当对象被创建或被引用时（如赋值给变量、作为参数传递），ob_refcnt 加 1。
  		当引用失效时（如变量被删除、离开作用域），ob_refcnt 减 1。
  		当 ob_refcnt 减到 0 时，对象占用的内存会被 Python 解释器回收。*/
      int ob_refcnt;
      /* 对象指针 */
      /* 指向该对象的 “类型对象”（struct _typeobject），用于标识当前对象的类型（如整数、列表、函数等）。
      类型对象中存储了该类型的元信息（如类型名、支持的方法、创建实例的逻辑等）。例如，一个列表对象的 ob_type 指向 list 类型对象，因此 Python 知道它是列表，支持 append()、len() 等操作。
       */
      struct _typeobject *ob_type;
  } PyObject;
  ```

  ```c
  /* 增加引用计数的宏定义 */
  #define Py_INCREF(op)   ((op)->ob_refcnt++)
  /* 减少引用计数的宏定义 */
  /* --(op)->ob_refcnt：先将引用计数减 1。
  if (..., != 0) ;：如果减 1 后引用计数不为 0，什么也不做（对象仍被其他地方引用）。
  else __Py_Dealloc(...)：如果引用计数变为 0，调用 __Py_Dealloc 函数释放对象内存（实际是调用对象类型对应的析构函数）。 */
  #define Py_DECREF(op) \ //减少计数
      if (--(op)->ob_refcnt != 0) \
          ; \
      else \
          __Py_Dealloc((PyObject *)(op))
  ```

  导致引用计数+1的情况：

  - 对象被创建，例如`a = 23`
  - 对象被引用，例如`b = a`
  - 对象被作为参数，传入到一个函数中，例如`f(a)`
  - 对象作为一个元素，存储在容器中，例如`list1 = [a, a]`

  导致引用计数-1的情况：

  - 对象的别名被显式销毁，例如`del a`
  - 对象的别名被赋予新的对象，例如`a = 24`
  - 一个对象离开它的作用域，例如f函数执行完毕时，f函数中的局部变量（全局变量不会）
  - 对象所在的容器被销毁，或从容器中删除对象

  引用计数可能会导致循环引用问题，而循环引用会导致内存泄露(循环引用会导致**不再被程序使用的对象，其引用计数始终无法降到 0**，从而无法被内存管理器回收，最终造成内存泄漏。)，如下面的代码所示。为了解决这个问题，Python中引入了“标记-清除”和“分代收集”。在创建一个对象的时候，对象被放在第一代中，如果在第一代的垃圾检查中对象存活了下来，该对象就会被放到第二代中，同理在第二代的垃圾检查中对象存活下来，该对象就会被放到第三代中。

  > 标记-清除
  >
  > #### 核心思想
  >
  > 通过 “标记” 和 “清除” 两个阶段，识别并回收所有 “不可达” 的对象（即程序无法再访问的对象）。
  >
  > #### 工作流程
  >
  > 1. **标记阶段（Mark）**
  >    - 从 “根对象”（Root Objects）开始遍历所有可达对象（被根对象直接或间接引用的对象）。
  >    - 根对象通常包括：全局变量、当前栈帧中的局部变量、寄存器中的对象等（程序运行时必然能访问到的对象）。
  >    - 遍历过程中，将所有可达对象标记为 “存活”。
  > 2. **清除阶段（Sweep）**
  >    - 遍历整个内存空间，回收所有未被标记（即 “不可达”）的对象，释放其占用的内存。
  >    - 同时，清除所有对象的标记，为下一次回收做准备。

  > 分代收集
  >
  > #### 核心思想
  >
  > 基于 “**大部分对象的生命周期很短**” 的统计规律（弱代假说），将对象按存活时间分为不同 “代”（Generation），对不同代采用不同频率的回收策略：存活时间越短（年轻代），回收频率越高；存活时间越长（老年代），回收频率越低。
  >
  > #### 工作原理
  >
  > 1. **分代划分**
  >    - 通常分为 3 代：年轻代（Young Generation）、中年代（Middle Generation）、老年代（Old Generation）（不同语言可能有差异，如 Java 分新生代、老年代）。
  >    - 新创建的对象放入年轻代，每次回收后存活的对象 “晋升” 到更老的代（年龄递增）。
  > 2. **回收策略**
  >    - 年轻代：对象数量多、生命周期短，采用频繁、快速的回收（如复制算法，效率高）。
  >    - 老年代：对象存活时间长、数量少，采用较少频率的回收（如标记 - 清除或标记 - 整理算法）。
  >    - 整体回收频率：年轻代 > 中年代 > 老年代。

  > - **标记 - 清除是基础算法**，分代收集是基于标记 - 清除（或其他基础算法）的优化策略。
  > - 分代收集通过 “按代回收” 减少标记 - 清除的扫描范围，提高整体效率；而标记 - 清除负责具体的 “识别不可达对象并回收” 的工作。

  ```python
  # 循环引用会导致内存泄露 - Python除了引用技术还引入了标记清理和分代回收
  # 在Python 3.6以前如果重写__del__魔术方法会导致循环引用处理失效
  # 如果不想造成循环引用可以使用弱引用
  list1 = []
  list2 = [] 
  list1.append(list2)
  list2.append(list1)
  ```

  以下情况会导致垃圾回收：

  - 调用`gc.collect()`
  - `gc`模块的计数器达到阀值
  - 程序退出

  如果循环引用中两个对象都定义了`__del__`方法，`gc`模块不会销毁这些不可达对象，因为gc模块不知道应该先调用哪个对象的`__del__`方法，这个问题在Python 3.6中得到了解决。

  也可以通过`weakref`模块构造弱引用的方式来解决循环引用的问题。

- 魔法属性和方法（请参考《Python魔法方法指南》）

  在 Python 中，**魔法属性（Magic Attributes）** 和**魔法方法（Magic Methods）** 是指以双下划线 `__` 开头和结尾的特殊属性与方法（也称为 “特殊属性”“特殊方法”）。它们由 Python 解释器自动调用，用于实现对象的核心功能（如运算、比较、初始化等），是 Python 面向对象编程的底层机制。

  **一、魔法属性（Magic Attributes）**
  
  魔法属性是类或实例自带的特殊属性，无需手动定义，可直接访问，用于获取对象的元信息（如类型、文档、模块等）。
  
  **二、魔法方法（Magic Methods）**
  
  魔法方法是类中定义的特殊方法，由解释器在特定场景下自动调用（无需手动调用），用于实现对象的核心行为（如初始化、运算、比较等）。
  
  有几个小问题请大家思考：
  
  - 自定义的对象能不能使用运算符做运算？
  
    在 Python 中，**自定义对象可以通过运算符进行运算**，但需要通过重写特定的 “魔法方法”（以双下划线 `__` 开头和结尾的特殊方法）来实现。这些方法定义了对象与运算符交互的规则，让自定义对象能像内置类型（如整数、列表）一样支持 `+`、`-`、`*`、`>`、`==` 等运算。
  
    **核心原理**
  
    Python 的运算符本质是 “语法糖”，例如 `a + b` 会被解释器自动转换为调用 `a.__add__(b)` 方法。因此，只要在自定义类中实现对应的魔法方法，就能让对象支持相应的运算符。
  
  - 自定义的对象能不能放到`set`中？能去重吗？
  
    在 Python 中，**自定义对象可以放到 `set` 中**，但需要满足 `set` 对元素的要求（可哈希）；同时，**能否去重取决于对象的哈希值和相等性判断逻辑**，需要通过重写特定魔法方法实现。
  
    **一、自定义对象放入 `set` 的前提：可哈希（Hashable）**
  
    `set` 是基于哈希表实现的，要求元素必须是**可哈希的**（即具有固定的哈希值，且支持相等性判断）。对于自定义对象，需满足：
  
    1. 实现 `__hash__(self)` 方法：返回对象的哈希值（整数），用于哈希表存储。
    2. 实现 `__eq__(self, other)` 方法：定义对象的相等性判断逻辑，用于检测哈希冲突时的元素是否真正相等。
  
    如果未实现这两个方法，Python 会使用默认逻辑（基于对象的内存地址），但这通常不符合实际去重需求。
  
  - 自定义的对象能不能作为`dict`的键？
  
    在 Python 中，**自定义对象可以作为 `dict` 的键**，但需要满足 `dict` 对键的核心要求 ——**可哈希性（hashable）**。这一特性需要通过重写特定的魔法方法来实现，与自定义对象能否放入 `set` 的原理一致。
  
  - 自定义的对象能不能使用上下文语法？
  
    自定义对象**可以使用上下文语法**，只需实现 `__enter__` 和 `__exit__` 方法：
  
    - `__enter__` 负责准备资源（如建立连接）并返回操作对象。
    - `__exit__` 负责清理资源（如关闭连接），并可处理异常。
  
    这种机制能让代码更简洁、安全，避免因忘记释放资源导致的问题，是 Python 中管理资源的推荐方式。
  
- 混入（Mixin）

  在 Python 中，**混入（Mixin）** 是一种特殊的类设计模式，用于**向其他类提供可复用的功能**，但自身通常不单独实例化。它的核心作用是**通过多继承实现功能组合**，避免单一继承带来的代码冗余和扩展性问题。

  **混入的核心特点**

  1. **功能单一**：一个混入通常通常只实现一组相关功能（如日志记录、序列化等），专注于 “做一件事”。
  2. **不单独实例化**：混入类的设计目的是被其他类继承，而非单独创建对象（无实际业务意义）。
  3. **依赖宿主类**：混入类可能依赖于被继承的 “宿主类” 实现某些某些方法或属性（需宿主类实现）。
  4. **多继承组合**：通过多继承，一个类可以同时继承多个混入类，组合多种功能。

  ### 混入的典型应用场景

  当多个类需要共享相同功能（但不属于同一继承体系）时，使用混入可以避免代码重复。例如：日志记录、数据验证、缓存等功能。

  例子：自定义字典限制只有在指定的key不存在时才能在字典中设置键值对。

  ```python
  class SetOnceMappingMixin:
      """自定义混入类"""
      # __slots__ = () 表示该类不允许添加实例属性，仅作为功能混入使用。
      # 不允许添加实例属性，节省内存
      __slots__ = ()
  
      def __setitem__(self, key, value):
          if key in self:
              raise KeyError(str(key) + ' already set')
          # 调用父类的__setitem__方法（实际会调用dict的__setitem__）
          return super().__setitem__(key, value)
  
  
  class SetOnceDict(SetOnceMappingMixin, dict):
      """自定义字典"""
      pass
  
  
  my_dict= SetOnceDict()
  try:
      my_dict['username'] = 'jackfrued'
      my_dict['username'] = 'hellokitty'
  except KeyError:
      pass
  print(my_dict)
  ```

- 元编程和元类

  对象是通过类创建的，类是通过元类创建的，元类提供了创建类的元信息。所有的类都直接或间接的继承自`object`，所有的元类都直接或间接的继承自`type`。

  例子：用元类实现单例模式。

  ```python
  import threading
  
  
  class SingletonMeta(type):
      """自定义元类：实现线程安全的单例模式"""
  
      def __init__(cls, *args, **kwargs):
          # 初始化类属性：存储唯一实例和线程锁
          cls.__instance = None  # 用于保存类的唯一实例
          cls.__lock = threading.RLock()  # 可重入锁，确保多线程安全
          super().__init__(*args, **kwargs)  # 调用父类（type）的初始化方法
  
      def __call__(cls, *args, **kwargs):
          # 重写__call__方法：控制类的实例化过程
          if cls.__instance is None:  # 第一次检查：未创建实例时进入
              with cls.__lock:  # 加锁：确保多线程环境下只有一个线程进入创建逻辑
                  if cls.__instance is None:  # 第二次检查：防止多线程同时通过第一次检查
                      # 调用父类（type）的__call__方法创建实例（即调用President的__init__）
                      cls.__instance = super().__call__(*args, **kwargs)
          return cls.__instance  # 返回唯一实例
  
  
  class President(metaclass=SingletonMeta):
      """总统(单例类)"""
      
      pass
  ```

- 面向对象设计原则

  - 单一职责原则 （**S**RP）- 一个类只做该做的事情（类的设计要高内聚）
  - 开闭原则 （**O**CP）- 软件实体应该对扩展开发对修改关闭
  - 依赖倒转原则（DIP）- 面向抽象编程（在弱类型语言中已经被弱化）
  - 里氏替换原则（**L**SP） - 任何时候可以用子类对象替换掉父类对象
  - 接口隔离原则（**I**SP）- 接口要小而专不要大而全（Python中没有接口的概念）
  - 合成聚合复用原则（CARP） - 优先使用强关联关系而不是继承关系复用代码
  - 最少知识原则（迪米特法则，Lo**D**）- 不要给没有必然联系的对象发消息

  > **说明**：上面加粗的字母放在一起称为面向对象的**SOLID**原则。

- GoF设计模式

  - 创建型模式：单例、工厂、建造者、原型
  - 结构型模式：适配器、门面（外观）、代理
  - 行为型模式：迭代器、观察者、状态、策略

  例子：可插拔的哈希算法（策略模式）。

  ```python
  class StreamHasher:
      """哈希摘要生成器"""
  
      def __init__(self, alg='md5', size=4096):
          self.size = size
          alg = alg.lower()
          self.hasher = getattr(__import__('hashlib'), alg.lower())()
  
      def __call__(self, stream):
          return self.to_digest(stream)
  
      def to_digest(self, stream):
          """生成十六进制形式的摘要"""
          for buf in iter(lambda: stream.read(self.size), b''):
              self.hasher.update(buf)
          return self.hasher.hexdigest()
  
  def main():
      """主函数"""
      hasher1 = StreamHasher()
      with open('Python-3.7.6.tgz', 'rb') as stream:
          print(hasher1.to_digest(stream))
      hasher2 = StreamHasher('sha1')
      with open('Python-3.7.6.tgz', 'rb') as stream:
          print(hasher2(stream))
  
  
  if __name__ == '__main__':
      main()
  ```

### 迭代器和生成器

- 迭代器是实现了迭代器协议的对象。

  - Python中没有像`protocol`或`interface`这样的定义协议的关键字。
  - Python中用魔术方法表示协议。
  - `__iter__`和`__next__`魔术方法就是迭代器协议。

  ```python
  class Fib(object):
      """迭代器：生成斐波那契数列的前num个元素"""
      
      def __init__(self, num):
          self.num = num  # 要生成的斐波那契数列元素个数
          self.a, self.b = 0, 1  # 斐波那契数列的初始值（a代表当前值，b代表下一个值）
          self.idx = 0  # 当前迭代到的索引（从0开始计数）
     
      def __iter__(self):
          # 迭代器协议：返回自身（因为自身实现了__next__方法）
          return self
  
      def __next__(self):
          # 迭代器协议：返回下一个元素，没有元素时抛出StopIteration
          if self.idx < self.num:
              # 计算下一个斐波那契数（更新a和b的值）
              self.a, self.b = self.b, self.a + self.b
              self.idx += 1  # 索引+1，记录已生成的元素个数
              return self.a  # 返回当前的斐波那契数
          # 当索引达到num时，抛出StopIteration终止迭代
          raise StopIteration()
  ```

- 生成器是语法简化版的迭代器。

  ```python
  def fib(num):
      """生成器"""
      a, b = 0, 1
      for _ in range(num):
          a, b = b, a + b
          yield a
  ```

  > `yield` 关键字
  >
  > - 每次执行 `yield a` 时，会返回 `a` 的值给调用者，同时**暂停函数执行**，保存当前的变量状态（`a`、`b` 和循环计数）。
  > - 下次调用生成器的 `__next__` 方法时，函数会从暂停的位置继续执行，直到再次遇到 `yield` 或函数结束。

- 生成器进化为协程。

  生成器对象可以使用`send()`方法发送数据，发送的数据会成为生成器函数中通过`yield`表达式获得的值。这样，生成器就可以作为协程使用，协程简单的说就是可以相互协作的子程序。

  ```python
  def calc_avg():
      """流式计算平均值"""
      total, counter = 0, 0
      avg_value = None
      while True:
          value = yield avg_value
          total, counter = total + value, counter + 1
          avg_value = total / counter
  
  # 创建生成器对象
  gen = calc_avg()
  
  # 启动生成器：必须先调用 next(gen) 或 gen.send(None) 启动生成器，使其执行到 yield 处暂停（否则直接调用 send() 会报错）。
  next(gen)
  print(gen.send(10))
  print(gen.send(20))
  print(gen.send(30))
  ```

### 并发编程

Python中实现并发编程的三种方案：多线程、多进程和异步I/O。并发编程的好处在于可以提升程序的执行效率以及改善用户体验；坏处在于并发的程序不容易开发和调试，同时对其他程序来说它并不友好。

- 多线程：Python中提供了`Thread`类并辅以`Lock`、`Condition`、`Event`、`Semaphore`和`Barrier`。Python中有GIL来防止多个线程同时执行本地字节码，这个锁对于CPython是必须的，因为CPython的内存管理并不是线程安全(多线程环境中，一段代码或数据结构在被多个线程同时访问和操作时，仍能保证**结果的正确性、一致性和可预测性**，不会出现数据混乱、逻辑错误或意外行为。)的，因为GIL的存在多线程并不能发挥CPU的多核特性。

  ```python
  """
  面试题：进程和线程的区别和联系？
  进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
  线程 - 操作系统分配CPU的基本单位
  并发编程（concurrent programming）
  1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
  2. 改善用户体验 - 让耗时间的操作不会造成程序的假死
  """
  # 用于查找符合特定模式的文件路径（如images/*.png匹配所有 PNG 图片）。
  import glob
  import os
  import threading
  # PIL 库（Pillow）的图像处理模块，用于打开图片、生成缩略图和保存图片。
  from PIL import Image
  
  PREFIX = 'thumbnails'
  
  
  def generate_thumbnail(infile, size, format='PNG'):
      """生成指定图片文件的缩略图"""
      # 分离文件名和扩展名（如"images/a.png" → file="images/a", ext=".png"）
      file, ext = os.path.splitext(infile)
      # 提取文件名（去掉路径，如"images/a" → "a"）
      file = file[file.rfind('/') + 1:]
      # 构造缩略图保存路径（如"thumbnails/a_32_32.png"）
      outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
      # 打开原始图片
      img = Image.open(infile)
      # 生成缩略图（ANTIALIAS表示抗锯齿，使缩略图更清晰）
      img.thumbnail(size, Image.ANTIALIAS)
      # 保存缩略图
      img.save(outfile, format)
  
  
  def main():
      """主函数"""
      # 若thumbnails目录不存在，则创建
      if not os.path.exists(PREFIX):
          os.mkdir(PREFIX)
      # 遍历images目录下所有PNG图片
      for infile in glob.glob('images/*.png'):
          # 为每种尺寸创建一个线程处理
          for size in (32, 64, 128):
              # 创建并启动线程，目标函数为generate_thumbnail
              threading.Thread(
                  target=generate_thumbnail, # 指定线程要执行的函数
                  args=(infile, (size, size))  # # 指定传给函数的参数
              ).start()
  			
  
  if __name__ == '__main__':
  	main()
  ```

  多个线程竞争资源的情况。

  ```python
  """
  多线程程序如果没有竞争资源处理起来通常也比较简单
  当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
  说明：临界资源就是被多个线程竞争的资源
  """
  import time
  import threading
  
  from concurrent.futures import ThreadPoolExecutor
  
  
  class Account(object):
      """银行账户"""
  
      def __init__(self):
          self.balance = 0.0  # 账户余额，初始为0
          self.lock = threading.Lock()  # 互斥锁，用于保护临界资源
  
      def deposit(self, money):
          # 通过with语句使用锁，自动获取和释放锁
          with self.lock:
              # 计算新余额
              new_balance = self.balance + money
              # 模拟耗时操作（放大线程安全问题）
              time.sleep(0.001)
              # 更新余额
              self.balance = new_balance
  
  
  def main():
      """主函数"""
      account = Account()  # 创建银行账户实例
      # 创建线程池，最多同时运行10个线程
      pool = ThreadPoolExecutor(max_workers=10)
      futures = []
      # 提交100次存款任务（每次存入1元）
      for _ in range(100):
          # 向线程池提交deposit方法，参数为1
          future = pool.submit(account.deposit, 1)
          futures.append(future)
      # 关闭线程池，等待所有任务完成
      pool.shutdown()
      # 等待所有任务执行完毕（获取结果，此处无返回值，仅确保完成）
      for future in futures:
          future.result()
      # 打印最终余额
      print(account.balance)  # 输出：100.0（线程安全，结果正确）
  
  
  if __name__ == '__main__':
      main()
  ```

  修改上面的程序，启动5个线程向账户中存钱，5个线程从账户中取钱，取钱时如果余额不足就暂停线程进行等待。为了达到上述目标，需要对存钱和取钱的线程进行调度，在余额不足时取钱的线程暂停并释放锁，而存钱的线程将钱存入后要通知取钱的线程，使其从暂停状态被唤醒。可以使用`threading`模块的`Condition`来实现线程调度，该对象也是基于锁来创建的，代码如下所示：

  ```python
  """
  多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
  多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
  多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
  """
  from concurrent.futures import ThreadPoolExecutor
  from random import randint
  from time import sleep
  
  import threading
  
  
  class Account:
      """银行账户"""
  
      def __init__(self, balance=0):
          self.balance = balance  # 账户余额
          # 创建可重入锁（RLock），允许同一线程多次获取锁
          lock = threading.RLock()
          # 基于锁创建条件变量（Condition），用于线程间通信
          # condition 条件变量：是线程同步的核心，内部包含一个锁（RLock），提供 wait()（等待）和 notify_all()（通知）方法，实现线程间的协作。
          self.condition = threading.Condition(lock)
  
      def withdraw(self, money):
      """取钱"""
      with self.condition:  # 获取条件变量的锁，确保操作原子性
          # 循环检查：若余额不足，让线程等待（避免虚假唤醒）
          while money > self.balance:
              self.condition.wait()  # 释放锁，进入等待状态，直到被通知
          # 余额足够时执行取款
          new_balance = self.balance - money
          sleep(0.001)  # 模拟耗时操作（如数据库更新）
          self.balance = new_balance
  
      def deposit(self, money):
      """存钱"""
      with self.condition:  # 获取锁，确保操作原子性
          # 执行存款
          new_balance = self.balance + money
          sleep(0.001)  # 模拟耗时操作
          self.balance = new_balance
          # 通知所有等待的线程：余额已更新，可能满足取款条件
          self.condition.notify_all()
  
  
  def add_money(account):
      while True:
          money = randint(5, 10)
          account.deposit(money)
          print(threading.current_thread().name, 
                ':', money, '====>', account.balance)
          sleep(0.5)
  
  
  def sub_money(account):
      while True:
          money = randint(10, 30)
          account.withdraw(money)
          print(threading.current_thread().name, 
                ':', money, '<====', account.balance)
          sleep(1)
  
  
  def main():
      account = Account()
      with ThreadPoolExecutor(max_workers=15) as pool:
          for _ in range(5):
              pool.submit(add_money, account)
          for _ in range(10):
              pool.submit(sub_money, account)
  
  
  if __name__ == '__main__':
      main()
  ```

- 多进程：多进程可以有效的解决GIL的问题(**限制了 Python 多线程的并行能力，导致 CPU 密集型任务无法通过多线程真正利用多核 CPU**。)，实现多进程主要的类是`Process`，其他辅助的类跟`threading`模块中的类似，进程间共享数据可以使用管道、套接字等，在`multiprocessing`模块中有一个`Queue`类，它基于管道和锁机制提供了多个进程共享的队列。下面是官方文档上关于多进程和进程池的一个示例。

  ```python
  """
  多进程和进程池的使用
  多线程因为GIL的存在不能够发挥CPU的多核特性
  对于计算密集型任务应该考虑使用多进程
  time python3 example22.py
  real    0m11.512s
  user    0m39.319s
  sys     0m0.169s
  使用多进程后实际执行时间为11.512秒，而用户时间39.319秒约为实际执行时间的4倍
  这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU
  """
  import concurrent.futures
  import math
  
  PRIMES = [
      1116281,
      1297337,
      104395303,
      472882027,
      533000389,
      817504243,
      982451653,
      112272535095293,
      112582705942171,
      112272535095293,
      115280095190773,
      115797848077099,
      1099726899285419
  ] * 5
  
  
  def is_prime(n):
      """判断素数"""
      # 若n是偶数（且不是2），直接返回False（偶数是偶数不是素数）
      if n % 2 == 0:
          return False
  
      # 计算n的平方根（向下取整）
      sqrt_n = int(math.floor(math.sqrt(n)))
      # 从3开始，步长为2（只检查奇数），直到sqrt_n
      for i in range(3, sqrt_n + 1, 2):
          if n % i == 0:  # 若能被i整除，不是素数
              return False
      return True  # 所有检查通过，是素数
  
  
  def main():
      """主函数"""
      with concurrent.futures.ProcessPoolExecutor() as executor:
          for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
              print('%d is prime: %s' % (number, prime))
  
  
  if __name__ == '__main__':
      main()
  ```

  > **重点**：**多线程和多进程的比较**。
  >
  > 以下情况需要使用多线程：
  >
  > 1. 程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。
  > 2. 程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。
  >
  > 以下情况需要使用多进程：
  >
  > 1. 程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
  > 2. 程序的输入可以并行的分成块，并且可以将运算结果合并。
  > 3. 程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）。

- 异步处理：从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，我们并不能保证任务将以某种顺序去执行，因为执行顺序取决于队列中的一项任务是否愿意将 CPU 处理时间让位给另一项任务。异步任务通常通过多任务协作处理的方式来实现，由于执行时间和顺序的不确定，因此需要通过回调式编程或者`future`对象来获取任务执行的结果。Python 3 通过`asyncio`模块和`await`和`async`关键字（在 Python 3.7 中正式被列为关键字）来支持异步处理。

  ```python
  """
  异步I/O - async / await
  """
  import asyncio
  
  
  def num_generator(m, n):
      """指定范围的数字生成器"""
      yield from range(m, n + 1)
  
  
  async def prime_filter(m, n):
      """素数过滤器：找出m到n之间的所有素数"""
      primes = []
      for i in num_generator(m, n):
          flag = True  # 标记是否为素数
          # 检查i是否能被2到√i之间的数整除
          for j in range(2, int(i **0.5 + 1)):
              if i % j == 0:
                  flag = False
                  break
          if flag:
              print('Prime =>', i)  # 打印素数
              primes.append(i)
          
          # 暂停0.001秒，允许事件循环切换到其他协程
          await asyncio.sleep(0.001)
      return tuple(primes)  # 返回找到的素数
  
  
  async def square_mapper(m, n):
      """平方映射器：计算m到n之间所有数字的平方"""
      squares = []
      for i in num_generator(m, n):
          print('Square =>', i * i)  # 打印平方结果
          squares.append(i * i)
          
          # 暂停0.001秒，允许事件循环切换到其他协程
          await asyncio.sleep(0.001)
      return squares  # 返回平方结果列表
  
  
  def main():
      """主函数：启动事件循环，执行异步任务"""
      loop = asyncio.get_event_loop()  # 获取事件循环
      # 并发运行两个协程：素数过滤（2-100）和平方映射（1-100）
      future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
      # 添加回调函数：任务完成后打印结果
      future.add_done_callback(lambda x: print(x.result()))
      # 运行事件循环，直到所有任务完成
      loop.run_until_complete(future)
      # 关闭事件循环
      loop.close()
  
  
  if __name__ == '__main__':
      main()
  ```

  > **说明**：上面的代码使用`get_event_loop`函数获得系统默认的事件循环，通过`gather`函数可以获得一个`future`对象，`future`对象的`add_done_callback`可以添加执行完成时的回调函数，`loop`对象的`run_until_complete`方法可以等待通过`future`对象获得协程执行结果。

  Python 中有一个名为`aiohttp`的三方库，它提供了异步的 HTTP 客户端和服务器，这个三方库可以跟`asyncio`模块一起工作，并提供了对`Future`对象的支持。Python 3.6中引入了`async`和`await`来定义异步执行的函数以及创建异步上下文，在 Python 3.7 中它们正式成为了关键字。下面的代码异步的从5个URL中获取页面并通过正则表达式的命名捕获组提取了网站的标题。

  ```python
  import asyncio
  import re
  
  import aiohttp
  
  PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
  
  
  async def fetch_page(session, url):
      # 使用异步上下文管理器发送GET请求，ssl=False禁用SSL验证（避免某些网站证书问题）
      async with session.get(url, ssl=False) as resp:
          # 等待并返回响应的文本内容（HTML）
          return await resp.text()
  
  
  async def show_title(url):
      # 创建异步HTTP会话（类似浏览器的会话）
      async with aiohttp.ClientSession() as session:
          # 调用fetch_page获取HTML，等待其完成
          html = await fetch_page(session, url)
          # 用正则表达式提取<title>标签内容并打印
          print(PATTERN.search(html).group('title'))
  
  
  def main():
      # 要爬取的URL列表
      urls = (
          'https://www.python.org/',
          'https://git-scm.com/',
          'https://www.jd.com/',
          'https://www.taobao.com/',
          'https://www.douban.com/'
      )
      # 获取事件循环（异步任务的调度中心）
      loop = asyncio.get_event_loop()
      # 创建任务列表：为每个URL创建一个show_title协程
      cos = [show_title(url) for url in urls]
      # 运行事件循环，等待所有任务完成（asyncio.wait会等待所有协程执行完毕）
      loop.run_until_complete(asyncio.wait(cos))
      # 关闭事件循环
      loop.close()
  
  
  if __name__ == '__main__':
      main()
  ```

  > **重点**：**异步I/O与多进程的比较**。
  >
  > 当程序不需要真正的并发性或并行性，而是更多的依赖于异步处理和回调时，`asyncio`就是一种很好的选择。如果程序中有大量的等待与休眠时，也应该考虑`asyncio`，它很适合编写没有实时数据处理需求的 Web 应用服务器。

  Python 还有很多用于处理并行任务的三方库，例如：`joblib`、`PyMP`等。实际开发中，要提升系统的可扩展性和并发性通常有垂直扩展（增加单个节点的处理能力）和水平扩展（将单个节点变成多个节点）两种做法。可以通过消息队列来实现应用程序的解耦合，消息队列相当于是多线程同步队列的扩展版本，不同机器上的应用程序相当于就是线程，而共享的分布式消息队列就是原来程序中的Queue。消息队列（面向消息的中间件）的最流行和最标准化的实现是 AMQP（高级消息队列协议），AMQP 源于金融行业，提供了排队、路由、可靠传输、安全等功能，最著名的实现包括：Apache 的 ActiveMQ、RabbitMQ 等。

  要实现任务的异步化，可以使用名为`Celery`的三方库。`Celery`是 Python 编写的分布式任务队列，它使用分布式消息进行工作，可以基于 RabbitMQ 或 Redis 来作为后端的消息代理。

## 30.Web前端入门

























