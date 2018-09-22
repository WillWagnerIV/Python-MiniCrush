# Will Wagner

import arcade
import random
from MiniPyCrush import POCGame as mpc




def MakeBuilding(self):

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600

    # Global Variables

    building_width = 18
    building_height = 8

    floor_width = 60

    wall_height = 60 

    master_solidity = 25   # suggested scale between 1 and 100

    building_solidity = 1   # suggested scale by decimals to increase number of permanent walls.  
                            # ex: .8 = fewer permanent walls.  1.2 = more permanent walls
       
    # =========  Create the Ground and Building  ========================
    building_width = int((SCREEN_WIDTH - 200 ) / floor_width)

    # =======  Objective  ======      Place Objective
    center_x = building_width * floor_width + 70
    center_y = building_height * wall_height - 10
    mpc.spawn_objective(self, center_x,center_y)

    # =======  Ground  ======        Build all Permanent Floors
    for x in range(building_width + 10):
        # Position the floor
        center_x = (x * floor_width)
        center_y = (wall_height/2)
        mpc.spawn_floor(center_x,center_y)

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
                mpc.spawn_wall(center_x,center_y)

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
                mpc.spawn_floor(center_x,center_y)

    mpc.walls_built = True

