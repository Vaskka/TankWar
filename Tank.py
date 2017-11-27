import pygame
from pygame.sprite import Sprite
class Tank(Sprite):
    '''The tank class'''
    def __init__(self, screen):
        self.screen = screen

        self.image_up_address = 'images/tank_up.bmp' 
        self.image_left_address = 'images/tank_left.bmp'
        self.image_down_address = 'images/tank_down.bmp'
        self.image_right_address = 'images/tank_right.bmp'

        #image and rect
        self.image = pygame.image.load(self.image_up_address)
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #move
        self.can_move_up = False
        self.can_move_left = False
        self.can_move_down = False
        self.can_move_right = False    
        #direction
        #1-up 2-left 3-down 4-right
        self.direction = 1

        #x and y
        self.x = self.rect.centerx
        self.y = self.rect.y

        #is fire
        self.fire = False
        '''
        #block direction 0:none 1:block
        self.block_up_direction = False
        self.block_left_direction = False
        self.block_down_direction = False
        self.block_right_direction = False
        '''

        '''
        #move
        self.move_up = False
        self.move_left = False
        self.move_down = False
        self.move_right = False
        '''
        '''
        #1-up 2-left 3-down 4-right
        self.direction = 1	
        '''
    def blit_tank(self):
        self.screen.blit(self.image, self.rect)

    def update_tank(self, ai_settings):
        if (self.can_move_up and self.direction == 1) and self.rect.top >= self.screen_rect.top:
            #go to up direction
            self.image = pygame.image.load(self.image_up_address)
            self.rect.y -= ai_settings.tank_speed
        elif (self.can_move_left and self.direction == 2) and self.rect.left > self.screen_rect.left:
            #go to left direction
            self.image = pygame.image.load(self.image_left_address)
            self.rect.centerx -= ai_settings.tank_speed
        elif (self.can_move_down and self.direction == 3) and self.rect.bottom <= self.screen_rect.bottom:
            #go to down direction
            self.image = pygame.image.load(self.image_down_address)
            self.rect.y += ai_settings.tank_speed
        elif (self.can_move_right and self.direction == 4) and self.rect.right < self.screen_rect.right:
            #go to right direction
            self.image = pygame.image.load(self.image_right_address)
            self.rect.right += ai_settings.tank_speed


    def reset_tank(self, screen, direction):
        self.image = pygame.image.load(self.image_down_address)

        #put it into the top of the screen 
        self.rect.centerx = screen.get_rect().centerx
        self.rect.top = screen.get_rect().top
        #set the tank's direction
        self.direction = direction

    def center_tank_A(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def center_tank_B(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    #get the position point (top, bottom -> y %<>% left, right -> x )

    def get_top_point(self):
        return (self.rect.left + int((self.rect.right - self.rect.left) / 2), self.rect.top)

    def get_left_point(self):
        return (self.rect.left, self.rect.top + int((self.rect.bottom - self.rect.top) / 2))

    def get_bottom_point(self):
        return (self.rect.left + int((self.rect.right - self.rect.left) / 2), self.rect.bottom)

    def get_right_point(self):
        return (self.rect.right, self.rect.top + int((self.rect.bottom - self.rect.top) / 2))
