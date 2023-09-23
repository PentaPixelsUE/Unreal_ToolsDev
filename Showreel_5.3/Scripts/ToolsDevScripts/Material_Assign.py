# import unreal
# import re
# from MaterialCreator import *

# meshes = eal.list_assets(directory_path=Mesh_Dir, recursive=True, include_folder=False)
# Materials = eal.list_assets(directory_path=MA_Dir, recursive=True, include_folder=False)
# meshes_list =[]
# materials_list=[]


# for mesh in meshes:
#     loaded_Mesh = unreal.load_asset(mesh)
#     mesh_name = loaded_Mesh.get_name()
#     meshes_list.append(mesh_name)
# for ma in Materials:
#     loaded_MA = unreal.load_asset(ma)
#     ma_name = loaded_MA.get_name()
#     materials_list.append(ma_name)

# def get_last_part_with_number(name):
#     parts = name.split("_")
    
#     for i in range(len(parts) - 1, -1, -1):
#         if re.search(r'\d', parts[i]):
#             return "_".join(parts[i-1:])
    
#     # If no part with a number is found, return the entire last part
#     return parts[-1]



# for mesh in meshes_list:
#     print(get_last_part_with_number(mesh))

# for ma in materials_list:
#     print(get_last_part_with_number(ma))


# unreal.StaticMesh.set_material(self=loaded_Mesh,material_index=0,new_material=loaded_MA)
import unreal
import re
from MaterialCreator import *

meshes = unreal.EditorAssetLibrary.list_assets(directory_path=Mesh_Dir, recursive=True, include_folder=False)
Materials = unreal.EditorAssetLibrary.list_assets(directory_path=MA_Dir, recursive=True, include_folder=False)
meshes_list = []
materials_list = []

for mesh in meshes:
    loaded_Mesh = unreal.EditorAssetLibrary.load_asset(mesh)
    mesh_name = loaded_Mesh.get_name()
    meshes_list.append((loaded_Mesh, mesh_name))

for ma in Materials:
    loaded_MA = unreal.EditorAssetLibrary.load_asset(ma)
    ma_name = loaded_MA.get_name()
    materials_list.append((loaded_MA, ma_name))

def get_last_part_with_number(name):
    parts = name.split("_")
    
    for i in range(len(parts) - 1, -1, -1):
        if re.search(r'\d', parts[i]):
            return "_".join(parts[i-1:])
    
    # If no part with a number is found, return the entire last part
    return parts[-1]

for mesh, mesh_name in meshes_list:
    mesh_number_part = get_last_part_with_number(mesh_name)
    
    # Find a matching material based on the extracted number part
    for material, material_name in materials_list:
        if mesh_number_part in material_name:
            unreal.StaticMesh.set_material(mesh, 0, material)

# Save the modified meshes if needed
for mesh, _ in meshes_list:
    unreal.EditorAssetLibrary.save_asset(mesh)

print("Materials applied to meshes based on name matching.")
