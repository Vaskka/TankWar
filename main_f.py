'''main_f.py'''

import sys
import pygame
from bullet import Bullet
from pygame.sprite import Sprite
from block import Block

def deal_with_keydown_event(event, tank, screen, ai_settings, bullets, block):
    if event.key == ai_settings.A_up:
        tank[0].can_move_up = True
        tank[0].direction = 1
    elif event.key == ai_settings.A_left:
        tank[0].can_move_left = True
        tank[0].direction = 2
    elif event.key == ai_settings.A_down:
        tank[0].can_move_down = True
        tank[0].direction = 3
    elif event.key == ai_settings.A_right:
        tank[0].can_move_right = True
        tank[0].direction = 4
    elif event.key == ai_settings.A_fire:
        #new_bullet = Bullet(screen, ai_settings, tank)
        bullets.add(Bullet(screen, ai_settings, tank[0]))
    elif event.key == ai_settings.B_up:
        tank[1].can_move_up = True
        tank[1].direction = 1
    elif event.key == ai_settings.B_left:
        tank[1].can_move_left = True
        tank[1].direction = 2
    elif event.key == ai_settings.B_down:
        tank[1].can_move_down = True
        tank[1].direction = 3
    elif event.key == ai_settings.B_right:
        tank[1].can_move_right = True
        tank[1].direction = 4
    elif event.key == ai_settings.B_fire:
        #new_bullet = Bullet(screen, ai_settings, tank)
        new_B_Bullet = Bullet(screen, ai_settings, tank[1])
        new_B_Bullet.reset_bullet_from()
        bullets.add(new_B_Bullet)


def deal_with_keyup_event(event, tank, ai_settings):
    if event.key == ai_settings.A_up:
        tank[0].can_move_up = False
    elif event.key == ai_settings.A_left:
        tank[0].can_move_left = False
    elif event.key == ai_settings.A_down:
        tank[0].can_move_down = False
    elif event.key == ai_settings.A_right:
        tank[0].can_move_right = False
    elif event.key == ai_settings.B_up:
        tank[1].can_move_up = False
    elif event.key == ai_settings.B_left:
        tank[1].can_move_left = False
    elif event.key == ai_settings.B_down:
        tank[1].can_move_down = False
    elif event.key == ai_settings.B_right:
        tank[1].can_move_right = False



def check_event(tank, screen, ai_settings, bullets, block):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            deal_with_keydown_event(event, tank, screen, ai_settings, bullets, block)
        elif event.type == pygame.KEYUP:
            deal_with_keyup_event(event, tank, ai_settings)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass

def updata_bullets(big_over_A, big_over_B, bullets, tank, block, tank_map, ai_settings, screen):
    for b in bullets:
        b.updata_bullet()

    for bu in bullets.copy():
        if bu.rect.bottom <= 0:
            bullets.remove(bu)
        elif bu.rect.right <= 0:
            bullets.remove(bu)
        elif bu.rect.left <= 0:
            bullets.remove(bu)
        elif bu.rect.top <= 0:
            bullets.remove(bu)
    #check if tank and bullets collision
    check_bigover(big_over_A, big_over_B, bullets, tank, block, tank_map, ai_settings, screen)
    check_tank_bullet_collision(tank, bullets)
    check_block_bullet_collision(block, bullets)

def check_bigover(big_over_A, big_over_B, bullets, tank, block, tank_map, ai_settings, screen):
    if pygame.sprite.spritecollide(big_over_A, bullets, True):
        restart_game(tank, block, tank_map, ai_settings, screen)
    elif pygame.sprite.spritecollide(big_over_B, bullets, True):
        restart_game(tank, block, tank_map, ai_settings, screen)

def restart_game(tank, block, tank_map, ai_settings, screen):
    tank[0].center_tank_A()
    tank[1].center_tank_B()

    block.empty()
    init_map(tank_map, block, screen, ai_settings)

def check_tank_bullet_collision(tank, bullets):
    for ct in tank:
        if pygame.sprite.spritecollideany(ct, bullets):
            if (ct is tank[0]) and (get_collision_bullet(ct, bullets).from_which_tank == 2):
                tank_hit(ct, tank, bullets)
            elif (ct is tank[1]) and (get_collision_bullet(ct, bullets).from_which_tank == 1):
                tank_hit(ct, tank, bullets)

def check_block_bullet_collision(block, bullets):
    for bu in bullets.copy():
        for bl in block.copy():
            if pygame.sprite.collide_rect(bl, bu):
                block.remove(bl)
                bullets.remove(bu)

def init_map(tank_map, block, screen, ai_settings):
    for new_point in tank_map.block_info:
        new_block = Block(screen, ai_settings)
        new_block.rect.x = new_point[0]
        new_block.rect.y = new_point[1]
        block.add(new_block)
    '''
    for bl in block:
        t = bl.rect.x
        bl.rect.x = bl.rect.y
        bl.rect.y = t
    '''
def updata_blocks(block):
    for bl in block:
        bl.show()

def get_collision_bullet(tank, bullets):
    for b in bullets:
        if pygame.sprite.collide_rect(tank, b):
            return b

def tank_hit(ct, tank, bullets):
    if ct is tank[0]:
        ct.center_tank_A()
        restart(bullets)
    else:
        ct.center_tank_B()
        restart(bullets)

def updata_tanks(tank, block, ai_settings):

    for tk in tank:
        #switch the direction
        #check if this direction can move
        #if not close the 'switch'
        if tk.direction == 1:
            for bl in block:
                if bl.rect.collidepoint(tk.get_top_point()):
                    #print('up')
                    tk.can_move_up = False
        if tk.direction == 2:
            for bl in block:
                if bl.rect.collidepoint(tk.get_left_point()):
                    #print('left')
                    tk.can_move_left = False
        if tk.direction == 3:
            for bl in block:
                if bl.rect.collidepoint(tk.get_bottom_point()):
                    #print('down')
                    tk.can_move_down = False
        if tk.direction == 4:
            for bl in block:
                if bl.rect.collidepoint(tk.get_right_point()):
                    #print('right')
                    tk.can_move_right = False

    for tank_all in tank:
        tank_all.update_tank(ai_settings)
        tank_all.blit_tank()

def updata_screen(screen, ai_settings, bullets):
    screen.blit(ai_settings.screen_background, (0, 0))
    for b in bullets.sprites():
        b.draw_bullet()

def updata_all():
    pygame.display.update()

def restart(bullets):
    for b in bullets:
        bullets.remove(b)
