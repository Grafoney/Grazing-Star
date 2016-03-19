#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pyglet


class Character:
    @staticmethod
    def create_sprites(*args):
        # Load sprites
        sprites = []
        for img_path in args:
            image = pyglet.resource.image(img_path)
            sprites.append(image)
        return sprites
