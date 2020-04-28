
msg = "Hello World"
print("msg")



#2020/4/3-
s = "he\nllo wor\tld"
html ="""<html>
<body></body>
</html>"""
print(s)
print(html)

pi = 3.141592
diameter = 12756.274
print( pi*diameter ) 

cal_per_1kg = 7200
cal_per_1minjog = 7.76
min_to_lose1kg = cal_per_1kg / cal_per_1minjog

hours_to_lose1kg = min_to_lose1kg / 60
print(hours_to_lose1kg)

day = 24
str_day =str(day)
date = str_day+"日"
print(date)

int("200")
float("3.14159265358979")

monk_fish_team = [158, 157, 163, 157, 145]

total = sum(monk_fish_team)
length = len(monk_fish_team)
mean = total/length
variance = 0

for height in monk_fish_team:
    variance += (height-mean)**2

variance = variance/length
print(variance)

print(variance**0.5)

volleyball_team = [143, 167, 170, 165]

total2 =sum(volleyball_team)
length2 =len(volleyball_team)
mean2 = total2/length2
variance2 = 0

for height in volleyball_team:
    variance2 += (height-mean2)**2

variance2 = variance2/length2
print(variance2**0.5)

for cnt in range(10):
    print(cnt)

savings = 100
for i in range(15):
    savings += savings*0.05
print(savings)

if 1 ==1:
    print("1番目はtrue")
if 5^(4-4)+9 ==10:
    print("2番目はtrue")
if 2< len([0, 1, 2]):
    print("3番目はtrue")
if sum([1, 2, 3, 4])<10:
    print("4番目はtrue")

    a_year = 2080
    if a_year >= 1993:
        if a_year ==1993:
            print(a_year,"年、れに誕生")
        else:
            print(a_year,"年、れに",a_year-1993,"歳")


purple = {"ニックネーム":"れにちゃん",
          "出身地":"神奈川県",
          "キャッチフレーズ":"感電少女"}
print(purple["出身地"])
print(purple)

purple["キャッチフレーズ"] = "鋼少女"
print(purple)
purple["生年月日"] = "1993年6月21日"
print(purple)
del purple["ニックネーム"]
print(purple)
def convert_number(num):
    #アラビア数字とローマ数字の対応表をディクショナリに定義
    roman_nums = {1:"Ⅰ",2:"Ⅱ",3:"Ⅲ",4:"Ⅳ",5:"Ⅴ",
                  6:"Ⅵ",7:"Ⅶ",8:"Ⅷ",9:"Ⅸ" }
    #ディクショナリのキーとして引数の整数が存在していたら
    #キーに対応する値を戻り値にする
    if num in roman_nums:
        return roman_nums[num]
    else:
        return "[変更できません]"

prime = {2,3,5,7,13,17}
fib = {1,1,2,3,5,8,13}

prime_fib = prime | fib
print(prime_fib)

dice = {1,2,3,4,5,6}
even = {2,4,6,8,10}

odd_dice = dice - even
print(odd_dice)

prefs = {"北海道","青森","秋田","岩手"}
capitals = {"札幌","青森","秋田","盛岡"}

pref_cap = prefs & capitals
print(pref_cap)

pref_cap2 = prefs^capitals
print(pref_cap2)

codon = ["ATG","GGC","TCC","AAG","TTC","TGG","GAC","TCC"]
s_codon = set(codon)
print(len(codon),len(s_codon))


