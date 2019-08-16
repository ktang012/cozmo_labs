import cozmo
import asyncio

from cozmo.objects import CustomObjectMarkers, CustomObjectTypes, LightCube1Id, LightCube2Id

from cozmo.song import NoteTypes, NoteDurations, SongNote


MAX_ATTEMPTS = 3
TIMEOUT = 30

def setup_custom_cubes(robot, cubes_to_markers, cube_size=44, marker_size=30):
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        try:
            custom_cubes = []
            for cube, marker in cubes_to_markers.items():
                custom_cube = robot.world.define_custom_cube(cube, marker, 
                                                             cube_size, marker_size, marker_size, 
                                                             is_unique=False)
                if custom_cube == None:
                    raise Exception("Internal error setting up custom cube")
                    
                custom_cubes.append(custom_cube)
        except Exception as e:
            print(e)
            attempts += 1
        print("***Initialized custom cubes.")
        return custom_cubes

def print_matched_info(observed, matched):
    print("Seen", observed, "matching", matched)
    print("*" * 15)

# define song notes here
def get_markers_to_notes():
    markers_to_notes = {
        CustomObjectMarkers.Circles2: SongNote(NoteTypes.C2, NoteDurations.Quarter), 
        CustomObjectMarkers.Circles3: SongNote(NoteTypes.C2_Sharp, NoteDurations.Quarter),
        CustomObjectMarkers.Circles4: SongNote(NoteTypes.D2, NoteDurations.Quarter), 
        CustomObjectMarkers.Circles5: SongNote(NoteTypes.D2_Sharp, NoteDurations.Quarter),
        CustomObjectMarkers.Diamonds2: SongNote(NoteTypes.E2, NoteDurations.Quarter), 
        CustomObjectMarkers.Diamonds3: SongNote(NoteTypes.F2, NoteDurations.Quarter),
        CustomObjectMarkers.Diamonds4: SongNote(NoteTypes.F2_Sharp, NoteDurations.Quarter), 
        CustomObjectMarkers.Diamonds5: SongNote(NoteTypes.G2, NoteDurations.Quarter),
        CustomObjectMarkers.Hexagons2: SongNote(NoteTypes.G2_Sharp, NoteDurations.Quarter), 
        CustomObjectMarkers.Hexagons3: SongNote(NoteTypes.A2, NoteDurations.Quarter),
        CustomObjectMarkers.Hexagons4: SongNote(NoteTypes.A2_Sharp, NoteDurations.Quarter), 
        CustomObjectMarkers.Hexagons5: SongNote(NoteTypes.B2, NoteDurations.Quarter),
        CustomObjectMarkers.Triangles2: SongNote(NoteTypes.C3, NoteDurations.Quarter), 
        CustomObjectMarkers.Triangles3: SongNote(NoteTypes.C3_Sharp, NoteDurations.Quarter),
        CustomObjectMarkers.Triangles4: SongNote(NoteTypes.Rest, NoteDurations.Quarter), 
        CustomObjectMarkers.Triangles5: SongNote(NoteTypes.C2_Sharp, NoteDurations.Quarter)
    }
    return markers_to_notes

def get_cubes_to_markers():
    cubes_to_markers = {
        CustomObjectTypes.CustomType00: CustomObjectMarkers.Circles2,
        CustomObjectTypes.CustomType01: CustomObjectMarkers.Circles3,
        CustomObjectTypes.CustomType02: CustomObjectMarkers.Circles4,
        CustomObjectTypes.CustomType03: CustomObjectMarkers.Circles5,
        CustomObjectTypes.CustomType04: CustomObjectMarkers.Diamonds2,
        CustomObjectTypes.CustomType05: CustomObjectMarkers.Diamonds3,
        CustomObjectTypes.CustomType06: CustomObjectMarkers.Diamonds4,
        CustomObjectTypes.CustomType07: CustomObjectMarkers.Diamonds5,
        CustomObjectTypes.CustomType08: CustomObjectMarkers.Hexagons2,
        CustomObjectTypes.CustomType09: CustomObjectMarkers.Hexagons3,
        CustomObjectTypes.CustomType10: CustomObjectMarkers.Hexagons4,
        CustomObjectTypes.CustomType11: CustomObjectMarkers.Hexagons5,
        CustomObjectTypes.CustomType12: CustomObjectMarkers.Triangles2,
        CustomObjectTypes.CustomType13: CustomObjectMarkers.Triangles3,
        CustomObjectTypes.CustomType14: CustomObjectMarkers.Triangles4,
        CustomObjectTypes.CustomType15: CustomObjectMarkers.Triangles5
    }
    return cubes_to_markers
