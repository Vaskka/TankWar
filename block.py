import pygame
import settings
from pygame.sprite import Sprite

class Block(Sprite):

    def __init__(self, screen, ai_settings):
        super(Block, self).__init__()
        self.screen = screen
        self.side = ai_settings.block_side

        # 0:common_block  1:A' big_over  2:B's big_over 
        self.big_over = 0;
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(ai_settings.block_img_1)
        self.rect = self.image.get_rect()

        #common position
        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom

    def reset_to_big_over_A(self, ai_settings):
        new_image = pygame.image.load(ai_settings.block_img_big_over_1)
        self.image = new_image
        self.rect = new_image.get_rect()


    def reset_to_big_over_B(self, ai_settings):
        new_image = pygame.image.load(ai_settings.block_img_big_over_2)
        self.image = new_image
        self.rect = new_image.get_rect()

    def set_A_big_over_position(self):
        self.rect.bottom = self.screen_rect.bottom
        self.rect.right = self.screen_rect.right

    def set_B_big_over_position(self):
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left

    def show(self):
        '''
        t = self.rect.x
        self.rect.x = self.rect.y
        self.rect.y = t
        '''
        self.screen.blit(self.image, self.rect)
        
