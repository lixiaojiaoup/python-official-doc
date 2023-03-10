# python-official-doc

##
### python特点
- 简单易学，有大量的标准库和第三方库
- 

### 变量
1. 变量的概念：变量就是一种标识符，是内存中数据的引用，是数据的名字
2. 变量的命名规范： 
   - 由字母，数字和下划线组成，不能以数字开头
   - 严格区分大小写
   - 不能将python的关键字作为变量名，关键字也即保留字，跟python语法相关的词，有特殊含义
   - 也最好不要将内置函数名作为变量名，一旦这么做了内置函数就失去了其本来的作用，容易引起冲突
3. 变量的作用域：查找的范围为 L-E-G-B
   - 局部作用域：local
   - 嵌套作用域：enclosed
   - 全局作用域：global
   - 内置作用域：built-in
   - 首先在函数内部进行搜索，搜索不到就到上层函数或者类中进行查找，再找不到就从全局作用域中查找，还找不到就进入预定义的内置作用域查找；再找不到就报错
   - 比如你在函数内定义了sum变量，当有地方使用sum，首先就会按照变量进行使用，后续如果想按照函数进行使用就会报错
4. 注意点
   - 变量不能只声明不赋值，必须在声明时就赋值，变量赋值后才会在内存中开辟一块空间，真正保存
   - 变量没有类型，虽然可以用type函数来查看类型，但本质上，查看的是变量引用的数据的类型
   - a = 1，在内存中开辟一块内存，存储该变量引用的数据，有type+value+内存地址+引用数量4个字段

### 字符串
1. 定义：字符串是由引号括起来的若干字符的集合，引号可以是单引号，双引号和三引号；
   - 当字符串内部有引号时，外部的要与其类型不一致
   - 或者使用转义字符\反斜杠进行转义
   - 三引号括起来的字符如果没有赋值给变量，相当于多行注释
2. 常用方法：
   - 字符串是比较常用的数据类型
   - 常用的方法有去除两端空格strip，对字符串进行切割split，以及其逆向操作join
   - 还有一些常用的判断，比如判断是否以指定字符开头和结尾，startswith和endswith
   - 还有就是字符串和数字之间的转换，ord和chr方法，这个工作中用的比较少，一般是leetcode刷题时用到
3. 常见运算：
   - 通过+号对字符串进行拼接
   - *号重复输出字符串
   - 通过索引获取单个字符串以及切片获取字符串的一部分
   - 然后就是格式化输出，比如在字符串最前面加上f字母，内部变量用花括号括起来；或者使用%的方式，然后就是format

### 列表
1. 定义：是存储一系列有序元素的集合的容器类型，容器内的元素类型可以不一致，也可以是列表，即嵌套列表
2. 列表可以说是python中使用最频繁的数据类型 
3. 可以使用[]中括号或者内置函数list创建列表
4. 支持常见的增删改查操作
   - 比如增加元素，可以使用append在尾部追加元素
   - 也可以使用insert在指定位置添加元素
   - 也可以使用extend对列表进行扩充
   - 以上方式都是就地增加
   - 
   - 然后是删，可以使用remove方法删除指定的元素，不过只能删除首个满足条件的元素
   - 也可以使用pop方法进行删除，如果不传入参数，默认删除末尾元素，如果传入索引参数，则删除指定所谓位置的元素
   - pop方法有返回值，在删除指定元素的同时还能继续使用该元素
   - 然后就是内置的del语句进行删除
   - 
   - 然后是元素的查询，可以通过索引，python支持正负索引，从前往后依次是0,1,依次类推，从后往前则是-1，-2这样的
   - 也可以通过切片，查询一段数据，插一句，列表的切片的浅拷贝
   - 
   - 再者就是改，可以通过查询到指定元素后，直接进行重新赋值以进行修改
   - 如果对单个索引的值进行修改，直接赋单个值
   - 如果是对一段切片进行修改，修改赋一个可迭代对象
5. 然后就是python的一些特点，比如python常常拿来和元组做对比
   - 因为列表中的元素是可变的，长度也是可变的，而元组中的元素是不可变的定义后长度也就确定了，所以列表要比元组多一些额外的存储空间，比如存储列表长度信息的字段等

### 元组

### 集合
- 集合通常用来去重和做成员存在与否的判断

### 字典
- 是一系列键值对的无序集合
- 使用一对{}或者dict函数来创建字典
- 键必须是不可变类型，从浅层解释就是，如果键可变，就没法保证键的唯一性了，因为字典的访问是通过键索引值，如果键不唯一那么就会导致数据查询结果冲突
- 字典查询用的比较多，也会有获取字典所有的键keys()或者所有的值values()以及所有的键值对items(),然后对它们进行迭代的操作
- 这个在工作中使用也是很多的，跟列表差不多

### 推导式
- 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列
- 比如有列表推导式，字典推导式,当然也有集合推导式
- 然后有种特殊的推导式，元组推导式，得到的结果是一个生成器表达式，使用tuple函数可以直接将生成器对象转换成元组
- 生成器对象具有惰性求值的特点，只在需要时生成新元素，比列表推导式更高效，空间占用更少，尤其适合大数据处理的场合
- 
### 函数
- 函数是封装好的实现单一功能的代码的集合，可以重复使用
- 使用def关键字进行定义
- 跟函数密切相关的内容有参数和返回值
- 函数可以是无参，也可以是有参，有参数时存在多种情况
- 比如有位置参数，调用函数时传入的实参，与函数定义时从左到右形参的位置一个个对应
- 然后也有关键字参数，调用函数时，通过参数名进行赋值，这样就算传入的参数顺序与定义时不一致也不影响实际效果
- 再者就是默认值参数，即函数定义时可以设置一个默认值，当函数调用时没有传入参数就使用该默认值参数，如果传入了参数就用传入的参数
- 最后就是不定长参数，比如函数定义时不确定要传入的参数类型和个数，就可以使用不定长参数，这个一般通过*号的个数来分区，
- *args表示的是
- **args表示的是
- 然后就是函数的返回值，python可以没有返回值，也可以有一个返回值，还可以是多个返回值
- 多个返回值通常是将多个值用一个元组存起来，然后通过元组解包进行赋值
- 注意点：
  - 参数的传递过程，其实就是实参对形参的赋值过程，是浅拷贝
  - 

### 匿名函数
- 使用lambda关键字进行定义，用一行代码就能实现的函数，格式为lambda 参数：表达式 其中参数不是必须的，但表达式是必须的
- 表达式的结果就是函数的返回值
- 经常的结合高阶函数比如filter，map等一起使用，不过有了推导式，这种高级用法我用的还是比较少
- 当然在排序时倒也常用，常常用作排序key的参数

### 类
- 类常见的概念就是封装，继承和多态
- 首先从类的封装来说，主要包括属性和方法
- 属性是找类的静态特征，方法主要是找类的动态行为
- 其中属性有成员属性和类属性，成员属性是每个实例成员独有的，彼此之间不共享，类属性是所有类成员共享的属性，一个成员改动了该属性，其他成员看见的就是改变后的值
- 方法主要有三种类型，包括成员方法，类方法和静态方法
- 成员方法就是常规的实例方法，通过实例对象进行调用
- 静态方法是通过@staticmethod装饰器进行装饰的方法，不过它并不会使用类内部的属性和方法，和外部的函数一样，只不过封装在类的内部方便类的使用
- 类方法是通过@classmethod装饰器装饰的方法，它传入的第一个参数cls class，类方法可以直接通过类进行调用
- 一般可以在创建实例之前做一些必要的判断等
- 然后就是继承
- python支持多继承，子类可以继承父类的属性和方法，也可以重写父类的属性和方法，还可以拥有自己的属性和方法
- 在多重继承下，方法的查找顺序为先查找自身，然后根据类名后括号内继承的顺序从左往右逐个查找
- 使用的是广度优先查找，即如果从第一个父类没有找到方法，就会从该父类的父类，依次往下找，遍历完后会返回再从第二个父类开始
- 最后是多态
- 我对多态的理解是，定义一个抽象类，子类只需要实现该方法即可，具体实现细节各自可以不同


## 常见题
### 赋值，深拷贝，浅拷贝的区别
- 赋值本质上就是浅拷贝
- 浅拷贝，拷贝的是对象的引用
- 深拷贝，拷贝的是整个对象的值，在内存中重新开辟了一块空间
- 可以通过copy库的deepcopy实现深拷贝
- 浅拷贝可以通过切片，赋值，工厂函数，copy模块的copy函数等实现

### python的变量，对象以及引用
- 变量是内存地址的引用，也就是指向对象的内存空间
- 对象的一块内存，表示它们所代表的值
- 引用就是自动形成的从变量到对象的指针
- 比如a = 1就是变量a引用对象1

### 什么是解释型语言，什么是编译型语言
- 计算机听不懂人类的语言，所以要把人类语言翻译成它能理解的机器语言
- 其中解释型语言，比如python，就是程序边执行的时候边解释
- 而编译型语言，比如go，就是在程序执行前，需要有一个专门的编译过程，把程序编译成机器语言
- 相对而言，解释型语言的编写效率较高，执行效率较低，编译型语言执行效率较高，代码编写效率较低，不过从go来看，编写效率也提高了不少

### python中的作用域
- 一个变量的作用域是由代码中被赋值的地方所决定的
- 通常它的搜索顺序为，内部函数，上级函数，全局作用域，内置作用域
- 如果在局部作用域内想使用全局作用域内的变量，可以使用global关键字声明一下
- 如果在内函数想使用外函数的变量，可以使用nonlocal关键字声明



