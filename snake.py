
class Snake:
    def __init__(self):
        self.step = 1       #the number of steps
        self.hold = [0]      #the list of the number which is held
    def down(self):          #if can't move, return None
        cur = self.hold[-1]
        if cur >=380 and cur<=399:
            return None
        else:
            self.step += 1
            cur += 20
            if cur in self.hold:
                return None
            else:
                self.hold.append(cur)
                if self.step > 5 and self.step % 5 != 0:
                    del self.hold[0]
        return self.hold
    def up(self):
        cur = self.hold[-1]
        if cur >= 0 and cur <= 20:
            return None
        else:
            self.step += 1
            cur -= 20
            if cur in self.hold:
                return None
            else:
                self.hold.append(cur)
                if self.step > 5 and self.step % 5 != 0:
                    del self.hold[0]
        return self.hold
    def left(self):
        cur = self.hold[-1]
        if cur in [20*x for x in range(20)]:
            return None
        else:
            self.step += 1
            cur -= 1
            if cur in self.hold:
                return None
            else:
                self.hold.append(cur)
                if self.step > 5 and self.step % 5 != 0:
                    del self.hold[0]
        return self.hold
    def right(self):
        cur = self.hold[-1]
        if cur in [19+20*x for x in range(20)]:
            return None
        else:
            self.step += 1
            cur += 1
            if cur in self.hold:
                return None
            else:
                self.hold.append(cur)
                if self.step > 5 and self.step % 5 != 0:
                    del self.hold[0]
        return self.hold
snake = Snake()
while True:
    m = raw_input('the direction:')
    if m == 's':
        if(snake.down() == None):
            print 'Defeat'
            break
    elif m == 'w':
        if (snake.up() == None):
            print 'Defeat'
            break
    elif m == 'a':
        if (snake.left() == None):
            print 'Defeat'
            break
    elif m == 'd':
        if (snake.right() == None):
            print 'Defeat'
            break
    print snake.hold