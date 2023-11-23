bl_info = {
    "name": "EdgeTally",
    "blender": (4, 0, 0),
    "category": "Object",
}

import bpy
import bmesh

class EdgeTallyOperator(bpy.types.Operator):
    """Display the count of selected mesh elements"""
    bl_idname = "mesh.edge_tally_operator"
    bl_label = "Count Selected Elements"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH' and context.active_object.mode == 'EDIT'

    def execute(self, context):
        """
        Execute the operator to count the selected mesh elements.

        Returns:
            dict: The result of the operator execution.
        """
        obj = context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        
        verts_selected = len([v for v in bm.verts if v.select])
        edges_selected = len([e for e in bm.edges if e.select])
        faces_selected = len([f for f in bm.faces if f.select])

        self.report({'INFO'}, f"Verts: {verts_selected} Edges: {edges_selected} Faces: {faces_selected}")
        return {'FINISHED'}

def menu_draw(self, context):
    self.layout.operator(EdgeTallyOperator.bl_idname, text="Count Selected Elements")

def register():
    bpy.utils.register_class(EdgeTallyOperator)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.prepend(menu_draw)

def unregister():
    bpy.utils.unregister_class(EdgeTallyOperator)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_draw)

if __name__ == "__main__":
    register()
