# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 00:45:17 2017

@author: czm
"""

'''settings.py'''
import pygame

class Settings():
    def __init__(self):
        
        #basic settings
        self.version = '1.0.0.0'
        self.win_height = 640
        self.win_width = 640
        self.background = 'images/bg1.bmp'
        self.screen_background = pygame.image.load(self.background) 

        #tank
        self.tank_speed = 1

        #bullet speed
        self.bullet_speed = 1.5
        self.bullet_width = 4
        self.bullet_height = 4
        self.bullet_color = 0, 0, 0
        
        #Player A's operator 
        self.A_up = pygame.K_UP
        self.A_left = pygame.K_LEFT
        self.A_down = pygame.K_DOWN
        self.A_right = pygame.K_RIGHT
        self.A_fire = pygame.K_SPACE

        #Player B's operator
        self.B_up = pygame.K_w
        self.B_left = pygame.K_a
        self.B_down = pygame.K_s
        self.B_right = pygame.K_d
        self.B_fire = pygame.K_q

        #Block
        self.block_side = 40
        self.block_img_1 = 'images/Block_1.bmp'
        self.block_img_2 = 'images/Block_2.bmp'
        self.block_img_big_over_1 = 'images/Big_Over_1.bmp'
        self.block_img_big_over_2 = 'images/Big_Over_2.bmp'
        self.block_img_big_over_3 = 'images/Big_Over_3.bmp'
