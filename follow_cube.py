import asyncio

import cozmo
import random
import time

from cozmo.util import degrees, distance_mm
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

def follow_cube(robot):
    target_id = LightCube1Id
    colors = [cozmo.lights.red_light, cozmo.lights.blue_light, cozmo.lights.green_light]
    
    cube = search_and_go_to_cube(robot, target_id)
    
    while cube:
        cube.set_lights(random.choice(colors))
        action = robot.go_to_object(cube, distance_mm(70.0))
        action.wait_for_completed()
        cube.set_lights_off()
        
        target_in_view = False
        for visible_object in robot.world.visible_objects:
            if isinstance(visible_object, cozmo.objects.LightCube) and visible_object.cube_id == target_id:
                target_in_view = True
        
        if not target_in_view:
            cube = search_and_go_to_cube(robot, target_id)
        else:
            time.sleep(2)
    
def search_and_go_to_cube(robot, target_id, search_attempts=3):
    cube = None
    attempts = 0
    
    while attempts < search_attempts:
        look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        try:
            cube = robot.world.wait_for_observed_light_cube(timeout=10)
            if cube.cube_id == target_id:
                look_around.stop()
                robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHappy, 
                                        ignore_body_track=True).wait_for_completed()
                return cube
    
        except asyncio.TimeoutError:
            print("Didn't find cube with id %s" % str(target_id))
            attempts += 1
            look_around.stop()
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabUnhappy, 
                                    ignore_body_track=True).wait_for_completed()
                                   
    
    return cube

if __name__ == '__main__':
    cozmo.run_program(follow_cube)
