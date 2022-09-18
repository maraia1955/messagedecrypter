n = int(input())
import re
de_str = ""
pattern1 = r'(\$[A-Za-z]+\$\:\s)(\[\d+\])\|(\[\d+\])\|(\[\d+\])\|'
pattern2 = r'(\%[A-Za-z]+\%\:\s)(\[\d+\])\|(\[\d+\])\|(\[\d+\])\|'
for i in range(n):
    my_string = input()
    match = re.findall(pattern1,my_string)
    if match:
        ä = ""
        b = "["
        c = "]"
        print(match[1])
        n1 = match[1].replace(b,a)
        n2 = n1.replace(c,a)
        de_str = de_str + chr(int(n2))
        n1 = match[2].replace(b,a)
        n2 = n1.replace(c,a)
        de_str = de_str + chr(int(n2))
        n1 = match[3].replace(b,a)
        n2 = n1.replace(c,a)
        de_str = de_str + chr(int(n2))
        print(de_str)

 
    

