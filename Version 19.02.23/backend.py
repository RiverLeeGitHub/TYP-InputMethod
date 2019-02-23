#coding:utf8

print("hello world!")
dictionary=['amazon','arizona',
            'berkeley','beijing',
            'colorado','catty',
            'dalian','dumpling',
            'email','embarrassment',
            'foshan','florida',
            'georgia','google',
            'happy','horrible',
            'ice','illness',
            'jackson','jiangli',
            'knowledge','keep',
            'loop','lean',
            'mississippi','massachusetts',
            'number','nosql',
            'oppress','original',
            'puppy','polish',
            'queen','query',
            'residence','roll',
            'shanghai','shenzhen',
            'taiwan','tornado',
            'universe','union',
            'virginia','victory',
            'wuhan','which',
            'xavier','x-ray',
            'yahoo','yummy',
            'zigzag','zhongguo']

dictionary=[(i,word) for (i,word) in enumerate(dictionary)]


import os
import curses
#初始化curses
screen=curses.initscr()
#设置不回显
curses.noecho()
#设置不需要按回车立即响应
curses.cbreak()
#开启键盘模式
screen.keypad(1)

#阻塞模式读取0 非阻塞 1
screen.nodelay(0)

line = ""
candidates = []

def get_candidate_words(next_available_pool):
    candidate_words=[]
    for (i,_) in next_available_pool:
        candidate_words.append(dictionary[i][1])
    return candidate_words


def execute(line,current_available_pool):

    next_available_pool = []  ## store cut words

    while True:
        order=screen.getch()## Get the ASCII code of the input

        char=chr(order)## transform ASCII into character

        os.system('clear')## clear the console
        if order == 127:## if input is backspace
            line= line[:-1]
            return False
        elif order == 10:## if input is return
            print ("return")
        else:## if input is an alphabet
            line += char

            next_available_pool_backup=next_available_pool
            next_available_pool=[]
            for (i,word) in current_available_pool:
                if char in word:
                    cut_word=word[word.find(char)+1:]## only contain the rest of the word to limit search
                    next_available_pool.append((i, cut_word))



            os.system("echo " + line)
            #print ("查询池：",next_available_pool)
            print ("候选词：",get_candidate_words(next_available_pool))

            outcome=execute(line,next_available_pool)
            if outcome==False:## if user typed backspace justnow, then return to the former state
                return

            os.system("echo " + line)
            #print ("查询池：",next_available_pool)
            print ("候选词：",get_candidate_words(next_available_pool))

            current_available_pool=next_available_pool## the candidate pool should changed according to the already typed alphabets


while True:
    execute(line, current_available_pool = dictionary)



# #恢复控制台默认设置（若不恢复，会导致即使程序结束退出了，控制台仍然是没有回显的）
# curses.nocbreak()
# screen.keypad(0)
# curses.echo()
# #结束窗口
# curses.endwin()