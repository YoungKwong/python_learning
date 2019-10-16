#1_导入模块
import re  #导入正则表达式模块
print('1_导入模块\n')

#2_简单python匹配
# matching string
pattern1 = 'cat'
pattern2 = 'bird'
string = "dog runs to cat"
print(pattern1 in string)  #pattern1在string里面返回True
print(pattern2 in string)  #pattern2不在string里面返回False
print('2_简单python匹配\n')


#3_用正则寻找配对
# regular expression
print(re.search(pattern1, string))  #用re.search()在第二个参数里面找有没有第一个参数
print(re.search(pattern2, string))  #如果在就返回一个object形式的信息，如果不在就返回None
print('3_用正则寻找配对\n')

#4_匹配多种可能 使用[]
# multiple patterns(""run" or "ran")
ptn = r"r[ua]n"  #r"***"是一个正则表达式，用“[情况1情况2]”可以同时考虑到多种情况
print(re.search(ptn, "dog rans to cat"))

#cohtinue
print(re.search(r"r[A-Z]n", "dog runs to cat"))  #匹配大写字母A-Z
print(re.search(r"r[a-z]n", "dog runs to cat"))  #匹配小写字母a-z
print(re.search(r"r[0-9]n", "dog r2ns to cat"))  #匹配数字0-9
print(re.search(r"r[0-9a-z]n", "dog runs to cat"))  #匹配数字0-9和小写字母a-z
print('4_匹配多种可能 使用[]\n')

#5_特殊种类匹配
#5-1_数字
print(re.search(r"r\dn", "run r4n"))  # \d：decimal digit(所有数字)
print(re.search(r"r\Dn", "run r4n"))  # \D：any non-decimal digit(除了所有数字之外)
print('5-1_数字\n')

#5-2_转义字符
print(re.search(r"r\sn", "r\nn r4n"))  # \s：any white space[\t\n\f\v](所有转义字符)
print(re.search(r"r\Sn", "r\nn r4n"))  # \S：opposite to \s, any non-white space(除了所有转义字符之外)
print('5-2_转义字符\n')

#5-3_所有字母数字和"_"
print(re.search(r"r\wn", "r\nn r4n"))  # \w：[a-zA-Z0-9_]
print(re.search(r"r\Wn", "r\nn r4n"))  # \W：opposite to \w
print('5-3_所有字母数字和"_"\n')

#5-4_空白字符
print(re.search(r"\bruns\b", "dog runs to cat"))  # \b：empty string (only at the start or end of the word)
print(re.search(r"\B runs \B", "dog    runs    to cat"))  # \B：empty string>1 (but not at the start or end of a word)
print('5-4_空白字符\n')

#5-5_特殊字符 任意字符
print(re.search(r"runs\\", "runs\ to me"))  # \\：match \
print(re.search(r"r.ns", "r-ns to me"))  # \.：match anything(except \n)
print('5-5_特殊字符 任意字符\n')

#6_句首句尾
print(re.search(r"^dog", "dog runs to cat"))  # ^：match line beginning
print(re.search(r"cat$", "dog runs to cat"))  # $：match line ending
print('6_句首句尾\n')

#7_多行匹配 M-->mulit-line
string = """
dog runs to cat
I run to dog.
"""
print(re.search(r"^I", string))  #匹配句首匹配不到
print(re.search(r"^I", string, flags=re.M))  #在search是给flags=re.M，把每一个句子看成单独的句子
print('7_多行匹配\n')

#8_是否
print(re.search(r"Mon(day)?", "Monday"))  # ?：may or may not occur
print(re.search(r"Mon(day)?", "Mon"))  # ()?括号里的内容无论有没有都可以匹配到
print('8_是否\n')

#9_0次或多次
print(re.search(r"ab*", "a"))  # *：occur 0 or more times
print(re.search(r"ab*", "abbbbb"))
print('9_0次或多次\n')

#10_1次或多次
print(re.search(r"ab+", "a"))  # +：occur 1 or more times
print(re.search(r"ab+", "abbbbb"))
print('10_1次或多次\n')

#11_可选次数
print(re.search(r"ab{2,10}", "a"))  # {n,m}：occur n to m times
print(re.search(r"ab{2,10}", "abbbbb"))
print('11_可选次数\n')

#12_group组
#group是想匹配并取出多个数据时使用，r"(group(1)), (group(2))"
match = re.search(r"ID:(\d+), Date:(.+)", "ID:021523, Date:Feb/12/2017")
print(match.group())  #.group()括号里面没有内容，返回全部group
print(match.group(1))
print(match.group(2))

#如果有很多group组，可以用 "?P<名字>" 给group组命名
match1 = re.search(r"ID:(?P<id>\d+), Date:(?P<date>.+)", "ID:021523, Date:Feb/12/2017")
print(match1.group('id'))  #group()括号里输入想索引的名字（记得用引号引起来）
print(match1.group('date'))
print('12_group组\n')

#13_寻找所有匹配
print(re.findall(r"r[au]n", "run ran ren"))  #用re.findall()把匹配的全部找出
print(re.findall(r"(ran|run)", "run ran ren"))  # |：or
print('13_寻找所有匹配\n')

#14_替换
print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))  #用re.sub()把第一个参数匹配到的替换成第二个参数的内容
print('14_替换\n')

#15_分裂
print(re.split(r"[,;\.]","a;b,ccc.d.e")) #re.split(r"[想要去除的东西]", "被分裂的内容")
print('15_分裂\n')

#16_compile
compiled_re = re.compile(r"r[ua]n")  #compile就是先把正则表达式r""编译到comiled_re
print(compiled_re.search("dog ran to cat"))  #可以再用comiled_re来search
print('16_compile\n')

