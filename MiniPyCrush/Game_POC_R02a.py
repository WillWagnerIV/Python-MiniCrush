"""
Starting Template From © Copyright 2018, Paul Vincent Craven. 

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_starting_template
"""
import arcade
import random

# Constants

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

SPRITE_SCALING_GROUND = .28
SPRITE_SCALING_FLOOR = 1
SPRITE_SCALING_WALL = 1

SPRITE_SCALING_PLAYER = .25
SPRITE_SCALING_SPHERE = 1
SPRITE_SCALING_CUBE = 1
SPRITE_SCALING_TRI = 1

# Variables

building_width = 18
building_height = 10

floor_width = 40

wall_height = 40 

master_solidity = 25   # suggested scale between 1 and 100

building_solidity = 1   # suggested scale by decimals to increase number of permanent walls.  ex: .8 = fewer permanent walls.  1.2 = more permanent walls





############# Create Classes for Shapes
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


      



class Walls():
    pass

class DWalls(Walls):
    pass

class PWalls(Walls):
    pass

class Floors():
    pass

class DFloors(Floors):
    pass

class PFloors(Floors):
    pass




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


    def setup(self):
        # Create your sprites and sprite lists here
        
        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite("Final_Project/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 65
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

        for y in range(building_height):
            
# =======  Building  ======       Build Walls                         |   |   |   |   |   |   |   |   |
            for x in range(building_width+ 1):

                # Randomize some Gaps for doors
                a_door = random.randint(0, 3)
                print(a_door)
                if a_door >= 1:

                    permanent = False
                    # Randomize the piece based on build solidity
                    strength = random.randrange(100 * building_solidity)
                    if strength > master_solidity:
                        permanent = True
                        print(permanent)

                    # Create the Wall instance
                    # wall image from kenney.nl
                    if permanent:
                        wall = arcade.Sprite("Final_Project/pwall.png", SPRITE_SCALING_WALL)
                        print('Added pwall')
                    else:
                        wall = arcade.Sprite("Final_Project/twall.png", SPRITE_SCALING_WALL)

                    # Position the wall
                    wall.center_x = (x * int(floor_width) + (floor_width/2)) + 100
                    print(wall.center_x)
                    wall.center_y = (y * wall_height) + (wall_height * 1.5)
                    print(wall.center_y)

                    # Add the wall to the lists
                    self.walls_list.append(wall)

# ==== Building ======      Build Floors                           |   |   |   |   |   |   |   |   |

        for y in range(building_height):            
            for x in range(building_width):

                # Randomize some Gaps for stairs
                a_stair = random.randint(0, 5)
                print(a_stair)
                if a_stair <= 3:

                    permanent = False
                    # Randomize the piece based on build solidity
                    strength = random.randrange(100 * building_solidity)
                    if strength > master_solidity:
                        permanent = True
                        print(permanent)
                    
                    # Create the floor instance                         ========----===-====---===--==-=
                    if permanent:
                        floor = arcade.Sprite("Final_Project/pfloor.png", SPRITE_SCALING_FLOOR)
                    else:
                        floor = arcade.Sprite("Final_Project/tfloor.png", SPRITE_SCALING_FLOOR)

                    

                    # Position the floor
                    floor.center_x = ((x * floor_width) + floor_width ) + 100
                    floor.center_y = ((40 * y) + (wall_height * 2))

                    # Add the floor to the lists
                    self.floors_list.append(floor)
        
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

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

        # for friends in self.friendlies_list:
        #     friends.draw()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        if self.right_arrow == True:
            print('Right Arrow held down')
            self.player_sprite.center_x += 1
            self.player_sprite_list.update()

        for friends in self.friendlies_list:
            print(type(friends))
            friends.update(delta_time)

        # # Generate a list of all sprites that collided with the player.
        # coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
        #                                                       self.coin_list)

        # # Loop through each colliding sprite, remove it, and add to the score.
        # for coin in coins_hit_list:
        #     coin.kill()
        #     self.score += 1

        # ==============================  Spawn Functions   ========================   #

    def spawn_friendly_sphere(self):

        position_x = self.player_sprite.center_x
        position_y = self.player_sprite.center_y
        print('Spawned a circle at: ' + str(position_x) + '  ' + str(position_y))

        change_x = 1
        change_y = 0 

        fsphere = MSphere(position_x,position_y,change_x,change_y)

        self.spheres_list.append(fsphere.sphere_sprite)
        self.friendlies_list.append(fsphere)


    def spawn_friendly_cube(self):

        pass

    def spawn_friendly_tri(self):

        pass



# =========================             Handle Key Presses                ===================
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

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.

        if key == arcade.key.LEFT:
            print("Left key hit")
        elif key == arcade.key.A:
            print("The 'a' key was hit")

        """
        if key == arcade.key.S:
            print ('s key released')
            self.spawn_friendly_sphere()

        if key == arcade.key.C:
            print ('c key released')
            self.spawn_friendly_cube()

        if key == arcade.key.T:
            print ('t key released')
            self.spawn_friendly_tri()

        if key == arcade.key.RIGHT:
            print ('right arrow key released')
            self.right_arrow = False
            

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


# Ball
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

        
    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def update(self, delta_time):
        
        # Start the shape to the right
        self.sphere_sprite.center_x += self.sphere_sprite.change_x

    

    # def draw(self):
    #     """ Draw the balls with the instance variables we have. """
    #     # arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


def main():
    """ Main method """
    game = POCGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()