import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, ai_settings, tank):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = tank.rect.centerx
        self.rect.centery = tank.rect.centery
        #self.rect.top = tank.rect.top

        self.x = float(self.rect.center[0])
        self.y = float(self.rect.center[1])

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

        self.direction = tank.direction

        #for denbug(the bullet which is a new one will hit the tank)
        self.just_new = True

        #whether the bullet is from A or B(A:1, B:2)
        self.from_which_tank = 1;

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def updata_bullet(self):
        if self.direction == 1:
            self.y -= self.speed
        elif self.direction == 2:
            self.x -= self.speed
        elif self.direction == 3:
            self.y += self.speed
        elif self.direction == 4:
            self.x += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def reset_bullet_from(self):
        self.from_which_tank = 2;
