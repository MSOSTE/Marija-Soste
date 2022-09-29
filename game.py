
hp = 999
def shoot(damage):
    global hp
    hp -= damage
    print('You dealt damage of {damage}')
    return hp

def game_over(name):
    print('Game over ' + name)

name = 'Marija'
def fly_left():
    print('You moved left')

def fly_right():
    print('You moved right')

def fly_forward():
    print('You moved forward')


if __name__ =='__main__':
    fly_left()
    shoot(9)
    fly_forward()
    fly_right()
    game_over('Marija ')