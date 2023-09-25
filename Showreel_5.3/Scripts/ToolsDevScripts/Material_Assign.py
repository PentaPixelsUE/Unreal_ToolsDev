import unreal
import re
from MaterialCreator import *

Mesh_Dir = "/Game/Shaders/Models/"
MA_Dir = "/Game/Shaders/Materials/"
materials=unreal.EditorAssetLibrary.list_assets(directory_path=MA_Dir, recursive=True, include_folder=False)
meshes = unreal.EditorAssetLibrary.list_assets(directory_path=Mesh_Dir, recursive=True, include_folder=False)

                
        
def get_last_part_with_number(name):
    parts = name.split("_")
    
    for i in range(len(parts) - 1, -1, -1):
        if re.search(r'\d', parts[i]):
            return "_".join(parts[i-1:])
    
    # If no part with a number is found, return the entire last part
    return parts[-1]

mesh_list=[]
mat_list=[]

for mat in materials:
    loaded_mat=unreal.EditorAssetLibrary.load_asset(mat)
    mat_name=loaded_mat.get_name()
    mat_name=get_last_part_with_number(mat_name)
    mat_list.append(mat_name)

for mesh in meshes:
    loaded_Mesh = unreal.EditorAssetLibrary.load_asset(mesh)
    mesh_name = loaded_Mesh.get_name()
    mesh_name =get_last_part_with_number(mesh_name)
    mesh_list.append(mesh_name)
    static_material = loaded_Mesh.get_editor_property("static_materials")
    
    if len(static_material)>1:
        for index, element in enumerate(static_material):
            slot_name = element.get_editor_property("material_slot_name")
            #print(f"{slot_name} of index {index}")
            for mat in materials:
                loaded_mat=unreal.EditorAssetLibrary.load_asset(mat)
                mat_name=loaded_mat.get_name()
                mat_name=get_last_part_with_number(mat_name)
                if slot_name == mat_name:
                    if mat_name in mesh_name:
                        print(f"{mat_name}wiill be assigned at  index {index} of {mesh_name}")
                        unreal.StaticMesh.set_material(loaded_Mesh,index,loaded_mat)
                    else:
                        unreal.StaticMesh.set_material(loaded_Mesh,index,loaded_mat)
                        print(f"{mat_name}wiill be assigned at  index {index} of {mesh_name}")
    elif len(static_material)==1:
        for index, element in enumerate(static_material):
            slot_name = element.get_editor_property("material_slot_name")
            print(f"{slot_name} of index {index}")
            for mat in materials:
                loaded_mat=unreal.EditorAssetLibrary.load_asset(mat)
                mat_name=loaded_mat.get_name()
                mat_name=get_last_part_with_number(mat_name)
                if mat_name in mesh_name:
                    unreal.StaticMesh.set_material(loaded_Mesh,0,loaded_mat)
                    print(f"{mat_name}wiill be assigned at  index {index} of {mesh_name}")
                        
            


