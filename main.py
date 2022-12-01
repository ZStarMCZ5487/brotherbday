import random
import pygame
import win32gui
import screen_brightness_control as scdisplay

pygame.init()

screen = pygame.display.set_mode((1080, 680))

pygame.display.set_caption("Stupid game for ppl like u")
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)
font = pygame.font.SysFont(None, 50)

bg = pygame.image.load("background.png")
door = pygame.image.load("door.png")
open_door = pygame.image.load("open-door.png")
play = pygame.image.load("play.png")

playerImg = pygame.image.load("player.png")
playerX = 50
playerY = 590
playerXchange = 0
playerYchange = 0
Is_Jump = False
JumpCount = 7
numX = 540
numY = 640

doorisopen = 0
buttonispress = 0
clicked = False
pressed = 0
islv18 = 0

levelmsg = ""
reallvmsg = ""


def player(x, y):
    screen.blit(playerImg, (x, y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -1
            if event.key == pygame.K_RIGHT:
                playerXchange = 1
            if event.key == pygame.K_F6:
                reallvmsg = "Level 28: ok i ran out of idea"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0

    keys = pygame.key.get_pressed()
    if islv18 == 1:
        if not (Is_Jump):
            if keys[pygame.K_UP]:
                Is_Jump = True
        else:
            if JumpCount >= -7:
                neg = 1.5

                if JumpCount < 0:
                    neg = -1.5

                playerY -= (JumpCount ** 2) * 0.5 * neg
                JumpCount -= 1
            else:
                Is_Jump = False
                JumpCount = 7

    screen.blit(bg, (0, 0))

    playerX += playerXchange
    playerY += playerYchange
    if playerX <= 18:
        playerX = 18
    elif playerX >= 1000:
        playerX = 1000
    if playerY >= 590:
        playerY = 590

    if levelmsg == "":
        reallvmsg = "go to the door to start"

    #start
    if levelmsg == "go to the door to start":
        if playerX == 550:
            buttonispress = 1
            doorisopen = 1

        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        if buttonispress == 0:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        elif buttonispress == 1:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 647, 90, 5))

        if playerX == 960:
            doorisopen = 0
            buttonispress = 0
            playerX = 50
            playerY = 590
            reallvmsg = "Level 1: go to the door again"

    #level1
    if levelmsg == "Level 1: go to the door again":
        if playerX == 550:
            buttonispress = 1
            doorisopen = 1

        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        if buttonispress == 0:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        elif buttonispress == 1:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 647, 90, 5))

        if playerX == 960:
            doorisopen = 0
            buttonispress = 0
            playerX = 50
            playerY = 590
            reallvmsg = "Level 2: What task you got?"

    #level2
    if levelmsg == "Level 2: What task you got?":

        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "Task Manager")
        if ui == 0:
            doorisopen = 0
        else:
            doorisopen = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 3: back"
    #level3
    if levelmsg == "Level 3: back":
        screen.blit(door, (950, 530))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        if playerX == 18:
            doorisopen = 0
            buttonispress = 0
            playerX = 50
            playerY = 590
            reallvmsg = "Level 4: press the button"
    #level4
    if levelmsg == "Level 4: press the button":

        pos = pygame.mouse.get_pos()

        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        if buttonispress == 0:
            on = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        elif buttonispress == 1:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 647, 90, 5))

        if on.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                buttonispress = 1
                doorisopen = 1

        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 5: Run"
    #level5
    if levelmsg == "Level 5: Run":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "Run")
        if ui == 0:
            doorisopen = 0
        else:
            doorisopen = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 6: throw your trash to recycle bin"
    if levelmsg == "Level 6: throw your trash to recycle bin":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "Recycle Bin")
        if ui == 0:
            doorisopen = 0
        else:
            doorisopen = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 7: what have you download?"
    if levelmsg == "Level 7: what have you download?":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "Downloads")
        if ui == 0:
            doorisopen = 0
        else:
            doorisopen = 1

        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 8: open the door"
    if levelmsg == "Level 8: open the door":
        pos = pygame.mouse.get_pos()

        if doorisopen == 0:
            on = screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        if on.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                doorisopen = 1

        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 9: Turn off start"
    if levelmsg == "Level 9: Turn off start":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "Start")
        if ui == 0:
            doorisopen = 1
        else:
            doorisopen = 0

        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 10: broken button"
    if levelmsg == "Level 10: broken button":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        if buttonispress == 0:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        elif buttonispress == 1:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 647, 90, 5))

        if pressed == 0:
            if playerX == 550:
                pressed = 1
                print(pressed)
        if pressed == 1:
            if playerX == 1000:
                pressed = 2
                print(pressed)
        if pressed == 2:
            if playerX == 550:
                pressed = 3
                print(pressed)
        if pressed == 3:
            if playerX == 18:
                pressed = 4
                print(pressed)
        if pressed == 4:
            if playerX == 550:
                doorisopen = 1
                buttonispress = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 11: empty"
    if levelmsg == "Level 11: empty":
        pos = pygame.mouse.get_pos()
        p = screen.blit(playerImg, (playerX, playerY))
        if p.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 12: watch a video"
    if levelmsg == "Level 12: watch a video":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "Movies & TV")
        if ui == 0:
            doorisopen = 0
        else:
            doorisopen = 1

        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 13: press harder"
    if levelmsg == "Level 13: press harder":
        pos = pygame.mouse.get_pos()
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        on = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        if buttonispress == 0:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 637, 90, 15))
        if buttonispress == 1:
            on = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        elif buttonispress == 2:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 647, 90, 5))

        if playerX == 550:
            buttonispress = 1
        if on.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                buttonispress = 2
                doorisopen = 1
        if playerX == 960:
            doorisopen = 0
            buttonispress = 0
            playerX = 50
            playerY = 590
            reallvmsg = "Level 14: Projector"
    if levelmsg == "Level 14: Projector":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "Project")
        if ui == 0:
            print("")
        else:
            doorisopen = 1

        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 15: its so dark"
    if levelmsg == "Level 15: its so dark":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        e = scdisplay.get_brightness()
        if e == [100]:
            doorisopen = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 16: fake"
    if levelmsg == "Level 16: fake":
        screen.blit(door, (950, 530))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        if playerX == 960:
            doorisopen = 0
            buttonispress = 0
            playerX = 50
            playerY = 590
            reallvmsg = "Level 17: open the door after press the button"
    if levelmsg == "Level 17: open the door after press the button":
        pos = pygame.mouse.get_pos()
        if doorisopen == 0:
            on = screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))
        if buttonispress == 0:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        elif buttonispress == 1:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 647, 90, 5))
        if playerX == 550:
            buttonispress = 1
        if buttonispress == 1:
            if on.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    doorisopen = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 18: Its Me! Mario!"
    if levelmsg == "Level 18: Its Me! Mario!":
        islv18 = 1
        p = screen.blit(playerImg, (playerX, playerY))
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))
        if buttonispress == 0:
            e = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 550, 90, 12))
        elif buttonispress == 1:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 557, 90, 5))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(530, 560, 110, 15))
        collide1 = pygame.Rect.colliderect(p, e)
        if collide1:
            playerXchange = 0
            playerYchange = 0
            buttonispress = 1
            doorisopen = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 19: Artist"
    if levelmsg == "Level 19: Artist":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "Paint")
        if ui == 0:
            print("")
        else:
            doorisopen = 1

        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 20: Find the button (hint: poop.png)"

    if levelmsg == "Level 20: Find the button (hint: poop.png)":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "button-2468")
        if ui == 0:
            doorisopen = 0
        else:
            doorisopen = 1

        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 21: Luck"
    if levelmsg == "Level 21: Luck":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        if buttonispress == 0:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        elif buttonispress == 1:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 647, 90, 5))

        if playerX == 550:
            num = random.randint(1, 10)
            if num == 8:
                doorisopen = 1
                buttonispress = 1

        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 22: Jump to open"
    if levelmsg == "Level 22: Jump to open":
        islv18 = 1
        #^ this for testing
        p = screen.blit(playerImg, (playerX, playerY))
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        if buttonispress == 0:
            a = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        elif buttonispress == 1:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 647, 90, 5))

        collide1 = pygame.Rect.colliderect(p, a)
        if collide1:
            if Is_Jump == True:
                doorisopen = 1
                buttonispress = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 23: https://youtu.be/dQw4w9WgXcQ"
    if levelmsg == "Level 23: https://youtu.be/dQw4w9WgXcQ":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "Rick Astley - Never Gonna Give You Up (Official Music Video) - YouTube - Google Chrome")
        if ui == 0:
            doorisopen = 0
        else:
            doorisopen = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 24: Magnifier"
    if levelmsg == "Level 24: Magnifier":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "Magnifier")
        if ui == 0:
            doorisopen = 0
        else:
            doorisopen = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 25: settings"
    if levelmsg == "Level 25: settings":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))

        ui = win32gui.FindWindow(None, "Lenovo Vantage")
        if ui == 0:
            doorisopen = 0
        else:
            doorisopen = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 26: click the button"
    if levelmsg == "Level 26: click the button":
        pos = pygame.mouse.get_pos()
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))
        button = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(numX, numY, 90, 12))
        if button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                numX = random.randint(0, 1080)
                numY = random.randint(0, 680)
                pressed += 1
        if pressed == 100:
            doorisopen = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 27: Too Bright"
    if levelmsg == "Level 27: Too Bright":
        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        e = scdisplay.get_brightness()
        if e == [0]:
            doorisopen = 1
        if doorisopen == 1:
            if playerX == 960:
                doorisopen = 0
                buttonispress = 0
                playerX = 50
                playerY = 590
                reallvmsg = "Level 28: ok i ran out of idea"
    if levelmsg == "Level 28: ok i ran out of idea":
        if playerX == 550:
            buttonispress = 1
            doorisopen = 1

        if doorisopen == 0:
            screen.blit(door, (950, 530))
        elif doorisopen == 1:
            screen.blit(open_door, (950, 530))

        if buttonispress == 0:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 640, 90, 12))
        elif buttonispress == 1:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(540, 647, 90, 5))

        if playerX == 960:
            doorisopen = 0
            buttonispress = 0
            playerX = 50
            playerY = 590
            pygame.quit()

    levelmsg = reallvmsg
    msg = font.render(levelmsg, True, (255, 255, 255))
    screen.blit(msg, (50, 340))
    player(playerX, playerY)
    pygame.display.update()
