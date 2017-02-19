# -*- coding: utf-8 -*-
from snake import Snake
import math
#AI类是snake的子类，别的与snake类相同，增添了估分方法cal  和选择方向方法 choose
class AI(Snake):
    def __init__(self):
        self.step = 1
        self.hold = [399]
    def cal(self, newAIHead, *snake_hold):
        snake_hold1 = [x for x in snake_hold[0][0]]     #将参数转换为列表
        q = []    #q模拟一个队列
        l = 0   #l模拟指针
        dist=[0 for x in range(20*20)]     #dist表示距离矩阵
        type=[0 for x in range(20*20)]     #type表示该点属于user还是AI的矩阵
        q.append(snake_hold1[-1])
        q.append(newAIHead)
        type[q[0]] = 1      #user先到达的点用1表示
        type[q[1]] = 2      #AI先到达的点用2表示
        t = [20, -20, -1, 1]  # 下上左右
        while l<q.__len__() and q.__len__() < 100:
            x = q[l]        #x为当前的点
            for i in range(4):
                # 首先判断往各方向是否出界
                if (i == 0 and x >= 380 and x <= 399):
                    continue
                elif (i == 1 and x >= 0 and x <= 20):
                    continue
                elif (i == 2 and x in [20 * x for x in range(20)]):
                    continue
                elif (i == 3 and x in [19 + 20 * x for x in range(20)]):
                    continue
                xx = x + t[i]
                #判断xx是否被占据
                if xx in snake_hold or xx in self.hold or xx == newAIHead:
                    continue
                if type[xx] != 0:
                    continue
                dist[xx] = dist[x] + 1
                type[xx] = type[x]
                q.append(xx)
            l+=1
        #计算分数
        summary = 0
        for i in range(20*20):
            if dist[i] == 0:
                continue
            if type[i] == 1:
                summary -= 1/math.sqrt(dist[i])
            else:
                summary += 1/math.sqrt(dist[i])

        return summary

    def choose(self, *snake_hold):
        t = [20, -20, -1, 1]     #下上左右
        direction = -1
        val = -2e9
        for i in range(4):
            #首先判断往各方向是否出界
            if (i == 0 and self.hold[-1] >=380 and self.hold[-1] <= 399):
                continue
            elif (i == 1 and self.hold[-1] >= 0 and self.hold[-1] <= 20):
                continue
            elif (i == 2 and self.hold[-1] in [20*x for x in range(20)]):
                continue
            elif (i == 3 and self.hold[-1] in [19+20*x for x in range(20)]):
                continue
            newAIHead = self.hold[-1] + t[i]
            if newAIHead in snake_hold or newAIHead in self.hold:
                continue
            try_val = self.cal(newAIHead, snake_hold)
            if try_val > val:
                val = try_val
                direction = i
        if direction == -1:
            print 'You win'
            return None
        elif direction == 0:
            return self.down()
        elif direction == 1:
            return self.up()
        elif direction == 2:
            return self.left()
        elif direction == 3:
            return self.right()