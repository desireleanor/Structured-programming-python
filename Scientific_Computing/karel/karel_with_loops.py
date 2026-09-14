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
    run()
    turn_right()
    finish()
    turn_around()
    run()
    turn_left()
    run()
    pick_beeper()
    turn_right()
    move_to_wall()

def turn_right():
    for i in range(3):
        turn_left()
    

def run():
    for i in range(3):
        move()
#or
#def move_down():
#    for i in range(3):
#        move()

def finish():
    for i in range(3):
        move()
    pick_beeper()

def turn_around():
    for x in range(2):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()
    

if __name__ == "__main__":
    run_karel_program()  