# -*- coding: utf-8 -*-
import snake
import ai_mod

class Gamecontroller:
    def __init__(self):
        self.usersnake = snake.Snake()
        self.aisnake = ai_mod.AI()
    def reset(self):
        self.usersnake.__init__()
        self.aisnake.__init__()
    def isAIOver(self):
        x = self.aisnake.hold[-1]
        t = [20, -20, -1, 1]  #up,down,left,right
        flag = False    #not find a direction
        for i in range(4):
            # 首先判断往各方向是否出界
            if (i == 0 and x >= 380 and x <= 399):
                continue
            elif (i == 1 and x >= 0 and x <= 19):
                continue
            elif (i == 2 and x in [20 * n for n in range(20)]):
                continue
            elif (i == 3 and x in [19 + 20 * n for n in range(20)]):
                continue
            xx = x + t[i]
            # 判断xx是否被占据
            if xx in self.aisnake.hold or xx in self.usersnake.hold:
                continue
            flag = True
            break
        #flag为Ture时表示未结束
        return flag

    #判断用户蛇是否无路可走
    def isUserOver(self):
        x = self.usersnake.hold[-1]
        t = [20, -20, -1, 1]  # 下上左右
        flag = False  # 未找到一个可行的方向
        for i in range(4):
            # 首先判断往各方向是否出界
            if (i == 0 and x >= 380 and x <= 399):
                continue
            elif (i == 1 and x >= 0 and x <= 19):
                continue
            elif (i == 2 and x in [20 * n for n in range(20)]):
                continue
            elif (i == 3 and x in [19 + 20 * n for n in range(20)]):
                continue
            xx = x + t[i]
            # 判断xx是否被占据
            if xx in self.aisnake.hold or xx in self.usersnake.hold:
                continue
            flag = True
            break
        # flag为True时表示未结束
        return flag

    def AIChoose(self):
        self.aisnake.choose(self.getUserHold())
    def getUserHold(self):
        return self.usersnake.hold
    def getAIHold(self):
        return self.aisnake.hold