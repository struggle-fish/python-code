import re

'''
\w 匹配字母数字以及下划线 等价于'[A-Za-z0-9_]'
\W 匹配非字母数字下划线 等价于 '[^A-Za-z0-9_]'

\s 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]
\S 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]

\d 匹配一个数字字符。等价于 [0-9]
\D 匹配一个非数字字符。等价于 [^0-9]


\b	
匹配一个单词边界，也就是指单词和空格间的位置。
例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	
匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。






\A 匹配字符串开始
\Z 匹配字符串结束 如果存在换行，只能匹配到换行前的结束

^ 匹配输入字符串的开始位置。
如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。
$ 匹配输入字符串的结束位置。
如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。


重复匹配：

1、. :匹配除了\n之外任意一个字符，指定re.DOTALL之后才能匹配换行符
匹配除换行符（\n、\r）之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用像"(.|\n)"的模式。

2、*：左侧字符重复0次或无穷次，性格贪婪
匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。

3、+：左侧字符重复1次或无穷次，性格贪婪
匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。

4、？：左侧字符重复0次或1次，性格贪婪
匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 。? 等价于 {0,1}。
?	
当该字符紧跟在任何一个其他限制符 (*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的。
非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。
例如，对于字符串 "oooo"，'o+?' 将匹配单个 "o"，而 'o+' 将匹配所有 'o'。




5、{n,m}：左侧字符重复n次到m次，性格贪婪
{0,} => *
{1,} => +
{0,1} => ?
{n}单独一个n代表只出现n次，多一次不行少一次也不行

{n}	
n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。

{n,}	
n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。

{n,m}	
m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。


|
x|y	
匹配 x 或 y。例如，'z|food' 能匹配 "z" 或 "food"。'(z|f)ood' 则匹配 "zood" 或 "food"。


[]匹配指定字符一个
[xyz]	
字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。
[^xyz]	
负值字符集合。匹配未包含的任意字符。例如， '[^abc]' 可以匹配 "plain" 中的'p'、'l'、'i'、'n'。
[a-z]	
字符范围。匹配指定范围内的任意字符。例如，'[a-z]' 可以匹配 'a' 到 'z' 范围内的任意小写字母字符。
[^a-z]	
负值字符范围。匹配任何不在指定范围内的任意字符。例如，'[^a-z]' 可以匹配任何不在 'a' 到 'z' 范围内的任意字符。

选择
用圆括号 () 将所有选择项括起来，相邻的选择项之间用 | 分隔。
() 表示捕获分组，() 会把每个分组里的匹配的值保存起来， 多个匹配值可以通过数字 n 来查看(n 是一个数字，表示第 n 个捕获组的内容)。


修饰符：imgs
i   ignore - 不区分大小写	将匹配设置为不区分大小写，搜索时不区分大小写: A 和 a 没有区别。
g	global - 全局匹配	查找所有的匹配项。
m	multi line - 多行匹配	使边界字符 ^ 和 $ 匹配每一行的开头和结尾，记住是多行，而不是整个字符串的开头和结尾。
s	特殊字符圆点 . 中包含换行符 \n	默认情况下的圆点 . 是匹配除换行符 \n 之外的任何字符，加上 s 修饰符之后, . 中包含换行符 \n。

运算符：
\	转义符

(), (?:), (?=), []	圆括号和方括号

*, +, ?, {n}, {n,}, {n,m}	限定符

^, $, \任何元字符、任何字符	定位点和序列（即：位置和顺序）

|	替换，"或"操作
字符具有高于替换运算符的优先级，使得"m|food"匹配"m"或"food"。若要匹配"mood"或"food"，请使用括号创建子表达式，从而产生"(m|f)ood"。

'''

print(re.findall('\w','aAbc123_*()-='))
# print(re.findall('\W','aAbc123_*()-= '))
# print(re.findall('\s','aA\rbc\t\n12\f3_*()-= '))
# print(re.findall('\S','aA\rbc\t\n12\f3_*()-= '))
# print(re.findall('\d','aA\rbc\t\n12\f3_*()-= '))
# print(re.findall('\D','aA\rbc\t\n12\f3_*()-= '))
# print(re.findall('\D','aA\rbc\t\n12\f3_*()-= '))
# print(re.findall('\Aalex',' alexis alex sb'))
#                          alex
# print(re.findall('sb\Z',' alexis alexsb sb'))
#                                       sb\Z
# print(re.findall('sb\Z',"""alex
# alexis
# alex
# sb
# """))

# print(re.findall('^alex','alexis alex sb'))
# print(re.findall('sb$','alexis alex sb'))
# print(re.findall('sb$',"""alex
# alexis
# alex
# sb
# """))

# print(re.findall('^alex$','alexis alex sb'))
# print(re.findall('^alex$','al       ex'))
# print(re.findall('^alex$','alex'))

# 重复匹配：| . | * | ? | .* | .*? | + | {n,m} |
# 1、.:匹配除了\n之外任意一个字符，指定re.DOTALL之后才能匹配换行符
# print(re.findall('a.b','a1b a2b a b abbbb a\nb a\tb a*b'))
#                                                   a.b
# ['a1b','a2b','a b','abb','a\tb','a*b']
# print(re.findall('a.b','a1b a2b a b abbbb a\nb a\tb a*b',re.DOTALL))

# 2、*：左侧字符重复0次或无穷次，性格贪婪
# print(re.findall('ab*','a ab abb abbbbbbbb bbbbbbbb'))
#                                                ab*
# ['a','ab','abb','abbbbbbbb']

# 3、+：左侧字符重复1次或无穷次，性格贪婪
# print(re.findall('ab+','a ab abb abbbbbbbb bbbbbbbb'))
#                         ab+

# 4、？：左侧字符重复0次或1次，性格贪婪
# print(re.findall('ab?','a ab abb abbbbbbbb bbbbbbbb'))
#                                                ab?
# ['a','ab','ab','ab']

# 5、{n,m}：左侧字符重复n次到m次，性格贪婪
# {0,} => *
# {1,} => +
# {0,1} => ?
# {n}单独一个n代表只出现n次，多一次不行少一次也不行

# print(re.findall('ab{2,5}','a ab abb abbb abbbb abbbbbbbb bbbbbbbb'))
#                                                           ab{2,5}
# ['abb','abbb','abbbb','abbbbb]

# print(re.findall('\d+\.?\d*',"asdfasdf123as1111111.123dfa12adsf1asdf3"))
#                                                                   \d+\.?\d*                                      \d+\.?\d+


# []匹配指定字符一个
# print(re.findall('a\db','a1111111b a3b a4b a9b aXb a b a\nb',re.DOTALL))
# print(re.findall('a[501234]b','a1111111b a3b a4b a9b aXb a b a\nb',re.DOTALL))
# print(re.findall('a[0-5]b','a1111111b a3b a1b a0b a4b a9b aXb a b a\nb',re.DOTALL))
# print(re.findall('a[0-9a-zA-Z]b','a1111111b axb a3b a1b a0b a4b a9b aXb a b a\nb',re.DOTALL))
#
# print(re.findall('a[^0-9a-zA-Z]b','a1111111b axb a3b a1b a0b a4b a9b aXb a b a\nb',re.DOTALL))
# print(re.findall('a-b','a-b aXb a b a\nb',re.DOTALL))
# print(re.findall('a[-0-9\n]b', 'a-b a0b a1b a8b aXb a b a\nb', re.DOTALL))
