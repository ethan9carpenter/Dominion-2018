'''from writersAndPrinters import printWithTabs
for year in range(2005, 2013):
    printWithTabs(year)
    print()'''
    
import re

lines = ("    6/4/2018 1 $ 1,125 $ 1,125 $ 791 $ 104 $ 895 Other Change of Unit 21225    ",
"    6/4/2018 2 $ 1,411 $ 1,411 $ 1,243 $ 123 $ 1,366  New Admission 21212     ",
"    •6/5/2018 1 $ 1,125 1,125 $ 1,052 $ 61 $ 1,113 New Admission 21216 .    ",
"    6/6/2018 0 $ 918 $ 918 $ 474 $ - $ 509 .., New Admission 21202    ",
"    •6/7/2018 1 $ 1,125 $ 1,125 $ 930 $ 61 $ 991 New Admission 21215 •    ",
"    . 6/7/2018 $ 1,125 $ 1,125 $ 1,100 $ - $ 1,100 New Admission 21217    ",
"    6/7/2018 1 $ 1,125 1,125 $ 865 $ 122 987 New Admission 21216    ",
"    6/8/2018 3 $ 1,815 1,815 $ 1,204 $ 249 $ 1,453 Other Change of Unit 21205    ",
"    6/11/2018 1 $ 1,125 $ 1,125 872 $ 113 $ 985  Other Change of Unit 21224    ",
"    6/11/2018  $ 1,125 $ 1,125 $ 865  $ 122 $ 987 New Admission 21216    ",
"    6/11/2018 1 $ 1,125 $ 1,125 $ 865 $ 122 987 New Admission 21216    ",
"    6/11/2018 1 $ 1,125 $ 1,125 $ 925 $ 103 $ 1,028 New Admission 21218    ",
"    6/12/2018 2 $ 1,411  $ 1,411 $ 953 $ 206 $ 1,159 Other Change of Unit 21223    ",
"    6/14/2018 1 $ 1,125 $ 1,125 $ 850 192 $ 1,042 ... New Admission 21215    ",
"    6/18/2018  $ 1,125 $ 1,125 $ 1,050  $ 96 $ 1,146 New Admission 21201    ",
"    6/19/2018 0 $ 918 $ 918 $ 900 $ - 900 New Admission 21217    ",
"    7/1/2018 2 $ 1,411 1,411 $ 800 $ 169 , $ 969  Other Change of Unit 21202 i    ",
"    I 2/20/2018 1 $ 1,125 $ 1,125 $ 872 $ 113 $ 985 ' New Admission 21224 .    ",
"    ' 2/20/2018  1 $ 1,125 $ 1,125 $ 950 $ - $ 950 , Other Change of Unit  21216    ",
"    2/20/2018 1 $ 1,125 $ 1,125 $ 800 $ 122 $ 922 New Admission 21230    ",
"    2/21/2018 1 $ 1,125 $ 1,125 $ 1,030 $ 193 $ 1,223 New Admission  21218    ",
"    2/21/2018 3 $ 1,815 $ 1,815 $ 1,355 $ 148 $ 1,503 New Admission   21224    ",
"    . 2/22/2018 3 $ 1,815 $ 1,815 $ 1,276 148 $ 1,424 Other Change of Unit 21215    ",
"    , 2/23/2018 1 $ .1,125 $ 1,125  $ 866 122 $ 988 Other Change of Unit 21201    ",
"    , 2/23/2018 i 1 1 $ 1,125 $ 1,125 $ 760 $ 95 $ 855 New Admission 21217    ",
"    2/23/2018  2  $ 1,411 $ 1,411 $ 1,203 $ 216 $ 1,419 Portability Move-in 21224    ",
"    ! 2/23/2018 2 $ 1,411 $ 1,411 $ 1,100 $ 123 $ 1,223 Other Change of Unit 21229    ",
"    2/26/2018 3 $ 1,815 $ 1,815 $ 1,088 $ 249 $ 1,337 New Admission  , 21215    ",
"    3/1/2018 0 $ 918 $ 918 $ 474 $ - $ 509 New Admission , 21202    ",
"    3/1/2018 1 $ 1,125 $ 1,125 $ 858 $ 95 $ 953 Other Change of Unit 21215    ",
"    3/1/2018 1 $ 1,125 $ 1,125 $ 885 $ 95 1 $ 980 Other Change of Unit 21218    ",
"    3/1/2018 1 $ 1,125 $ 1,125 $ 821 $ 95 $ 916 Other Change of Unit 21234    ",
"    3/1/2018 1 , $ 1,125 $ 1,125 $ 900 $ 103 $ 1,003 Other Change of Unit 21202    ",
"    3/1/2018 1 $ 1,125 $ 1,125 $ 899 $ 95 $ 994 Other Change of Unit 21230     ",
"    3/1/2018 1 . $ 1,125 $ 1,125 $ 844 $ 175 $ 1,019 Other Change of Unit 21205    ",
"    3/1/2018 $ 1,125 $ 1,125 $ 1,100 $ - $ 1,100 Other Change of Unit 21217 :    ",
"    3/1/2018 1 $ 1,125 $ 1,125 $ 966 $ 174 $ 1,140 Other Change of Unit 21230     ",
"    3/1/2018 I 1 $ 1,125 $ 1,125 $ 794 I $ 104 $ 898 Other Change of Unit  21217 :    ",
"    3/1/2018 1 ' $ 1,125 $ 1,125 $ 850 1 $ 103 $ 953 Other Change of Unit : 21212    ",
"    3/1/2018 1 $ 1,125 $ 1,125 $ 807 $ 95  $ 902 Other Change of Unit ' 21213    ",
"    3/1/2018 1 $ 1,125 $ 1,125 $ 850 $ - 0 $ 850 Other Change of Unit 21205    ",
"    3/1/2018 1 $ 1,125$ 1,125 $ 924 $ 103 $ 1,027 Other Change of Unit 21213    ",
"    . 3/1/2018 2 $ 1,411 $ 1,411 $ 1,217 . $ 215 $ 1,432 Other Change of Unit 21216    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,075 123 $ 1,198 Other Change of Unit . 21215    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,206 215 $ 1,421 New Admission 21213    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,275 $ 206 $ 1,481 Other Change of Unit 21213    ",
"    3/1/2018 ', 2 $ 1,411 1 $ 1,411 $ 907 $ 206 $ 1,113 Other Change of Unit 21223    ",
"    3/1/2018 2 $ 1,411 I $ 1,411 $ 1,020 $ 123 $ 1,143 New Admission j 21206    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,197  $ 156 $ 1,353 1 Other Change of Unit 21217    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,208 $ 123 $ 1,331. Other Change of Unit 21206    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 805 $ 157 $ 962 Other Chan me of Unit 21223    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,254 $ 157 $ 1,411 Other Change of Unit 21201    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,069 $ 206 $ 1,275 Other Change of Unit 21216 .    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,178 $ 215 $ 1,393 Other Change of Unit 21224    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,250 $ 206 $ 1,456 Other Change of Unit 21213    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,205 $ 123 $ 1,328 Other Change of Unit ;: 21208 .    ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,280 $ 123 $ 1,403 Other Change of Unit  21212     ",
"    3/1/2018 2 $ 1,411 $ 1,411 $ 1,187 $ 206 $ 1,393 Other Change of Unit 21218     ",
"    3/1/2018  2  $ 1,411 $ 1,411 $ 1,030 $  206 $ 1,236 Other Change of Unit 21223]    ",
"    3/1/2018 0 $ 918 $ 918 $ 615 $ 96 $ 711 Other Change of unit 21229    ",
"    3/1/2018 1 $ 1,125 $ 1,125 $ 900 $ 166 $ 1,066 New Admission 21215    ")

for line in lines:
    line = re.split(' ', line)
    newLine = []
    banned = ('', '$', 'Change', 'of', 'Unit', 'Admission', '.', ',', '...', "'")
    for word in line:
        if word not in banned:
            newLine.append(word)
    line = ""
    for word in newLine:
        line += word + "\t"
    print(line)

