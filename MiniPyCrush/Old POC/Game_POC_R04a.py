# Will Wagner
# IST341 Final Project - Shapes Game POC
# 4-20-2018

import arcade
import random

# Constants

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

SPRITE_SCALING_GROUND = .28
SPRITE_SCALING_FLOOR = 1
SPRITE_SCALING_WALL = 1

SPRITE_SCALING_PLAYER = .25
SPRITE_SCALING_SPHERE = .5
SPRITE_SCALING_CUBE = 1
SPRITE_SCALING_TRI = 1

# Variables

building_width = 18
building_height = 10

floor_width = 40

wall_height = 40 

master_solidity = 25   # suggested scale between 1 and 100

building_solidity = 1   # suggested scale by decimals to increase number of permanent walls.  
                        # ex: .8 = fewer permanent walls.  1.2 = more permanent walls


# ===  Create Classes for Shapes
# Shapes will be super class and the individual shapes will be inherited

'''
# Shapes
class MShapes():
    def __init__(self, position_x, position_y, change_x, change_y):

    def update(self):
        # Move the Shape
        self.position_y += self.change_y
        self.position_x += self.change_x
'''

class POCGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

        self.player_sprite_list = arcade.SpriteList()

        self.friendlies_list = [ ]
        self.hostiles_list = [ ]

        self.spheres_list = arcade.SpriteList()
        self.tris_list = arcade.SpriteList()
        self.cubes_list = arcade.SpriteList()

        self.walls_list = arcade.SpriteList()
        self.floors_list = arcade.SpriteList()

        self.walls_built = False


    def setup(self):
        # Create your sprites and sprite lists here
        
        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite("Final_Project/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 30
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)

        # Handle special keyboard situations
        self.right_arrow = False
        self.left_arrow = False
        self.up_arrow = False
        self.down_arrow = False

        # =========  Create the Building  ==================================================================
        # ==================================================================================================
        building_width = int((SCREEN_WIDTH - 200 ) / floor_width)
        # =========  Building  ========     Create the Ground                     ==========================
        for x in range(int(SCREEN_WIDTH/(floor_width/2))):

            # Create the floor instance
            # Coin image from kenney.nl
            pfloor = arcade.Sprite("Final_Project/boxCrate_double.png", SPRITE_SCALING_GROUND)

            # Position the floor
            pfloor.center_x = (x * int(floor_width/2))
            pfloor.center_y = 20

            # Add the floor to the lists
            self.floors_list.append(pfloor)

        # Create all the Other Walls and Floors

        # =======  Building  ======       Build Walls                         |   |   |   |   |   |   |   |   |

        for y in range(building_height):
            for x in range(building_width + 1):

                # Randomize some Gaps for doors
                a_door = random.randint(0, 3)
                print(a_door)
                if a_door >= 1:

                    # Position the wall
                    center_x = ((x * floor_width) + floor_width ) + 100
                    center_y = (y * wall_height) + (wall_height * 1.5)
                    self.spawn_wall(center_x,center_y)

        # =======  Building  ======      Build Floors                          =======-----=-=-------=====-=====--

        for y in range(building_height):            
            for x in range(building_width):

                # Randomize some Gaps for stairs
                a_stair = random.randint(0, 5)
                print(a_stair)
                if a_stair <= 3:

                    # Position the floor
                    center_x = ((x * floor_width) + floor_width ) + 100
                    center_y = ((40 * y) + (wall_height * 2))
                    self.spawn_floor(center_x,center_y)

                    

                    

                    
        
        self.walls_built = True

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # ==============      END UPDATE      ===============

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below

         # ===========            Draw all the sprite lists.             <==================
        self.floors_list.draw()
        self.walls_list.draw()

        self.spheres_list.draw()
        self.cubes_list.draw()
        self.tris_list.draw()

        self.player_sprite_list.draw()


    # ==============================    UPDATE
    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        spheres_hit_list = []

        # Handle multiple keys and keys held down
        if self.right_arrow == True:
            print('Right Arrow held down')
            self.player_sprite.center_x += 1
            self.player_sprite_list.update()

        if self.left_arrow == True:
            print('Left Arrow held down')
            self.player_sprite.center_x -= 1
            self.player_sprite_list.update()

        for friends in self.friendlies_list:
            friends.update(delta_time)

        # Handle Bombs
        # Generate a list of all spheres that collided
        for bomb in self.spheres_list:
            spheres_hit_list = arcade.check_for_collision_with_list(bomb, self.walls_list)

            # Loop through each colliding sprite, remove it, and add to the score.
            for collision in spheres_hit_list:
                collision.hp -= 1000
                if collision.hp < 0:
                    collision.kill()
                bomb.kill()
                self.score += 1


        # ==============================  Spawn Functions   ========================   #

    def spawn_friendly_sphere(self,position_x, position_y):

        change_x = 1
        change_y = 0 

        fsphere = MSphere(position_x,position_y,change_x,change_y)

        self.spheres_list.append(fsphere.sphere_sprite)
        self.friendlies_list.append(fsphere)

        print('Spawned a circle at: ' + str(position_x) + '  ' + str(position_y))


    def spawn_friendly_cube(self):

        pass

    def spawn_friendly_tri(self):

        pass

    #  Spawn it and add to the list
    def spawn_wall(self , center_x , center_y ):
        wall = Wall(center_x,center_y)
        self.walls_list.append(wall.wall_sprite)
        print('Spawned a wall at: ' + str(center_x) + '  ' + str(center_y))


    #  Spawn it and add to the list
    def spawn_floor(self , center_x , center_y ):
        floor = Floor(center_x,center_y)
        self.floors_list.append(floor.floor_sprite)
        print('Spawned a floor at: ' + str(center_x) + '  ' + str(center_y))

        


# =========================             Handle Keyboard Input                ===================
    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.color.html
        """
        if key == arcade.key.RIGHT:
            print ('right arrow key pressed')
            self.player_sprite.center_x += 1
            self.right_arrow = True

        if key == arcade.key.LEFT:
            print ('left arrow key pressed')
            self.player_sprite.center_x -= 1
            self.left_arrow = True

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.S:
            print ('s key released')
            position_x = self.player_sprite.center_x
            position_y = self.player_sprite.center_y
            self.spawn_friendly_sphere(position_x,position_y)

        if key == arcade.key.C:
            print ('c key released')
            position_x = self.player_sprite.center_x
            position_y = self.player_sprite.center_y
            self.spawn_friendly_cube(position_x,position_y)

        if key == arcade.key.T:
            print ('t key released')
            position_x = self.player_sprite.center_x
            position_y = self.player_sprite.center_y
            self.spawn_friendly_tri(position_x,position_y)

        if key == arcade.key.RIGHT:
            print ('right arrow key released')
            self.right_arrow = False

        if key == arcade.key.LEFT:
            print ('left arrow key released')
            self.left_arrow = False
            

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


# ==================  Shapes Classes  ===================================
# Spheres
class MSphere():
    def __init__(self, center_x, center_y, change_x, change_y):

        # Call the parent class's init function
        # super().__init__(position_x, position_y, change_x, change_y)

        # Make it a Sprite
        self.sphere_sprite = arcade.Sprite("Final_Project/sphere.png", SPRITE_SCALING_SPHERE)
        
        # Take the parameters of the init function above, and create instance variables out of them.
        self.sphere_sprite.center_x = center_x
        self.sphere_sprite.center_y = center_y
        self.sphere_sprite.change_x = change_x
        self.sphere_sprite.change_y = change_y

        self.hp = 1
        
    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def update(self, delta_time):       
        # Start the shape to the right
        self.sphere_sprite.center_x += self.sphere_sprite.change_x

    def explode(self):
        pass

class Wall():
    def __init__(self, center_x, center_y):

        # Call the parent class's init function
        # super().__init__(position_x, position_y, change_x, change_y)

        permanent = False
        # Randomize the piece based on build solidity
        strength = random.randrange(100 * building_solidity)
        if strength > master_solidity:
            permanent = True
            
        # Create the Wall instance
        # wall image from kenney.nl
        if permanent:
            self.wall_sprite = arcade.Sprite("Final_Project/pwall.png", SPRITE_SCALING_WALL)
            self.wall_sprite.hp = 10000
            print('Added pwall')
        else:
            self.wall_sprite = arcade.Sprite("Final_Project/twall.png", SPRITE_SCALING_WALL)
            self.wall_sprite.hp = 1000

        self.wall_sprite.center_x = center_x
        self.wall_sprite.center_y = center_y

class Floor():
    def __init__(self, center_x, center_y):

        # Call the parent class's init function
        # super().__init__(position_x, position_y, change_x, change_y)

        permanent = False
        # Randomize the piece based on build solidity
        strength = random.randrange(100 * building_solidity)
        if strength > master_solidity:
            permanent = True
            print(permanent)
        
        # Create the floor instance                         
        if permanent:
            self.floor_sprite = arcade.Sprite("Final_Project/pfloor.png", SPRITE_SCALING_FLOOR)
            self.floor_sprite.hp = 50000
        else:
            self.floor_sprite = arcade.Sprite("Final_Project/tfloor.png", SPRITE_SCALING_FLOOR)
            self.floor_sprite.hp = 10000
        
        # Position the floor
        self.floor_sprite.center_x = center_x
        self.floor_sprite.center_y = center_y
                    


# ==============================================================================================

def main():
    """ Main method """
    game = POCGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()