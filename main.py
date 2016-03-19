#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pyglet
import pyglet.window.key
from pyglet import clock
from random import randint


class Character():
    def ImageSource(self, *args):
        ''' Load sprites '''
        # Надо сделать так, чтобы ставилось столько спрайтов, сколько укажешь
        image0 = pyglet.resource.image(args)
        image1 = pyglet.resource.image(args)
        sprites = [image0, image1]
        return sprites

    def Animation(self, sprites):
        ''' Create animation '''
        source = pyglet.image.Animation.from_image_sequence(sprites, 0.5, True)
        sprite = pyglet.sprite.Sprite(source)
        return sprite


# Set refresh rate
clock.set_fps_limit(60)

# Create and open a window
window = pyglet.window.Window(caption='Pyglet test', width=480, height=640)

# Make control
key = pyglet.window.key
keyboard = key.KeyStateHandler

# Load sprites
s0 = pyglet.resource.image('Images/hero.png')
s1 = pyglet.resource.image('Images/hero2.png')
sprites = [s0, s1]
'''
enemy0 = pyglet.resource.image('Images/enemy.png')
enemy1 = pyglet.resource.image('Images/enemy2.png')
enemySprites = [enemy0, enemy1]
'''

# Animation
anim = pyglet.image.Animation.from_image_sequence(sprites, 0.5, True)
sprite = pyglet.sprite.Sprite(anim)

# Start position of the sprites
sprite.x, sprite.y = 0, 0
x_velocity, y_velocity = 0, 0


def update_position(event):
    ''' Set the new positions of the sprites '''
    global x_velocity, y_velocity

    sprite.x += x_velocity
    sprite.y += y_velocity
    enemySprite.x += x_velEnemy
    enemySprite.y += y_velEnemy

    # Check borders of screen for player
    if sprite.x < 0:
        x_velocity = 0
        sprite.x = 0

    elif sprite.x > 440:
        x_velocity = 0
        sprite.x = 440

    elif sprite.y < 0:
        y_velocity = 0
        sprite.y = 0

    elif sprite.y > 590:
        y_velocity = 0
        sprite.y = 590

# The enemy
img = pyglet.resource.image('Images/enemy.png')
enemySprite = pyglet.sprite.Sprite(img)
enemySprite.x, enemySprite.y = 200, 300
x_velEnemy, y_velEnemy = randint(-50, 50), randint(-50, 50)


def update_enemy_position(event):
    ''' Update enemy position and generate the new one'''
    global x_velEnemy, y_velEnemy
    # Check borders of screen for enemy
    if enemySprite.x <= 0:
        enemySprite.x = 0
        x_velEnemy = randint(0, 50)
        y_velEnemy = randint(-50, 50)

    elif enemySprite.x >= 440:
        enemySprite.x = 440
        x_velEnemy = randint(-50, 0)
        y_velEnemy = randint(-50, 50)

    elif enemySprite.y <= 0:
        enemySprite.y = 0
        y_velEnemy = randint(0, 50)
        x_velEnemy = randint(-50, 50)

    elif enemySprite.y >= 590:
        enemySprite.y = 590
        y_velEnemy = randint(-50, 0)
        x_velEnemy = randint(-50, 50)


def check_collision(event):
    '''Check collision between player and enemy'''
    if sprite.x == enemySprite.x and sprite.y == enemySprite.y:
        print("BANG!")
    # print("Checking...")


@window.event
def on_key_press(symbol, modifier):
    global x_velocity, y_velocity
    if symbol == key.LEFT:
        x_velocity -= 10

    elif symbol == key.RIGHT:
        x_velocity += 10

    elif symbol == key.UP:
        y_velocity += 10

    elif symbol == key.DOWN:
        y_velocity -= 10


@window.event
def on_draw():
    window.clear()
    sprite.draw()
    enemySprite.draw()

if __name__ == '__main__':
    # Call update a position every .10 seconds
    clock.schedule_interval(update_position, .10)
    clock.schedule_interval(update_enemy_position, .10)
    clock.schedule_interval(check_collision, .10)

    pyglet.app.run()
