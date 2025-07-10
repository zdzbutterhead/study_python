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

## 14.函数应用实战

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









