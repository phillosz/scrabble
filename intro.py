alien = Actor("alien")
alien.pos = 200, 60
WIDTH = 500
HEIGHT = alien.height + 60

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Hit")
    else:
        print("Miss")