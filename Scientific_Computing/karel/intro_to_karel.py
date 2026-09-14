from stanfordkarel import *
print("Karel library imported successfully!")

def main():
    move()
    put_beeper()
    move()
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    move()
    put_beeper()
    turn_right()
    move_down()
    turn_right()
    finish()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_down():
    move()
    move()
    move()
#or
#def move_down():
#    for i in range(3):
#        move()

def finish():
    move()
    move()
    move()
    pick_beeper()
    

if __name__ == "__main__":
    run_karel_program()  