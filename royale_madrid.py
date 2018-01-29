self.Dangerzoneplayer2 = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None}


def player2inDangerZone(self):
    for i in player2.soldiers:
        if i.x == 536 and i.y == 325 and i.health[str(i.image)] > 0:
            self.Dangerzoneplayer2['1'] = True
            if (self.x == 570 and self.y == 325) or (self.x == 620 and self.y == 325):
                if int(timer) % 2 == 0:
                    i.health[str(i.image)] -= 10

        else:
            self.Dangerzoneplayer2['1'] = False
        if i.x == 536 and i.y == 385 and i.health[str(i.image)] > 0:
            self.Dangerzoneplayer2['2'] = True
            if (self.x == 570 and self.y == 385) or (self.x == 620 and self.y == 385):
                if int(timer) % 2 == 0:
                    i.health[str(i.image)] -= 10

        else:
            self.Dangerzoneplayer2['2'] = False
        if i.x == 650 and i.y == 385 and i.health[str(i.image)] > 0:
            self.Dangerzoneplayer2['3'] = True
            if (self.x == 620 and self.y == 385) or (self.x == 536 and self.y == 385):
                if int(timer) % 2 == 0:
                    i.health[str(i.image)] -= 10
            if (self.x == 680 and self.y == 385) or (self.x == 752 and self.y == 385):
                if int(timer) % 2 == 0:
                    i.health[str(i.image)] -= 10
        else:
            self.Dangerzoneplayer2['3'] = False
        if i.x == 595 and i.y == 490 and i.health[str(i.image)] > 0:
            self.Dangerzoneplayer2['6'] = True
            if (self.x == 570 and self.y == 490) or (self.x == 620 and self.y == 385):
                if int(timer) % 2 == 0:
                    i.health[str(i.image)] -= 10
        else:
            self.Dangerzoneplayer2['6'] = False
        if i.x == 753 and i.y == 325 and i.health[str(i.image)] > 0:
            self.Dangerzoneplayer2['4'] = True
            if (self.x == 720 and self.y == 325) or (self.x == 680 and self.y == 325):
                if int(timer) % 2 == 0:
                    i.health[str(i.image)] -= 10

        else:
            self.Dangerzoneplayer2['4'] = False
        if i.x == 753 and i.y == 385 and i.health[str(i.image)] > 0:
            self.Dangerzoneplayer2['5'] = True
            if (self.x == 720 and self.y == 385) or (self.x == 680 and self.y == 385):
                if int(timer) % 2 == 0:
                    i.health[str(i.image)] -= 10
        else:
            self.Dangerzoneplayer2['5'] = False
        if i.x == 690 and i.y == 490 and i.health[str(i.image)] > 0:
            self.Dangerzoneplayer2['7'] = True
            if (self.x == 720 and self.y == 490) or (self.x == 720 and self.y == 490):
                if int(timer) % 2 == 0:
                    i.health[str(i.image)] -= 10
        else:
            self.Dangerzoneplayer2['7'] = False


def fightplayer1(self):
    if self.Dangerzoneplayer2['1'] == True and self.x < 660 and self.y > 325:
        if self.x < 570:
            self.x += 1
        if 570 < self.x < 660:  # 1
            self.x -= 1
        if self.y > 325:
            self.y -= 1
        if self.x == 570 and self.y == 325:
            if int(timer) % 2 == 0:
                bullet = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet, (550, 340))
    if self.Dangerzoneplayer2['2'] == True and self.x < 660 and self.y > 325:
        if self.x < 570:
            self.x += 1
        if 570 < self.x < 660:
            self.x -= 1
        if 385 > self.y > 325:  # 2
            self.y += 1
        if self.y > 385:
            self.y -= 1
        if self.x == 570 and self.y == 385:
            if int(timer) % 2 == 0:
                bullet = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet, (550, 400))
    if self.Dangerzoneplayer2['4'] == True and self.x > 660 and self.y > 325:
        if self.x > 720:
            self.x -= 1
        if 660 < self.x < 720:  # 4
            self.x += 1
        if self.y > 325:
            self.y -= 1
        if self.x == 720 and self.y == 325:
            if int(timer) % 2 == 0:
                bullet = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet, (740, 340))
    if self.Dangerzoneplayer2['5'] == True and self.x > 660 and self.y > 325:
        if self.x > 720:
            self.x -= 1
        if 660 < self.x < 720:
            self.x += 1
        if 385 > self.y > 325:  # 5
            self.y += 1
        if self.y > 385:
            self.y -= 1
        if self.x == 720 and self.y == 385:
            if int(timer) % 2 == 0:
                bullet = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet, (740, 400))
    if self.Dangerzoneplayer2['3'] == True and self.x < 650 and self.y > 325:
        if 620 < self.x < 650:
            self.x -= 1
        if self.x < 620:
            self.x += 1
        if 325 < self.y < 385:  # 3
            self.y += 1
        if self.y > 385:
            self.y -= 1
        if self.x == 620 and self.y == 385:
            if int(timer) % 2 == 0:
                bullet = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet, (640, 400))
    if self.Dangerzoneplayer2['3'] == True and self.x > 650 and self.y > 325:
        if 650 < self.x < 680:
            self.x += 1
        if self.x > 680:
            self.x -= 1
        if 325 < self.y < 385:  # 3
            self.y += 1
        if self.y > 385:
            self.y -= 1
        if self.x == 680 and self.y == 385:
            if int(timer) % 2 == 0:
                bullet = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet, (660, 400))
    if self.Dangerzoneplayer2['6'] == True and self.x < 660 and self.y > 325:
        if self.x < 570:
            self.x += 1
        if 580 < self.x < 660:
            self.x -= 1
        if 325 < self.y < 490:  # 6
            self.y += 1
        if self.x == 570 and self.y == 490:
            if int(timer) % 2 == 0:
                bullet = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet, (590, 500))
    if self.Dangerzoneplayer2['7'] == True and self.x > 660 and self.y > 325:
        if self.x > 720:
            self.x -= 1
        if 660 < self.x < 720:
            self.x += 1
        if 325 < self.y < 490:  # 7
            self.y += 1
        if self.x == 720 and self.y == 325:
            if int(timer) % 2 == 0:
                bullet = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet, (700, 500))
            b.player2inDangerZone()
            if (b.Dangerzoneplayer2['1'] == True or b.Dangerzoneplayer2['2'] == True or b.Dangerzoneplayer2['3'] == True or b.Dangerzoneplayer2['6'] == True) and \
                b.x < 660 and b.y > 320:
                b.fightplayer1()
                b.drawhero()
                print('kir')
            elif (b.Dangerzoneplayer2['4'] == True or b.Dangerzoneplayer2['5'] == True or b.Dangerzoneplayer2['7'] == True or b.Dangerzoneplayer2['3'] == True) \
                and b.x > 660 and b.y > 320:
                b.fightplayer1()
                b.drawhero()

            else:
                if b.image == 'giant' or b.image == 'Knight' or b.image == 'hog' or b.image == 'Barbarian':
                    if b.healthheroesUnarmed() == True:
                        b.moveplayer1Unarmed()
                        b.drawhero()
                else:
                    if b.healthheroes() == True:
                        b.moveplayer1()
                        b.drawhero()
