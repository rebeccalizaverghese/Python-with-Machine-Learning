import pygame
pygame.init()

window=pygame.display.set_mode ((800,700))
pygame.display.set_caption("Game_Development")

icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

spaceship=pygame.image.load("icon.png")
spaceship_x=200
spaceship_y=300

def display_spaceship(x,y):
    window.blit(spaceship, (x,y))


bg=pygame.image.load("Background.jpg")


gameon=True
while gameon: # if condition is true it will carry out arguement, if false it will end function
    window.blit(bg,(0,0)) #(blit - allows to add image to windows)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameon=False
    keys=pygame.key.get_pressed()# use of keys to move spaceship
    if keys[pygame.K_LEFT]:
        spaceship_x-=1 #incremented by 1
    if keys[pygame.K_RIGHT]:
        spaceship_x+=1 #decremented by 1
    if keys[pygame.K_UP]:
        spaceship_y-=1 #incremented by 1
    if keys[pygame.K_DOWN]:
        spaceship_y+=1 #decremented by 1
        
    display_spaceship(spaceship_x,spaceship_y)
    pygame.display.update()
pygame.quit()

