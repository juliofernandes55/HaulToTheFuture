#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH


class entityFactory:
    pass

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'bground':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'bground{i}.png', (0, 0)))
                    list_bg.append(Background(f'bground{i}.png', (WIN_WIDTH, 0)))
                return list_bg
