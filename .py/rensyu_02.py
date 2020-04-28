month_names = ("January","February","March","April","May","June","July")
print(month_names[1])

month_names = month_names + ("August","September","October","November","December")
print(month_names[11])


from random import randint
hands = {0:"グー",1:"チョキ",2:"パー"}
rules ={(0,0):"あいこ",(0,1):"勝ち",(0,2):"負け",
        (1,0):"勝ち",(1,1):"あいこ",(1,2):"負け",
        (2,0):"勝ち",(2,1):"負け",(2,2):"あいこ"}

        ###  本当は True
        #     
        ###

while False:    
    pc_hand = randint(0,2)
    user_hand_str = input("0:グー 1:チョキ 2:パー 3:やめる")
    if user_hand_str == "3":
        break
    if user_hand_str not in ("0","1","2"):
        continue
    user_hand = int(user_hand_str)
    print("あなた"+hands[user_hand] +"、コンピュータ："+hands[pc_hand])

    print(rules[(user_hand,pc_hand)])

   def func():
       words = """ゆく河の流れは絶えずして￥nしかももとの水にあらず"""
       print(words)
   func()
