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
SPRITE_SCALING_SPHERE = .76
SPRITE_SCALING_CUBE = .75
SPRITE_SCALING_TRI = .75

# Physics
MOVEMENT_SPEED = 1.35
JUMP_SPEED = 1.25
GRAVITY = 0.1

# Global Variables

building_width = 18
building_height = 8

floor_width = 60

wall_height = 60 

master_solidity = 25   # suggested scale between 1 and 100

building_solidity = 1   # suggested scale by decimals to increase number of permanent walls.  
                        # ex: .8 = fewer permanent walls.  1.2 = more permanent walls

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

        self.friendlies_list = arcade.SpriteList()
        self.hostiles_list = arcade.SpriteList()

        self.spheres_list = arcade.SpriteList()
        self.tris_list = arcade.SpriteList()
        self.cubes_list = arcade.SpriteList()

        self.hostile_spheres_list = arcade.SpriteList()
        self.hostile_cubes_list = arcade.SpriteList()
        self.hostile_tris_list = arcade.SpriteList()

        self.walls_list = arcade.SpriteList()
        self.floors_list = arcade.SpriteList()
        self.objectives_list = arcade.SpriteList()

        # Global Variables within this Window

        self.walls_built = False
        self.base_score = 10
        self.game_over = False

        # Physics engine
        self.physics_engine = None

    # ==============      END INIT      ===============
    # ==============      START SETUP      ===============
    def setup(self):
        
        # Set up the player     
        self.player_sprite = arcade.Sprite("Final_Project/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 30
        self.player_sprite.center_y = 50
        self.player_sprite.score = 0
        self.player_sprite_list.append(self.player_sprite)
        self.friendlies_list.append(self.player_sprite)       

        # Handle special keyboard situations
        self.right_arrow = False
        self.left_arrow = False
        self.up_arrow = False
        self.down_arrow = False

        # =========  Create the Ground and Building  ========================
        building_width = int((SCREEN_WIDTH - 200 ) / floor_width)

        # =======  Objective  ======      Place Objective
        center_x = building_width * floor_width + 70
        center_y = building_height * wall_height - 10
        self.spawn_objective(center_x,center_y)

        # =======  Ground  ======        Build all Permanent Floors
        for x in range(building_width + 10):
            # Position the floor
            center_x = (x * floor_width)
            center_y = (wall_height/2)
            self.spawn_floor(center_x,center_y)

        # =======  Building  ======       Build Walls                         |   |   |   |   |   |   |   |   |

        for y in range(building_height):
            for x in range(building_width + 1):

                # Randomize some Gaps for doors
                a_door = random.randint(0, 3)
                print(a_door)
                if a_door >= 1:

                    # Position the wall
                    center_x = (x * floor_width) + 100
                    center_y = (y * wall_height) + 50
                    self.spawn_wall(center_x,center_y)

        # =======  Building  ======      Build Floors                          =======-----=-=-------=====-=====--

        for y in range(building_height):            
            for x in range(building_width):

                # Randomize some Gaps for stairs
                a_stair = random.randint(0, 5)
                print(a_stair)
                if a_stair <= 3:

                    # Position the floor
                    center_x = (x * floor_width) + 130
                    center_y = (y * wall_height) + 80
                    self.spawn_floor(center_x,center_y)

        self.walls_built = True

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Make player affected by gravity
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.floors_list,
                                                             gravity_constant=GRAVITY)


        # ==============      END SETUP      ===============
        # ==============      START DRAW      ===============

    def on_draw(self):
        """  Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below

         # ===========            Draw all the sprite lists.             <==================
        self.floors_list.draw()
        self.walls_list.draw()
        self.objectives_list.draw()

        self.spheres_list.draw()
        self.cubes_list.draw()
        self.tris_list.draw()

        self.hostile_spheres_list.draw()
        self.hostile_cubes_list.draw()
        self.hostile_tris_list.draw()

        self.player_sprite_list.draw()

        # Put the text on the screen.
        output = "Score: " + str(self.player_sprite.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        # ==============      END DRAW      ===============
        # ==============      START UPDATE      ===============
    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        # Check if Game is Over
        if self.game_over == True:
            # This is where the Game Over stuff will go!
            pass

        # Handle multiple keys and keys held down
        # Check for collisions before moving
        # Generate a list of all friendly players that collided with walls
        for player in self.player_sprite_list:

            # Check if Player has reached Objective!
            player_hit_list = arcade.check_for_collision_with_list(player, self.objectives_list)
            for collision in player_hit_list:
                self.game_over = True
                collision.kill()




            player.disable_keys = False
            player_hit_list = arcade.check_for_collision_with_list(player, self.walls_list)
            # Loop through each colliding sprite and disable keyboard input
            for collision in player_hit_list:
                player.disable_keys = True
            # IF keyboard not disabled then check keys
            if player.disable_keys == False:             
                if self.right_arrow == True:
                    print('Right Arrow held down')            
                    self.player_sprite.center_x += 1
                    self.player_sprite_list.update()

                if self.left_arrow == True:
                    print('Left Arrow held down')
                    self.player_sprite.center_x -= 1
                    self.player_sprite_list.update()

        self.friendlies_list.update()
        self.hostiles_list.update()
        self.physics_engine.update()

        # Handle Bombs
        # Generate a list of all friendly spheres that collided with walls
        for bomb in self.spheres_list:
            spheres_hit_list = arcade.check_for_collision_with_list(bomb, self.walls_list)
            # Loop through each colliding sprite, remove it, and add to the score.
            for collision in spheres_hit_list:
                collision.hp -= 1000
                if collision.hp < 0:
                    collision.kill()
                bomb.kill()
                self.player_sprite.score += self.base_score
            for sprites in self.friendlies_list:
                if sprites not in spheres_hit_list:
                    if sprites not in self.player_sprite_list:
                        sprites.change_x = 1
        # Generate a list of all hostile spheres that collided with walls
        for bomb in self.hostile_spheres_list:
            spheres_hit_list = arcade.check_for_collision_with_list(bomb, self.walls_list)
            # Loop through each colliding sprite, remove it, and add to the score.
            for collision in spheres_hit_list:
                collision.hp -= 3000
                if collision.hp < 0:
                    collision.kill()
                bomb.kill()
                self.player_sprite.score += self.base_score        

        # Handle Cubes
        # Generate a list of all friendly spheres that collided with walls
        for cube in self.cubes_list:
            cubes_hit_list = arcade.check_for_collision_with_list(cube, self.walls_list)
            # Loop through each colliding sprite, set its movement to 0
            for collision in cubes_hit_list:
                cube.change_x = 0
        # Generate a list of all hostile spheres that collided with walls
        for cube in self.hostile_cubes_list:
            cubes_hit_list = arcade.check_for_collision_with_list(cube, self.walls_list)
            # Loop through each colliding sprite, set its movement to 0
            for collision in cubes_hit_list:
                cube.change_x = 0

        # Handle Tris
        # Generate a list of all friendly tris that collided with walls
        for tri in self.tris_list:
            tris_hit_list = arcade.check_for_collision_with_list(tri, self.walls_list)
            # Loop through each colliding sprite, remove it, and add to the score.
            for collision in tris_hit_list:
                tri.change_x = 0
            # Generate a list of all friendly tris that collided with friendlies
            tris_hit_list = arcade.check_for_collision_with_list(tri, self.friendlies_list)
            for collision in tris_hit_list:
                # collision.change_y = JUMP_SPEED
                collision.center_y = tri.center_y + 60
        # Generate a list of all hostile tris that collided with walls
        for tri in self.hostile_tris_list:
            tris_hit_list = arcade.check_for_collision_with_list(tri, self.walls_list)
            # Loop through each colliding sprite, remove it, and add to the score.
            for collision in tris_hit_list:
                tri.change_x = 0
            tris_hit_list = arcade.check_for_collision_with_list(tri, self.hostiles_list)
            for collision in tris_hit_list:
                # collision.change_y = 0
                collision.center_x = tri.center_x
                collision.center_y = tri.center_y + 60

    # =============================^  END UPDATE  ^========================   #

    # ==============================  START SPAWN FUNCTIONS   ========================   #
    #  Spawn them and add to appropriate list

    def spawn_sphere(self,position_x, position_y, friendly):
        if friendly:
            fsphere = MSphere(position_x,position_y,1,0,1)
            self.spheres_list.append(fsphere.sphere_sprite)
            self.friendlies_list.append(fsphere.sphere_sprite)
            print('Spawned a circle at: ' + str(position_x) + '  ' + str(position_y))
        else:
            fsphere = MSphere(position_x,position_y,-1,0,0)
            self.hostile_spheres_list.append(fsphere.sphere_sprite)
            self.hostiles_list.append(fsphere.sphere_sprite)
            print('Spawned a circle at: ' + str(position_x) + '  ' + str(position_y))


    def spawn_cube(self,position_x, position_y,friendly):
        if friendly:
            fcube = MCube(position_x,position_y,1,0,1)
            self.cubes_list.append(fcube.cube_sprite)
            self.friendlies_list.append(fcube.cube_sprite)
            print('Spawned a cube at: ' + str(position_x) + '  ' + str(position_y))
        else:
            fcube = MCube(position_x,position_y,-1,0,0)
            self.hostile_cubes_list.append(fcube.cube_sprite)
            self.hostiles_list.append(fcube.cube_sprite)
            print('Spawned a cube at: ' + str(position_x) + '  ' + str(position_y))


    def spawn_tri(self,position_x, position_y, friendly):
        if friendly:
            ftri = MTri(position_x,position_y,1,0,1)
            self.tris_list.append(ftri.tri_sprite)
            self.friendlies_list.append(ftri.tri_sprite)
            print('Spawned a Tri at: ' + str(position_x) + '  ' + str(position_y))
        else:
            ftri = MTri(position_x,position_y,-1,0,0)
            self.hostile_tris_list.append(ftri.tri_sprite)
            self.hostiles_list.append(ftri.tri_sprite)
            print('Spawned a Tri at: ' + str(position_x) + '  ' + str(position_y))


    def spawn_hostile(self,position_x, position_y):
        self.spawn_sphere(position_x, position_y, False)
        which_unit = random.randrange(1,101)
        # if which_unit >= 90:
        #     self.spawn_tri(position_x, position_y, False)
        if which_unit >= 80:
            self.spawn_cube(position_x, position_y, False)      

    def spawn_wall(self , center_x , center_y ):
        wall = Wall(center_x,center_y)
        self.walls_list.append(wall.wall_sprite)
        print('Spawned a wall at: ' + str(center_x) + '  ' + str(center_y))

    def spawn_floor(self , center_x , center_y ):
        floor = Floor(center_x,center_y)
        self.floors_list.append(floor.floor_sprite)
        print('Spawned a floor at: ' + str(center_x) + '  ' + str(center_y))

    def spawn_objective(self , center_x , center_y ):
        objective = Final_Objective(center_x,center_y)
        self.objectives_list.append(objective.objective_sprite)
        print('Spawned Objective at: ' + str(center_x) + '  ' + str(center_y)) 


    # =========================             Handle Keyboard Input                ===================

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.color.html
        """
        if key == arcade.key.UP:
            # Checks to make sure there is a platform underneath
            # Can't jump if there isn't ground beneath your feet.
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
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
            self.spawn_sphere(position_x,position_y,1)
            self.spawn_hostile(SCREEN_WIDTH - 10, position_y)

        if key == arcade.key.C:
            print ('c key released')
            position_x = self.player_sprite.center_x
            position_y = self.player_sprite.center_y
            self.spawn_cube(position_x,position_y,1)
            self.spawn_hostile(SCREEN_WIDTH - 10, position_y)

        if key == arcade.key.T:
            print ('t key released')
            position_x = self.player_sprite.center_x
            position_y = self.player_sprite.center_y
            self.spawn_tri(position_x,position_y,1)
            self.spawn_hostile(SCREEN_WIDTH - 10, position_y)

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
# ==================  Shapes Classes  ===================================
# Spheres
class MSphere():
    def __init__(self, center_x, center_y, change_x, change_y, friendly):

        # Call the parent class's init function
        # super().__init__(position_x, position_y, change_x, change_y)

        # Make it a Sprite
        self.sphere_sprite = arcade.Sprite("Final_Project/sphere.png", SPRITE_SCALING_SPHERE)
        
        # Take the parameters of the init function above, and create instance variables out of them.
        self.sphere_sprite.center_x = center_x
        self.sphere_sprite.center_y = center_y
        self.sphere_sprite.change_x = change_x
        # self.sphere_sprite.change_y = change_y
        self.sphere_sprite.friendly = friendly

        self.sphere_sprite.hp = 1

        self.sphere_sprite.physics_engine = None
        
    def setup(self):

        # Make Sphere affected by gravity
        print('Sphere Setup - floors list: ' + str(POCGame().floors_list))
        self.sphere_sprite.physics_engine = arcade.PhysicsEnginePlatformer(self.sphere_sprite, 
                                                                            platforms =  POCGame.floors_list,
                                                                            gravity_constant=GRAVITY)

    def update(self, delta_time):       
        # Start the shape to the right
        # self.sphere_sprite.center_x += self.sphere_sprite.change_x
        # self.sphere_sprite.change_y = 0

        self.sphere_sprite.physics_engine.update()

    def explode(self):
        pass

class MCube():
    def __init__(self, center_x, center_y, change_x, change_y, friendly):

        # Call the parent class's init function
        # super().__init__(position_x, position_y, change_x, change_y)

        # Make it a Sprite
        self.cube_sprite = arcade.Sprite("Final_Project/cube.png", SPRITE_SCALING_SPHERE)
        
        # Take the parameters of the init function above, and create instance variables out of them.
        self.cube_sprite.center_x = center_x
        self.cube_sprite.center_y = center_y
        self.cube_sprite.change_x = change_x
        self.cube_sprite.change_y = change_y

        self.hp = 1
        
    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def update(self, delta_time):       
        # Start the shape to the right
        self.cube_sprite.center_x += self.cube_sprite.change_x

    def explode(self):
        pass

class MTri():
    def __init__(self, center_x, center_y, change_x, change_y, friendly):

        # Call the parent class's init function
        # super().__init__(position_x, position_y, change_x, change_y)

        # Make it a Sprite
        self.tri_sprite = arcade.Sprite("Final_Project/tri.png", SPRITE_SCALING_SPHERE)
        
        # Take the parameters of the init function above, and create instance variables out of them.
        self.tri_sprite.center_x = center_x
        self.tri_sprite.center_y = center_y
        self.tri_sprite.change_x = change_x
        self.tri_sprite.change_y = 0

        self.tri_sprite.physics_engine = None

        self.tri_sprite.hp = 100
        
    def setup(self):
        # Create your sprites and sprite lists here
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.tri_sprite,
                                                             platforms = POCGame.floors_list,
                                                             gravity_constant=GRAVITY)

    def update(self, delta_time):       
        # Start the shape to the right
        self.tri_sprite.change_x += MOVEMENT_SPEED
        # self.tri_sprite.center_y += self.tri_sprite.change_y
        # Gravity from the physics engine
        # self.physics_engine = arcade.PhysicsEnginePlatformer(self.tri_sprite,
        #                                                      self.floors_list,
        #                                                      gravity_constant=GRAVITY)
        

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

        # Position the Floor
        self.floor_sprite.center_x = center_x
        self.floor_sprite.center_y = center_y

class Final_Objective():
    def __init__(self, center_x, center_y):
        
        # Create the Final_Objective instance                         
        self.objective_sprite = arcade.Sprite("Final_Project/coin_01.png", SPRITE_SCALING_PLAYER)
        self.objective_sprite.hp = 50000
          
        # Position the objective
        self.objective_sprite.center_x = center_x
        self.objective_sprite.center_y = center_y
                    


# ==============================================================================================

def main():
    """ Main method """
    game = POCGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()