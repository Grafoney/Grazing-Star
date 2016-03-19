#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pyglet

from character import Character


class Animate:
    @staticmethod
    def create_animated_sprite():
        """Create animation"""
        char = Character()
        sprites = char.create_sprites("Images/player.png", "Images/player2.png")

        source = pyglet.image.Animation.from_image_sequence(sprites, 0.5, True)
        sprite = pyglet.sprite.Sprite(source)
        return sprite
