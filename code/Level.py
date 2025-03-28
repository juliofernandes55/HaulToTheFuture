#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code import Entity, EntityFactory
from code.Entity import Entity
from code.EntityFactory import entityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option #opção do menu
        self.entity_list = list[Entity]()
        self.entity_list.extend(entityFactory.get_entity('bground'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
