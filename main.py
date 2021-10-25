import pygame
import random

pygame.init()
win = pygame.display.set_mode((400, 400))
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
run = True
pawns = []
runda = 0
closedpawns = []


class Pawn():
    def __init__(self, x, y, colour, clicked=False):
        self.x = x
        self.y = y
        self.colour = colour
        self.type = "normalpawn"
        self.clicked = clicked

    def draw_pawn(self):
        if self.clicked == False:
            pygame.draw.circle(win, self.colour, (self.x, self.y), 20)
        else:
            pygame.draw.circle(win, (0, 255, 0), (self.x, self.y), 20)

    def move_pawn(self, mousepos):
        # lewo w dół
        global runda
        help = 0
        if self.colour == red and runda % 2 == 0:
            if self.x - 75 <= mousepos[0] <= self.x - 25 and self.y + 25 <= mousepos[1] <= self.y + 75:
                for pawn in pawns:
                    if self.x - 50 == pawn.x and self.y + 50 == pawn.y:
                        help = 1
                if help == 0:
                    self.x -= 50
                    self.y += 50

                    return True

            elif self.x + 25 <= mousepos[0] <= self.x + 75 and self.y + 25 <= mousepos[1] <= self.y + 75:
                for pawn in pawns:
                    if self.x + 50 == pawn.x and self.y + 50 == pawn.y:
                        help = 1
                if help == 0:
                    self.x += 50
                    self.y += 50
                    return True

        elif self.colour == blue and runda % 2 == 1:
            if self.x - 75 <= mousepos[0] <= self.x - 25 and self.y - 75 <= mousepos[1] <= self.y - 25:
                for pawn in pawns:
                    if self.x - 50 == pawn.x and self.y - 50 == pawn.y:
                        help = 1
                if help == 0:
                    self.x -= 50
                    self.y -= 50
                    return True

            elif self.x + 25 <= mousepos[0] <= self.x + 75 and self.y - 75 <= mousepos[1] <= self.y - 25:
                for pawn in pawns:
                    if self.x + 50 == pawn.x and self.y - 50 == pawn.y:
                        help = 1
                if help == 0:
                    self.x += 50
                    self.y -= 50

                    return True
        return False

    def defeat_pawn(self, mousepos):
        global BlockingPawn
        help = 0
        # lewydol
        if self.x - 125 <= mousepos[0] <= self.x - 75 and self.y + 75 <= mousepos[1] <= self.y + 125:
            for pawn in pawns:
                if self.x - 50 == pawn.x and self.y + 50 == pawn.y:
                    help = 1
                    BlockingPawn = [pawn.colour, pawn.x, pawn.y]
        if help == 1:
            if BlockingPawn[0] != self.colour:
                help = 2
                for pawn in pawns:
                    if self.x - 100 == pawn.x and self.y + 100 == pawn.y:
                        help = 3
        if help == 2:
            for pawn in range(len(pawns) - 1):
                if pawns[pawn].x == BlockingPawn[1] and pawns[pawn].y == BlockingPawn[2]:
                    pawns.pop(pawn)
            self.x -= 100
            self.y += 100
            return True
        help = 0
        # lewygora
        if self.x - 125 <= mousepos[0] <= self.x - 75 and self.y - 125 <= mousepos[1] <= self.y - 75:
            for pawn in pawns:
                if self.x - 50 == pawn.x and self.y - 50 == pawn.y:
                    help = 1
                    BlockingPawn = [pawn.colour, pawn.x, pawn.y]
        if help == 1:
            if BlockingPawn[0] != self.colour:
                help = 2
                for pawn in pawns:
                    if self.x - 100 == pawn.x and self.y - 100 == pawn.y:
                        help = 3
        if help == 2:
            for pawn in range(len(pawns) - 1):
                if pawns[pawn].x == BlockingPawn[1] and pawns[pawn].y == BlockingPawn[2]:
                    pawns.pop(pawn)
            self.x -= 100
            self.y -= 100
            return True
        # prwaydol
        help = 0
        if self.x + 75 <= mousepos[0] <= self.x + 125 and self.y + 75 <= mousepos[1] <= self.y + 125:
            for pawn in pawns:
                if self.x + 50 == pawn.x and self.y + 50 == pawn.y:
                    help = 1
                    BlockingPawn = [pawn.colour, pawn.x, pawn.y]
        if help == 1:
            if BlockingPawn[0] != self.colour:
                help = 2
                for pawn in pawns:
                    if self.x + 100 == pawn.x and self.y + 100 == pawn.y:
                        help = 3
        if help == 2:
            for pawn in range(len(pawns) - 1):
                if pawns[pawn].x == BlockingPawn[1] and pawns[pawn].y == BlockingPawn[2]:
                    pawns.pop(pawn)
            self.x += 100
            self.y += 100
            return True
        # prawygora
        help = 0
        if self.x + 75 <= mousepos[0] <= self.x + 125 and self.y - 125 <= mousepos[1] <= self.y - 75:
            for pawn in pawns:
                if self.x + 50 == pawn.x and self.y - 50 == pawn.y:
                    help = 1
                    BlockingPawn = [pawn.colour, pawn.x, pawn.y]
        if help == 1:
            if BlockingPawn[0] != self.colour:
                help = 2
                for pawn in pawns:
                    if self.x + 100 == pawn.x and self.y - 100 == pawn.y:
                        help = 3
        if help == 2:
            for pawn in range(len(pawns) - 1):
                if pawns[pawn].x == BlockingPawn[1] and pawns[pawn].y == BlockingPawn[2]:
                    pawns.pop(pawn)
            self.x += 100
            self.y -= 100
            return True
        return False

    def checkIfenemyclose(self):
        for pawn in pawns:
            if self.x + 50 == pawn.x and self.y - 50 == pawn.y or self.x + 50 == pawn.x and \
                    self.y + 50 == pawn.y or self.x - 50 == pawn.x and self.y - 50 == pawn.y or \
                    self.x - 50 == pawn.x and self.y + 50 == pawn.y:
                if self.colour != pawn.colour:
                    if pawn not in closedpawns:
                        closedpawns.append(pawn)
        return closedpawns

    def checkclearposbehind(self):
        help = 0
        for closepawn in closedpawns:
            for pawn in pawns:
                # lewygorny
                if closepawn.x < self.x and closepawn.y < self.x:
                    if closepawn.x - 50 == pawn.x and closepawn.y - 50 == pawn.y or closepawn.x - 50 >= 0:
                        help += 1
                # prawygorny
                if closepawn.x > self.x and closepawn.y < self.x:
                    if closepawn.x + 50 == pawn.x and closepawn.y - 50 == pawn.y  or closepawn.x + 50 <= 400:
                        help += 1

                # prawydolny
                if closepawn.x > self.x and closepawn.y > self.x:
                    if closepawn.x + 50 == pawn.x and closepawn.y + 50 == pawn.y or closepawn.x + 50 <= 400:
                        help += 1

                # lewydolny
                if closepawn.x < self.x and closepawn.y > self.x:
                    if closepawn.x - 50 == pawn.x and closepawn.y + 50 == pawn.y or closepawn.x - 50 >= 0:
                        help += 1

            if help < len(closedpawns):
                if runda%2 == 0 and closedpawns[0].colour == blue:
                    return True
                elif runda%2 == 1 and closedpawns[0].colour == red:
                    return True
                else:
                    return False


def unclickpawns():
    for pawn in pawns:
        pawn.clicked = False


def draw_board():
    iterationOfColour = 0
    for x in range(0, 400, 50):
        for y in range(0, 400, 50):
            if iterationOfColour % 2 == 0:
                pygame.draw.rect(win, white, (x, y, x + 50, y + 50))
            else:
                pygame.draw.rect(win, black, (x, y, x + 50, y + 50))
            iterationOfColour += 1
        iterationOfColour += 1


def createRedPawn():
    iterationOfplace = 0
    for x in range(0, 400, 50):
        for y in range(0, 150, 50):
            if iterationOfplace % 2 == 0:
                pawns.append(Pawn(x + 25, y + 25, red))
            iterationOfplace += 1


def wichPawnWasClicked(mousepos):
    for pawn in pawns:
        if pawn.x - 25 <= mousepos[0] <= pawn.x + 25 and pawn.y - 25 <= mousepos[1] <= pawn.y + 25:
            if runda % 2 == 0 and pawn.colour == red:
                unclickpawns()
                pawn.clicked = True
            if runda % 2 == 1 and pawn.colour == blue:
                unclickpawns()
                pawn.clicked = True


def clickedPawn():
    for pawn in pawns:
        if pawn.clicked == True:
            pawn_with_click = pawn
            return pawn_with_click
    return False


def createBlackPawn():
    iterationOfplace = 0
    for x in range(0, 400, 50):
        for y in range(250, 400, 50):
            if not iterationOfplace % 2 == 0:
                pawns.append(Pawn(x + 25, y + 25, blue))
            iterationOfplace += 1


def posibillitytostrike():
    for pawn in pawns:
        if Pawn.checkIfenemyclose(pawn):
            if Pawn.checkclearposbehind(pawn):
                return True
    return False


createRedPawn()
createBlackPawn()


def redraw_win():
    win.fill((0, 0, 0))
    draw_board()
    for pawn in pawns:
        Pawn.draw_pawn(pawn)
    pygame.display.update()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseposition = pygame.mouse.get_pos()
            if clickedPawn() == False:
                wichPawnWasClicked(mouseposition)
            else:
                if posibillitytostrike():
                    if Pawn.defeat_pawn(clickedPawn(), mouseposition):
                        closedpawns.clear()
                        if posibillitytostrike():
                            print("hello")
                            pass
                        else:
                            runda += 1
                            unclickpawns()
                            closedpawns.clear()
                else:
                    if Pawn.move_pawn(clickedPawn(), mouseposition):
                        print("posuniecie")
                        unclickpawns()
                        runda += 1
                        closedpawns.clear()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                unclickpawns()

    redraw_win()
