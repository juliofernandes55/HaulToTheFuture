#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option  # opção do menu
        self.entity_list = list[Entity]()
        self.entity_list.extend(EntityFactory.get_entity('bground'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 30000
        pygame.time.set_timer(EVENT_ENEMY, 2000, )

    def run(self, ):
        pygame.mixer_music.load('./asset/Levelsong.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))
                    self.entity_list.append(EntityFactory.get_entity('Enemy2'))

            self.level_text(14, f'{self.name} - TIMEOUT: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (80, 5))
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', COLOR_WHITE, (18, WIN_HEIGHT - 35))
            self.level_text(14, f'ENTIDADES: {len(self.entity_list)}', COLOR_WHITE, (38, WIN_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
