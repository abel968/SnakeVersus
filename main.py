#encoding:utf-8
import gamecontroller_mod

gc = gamecontroller_mod.Gamecontroller()
flag = 0        #为1时表示user赢了  为2时表示AI赢了
while not flag:
    direction = raw_input(u'请输入方向：')
    if direction == 'w':
        if gc.usersnake.up() == None:
            continue
    elif direction == 's':
        if gc.usersnake.down() == None:
            continue
    elif direction == 'a':
        if gc.usersnake.left() == None:
            continue
    elif direction == 'd':
        if gc.usersnake.right() == None:
            continue
    print u'当前用户蛇所占据位置为：' + str(gc.getUserHold())
    if not gc.isAIOver():
        flag = 1
        break
    gc.AIChoose()
    print u'当前AI蛇所占据位置为：' + str(gc.getAIHold())
    if not gc.isUserOver():
        flag = 2
        break
if flag == 1:
    print u'你赢了'
else:
    print u'你输了'
