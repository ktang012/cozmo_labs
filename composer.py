import asyncio
import time
import cozmo
import cozmo.objects as c_objects

import composer_utils

# tune this to set time for when objects disappear
# c_objects.OBJECT_VISIBILITY = 0.4

START_CUBE = c_objects.LightCube1Id # paperclip
END_CUBE = c_objects.LightCube2Id # lamp/heart
MAX_ATTEMPTS = composer_utils.MAX_ATTEMPTS
TIMEOUT = composer_utils.TIMEOUT


# we have a limited range and are working with quarter notes
# so the songs won't sound as good
# songs to play
# zelda's lullaby: e g d e g d e g d c g
# song of healing: a g d a g d a g d c d
# song of storms: d f d R d f d R e R f e f e c3

def composer(robot):
    markers_to_notes = composer_utils.get_markers_to_notes()
    cubes_to_markers = composer_utils.get_cubes_to_markers()
    composer_utils.setup_custom_cubes(robot, cubes_to_markers)
    
    song = []
    start_recording = False
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        try:
            print("***Waiting for observation.")
            observation = robot.world.wait_for(c_objects.EvtObjectAppeared, timeout=TIMEOUT)
            if (start_recording and isinstance(observation.obj, c_objects.CustomObject)):
                object_type = observation.obj.object_type
                marker = cubes_to_markers[object_type]
                song_note = markers_to_notes[marker]
                song.append(song_note)
                composer_utils.print_matched_info(marker, song_note)
                print("***Observed", song_note)
                
            elif isinstance(observation.obj, c_objects.LightCube):
                if observation.obj.cube_id == START_CUBE and not start_recording:
                    start_recording = True
                    print("***Observed START cube.")
                elif observation.obj.cube_id == END_CUBE:
                    print("***Observed END cube.")
                    break
                    
        except asyncio.TimeoutError:
            if not start_recording:
                print("******Timed out waiting for start cube.")
            else:
                print("******Timed out waiting for note or end cube.")
            attempts += 1
         
    if song:
        robot.play_song(song, loop_count=3).wait_for_completed()
    else:
        print("***Nothing to play")


if __name__ == '__main__':
    cozmo.run_program(composer, use_viewer=True)
    
    
