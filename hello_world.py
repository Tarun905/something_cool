import sys,pygame
from pygame.locals import*
pygame.init()


screen_info = pygame.display.Info()
x = screen_info.current_w
y = screen_info.current_h

screen = pygame.display.set_mode((x,y))
clock = pygame.time.Clock()
color = (0,255,255)

image = pygame.image.load("fish1.png")
rect = image.get_rect()
rect.center = (x//2,y//2)


speed = pygame.math.Vector2(0,10)
def update():
    rect.move_ip(speed)

def main():
    print("hello world")
    while True:
        clock.tick(60)
        screen.fill(color)
        update()
        screen.blit(image, rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()

import sys,program,random
random,randomInt(0,360)











