'''TankWar.py'''
import pygame
from pygame.sprite import Group
from settings import Settings
import main_f as f
from tank import Tank
from block import Block

from map1 import Map_1

#from pygame.locals import *

def debug(tank):
    print("the tank's bottom is " + str(tank.rect.bottom))
    print("the screen's bottom is " + str(tank.screen_rect.bottom))
    print('0---------------------------------------0')

def run_game():
    
    pygame.init()
    
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.win_height, ai_settings.win_width))
    
    pygame.display.set_caption('TankWar - '+ ai_settings.version)
    
    #screen.fill(ai_settings.bgcolor)
    #background_image = pygame.image.load(ai_settings.background)
    
    #init a new A tank
    tank_A = Tank(screen)

    #set another B tank and reset tank's attribute
    tank_B = Tank(screen)
    tank_B.reset_tank(screen, 3)
    
    #init bullets group
    bullets = Group()
    
    #init blocks group(test)
    block = Group()
    ##block.add(Block(screen, ai_settings))

    #init map
    tank_map = Map_1()
    f.init_map(tank_map, block, screen, ai_settings)

    #init tank with list
    tank = []
    tank.append(tank_A)
    tank.append(tank_B)

    #init the A's big_over
    big_over_A = Block(screen, ai_settings)
    big_over_A.big_over = 1
    big_over_A.reset_to_big_over_A(ai_settings)
    big_over_A.set_A_big_over_position()

    #init the B's big_over
    big_over_B = Block(screen, ai_settings)
    big_over_B.big_over = 2 
    big_over_B.reset_to_big_over_B(ai_settings)
    big_over_B.set_B_big_over_position()

    while True:
        #deal with event
        f.check_event(tank, screen, ai_settings, bullets, block)

        #deal with screen
        f.updata_screen(screen, ai_settings, bullets)

        #deal with tanks
        f.updata_tanks(tank, block, ai_settings)

        #deal with bullets
        f.updata_bullets(big_over_A, big_over_B, bullets, tank, block, tank_map, ai_settings, screen)

        #deal with blocks
        big_over_A.show()
        big_over_B.show()
        f.updata_blocks(block)
        '''
        #for debug
        pygame.draw.rect(screen, (34,255, 0), test_up_rect)
        pygame.draw.rect(screen, (34,255, 0), test_left_rect)
        pygame.draw.rect(screen, (34,255, 0), test_down_rect)
        pygame.draw.rect(screen, (34,255, 0), test_right_rect)
        '''
        #deal with all_screen
        f.updata_all()


run_game()

#python TankWar.py
