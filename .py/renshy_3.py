tank_data = [('IV号気戦車',38,80,75),('LT-38',42,50,37),
             ('八九式中戦車',20,17,57),('ⅠⅠⅠ号突撃砲',40,50,75),
             ('M3中戦車',39,51,75)]

tank_data.sort(key=lambda tup:sum(tup[1:4]),reverse=True)

#print(tank_data)

monk_fish_team = [158,157,163,157,145]

total = sum(monk_fish_team)
length = len(monk_fish_team)
mean = total/length

variance = sum([(height-mean)**2 for height in monk_fish_team])/length

#print(variance)

str_speeds ="38 42 20 40 39"
speeds = [int(s) for s in str_speeds.split()]
#print(speeds)

tz = {"GMT":"+000","BST":"+100","EET":"+200","JST":"+900"}

revtz = {off:zone for zone, off in tz.items()}
#print(revtz)

names = ["BOB","burton","dave","bob"]
unames = {x.lower() for x in names}
#print(unames)

def excecute(func, arg):
    return func(arg)
#print(excecute(int,"100"))
