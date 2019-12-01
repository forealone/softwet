# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:48:21 2019
@author: WangZheng
"""

import random
import tkinter as tk

#定义洗牌函数
def shuffle():
    global deck
    global maxcards
    deck = ['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,
            10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K']
    n=0
    while n<=2:
        deck.extend(deck)
        n = n+1
    maxcards = len(deck)
    print('洗牌...')
    
#定义发牌函数
def drawcard():
    global maxcards
    x = random.randint(0,maxcards-1)
    card = deck[x]
    maxcards = maxcards - 1
    deck.pop(x)
    return card

def draw4card():
    global player_card1
    global banker_card1
    global player_card2
    global banker_card2
    player_card1 = drawcard()
    banker_card1 = drawcard()
    player_card2 = drawcard()
    banker_card2 = drawcard()
    print('庄家%s&%s \n VS \n闲家%s&%s' %(banker_card1,banker_card2,player_card1,player_card2))
    print('（当前8副牌还剩余%s张）' %maxcards)
    text1 = ('庄家%s&%s VS 闲家%s&%s' %(banker_card1,banker_card2,player_card1,player_card2))
    text2 = ('（当前8副牌还剩余%s张）' %maxcards)
    return text1, text2

#定义卡牌数字转换
def convert(card):
    if card == 'K':
        card_num = 0
        return card_num
    elif card =='Q':
        card_num = 0
        return card_num
    elif card =='J':
        card_num = 0
        return card_num
    elif card =='A':
        card_num = 1
        return card_num
    else:
        card_num = card
        return card_num

#定义庄家闲家最终点数
def count():
    global banker
    global player
    global player_card1
    global banker_card1
    global player_card2
    global banker_card2
    if banker_card1 == banker_card2:
        print('庄家一对！') 
        text_b = '庄家一对！'
    else:
        text_b = ''
    if player_card1 == player_card2:
        print('闲家一对！')
        text_p = '闲家一对！'
    else:
        text_p = ''
    banker = convert(banker_card1)+convert(banker_card2)
    player = convert(player_card1)+convert(player_card2)
    while banker >= 10:
        banker = banker - 10
    while player >= 10:
        player = player - 10
    print('庄家当前%s点，闲家当前%s点' %(banker,player))
    result = ('庄家当前%s点，闲家当前%s点' %(banker,player))
    result2 = ('%s              %s' %(text_b,text_p))
    return result, result2

#定义补牌规则
def draw_again():
    global banker
    global player
    global player_card1
    global banker_card1
    global player_card2
    global banker_card2
    global player_card3
    global banker_card3
    if (player >= 8) | (banker >= 8):
        print('一方有8或9，比大小')
        result = ('一方有8或9，比大小')
        result2,result3,result4,result5,result6,result7 = '','','','','',''
    elif (player >= 6) & (banker >=6):
        print('两边均大于等于6，比大小')
        result = ('两边均大于等于6，比大小')
        result2,result3,result4,result5,result6,result7 = '','','','','',''
    elif (player >= 6) & (banker <6):
        banker_card3 = drawcard()
        print('闲家大于等于6，庄家小于6，庄家补牌！ \n 庄家%s&%s&%s VS 闲家%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2))
        print('(当前8副牌还剩余%s张)' %maxcards)
        result = ('闲家大于等于6，庄家小于6，庄家补牌！')
        result2 = ('庄家%s&%s&%s VS 闲家%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2))
        result3 = ('(当前8副牌还剩余%s张)' %maxcards)
        result4,result5,result6,result7 = '','','',''        
        banker = banker+convert(banker_card3)
        while banker >= 10:
            banker = banker - 10
    elif (player < 6) &(banker <= 7):
        player_card3 = drawcard()
        print('闲家小于6（庄家小于等于7），闲家补牌！ \n 庄家%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,player_card1,player_card2,player_card3))
        print('(当前8副牌还剩余%s张)' %maxcards)
        result = ('闲家小于6（庄家小于等于7），闲家补牌！')
        result2 = ('庄家%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,player_card1,player_card2,player_card3))
        result3 = ('(当前8副牌还剩余%s张)' %maxcards)
        result4,result5,result6,result7 = '','','',''
        player = player+convert(player_card3)
        while player >= 10:
            player = player - 10
        if (banker == 6) & (convert(player_card3) >= 6) & (convert(player_card3) <= 7):
            print('庄家当前%s点，闲家当前%s点' %(banker,player))
            banker_card3 = drawcard()
            print('庄家6点，闲家补牌6或7，庄家补牌！ \n 庄家%s&%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2,player_card3))
            print('(当前8副牌还剩余%s张)' %maxcards)
            result4 = ('庄家当前%s点，闲家当前%s点' %(banker,player))
            result5 = ('庄家6点，闲家补牌6或7，庄家补牌！')
            result6 = ('庄家%s&%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2,player_card3))
            result7 = ('(当前8副牌还剩余%s张)' %maxcards)
            banker = banker+convert(banker_card3)
            while banker >= 10:
                banker = banker - 10
        elif (banker == 5) & (convert(player_card3) >= 4) & (convert(player_card3) <= 7):
            print('庄家当前%s点，闲家当前%s点' %(banker,player))
            banker_card3 = drawcard()
            print('庄家5点，闲家补牌4~7，庄家补牌！ \n 庄家%s&%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2,player_card3))
            print('(当前8副牌还剩余%s张)' %maxcards)
            result4 = ('庄家当前%s点，闲家当前%s点' %(banker,player))
            result5 = ('庄家5点，闲家补牌4~7，庄家补牌！')
            result6 = ('庄家%s&%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2,player_card3))
            result7 = ('(当前8副牌还剩余%s张)' %maxcards)
            banker = banker+convert(banker_card3)
            while banker >= 10:
                banker = banker - 10
        elif (banker == 4) & (convert(player_card3) >= 2) & (convert(player_card3) <= 7):
            print('庄家当前%s点，闲家当前%s点' %(banker,player))
            banker_card3 = drawcard()
            print('庄家4点，闲家补牌2~7，庄家补牌！ \n 庄家%s&%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2,player_card3))
            print('(当前8副牌还剩余%s张)' %maxcards)
            result4 = ('庄家当前%s点，闲家当前%s点' %(banker,player))
            result5 = ('庄家4点，闲家补牌2~7，庄家补牌！')
            result6 = ('庄家%s&%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2,player_card3))
            result7 = ('(当前8副牌还剩余%s张)' %maxcards)
            banker = banker+convert(banker_card3)
            while banker >= 10:
                banker = banker - 10
        elif (banker == 3) & (convert(player_card3) <= 7) | (convert(player_card3) == 9):
            print('庄家当前%s点，闲家当前%s点' %(banker,player))
            banker_card3 = drawcard()
            print('庄家3点，闲家补牌不是8，庄家补牌！ \n 庄家%s&%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2,player_card3))
            print('(当前8副牌还剩余%s张)' %maxcards)
            result4 = ('庄家当前%s点，闲家当前%s点' %(banker,player))
            result5 = ('庄家3点，闲家补牌不是8，庄家补牌！')
            result6 = ('庄家%s&%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2,player_card3))
            result7 = ('(当前8副牌还剩余%s张)' %maxcards)
            banker = banker+convert(banker_card3)
            while banker >= 10:
                banker = banker - 10
        elif (banker <= 2):
            print('庄家当前%s点，闲家当前%s点' %(banker,player))
            banker_card3 = drawcard()
            print('庄家2点及以下，庄家补牌！ \n 庄家%s&%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2,player_card3))
            print('(当前8副牌还剩余%s张)' %maxcards)        
            result4 = ('庄家当前%s点，闲家当前%s点' %(banker,player))
            result5 = ('庄家2点及以下，庄家补牌！')
            result6 = ('庄家%s&%s&%s VS 闲家%s&%s&%s' %(banker_card1,banker_card2,banker_card3,player_card1,player_card2,player_card3))
            result7 = ('(当前8副牌还剩余%s张)' %maxcards)
            banker = banker+convert(banker_card3)
            while banker >= 10:
                banker = banker - 10
        else:        
            print('庄家不再补牌')
            result4 = ('庄家当前%s点，闲家当前%s点' %(banker,player))
            result5 = ('庄家不再补牌')
            result6,result7 = '',''
    else:
        print('应该没有其他情况了，如果有，是BUG')
        result = ('补牌规则有误，需修改代码')
        result2,result3,result4,result5,result6,result7 = '','','','','',''
    return result,result2,result3,result4,result5,result6,result7
    
#定义比大小函数
def compare():
    global banker
    global player
    if banker > player:
        print('最终点数：庄家 %s 点 VS 闲家 %s 点，庄家赢！' %(banker,player))
        result = ('最终点数：庄家 %s 点 VS 闲家 %s 点，庄家赢！' %(banker,player))
    elif banker < player:
        print('最终点数：庄家 %s 点 VS 闲家 %s 点，闲家赢！' %(banker,player))
        result = ('最终点数：庄家 %s 点 VS 闲家 %s 点，闲家赢！' %(banker,player))
    else:
        print('最终点数：庄家 %s 点 VS 闲家 %s 点，平局！' %(banker,player))
        result = ('最终点数：庄家 %s 点 VS 闲家 %s 点，平局！' %(banker,player))
    return result

#定义牌库是否还够发牌
def another_game():
    if maxcards <=6:
        shuffle()
        print('（8副牌已发完，重新洗牌）')
        result = ('（8副牌已发完，重新洗牌）')        
    else:
        print('（牌库还有6张牌以上，继续下一回合发牌）')
        result = ('（牌库还有6张牌以上，继续下一回合发牌）')
    return result

#以上是基本工能的函数定义

#洗牌，游戏开始
window = tk.Tk()
window.title('Baccarat!')
window.geometry('1024x768')

var1 = tk.StringVar()
deck_count = 0
def hit_shuffle():
    global deck_count
    deck_count += 1
    shuffle()
    var1.set('游戏开始，洗牌...第%s局洗牌' %deck_count)

button1 = tk.Button(window,text='洗牌',  font=('宋体', 12), width=20, height=1,command=hit_shuffle)
button1.pack()

label1 = tk.Label(window, textvariable=var1, font=('宋体', 12), bg='green', fg='white', width=30, height=2)
label1.pack()

#发4张牌
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
var5 = tk.StringVar()

def hit_draw_and_count():
    tuple1 = draw4card()
    var2.set(tuple1[0])  #展示4张牌
    var3.set(tuple1[1])
    tuple2 = count()
    var4.set(tuple2[0])  #展示两张牌当前点数
    var5.set(tuple2[1])
    
button2 = tk.Button(window,text='发牌',  font=('宋体', 12), width=20, height=1,command=hit_draw_and_count)
button2.pack()

label2 = tk.Label(window, textvariable=var2, font=('宋体', 12), bg='green', fg='white', width=30, height=2)
label2.pack()
label3 = tk.Label(window, textvariable=var3, font=('宋体', 9), bg='green', fg='white', width=25, height=2)
label3.pack()

label4 = tk.Label(window, textvariable=var4, font=('宋体', 12), bg='green', fg='white', width=40, height=2)
label4.pack()
label5 = tk.Label(window, textvariable=var5, font=('宋体', 12), bg='green', fg='white', width=40, height=2)
label5.pack()




#判断是否补牌
var6 = tk.StringVar()
var7 = tk.StringVar()
var8 = tk.StringVar()
var9 = tk.StringVar()
var10 = tk.StringVar()
var11 = tk.StringVar()
var12 = tk.StringVar()

def hit_draw_again():
    tuple1 = draw_again()
    var6.set(tuple1[0])  #展示补牌相关信息
    var7.set(tuple1[1])
    var8.set(tuple1[2])
    var9.set(tuple1[3])
    var10.set(tuple1[4])
    var11.set(tuple1[5])
    var12.set(tuple1[6])

    
button3 = tk.Button(window,text='补牌',  font=('宋体', 12), width=20, height=1,command=hit_draw_again)
button3.pack()

label6 = tk.Label(window, textvariable=var6, font=('宋体', 9), bg='green', fg='white', width=40, height=2)
label6.pack()
label7 = tk.Label(window, textvariable=var7, font=('宋体', 12), bg='green', fg='white', width=30, height=2)
label7.pack()
label8 = tk.Label(window, textvariable=var8, font=('宋体', 9), bg='green', fg='white', width=30, height=2)
label8.pack()
label9 = tk.Label(window, textvariable=var9, font=('宋体', 9), bg='green', fg='white', width=40, height=2)
label9.pack()
label10 = tk.Label(window, textvariable=var10, font=('宋体', 12), bg='green', fg='white', width=30, height=2)
label10.pack()
label11 = tk.Label(window, textvariable=var11, font=('宋体', 9), bg='green', fg='white', width=30, height=2)
label11.pack()
label12 = tk.Label(window, textvariable=var12, font=('宋体', 9), bg='green', fg='white', width=30, height=2)
label12.pack()



#比大小

var13 = tk.StringVar()
var14 = tk.StringVar()
def hit_compare():
    var13.set(compare())
    var14.set(another_game())  #将来可优化一下，牌库不足6张时给窗口提示，重新发牌

button4 = tk.Button(window,text='比大小',  font=('宋体', 12), width=20, height=1,command=hit_compare)
button4.pack()

label13 = tk.Label(window, textvariable=var13, font=('宋体', 9), bg='green', fg='white', width=40, height=2)
label13.pack()
label14 = tk.Label(window, textvariable=var14, font=('宋体', 9), bg='green', fg='white', width=40, height=2)
label14.pack()


canvas = tk.Canvas(window, bg='green', height='200', width='150')
image_file = tk.PhotoImage(file='F:\My_python\KoC.jpg')
image = canvas.create_image(75, 0, anchor='n',image=image_file)
canvas.pack()

window.mainloop()
