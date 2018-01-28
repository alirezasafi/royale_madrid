import pygame, sys, random

pygame.init()


class player():
    def __init__(self, x, y, pygame, surface):
        self.wizard = None
        self.musketeer = None
        self.giant = None
        self.hunter = None
        self.icewizard = None
        self.princess = None
        self.dart = None
        self.executioner = None
        self.x = x
        self.y = y
        self.pygame = pygame
        self.surface = surface
        self.heroes = ['Wizard', 'giant', 'Musketeers', 'hunter', 'Barbarian', 'Archer', 'Knight', 'hog']
        self.heroes_push = []
        self.check = [1]
        self.replace1 = False
        self.replace2 = False
        self.replace3 = False
        self.replace4 = False
        self.X = False
        self.soldiers = []
        self.elixir = {'elixir1': None, 'elixir2': None, 'elixir3': None, 'elixir4': None}
        self.num_elixir = {'num1': None, 'num2': None, 'num3': None, 'num4': None}
        self.right_choice = False

    def blitheroes(self, image, x, y):
        image = self.pygame.image.load(str(image) + '.jpg')
        self.surface.blit(image, (x, y))

    def push(self):
        if len(self.heroes) == 8:
            hero1 = random.choice(self.heroes)
            self.heroes_push.append(hero1)
            self.heroes.remove(hero1)
            hero2 = random.choice(self.heroes)
            self.heroes_push.append(hero2)
            self.heroes.remove(hero2)
            hero3 = random.choice(self.heroes)
            self.heroes_push.append(hero3)
            self.heroes.remove(hero3)
            hero4 = random.choice(self.heroes)
            self.heroes_push.append(hero4)
            self.heroes.remove(hero4)
        self.blitheroes(str(self.heroes_push[0]) + 'Card', 945, 490)
        self.blitheroes(str(self.heroes_push[1]) + 'Card', 1032, 490)
        self.blitheroes(str(self.heroes_push[2]) + 'Card', 1120, 490)
        self.blitheroes(str(self.heroes_push[3]) + 'Card', 1205, 490)

    def click(self, L1, L2, R1, R2, X, x, y):
        if int(timer) % 3 == 0 and self.elixir['elixir1'] == None:
            self.elixir['elixir1'] = True
            self.num_elixir['num1'] = int(timer)
        if int(timer) % 3 == 0 and self.elixir['elixir1'] == True and self.elixir['elixir2'] == None:
            if int(timer) != self.num_elixir['num1']:
                self.elixir['elixir2'] = True
                self.num_elixir['num2'] = int(timer)
        if int(timer) % 3 == 0 and self.elixir['elixir2'] == True and self.elixir['elixir3'] == None:
            if int(timer) != self.num_elixir['num1'] and int(timer) != self.num_elixir['num2']:
                self.elixir['elixir3'] = True
                self.num_elixir['num3'] = int(timer)
        if int(timer) % 3 == 0 and self.elixir['elixir3'] == True and self.elixir['elixir4'] == None:
            if int(timer) != self.num_elixir['num1'] and int(timer) != self.num_elixir['num2'] and int(timer) != \
                    self.num_elixir['num3']:
                self.elixir['elixir4'] = True
                self.num_elixir['num4'] = int(timer)
        if self.elixir['elixir1'] == True and self.elixir['elixir2'] == True and self.elixir['elixir3'] == True and \
                self.elixir['elixir4'] == True:
            self.right_choice = True
        else:
            self.right_choice = False
        if len(self.check) == 1:
            self.selecthero1 = False
            self.selecthero2 = False
            self.selecthero3 = False
            self.selecthero4 = False
        self.check.append(3)
        if L1 == 1:
            self.selecthero1 = True
            if len(self.heroes) == 4 and self.replace1 == False:
                self.heroes.append(self.heroes_push[0])
                self.heroes_push[0] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[0]) + 'Card', 945, 490)
            self.replace1 = True
        if L2 == 1:
            self.selecthero2 = True
            if len(self.heroes) == 4 and self.replace2 == False:
                self.heroes.append(self.heroes_push[1])
                self.heroes_push[1] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[1]) + 'Card', 1032, 490)
            self.replace2 = True
        if R1 == 1:
            self.selecthero3 = True
            if len(self.heroes) == 4 and self.replace3 == False:
                self.heroes.append(self.heroes_push[2])
                self.heroes_push[2] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[2]) + 'Card', 1120, 490)
            self.replace3 = True
        if R2 == 1:
            self.selecthero4 = True
            if len(self.heroes) == 4 and self.replace4 == False:
                self.heroes.append(self.heroes_push[3])
                self.heroes_push[3] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[3]) + 'Card', 1205, 490)
            self.replace4 = True
        if self.selecthero1 == True:
            self.pointer_position(x, y)
            if X == 1 and self.X == False and self.right_choice == True:
                self.selecthero1 = False
                self.replace1 = False
                self.soldiers.append(soldier(x - 17, y - 20, self.pygame, self.surface, self.heroes[3]))
                self.elixir['elixir1'] = None
                self.elixir['elixir2'] = None
                self.elixir['elixir3'] = None
                self.elixir['elixir4'] = None
        if self.selecthero2 == True:
            self.pointer_position(x, y)
            if X == 1 and self.X == False and self.right_choice == True:
                self.selecthero2 = False
                self.replace2 = False
                self.soldiers.append(soldier(x - 17, y - 20, self.pygame, self.surface, self.heroes[3]))
                self.elixir['elixir1'] = None
                self.elixir['elixir2'] = None
                self.elixir['elixir3'] = None
                self.elixir['elixir4'] = None
        if self.selecthero3 == True:
            self.pointer_position(x, y)
            if X == 1 and self.X == False and self.right_choice == True:
                self.selecthero3 = False
                self.replace3 = False
                self.soldiers.append(soldier(x - 17, y - 20, self.pygame, self.surface, self.heroes[3]))
                self.elixir['elixir1'] = None
                self.elixir['elixir2'] = None
                self.elixir['elixir3'] = None
                self.elixir['elixir4'] = None
        if self.selecthero4 == True:
            self.pointer_position(x, y)
            if X == 1 and self.X == False and self.right_choice == True:
                self.selecthero4 = False
                self.replace4 = False
                self.soldiers.append(soldier(x - 17, y - 20, self.pygame, self.surface, self.heroes[3]))
                self.elixir['elixir1'] = None
                self.elixir['elixir2'] = None
                self.elixir['elixir3'] = None
                self.elixir['elixir4'] = None
        if self.elixir['elixir1'] == True:
            self.surface.blit(elixir, (1199, 428))
        if self.elixir['elixir2'] == True:
            self.surface.blit(elixir, (1110, 428))
        if self.elixir['elixir3'] == True:
            self.surface.blit(elixir, (1021, 428))
        if self.elixir['elixir4'] == True:
            self.surface.blit(elixir, (932, 428))

    def pointer_position(self, x, y):
        self.pygame.draw.circle(self.surface, (255, 255, 255), (x, y), 5, 0)

    def drawsoldier(self):
        for b in self.soldiers:
            if b.image == 'giant' or b.image == 'Knight' or b.image == 'hog' or b.image == 'Barbarian':
                if b.healthheroesUnarmed() == True:
                    b.moveplayer1Unarmed()
                    b.drawhero()
            else:
                if b.healthheroes() == True:
                    b.moveplayer1()
                    b.drawhero()


class player2():
    def __init__(self, x, y, pygame, surface):
        self.wizard = None
        self.musketeer = None
        self.giant = None
        self.hunter = None
        self.icewizard = None
        self.princess = None
        self.dart = None
        self.executioner = None
        self.x = x
        self.y = y
        self.pygame = pygame
        self.surface = surface
        self.heroes = ['Wizard', 'giant', 'Musketeers', 'hunter', 'Barbarian', 'Archer', 'Knight', 'hog']
        self.heroes_push = []
        self.check = [1]
        self.replace1 = False
        self.replace2 = False
        self.replace3 = False
        self.replace4 = False
        self.X = False
        self.coordients = {'x': None, 'y': None}
        self.soldiers = []
        self.elixir = {'elixir1': None, 'elixir2': None, 'elixir3': None, 'elixir4': None}
        self.num_elixir = {'num1': None, 'num2': None, 'num3': None, 'num4': None}
        self.right_choice = False

    def blitheroes(self, image, x, y):
        image = self.pygame.image.load(str(image) + '.jpg')
        self.surface.blit(image, (x, y))

    def push(self):
        if len(self.heroes) == 8:
            hero1 = random.choice(self.heroes)
            self.heroes_push.append(hero1)
            self.heroes.remove(hero1)
            hero2 = random.choice(self.heroes)
            self.heroes_push.append(hero2)
            self.heroes.remove(hero2)
            hero3 = random.choice(self.heroes)
            self.heroes_push.append(hero3)
            self.heroes.remove(hero3)
            hero4 = random.choice(self.heroes)
            self.heroes_push.append(hero4)
            self.heroes.remove(hero4)
        self.blitheroes(str(self.heroes_push[0]) + 'Card', 20, 80)
        self.blitheroes(str(self.heroes_push[1]) + 'Card', 105, 80)
        self.blitheroes(str(self.heroes_push[2]) + 'Card', 193, 80)
        self.blitheroes(str(self.heroes_push[3]) + 'Card', 282, 80)

    def click(self, L1, L2, R1, R2, X, x, y):
        if int(timer) % 3 == 0 and self.elixir['elixir1'] == None:
            self.elixir['elixir1'] = True
            self.num_elixir['num1'] = int(timer)
        if int(timer) % 3 == 0 and self.elixir['elixir1'] == True and self.elixir['elixir2'] == None:
            if int(timer) != self.num_elixir['num1']:
                self.elixir['elixir2'] = True
                self.num_elixir['num2'] = int(timer)
        if int(timer) % 3 == 0 and self.elixir['elixir2'] == True and self.elixir['elixir3'] == None:
            if int(timer) != self.num_elixir['num1'] and int(timer) != self.num_elixir['num2']:
                self.elixir['elixir3'] = True
                self.num_elixir['num3'] = int(timer)
        if int(timer) % 3 == 0 and self.elixir['elixir3'] == True and self.elixir['elixir4'] == None:
            if int(timer) != self.num_elixir['num1'] and int(timer) != self.num_elixir['num2'] and int(timer) != \
                    self.num_elixir['num3']:
                self.elixir['elixir4'] = True
                self.num_elixir['num4'] = int(timer)
        if self.elixir['elixir1'] == True and self.elixir['elixir2'] == True and self.elixir['elixir3'] == True and \
                self.elixir['elixir4'] == True:
            self.right_choice = True
        else:
            self.right_choice = False
        if len(self.check) == 1:
            self.selecthero1 = False
            self.selecthero2 = False
            self.selecthero3 = False
            self.selecthero4 = False
            self.check.append(3)
        if L1 == 1:
            self.selecthero1 = True
            if len(self.heroes) == 4 and self.replace1 == False:
                self.heroes.append(self.heroes_push[0])
                self.heroes_push[0] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[0]) + 'Card', 20, 80)
            self.replace1 = True
        if L2 == 1:
            self.selecthero2 = True
            if len(self.heroes) == 4 and self.replace2 == False:
                self.heroes.append(self.heroes_push[1])
                self.heroes_push[1] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[1]) + 'Card', 105, 80)
            self.replace2 = True
        if R1 == 1:
            self.selecthero3 = True
            if len(self.heroes) == 4 and self.replace3 == False:
                self.heroes.append(self.heroes_push[2])
                self.heroes_push[2] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[2]) + 'Card', 193, 80)
            self.replace3 = True
        if R2 == 1:
            self.selecthero4 = True
            if len(self.heroes) == 4 and self.replace4 == False:
                self.heroes.append(self.heroes_push[3])
                self.heroes_push[3] = self.heroes[0]
                self.heroes.remove(self.heroes[0])
                self.blitheroes(str(self.heroes_push[3]) + 'Card', 282, 80)
            self.replace4 = True
        if self.selecthero1 == True:
            self.pointer_position(x, y)
            if X == 1 and self.X == False and self.right_choice == True:
                self.selecthero1 = False
                self.replace1 = False
                self.soldiers.append(soldier(x - 17, y - 20, self.pygame, self.surface, self.heroes[3]))
                self.elixir['elixir1'] = None
                self.elixir['elixir2'] = None
                self.elixir['elixir3'] = None
                self.elixir['elixir4'] = None

        if self.selecthero2 == True:
            self.pointer_position(x, y)
            if X == 1 and self.X == False and self.right_choice == True:
                self.selecthero2 = False
                self.replace2 = False
                self.soldiers.append(soldier(x - 17, y - 20, self.pygame, self.surface, self.heroes[3]))
                self.elixir['elixir1'] = None
                self.elixir['elixir2'] = None
                self.elixir['elixir3'] = None
                self.elixir['elixir4'] = None
        if self.selecthero3 == True:
            self.pointer_position(x, y)
            if X == 1 and self.X == False and self.right_choice == True:
                self.selecthero3 = False
                self.replace3 = False
                self.soldiers.append(soldier(x - 17, y - 20, self.pygame, self.surface, self.heroes[3]))
                self.elixir['elixir1'] = None
                self.elixir['elixir2'] = None
                self.elixir['elixir3'] = None
                self.elixir['elixir4'] = None
        if self.selecthero4 == True:
            self.pointer_position(x, y)
            if X == 1 and self.X == False and self.right_choice == True:
                self.selecthero4 = False
                self.replace4 = False
                self.soldiers.append(soldier(x - 17, y - 20, self.pygame, self.surface, self.heroes[3]))
                self.elixir['elixir1'] = None
                self.elixir['elixir2'] = None
                self.elixir['elixir3'] = None
                self.elixir['elixir4'] = None
        if self.elixir['elixir1'] == True:
            self.surface.blit(elixir, (13, 178))
        if self.elixir['elixir2'] == True:
            self.surface.blit(elixir, (102, 178))
        if self.elixir['elixir3'] == True:
            self.surface.blit(elixir, (191, 178))
        if self.elixir['elixir4'] == True:
            self.surface.blit(elixir, (280, 178))

    def pointer_position(self, x, y):
        self.pygame.draw.circle(self.surface, (255, 255, 255), (x, y), 5, 0)

    def drawsoldier(self):
        for b in self.soldiers:
            if b.image == 'giant' or b.image == 'Knight' or b.image == 'hog' or b.image == 'Barbarian':
                if b.healthheroesUnarmed() == True:
                    b.moveplayer2Unarmed()
                    b.drawhero()
            else:
                if b.healthheroes() == True:
                    b.moveplayer2()
                    b.drawhero()


class soldier():
    def __init__(self, x, y, pygame, surface, image):
        self.pygame = pygame
        self.surface = surface
        self.x = x
        self.y = y
        self.image = image
        self.Bullets = []
        self.health = {'Wizard': 656, 'Archer': 300, 'giant': 1100, 'Knight': 1000, 'hunter': 576, 'Barbarian': 1100,
                       'hog': 944, 'Musketeers': 600}

    def drawhero(self):
        image = self.pygame.image.load(str(self.image) + '.jpg')
        self.surface.blit(image, (self.x, self.y))

    def moveplayer1(self):
        if tower3.healthtowers['tower3']>0:
            if 470 < self.x < 536:
                self.x += 1
            if 536 < self.x < 670:
                self.x -= 1
            if 260 < self.y < 680 and self.x == 536:
                self.y -= 1
        if tower4.healthtowers['tower4']>0:
            if 670 < self.x < 753:
                self.x += 1
            if 753 < self.x < 865:
                self.x -=1
            if 260 < self.y < 680 and self.x == 753:
                self.y -= 1
        if tower3.healthtowers['tower3']<=0:
            if 470 < self.x < 536 and self.y !=180 and self.y!=260:
                self.x += 1
            if 536 < self.x < 670 and self.y!=180 and self.y!=260:
                self.x -= 1
            if self.y > 180 and tower4.healthtowers['tower4']<=0:
                self.y-=1
            if self.y == 180 and self.x <650:
                self.x += 1
        if tower4.healthtowers['tower4']<=0:
            if 670 < self.x < 753 and self.y!=180  and self.y!=260:
                self.x += 1
            if 753 < self.x < 865 and self.y !=180 and self.y !=260:
                self.x -=1
            if self.y == 180 and self.x > 650:
                self.x -= 1
            if self.y > 180 and tower3.healthtowers['tower3']<=0:
                self.y -= 1
    def moveplayer2(self):
        if tower1.healthtowers['tower1']>0:
            if 470 < self.x < 536:
                self.x += 1
            if 536 < self.x < 670:
                self.x -= 1
            if 65 < self.y < 325 and self.x == 536:
                self.y += 1
        if tower2.healthtowers['tower2']>0:
            if 670 < self.x < 753:
                self.x += 1
            if 753 < self.x < 865:
                self.x -=1
            if 65 < self.y < 325 and self.x == 753:
                self.y += 1
        if tower1.healthtowers['tower1']<=0:
            if 470 < self.x < 536 and self.y !=385 and self.y!=325:
                self.x += 1
            if 536 < self.x < 670 and self.y!=385 and self.y!=325:
                self.x -= 1
            if self.y < 385 and tower2.healthtowers['tower2']<=0:
                self.y+=1
            if self.y == 385 and self.x <650:
                self.x += 1
        if tower2.healthtowers['tower2']<=0:
            if 670 < self.x < 753 and self.y!=385  and self.y!=325:
                self.x += 1
            if 753 < self.x < 865 and self.y !=385 and self.y !=325:
                self.x -=1
            if self.y == 385 and self.x > 650:
                self.x -= 1
            if self.y < 385 and tower1.healthtowers['tower1']<=0:
                self.y += 1
    def moveplayer2Unarmed(self):
        if tower1.healthtowers['tower1']>0:
            if 470 < self.x < 536:
                self.x += 1
            if 536 < self.x < 670:
                self.x -= 1
            if 65 < self.y < 385 and self.x == 536:
                self.y += 1
        if tower2.healthtowers['tower2']>0:
            if 670 < self.x < 753:
                self.x += 1
            if 753 < self.x < 865:
                self.x -=1
            if 65 < self.y < 385 and self.x == 753:
                self.y += 1
        if tower1.healthtowers['tower1']<=0 :
            if 470 < self.x < 536 and self.y !=385 and self.y !=490:
                self.x += 1
            if 536 < self.x < 670 and self.y!=385 and self.y != 490:
                self.x -= 1
            if self.y == 490 and self.x < 595:
                self.x += 1
            if self.y < 490 and tower2.healthtowers['tower2']<=0:
                self.y += 1
        if tower2.healthtowers['tower2']<=0:
            if 670 < self.x < 753 and self.y!=490  and self.y!=385:
                self.x += 1
            if 753 < self.x < 865 and self.y !=490 and self.y !=385:
                self.x -=1
            if self.y == 490 and self.x > 690:
                self.x -= 1
            if self.y < 490 and tower1.healthtowers['tower1']<=0:
                self.y += 1
    def moveplayer1Unarmed(self):
        if tower3.healthtowers['tower3']>0:
            if 470 < self.x < 536:
                self.x += 1
            if 536 < self.x < 670:
                self.x -= 1
            if 180 < self.y < 680 and self.x == 536:
                self.y -= 1
        if tower4.healthtowers['tower4']>0:
            if 670 < self.x < 753:
                self.x += 1
            if 753 < self.x < 865:
                self.x -=1
            if 180 < self.y < 680 and self.x == 753:
                self.y -= 1
        if tower3.healthtowers['tower3']<=0 :
            if 470 < self.x < 536 and self.y !=180 and self.y !=90:
                self.x += 1
            if 536 < self.x < 670 and self.y!=180 and self.y != 90:
                self.x -= 1
            if self.y == 90 and self.x < 595:
                self.x += 1
            if self.y > 90 and tower4.healthtowers['tower4']<=0:
                self.y -= 1
        if tower4.healthtowers['tower4']<=0:
            if 670 < self.x < 753 and self.y!=90  and self.y!=180:
                self.x += 1
            if 753 < self.x < 865 and self.y !=90 and self.y !=180:
                self.x -=1
            if self.y == 90 and self.x > 690:
                self.x -= 1
            if self.y > 90 and tower3.healthtowers['tower3']<=0:
                self.y -= 1
    def healthheroes(self):
        if self.y == 260 and self.x == 536:
            if int(timer) % 2 == 0 and self.health[str(self.image)] > 0 and tower3.healthtowers['tower3'] > 0:
                tower3.fireUpToDown()
                if self.image == 'Wizard':
                    tower3.healthtowers['tower3'] -= 4
                if self.image == 'Archer':
                    tower3.healthtowers['tower3'] -= 2
                if self.image == 'Musketters':
                    tower3.healthtowers['tower3'] -= 4
                if self.image == 'hunter':
                    tower3.healthtowers['tower3'] -= 4
                self.fireDownToUp()
                self.drawBulletDownToUp()
                self.health[str(self.image)] -= 5

        if self.y == 260 and self.x == 753 and self.health[str(self.image)] > 0 and tower4.healthtowers['tower4'] > 0:
            if int(timer) % 2 == 0:
                tower4.fireUpToDown()
                if self.image == 'Wizard':
                    tower4.healthtowers['tower4'] -= 4
                if self.image == 'Archer':
                    tower4.healthtowers['tower4'] -= 2
                if self.image == 'Musketters':
                    tower4.healthtowers['tower4'] -= 4
                if self.image == 'hunter':
                    tower4.healthtowers['tower4'] -= 4
                self.fireDownToUp()
                self.drawBulletDownToUp()
                self.health[str(self.image)] -= 5
        if self.y == 325 and self.x == 536 and self.health[str(self.image)] > 0 and tower1.healthtowers['tower1'] > 0:
            if int(timer) % 2 == 0:
                tower1.fireDownToUp()
                self.fireUpToDown()
                self.drawBulletUpToDown()
                if self.image == 'Wizard':
                    tower1.healthtowers['tower1'] -= 4
                if self.image == 'Archer':
                    tower1.healthtowers['tower1'] -= 2
                if self.image == 'Musketters':
                    tower1.healthtowers['tower1'] -= 4
                if self.image == 'hunter':
                    tower1.healthtowers['tower1'] -= 4
                self.health[str(self.image)] -= 5

        elif self.y == 325 and self.x == 753 and self.health[str(self.image)] > 0 and tower2.healthtowers['tower2'] > 0:
            if int(timer) % 2 == 0:
                tower2.fireDownToUp()
                self.fireUpToDown()
                self.drawBulletUpToDown()
                if self.image == 'Wizard':
                    tower3.healthtowers['tower2'] -= 4
                if self.image == 'Archer':
                    tower3.healthtowers['tower2'] -= 2
                if self.image == 'Musketters':
                    tower3.healthtowers['tower2'] -= 4
                if self.image == 'hunter':
                    tower3.healthtowers['tower2'] -= 4
                self.health[str(self.image)] -= 5
        elif self.y == 180 and self.x == 650 and self.health[str(self.image)]>0 and main_towerUp.healthtowers['main_towerUp']>0:
            if int(timer)%2 == 0:
                main_towerUp.fireUpToDown()
                main_towerUp.drawFrommainTowerU()
                self.health[str(self.image)] -= 5
                self.fireTomainTowerUp()
                self.drawTomainTowerUp()
                if self.image == 'Wizard':
                    main_towerUp.healthtowers['main_towerUp'] -= 4
                if self.image == 'Archer':
                    main_towerUp.healthtowers['main_towerUp'] -= 2
                if self.image == 'Musketeers':
                    main_towerUp.healthtowers['main_towerUp'] -= 4
                if self.image == 'hunter':
                    main_towerUp.healthtowers['main_towerUp'] -= 4
        elif self.y == 385 and self.x == 650 and self.health[str(self.image)]>0 and main_towerDown.healthtowers['main_towerDown']>0:
            if int(timer)%2 == 0:
                main_towerDown.fireDownToUp()
                main_towerDown.drawFrommainTowerD()
                self.health[str(self.image)] -= 5
                self.fireTomainTowerDown()
                self.drawTomainTowerDown()
                if self.image == 'Wizard':
                    main_towerDown.healthtowers['main_towerDown'] -= 4
                if self.image == 'Archer':
                    main_towerDown.healthtowers['main_towerDown'] -= 2
                if self.image == 'Musketeers':
                    main_towerDown.healthtowers['main_towerDown'] -= 4
                if self.image == 'hunter':
                    main_towerDown.healthtowers['main_towerDown'] -= 4
        if self.health[str(self.image)] <= 0:
            return False
        else:
            return True

    def healthheroesUnarmed(self):
        if self.y == 180 and self.x == 536:
            if int(timer) % 2 == 0 and self.health[str(self.image)] > 0 and tower3.healthtowers['tower3'] > 0:
                tower3.fireforUnarmed(550, 170)
                if self.image == 'Knight':
                    tower3.healthtowers['tower3'] -= 4
                if self.image == 'giant':
                    tower3.healthtowers['tower3'] -= 7
                if self.image == 'hog':
                    tower3.healthtowers['tower3'] -= 5
                if self.image == 'Barbarian':
                    tower3.healthtowers['tower3'] -= 6
                self.fireDownToUp()
                self.drawBulletDownToUp()
                self.health[str(self.image)] -= 5
        if self.y == 180 and self.x == 753 and self.health[str(self.image)] > 0 and tower4.healthtowers['tower4'] > 0:
            if int(timer) % 2 == 0:
                tower4.fireforUnarmed(765, 170)
                if self.image == 'Knight':
                    tower4.healthtowers['tower4'] -= 4
                if self.image == 'giant':
                    tower4.healthtowers['tower4'] -= 7
                if self.image == 'hog':
                    tower4.healthtowers['tower4'] -= 5
                if self.image == 'Barbarian':
                    tower4.healthtowers['tower4'] -= 6
                self.fireDownToUp()
                self.drawBulletDownToUp()
                self.health[str(self.image)] -= 5
        if self.y == 385 and self.x == 536 and self.health[str(self.image)] > 0 and tower1.healthtowers['tower1'] > 0:
            if int(timer) % 2 == 0:
                tower1.fireforUnarmed(550, 410)
                self.fireUpToDown()
                self.drawBulletUpToDown()
                if self.image == 'Knight':
                    tower1.healthtowers['tower1'] -= 4
                if self.image == 'giant':
                    tower1.healthtowers['tower1'] -= 7
                if self.image == 'hog':
                    tower1.healthtowers['tower1'] -= 5
                if self.image == 'Barbarian':
                    tower1.healthtowers['tower1'] -= 6
                self.health[str(self.image)] -= 5

        elif self.y == 385 and self.x == 753 and self.health[str(self.image)] > 0 and tower2.healthtowers['tower2'] > 0:
            if int(timer) % 2 == 0:
                tower2.fireforUnarmed(765, 410)
                self.fireUpToDown()
                self.drawBulletUpToDown()
                if self.image == 'Knight':
                    tower2.healthtowers['tower2'] -= 4
                if self.image == 'giant':
                    tower2.healthtowers['tower2'] -= 7
                if self.image == 'hog':
                    tower2.healthtowers['tower2'] -= 5
                if self.image == 'Barbarian':
                    tower2.healthtowers['tower2'] -= 6
                self.health[str(self.image)] -= 5
        elif self.y == 90 and self.x == 595 and self.health[str(self.image)]>0 and main_towerUp.healthtowers['main_towerUp']>0:
            if int(timer)%2 == 0:
                bullet2 = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet2,(625,90))
                self.surface.blit(bullet2,(625,100))
                self.health[str(self.image)] -= 5
                if self.image == 'Knight':
                    main_towerUp.healthtowers['main_towerUp'] -= 4
                if self.image == 'giant':
                    main_towerUp.healthtowers['main_towerUp'] -= 7
                if self.image == 'hog':
                    main_towerUp.healthtowers['main_towerUp'] -= 5
                if self.image == 'Barbarian':
                    main_towerUp.healthtowers['main_towerUp'] -= 6
        elif self.y == 90 and self.x == 690 and self.health[str(self.image)]>0 and main_towerUp.healthtowers['main_towerUp']>0:
            if int(timer)%2 == 0:
                bullet2 = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet2,(680,90))
                self.surface.blit(bullet2,(680,100))
                self.health[str(self.image)] -= 5
                if self.image == 'Knight':
                    main_towerUp.healthtowers['main_towerUp'] -= 4
                if self.image == 'giant':
                    main_towerUp.healthtowers['main_towerUp'] -= 7
                if self.image == 'hog':
                    main_towerUp.healthtowers['main_towerUp'] -= 5
                if self.image == 'Barbarian':
                    main_towerUp.healthtowers['main_towerUp'] -= 6
        elif self.y == 490 and self.x == 595 and self.health[str(self.image)]>0 and main_towerDown.healthtowers['main_towerDown']>0:
            if int(timer)%2 == 0:
                bullet2 = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet2,(625,515))
                self.surface.blit(bullet2,(625,505))
                self.health[str(self.image)] -= 5
                if self.image == 'Knight':
                    main_towerDown.healthtowers['main_towerDown'] -= 4
                if self.image == 'giant':
                    main_towerDown.healthtowers['main_towerDown'] -= 7
                if self.image == 'hog':
                    main_towerDown.healthtowers['main_towerDown'] -= 5
                if self.image == 'Barbarian':
                    main_towerDown.healthtowers['main_towerDown'] -= 6
        elif self.y == 490 and self.x == 690 and self.health[str(self.image)]>0 and main_towerDown.healthtowers['main_towerDown']>0:
            if int(timer)%2 == 0:
                bullet2 = self.pygame.image.load('bullet2.png')
                self.surface.blit(bullet2,(680,515))
                self.surface.blit(bullet2,(680,505))
                self.health[str(self.image)] -= 5
                if self.image == 'Knight':
                    main_towerDown.healthtowers['main_towerDown'] -= 4
                if self.image == 'giant':
                    main_towerDown.healthtowers['main_towerDown'] -= 7
                if self.image == 'hog':
                    main_towerDown.healthtowers['main_towerDown'] -= 5
                if self.image == 'Barbarian':
                    main_towerDown.healthtowers['main_towerDown'] -= 6
        if self.health[str(self.image)] <= 0:
            return False
        else:
            return True
    def fireTomainTowerUp(self):
        self.Bullets.append(Bullet(self.x,self.y,self.pygame,self.surface))
    def drawTomainTowerUp(self):
        for i in self.Bullets:
            i.moveToUp()
            i.drawTomainTowerUp()
    def fireTomainTowerDown(self):
        self.Bullets.append(Bullet(self.x, self.y, self.pygame, self.surface))
    def drawTomainTowerDown(self):
        for i in self.Bullets:
            i.moveToDown()
            i.drawTomainTowerDown()
    def fireDownToUp(self):
        self.Bullets.append(Bullet(self.x, self.y, self.pygame, self.surface))

    def drawBulletDownToUp(self):
        for i in self.Bullets:
            i.moveToUp()
            i.drawbullets2()

    def fireUpToDown(self):
        self.Bullets.append(Bullet(self.x, self.y, self.pygame, self.surface))

    def drawBulletUpToDown(self):
        for i in self.Bullets:
            i.moveToDown()
            i.drawbullets1()


class tower():
    def __init__(self, x, y, pygame, surface):
        self.x = x
        self.y = y
        self.pygame = pygame
        self.surface = surface
        self.BulletsUpToDown = []
        self.BulletDownToUp = []
        self.healthtowers = {'tower1': 2786, 'tower2': 2786, 'tower3': 2786, 'tower4': 2786,'main_towerUp':3000 ,'main_towerDown':3000}
    def fireUpToDown(self):
        self.BulletsUpToDown.append(Bullet(self.x, self.y, self.pygame, self.surface))

    def drawUpToDown(self):
        for i in self.BulletsUpToDown:
            i.moveToDown()
            i.drawbulletUpToDown()

    def fireDownToUp(self):
        self.BulletDownToUp.append(Bullet(self.x, self.y, self.pygame, self.surface))

    def drawDownToUp(self):
        for i in self.BulletDownToUp:
            i.moveToUp()
            i.drawbulletDownToUp()
    def fireforUnarmed(self, x, y):
        bulletimage = self.pygame.image.load('bullet.png')
        self.surface.blit(bulletimage, (x, y))
    def drawFrommainTowerU(self):
        for i in self.BulletsUpToDown:
            i.moveToDown()
            i.drawFrommainTowerUp()
    def drawFrommainTowerD(self):
        for i in self.BulletDownToUp:
            i.moveToUp()
            i.drawFrommainTowerDown()


class Bullet():
    def __init__(self, x, y, pygame, surface):
        self.x = x
        self.y = y
        self.pygame = pygame
        self.surface = surface
        self.speed = 10

    def moveToUp(self):
        self.y -= self.speed

    def moveToDown(self):
        self.y += self.speed

    def drawbulletUpToDown(self):
        if self.y < 250:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage, (self.x, self.y))

    def drawbulletDownToUp(self):
        if self.y > 350:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage, (self.x, self.y))

    def drawbullets2(self):
        if self.y > 152:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage, (self.x, self.y))

    def drawbullets1(self):
        if self.y < 420:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage, (self.x, self.y))
    def drawTomainTowerUp(self):
        if self.y > 108:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage, (self.x, self.y))
    def drawFrommainTowerDown(self):
        if self.y > 410:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage, (self.x, self.y))
    def drawFrommainTowerUp(self):
        if self.y <180:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage, (self.x, self.y))
    def drawTomainTowerDown(self):
        if self.y < 480:
            bulletimage = self.pygame.image.load('bullet.png')
            self.surface.blit(bulletimage, (self.x, self.y))


windowwidth = 1280
windowheight = 605
window = pygame.display.set_mode((windowwidth, windowheight), pygame.FULLSCREEN)
battleScreen = pygame.image.load('battle Screen.jpg')
start_Screen = pygame.image.load('start_Screen.jpg')
guidance = pygame.image.load('guidance.png')
blue_winner = pygame.image.load('blue winner.png')
red_winner = pygame.image.load('red winner.png')
one = pygame.image.load('1.png')
two = pygame.image.load('2.png')
three = pygame.image.load('3.png')
blue_crown = pygame.image.load('blue_crown.png')
red_crown = pygame.image.load('red_crown.png')
timer_icon = pygame.image.load('timer_icon.png')
timer_box = pygame.image.load('timer_box.png')
elixir = pygame.image.load('elixir.jpg')
destroyed_tower = pygame.image.load('tower destroyed.jpg')
victory_sound = pygame.mixer.Sound('victory_sound.ogg')
player = player(windowwidth / 2, windowheight / 2, pygame, window)
player2 = player2(windowwidth / 2, windowheight / 2, pygame, window)
start_sound = pygame.mixer.Sound('menu.ogg')
start_sound.play(-1)
bullet = pygame.image.load('bullet.png')
box = pygame.image.load('box.jpg')
box2 = pygame.image.load('box.jpg')
battle_sound = pygame.mixer.Sound('battle.ogg')
pygame.joystick.init()
tower1 = tower(548, 420, pygame, window)
tower2 = tower(765, 420, pygame, window)
tower3 = tower(548, 148, pygame, window)
tower4 = tower(765, 148, pygame, window)
main_towerUp = tower(670,104,pygame,window)
main_towerDown = tower(670,500,pygame,window)


def destroyedTower():
    if tower1.healthtowers['tower1'] <= 0:
        window.blit(destroyed_tower, (500, 420))
    if tower2.healthtowers['tower2'] <= 0:
        window.blit(destroyed_tower, (720, 420))
    if tower3.healthtowers['tower3'] <= 0:
        window.blit(destroyed_tower, (500, 102))
    if tower4.healthtowers['tower4'] <= 0:
        window.blit(destroyed_tower, (720, 100))
    if  main_towerUp.healthtowers['main_towerUp'] <= 0:
        window.blit(destroyed_tower, (617 , 49))
    if main_towerDown.healthtowers['main_towerDown'] <= 0 :
         window.blit(destroyed_tower, (605, 470))

check_win = False
def draw_game():
    global score1, score2, score3, score4 ,score5 ,score6
    global hat, x, y
    window.blit(battleScreen, (0, 0))
    window.blit(box, (934, 475))
    window.blit(box2, (11, 67))
    window.blit(timer_icon, (10, 20))
    window.blit(timer_box, (80, 20))
    destroyedTower()

    score1 = False
    score2 = False
    score3 = False
    score4 = False
    score5 = False
    score6 = False
    # window.blit(two, (150, 350))
    # window.blit(one, (0, 0))
    if tower1.healthtowers['tower1'] <= 0 or tower2.healthtowers['tower2'] <= 0:
        score1 = True
    if tower1.healthtowers['tower1'] <= 0 and tower2.healthtowers['tower2'] <= 0:
        score1 = False
        score2 = True
    if score2 == True and main_towerDown.healthtowers['main_towerDown'] <= 0:
        score5 = True
    if tower3.healthtowers['tower3'] <= 0 or tower4.healthtowers['tower4'] <= 0:
        score3 = True
    if tower3.healthtowers['tower3'] <= 0 and tower4.healthtowers['tower4'] <= 0:
        score3 = False
        score4 = True
    if score4 == True and main_towerUp.healthtowers['main_towerUp'] <= 0 :
        score6 = True
    if score1 == True:
        window.blit(one, (1050, 213))
        window.blit(red_crown, (1050, 177))
    if score2 == True:
        window.blit(two, (1040, 205))
        window.blit(red_crown, (1050, 177))
    if score3 == True:
        window.blit(one, (1050, 350))
        window.blit(blue_crown, (1050, 310))
    if score4 == True:
        window.blit(two, (1040, 340))
        window.blit(blue_crown, (1050, 310))
    if score1 == False and score2 == False:
        window.blit(red_crown, (1050, 200))
        # window.blit(zero , (1060,213))
    if score3 == False and score4 == False:
        window.blit(blue_crown, (1050, 333))
        # window.blit(zero , (1055,350))
    if score5 == True:
        window.blit(three, (1040, 205))
        window.blit(red_crown, (1050, 177))
    if score6 == True:
        window.blit(three, (1040, 340))
        window.blit(blue_crown, (1050, 310))
    player.push()
    player2.push()
    player.click(L1, L2, R1, R2, X, x1, y1)
    player.drawsoldier()
    player2.click(L12, L22, R12, R22, X2, x2, y2)
    player2.drawsoldier()
    tower1.drawDownToUp()
    tower2.drawDownToUp()
    tower3.drawUpToDown()
    tower4.drawUpToDown()

def winning_match():
    global check_win
    if main_towerDown.healthtowers['main_towerDown'] <= 0 :
        check_win = True
        window.blit(red_winner, (130,0))
    if main_towerUp.healthtowers['main_towerUp'] <= 0 :
        check_win = True
        window.blit(blue_winner, (130,0))


counter = 0
match_draw = False
if match_draw == False :
    timer = 100
    dt = 0

def timer2():
    global timer,dt ,counter, match_draw, check_win
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    blue = pygame.Color('red')
    if counter == 1 and score1 == score2 == score3 == score4 == False:
        match_draw = True
    timer -= dt
    if timer <= 0:
        timer = 0
        counter = 1
        if match_draw == True:
            timer = 60
            dt = 0
    if match_draw == True:
        if score1 == True :
            check_win = True

        if score3 == True:
            check_win = True

    txt = font.render(str(round(timer, 1)), True, blue)
    window.blit(txt, (90, 30))
    dt = clock.tick(250) / 100

draw_guidance = False
start_battle = False
x1 = 640
y1 = 395
x2 = 665
y2 = 273
playSound = True
while True:
    mouseState = pygame.mouse.get_pressed()
    mousepos = pygame.mouse.get_pos()
    #print(mousepos)
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if 460 < mousepos[0] < 780 and 185 < mousepos[1] < 277 and mouseState[0] == True:
            start_battle = False
            draw_guidance = True
        if 483 < mousepos[0] < 777 and 465 < mousepos[1] < 574 and mouseState[0] == True:
            start_battle = True
            start_sound.stop()
            if playSound == True :
                battle_sound.play(-1)
                playSound = False
    joystuck_count = pygame.joystick.get_count()
    # for i in range(1):
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    hats = joystick.get_numhats()
    hat = joystick.get_hat(0)
    butttons = joystick.get_numbuttons()
    L1 = joystick.get_button(4)
    L2 = joystick.get_button(5)
    R1 = joystick.get_button(6)
    R2 = joystick.get_button(7)
    X = joystick.get_button(2)
    joystick = pygame.joystick.Joystick(1)
    joystick.init()
    hats2 = joystick.get_numhats()
    hat2 = joystick.get_hat(0)
    butttons2 = joystick.get_numbuttons()
    L12 = joystick.get_button(4)
    L22 = joystick.get_button(5)
    R12 = joystick.get_button(6)
    R22 = joystick.get_button(7)
    X2 = joystick.get_button(2)
    winning_match()
    if start_battle == True:
        if hat[0] == 1:
            x1 += 5
        if hat[0] == -1:
            x1 -= 5
        if hat[1] == 1:
            y1 -= 5
        if hat[1] == -1:
            y1 += 5
        if hat2[0] == 1:
            x2 += 5
        if hat2[0] == -1:
            x2 -= 5
        if hat2[1] == 1:
            y2 -= 5
        if hat2[1] == -1:
            y2 += 5
        if check_win == False :
            draw_game()
            timer2()

        if check_win == True:
            battle_sound.stop()
            victory_sound.play(-1)
            if score1 == True:
                window.blit(red_winner, (130, 0))
            if score3 == True:
                window.blit(blue_winner, (130, 0))

    elif draw_guidance == True:
        window.blit(guidance,(100,0))
        if 117 < mousepos[0] < 252 and 58 < mousepos[1] < 188 and mouseState[0] == True:
            start_battle = True
            start_sound.stop()
            if playSound == True:
                battle_sound.play(-1)
                playSound = False
    else:
        window.blit(start_Screen, (0, 0))
    pygame.display.update()
