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
  - 惯例2：受保护的变量用单个下划线开头。
  - 惯例3：私有的变量用两个下划线开头。

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



