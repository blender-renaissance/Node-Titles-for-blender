bl_info = {
    "name": "Node_titles_for_blender",
    "author": "Vikrant Jadhav, Blender Renaissance",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > Node Titles",
    "description": "Customization for Geometry Node Titles",
    "warning": "",
    "doc_url": "https://twitter.com/b3d_Renaissance",
    "category": "3D View",
}

import bpy
import os

from bpy.types import (Panel,
                       Menu,
                       PropertyGroup,
                       )
                       
class MyProperties_Node_titles(bpy.types.PropertyGroup):
    
    my_float_duration_control: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 0,
        min = 0.1,
        max = 30.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatordc()
        )
        
    my_float_length_of_animation: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 30.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatordc()
        )
        
    my_pathfont_nodetitlesA: bpy.props.StringProperty(
        name = "",
        description="link to font file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfont_nodetitlesB: bpy.props.StringProperty(
        name = "",
        description="link to font file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfont_nodetitlesC: bpy.props.StringProperty(
        name = "",
        description="link to font file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfont_nodetitlesD: bpy.props.StringProperty(
        name = "",
        description="link to font file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
                       
class NG_PT_NodeTitles(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Node Titles'
    bl_options = {"DEFAULT_CLOSED"} 
    
class NG_PT_NodeTitles_1(NG_PT_NodeTitles, bpy.types.Panel):    
    bl_label = "Node Titles for Blender"
    bl_idname = "NG_PT_NodeTitlesforBlender_1"  
   
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool2
        
        rownodetitlesduration1 = layout.row()
        rownodetitlesduration1.label(text= "Select a Title") 
        
        rownodetitlesduration2 = layout.row()
        rownodetitlesduration2.label(text= "before using the below options")                 
        
class NG_PT_NodeTitles_3(NG_PT_NodeTitles, bpy.types.Panel):
    bl_parent_id = "NG_PT_NodeTitlesforBlender_1"    
    bl_label = "Font Customization"
    bl_idname = "NG_PT_NodeTitlesforBlender_3"  
   
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool2
        
        rownodetitlefonts = layout.row()
        rownodetitlefonts.label(text= "Change Font A:")        
        layout.prop(mytool, "my_pathfont_nodetitlesA")
        
        rownodetitlefonts = layout.row()
        rownodetitlefonts.label(text= "Change Font B: (If any)")        
        layout.prop(mytool, "my_pathfont_nodetitlesB")
        
        rownodetitlefonts = layout.row()
        rownodetitlefonts.label(text= "Change Font C: (If any)")        
        layout.prop(mytool, "my_pathfont_nodetitlesC")

        rownodetitlefonts = layout.row()
        rownodetitlefonts.label(text= "Change Font D: (If any)")        
        layout.prop(mytool, "my_pathfont_nodetitlesD") 
        layout.operator("addonname.myop_operatorf")
        
        rowresetcg = layout.row()
        rowresetcg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatorres")
        
class ADDONNAME_OT_my_durationcontrol(bpy.types.Operator):
    bl_label = "Change Duration"
    bl_idname = "addonname.myop_operatordc"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool2
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_22"]'
        data_path2 = 'modifiers["GeometryNodes"]["Input_23"]'
        data_path3 = 'modifiers["GeometryNodes"]["Input_24"]'
        index = 0
        stringc = mytool.my_float_duration_control
        frc = bpy.context.scene.render.fps
        jeffc = stringc*frc
        jeffc2 = ((stringc*frc)+3)
        onemorec =  (mytool.my_float_length_of_animation*frc) + jeffc
        onemorec2 =  (mytool.my_float_length_of_animation*frc) + jeffc2
        bobc = onemorec 
        bobc2 = onemorec2

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobc = int(bobc)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffc
                kps.handle_left[0] = jeffc-30
                kps.handle_right[0] = jeffc
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobc
                kpz.handle_left[0] = bobc-60
                kpz.handle_right[0] = bobc+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path2, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobc2 = int(bobc2)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffc2
                kps.handle_left[0] = jeffc2-30
                kps.handle_right[0] = jeffc2
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobc2
                kpz.handle_left[0] = bobc2-60
                kpz.handle_right[0] = bobc2+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path3, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobc = int(bobc)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffc
                kps.handle_left[0] = jeffc-30
                kps.handle_right[0] = jeffc
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobc
                kpz.handle_left[0] = bobc-60
                kpz.handle_right[0] = bobc+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                

             
        return {'FINISHED'} 

    
class Fontchange(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatorf"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool2
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers.get("GeometryNodes")  # Use .get() to avoid KeyError if the modifier doesn't exist
        if modifier:
            node_groupnt = modifier.node_group
            
            # Check if the node 'String to Curves.005' exists
            try:
                nodenttitle = node_groupnt.nodes['String to Curves.005']
                datanttitle_font = bpy.data.fonts.load(mytool.my_pathfont_nodetitlesA)
                nodenttitle.font = datanttitle_font
            except KeyError:
                # Node 'String to Curves.005' doesn't exist
                print("Node 'String to Curves.005' does not exist.")
                
            nodentlongtitle_names = ['String to Curves', 'String to Curves.002', 'String to Curves.003', 'String to Curves.004', 'String to Curves.009', 'String to Curves.010', 'String to Curves.011', 'String to Curves.012', 'String to Curves.013', 'String to Curves.014', 'String to Curves.015']
            for name in nodentlongtitle_names:
                nodentlongtitle = node_groupnt.nodes.get(name)
                datantlongtitle_font = bpy.data.fonts.load(mytool.my_pathfont_nodetitlesA)
                if nodentlongtitle is not None:  # Check if the node exists
                    nodentlongtitle.font = datantlongtitle_font
                else:
                    print(f"Node '{name}' does not exist.")
            
            # Repeat the same process for other nodes
            
            # Check if the node 'String to Curves.006' exists
            try:
                nodentsubtitle = node_groupnt.nodes['String to Curves.006']
                datantsubtitle_font = bpy.data.fonts.load(mytool.my_pathfont_nodetitlesB)
                nodentsubtitle.font = datantsubtitle_font
            except KeyError:
                # Node 'String to Curves.006' doesn't exist
                print("Node 'String to Curves.006' does not exist.")
            
            # Repeat the same process for other nodes
            
            # Check if the node 'String to Curves' exists
            try:
                nodentvalue = node_groupnt.nodes['String to Curves.007']
                datantvalue_font = bpy.data.fonts.load(mytool.my_pathfont_nodetitlesC)
                nodentvalue.font = datantvalue_font
            except KeyError:
                # Node 'String to Curves' doesn't exist
                print("Node 'String to Curves' does not exist.")
            
            # Repeat the same process for other nodes
            
            # Check if the node 'String to Curves.001' exists
            try:
                nodentdescription = node_groupnt.nodes['String to Curves.008']
                datantdescription_font = bpy.data.fonts.load(mytool.my_pathfont_nodetitlesD)
                nodentdescription.font = datantdescription_font
            except KeyError:
                # Node 'String to Curves.001' doesn't exist
                print("Node 'String to Curves.001' does not exist.")
            
            bpy.ops.file.pack_all()
        
        return {'FINISHED'}
    
class Fontrestore(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorres"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool2
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers.get("GeometryNodes")  # Use .get() to avoid KeyError if the modifier doesn't exist
        if modifier:
            noderestorent_group = modifier.node_group
            
            # Check if the node 'String to Curves.005' exists
            try:
                noderestorenttitle = noderestorent_group.nodes['String to Curves.005']
                datarestorenttitle_font = bpy.data.fonts.get("Open Sans Extrabold")  # Use .get() to avoid KeyError if the font doesn't exist
                if datarestorenttitle_font:
                    noderestorenttitle.font = datarestorenttitle_font
                else:
                    print("Font 'Open Sans Extrabold' does not exist.")
            except KeyError:
                # Node 'String to Curves.005' doesn't exist
                print("Node 'String to Curves.005' does not exist.")
            
            # Repeat the same process for other nodes
            
            try:
                nodentrestorelongtitle_names = ['String to Curves', 'String to Curves.002', 'String to Curves.003', 'String to Curves.004', 'String to Curves.009', 'String to Curves.010', 'String to Curves.011', 'String to Curves.012', 'String to Curves.013', 'String to Curves.014', 'String to Curves.015']
                for name in nodentrestorelongtitle_names:
                    nodentrestorelongtitle = noderestorent_group.nodes.get(name)
                    datantrestorelongtitle_font = bpy.data.fonts["Open Sans Extrabold"]
                    if nodentrestorelongtitle is not None:  # Check if the node exists
                        nodentrestorelongtitle.font = datantrestorelongtitle_font
                    else:
                        print(f"Node '{name}' does not exist.")
            except KeyError:
                print("Node 'Long title nodes' does not exist.")
                     
            
            # Check if the node 'String to Curves.006' exists
            try:
                noderestorentsubtitle = noderestorent_group.nodes['String to Curves.006']
                datarestorentsubtitle_font = bpy.data.fonts.get("Open Sans Light")
                if datarestorentsubtitle_font:
                    noderestorentsubtitle.font = datarestorentsubtitle_font
                else:
                    print("Font 'Open Sans Light' does not exist.")
            except KeyError:
                # Node 'String to Curves.006' doesn't exist
                print("Node 'String to Curves.006' does not exist.")
            
            # Repeat the same process for other nodes
            
            # Check if the node 'String to Curves.007' exists
            try:
                noderestorentvalue = noderestorent_group.nodes['String to Curves.007']
                datarestorentvalue_font = bpy.data.fonts.get("Open Sans Regular")
                if datarestorentvalue_font:
                    noderestorentvalue.font = datarestorentvalue_font
                else:
                    print("Font 'Open Sans Regular' does not exist.")
            except KeyError:
                # Node 'String to Curves' doesn't exist
                print("Node 'String to Curves' does not exist.")
            
            # Repeat the same process for other nodes
            
            # Check if the node 'String to Curves.008' exists
            try:
                noderestorentdescription = noderestorent_group.nodes['String to Curves.008']
                datarestorentdescription_font = bpy.data.fonts.get("Open Sans Regular")
                if datarestorentdescription_font:
                    noderestorentdescription.font = datarestorentdescription_font
                else:
                    print("Font 'Open Sans Regular' does not exist.")
            except KeyError:
                # Node 'String to Curves.001' doesn't exist
                print("Node 'String to Curves.001' does not exist.")
            
            bpy.ops.file.pack_all()
        
        return {'FINISHED'}


        
classes = [MyProperties_Node_titles, NG_PT_NodeTitles_1, NG_PT_NodeTitles_3, ADDONNAME_OT_my_durationcontrol, Fontchange, Fontrestore]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
    bpy.types.Scene.my_tool2 = bpy.props.PointerProperty(type= MyProperties_Node_titles)
        
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
    del bpy.types.Scene.my_tool2

    
if __name__ == "__main__":
    register()    