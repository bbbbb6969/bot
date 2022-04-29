import random
manu={'飯糰':30,'豆漿':15,'奶茶':20,'蛋餅':25,'漢堡':35,'1號餐':45}
manu1=['飯糰','豆漿','奶茶','蛋餅','漢堡','1號餐']
manu2=[]
list=[]
for a in manu:
    print(a,manu[a],'元')
print('1號餐:漢堡+豆漿')

while (True):
    i=input('請輸入你要的餐點: ')
    manu2.append(i)
    if i=='不知道吃啥':
        j=random.choice(manu1)
        print('我推薦你吃',j,manu[j],'元')
        list.append(manu[j])
        break
    else:
        print(manu[i],'元')
        k=input('是否繼續點餐?')
        if k=='y':
            continue
        elif k=='n':
            for c in manu2:
                list.append(manu[c])
            print('一共是',sum(list),'元')
            break
        else:
            print('從頭再一次')
            list.clear()
            continue
money=int(input('請輸入你給的錢: '))
total=sum(list)
if money<total:
    print('錢不夠')
else:
    print('找你',money-total,'元，多謝惠顧!')