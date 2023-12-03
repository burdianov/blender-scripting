import math

import bpy

bpy.ops.mesh.primitive_cube_add(
    size=2, enter_editmode=False, align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
)

cube = bpy.context.active_object

start_frame = 1
cube.keyframe_insert("rotation_euler", frame=start_frame)

degrees = 360
radians = math.radians(degrees)
cube.rotation_euler.z = radians

end_frame = 180
cube.keyframe_insert("rotation_euler", frame=end_frame)
