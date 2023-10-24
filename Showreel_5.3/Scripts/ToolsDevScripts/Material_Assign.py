import unreal
import re

Mesh_Dir = "/Game/Shaders/Models/"
MA_Dir = "/Game/Shaders/Materials/"
materials = unreal.EditorAssetLibrary.list_assets(directory_path=MA_Dir, recursive=True, include_folder=False)
meshes = unreal.EditorAssetLibrary.list_assets(directory_path=Mesh_Dir, recursive=True, include_folder=False)

def get_last_part_with_number(name):
    parts = name.split("_")
    
    for i in range(len(parts) - 1, -1, -1):
        if re.search(r'\d', parts[i]):
            return "_".join(parts[i-1:])
    
    # If no part with a number is found, return the entire last part
    return parts[-1]

mesh_list = []
mat_list = []
Preview_meshes=[]

for mat in materials:
    loaded_mat = unreal.EditorAssetLibrary.load_asset(mat)
    mat_name = str(loaded_mat.get_name())  # Convert to string
    mat_name = get_last_part_with_number(mat_name)
    mat_list.append(mat_name)

for mesh in meshes:
    loaded_mesh = unreal.EditorAssetLibrary.load_asset(mesh)
    mesh_name = str(loaded_mesh.get_name())  # Convert to string
    mesh_name = get_last_part_with_number(mesh_name)
    mesh_list.append(mesh_name)
    static_materials = loaded_mesh.get_editor_property("static_materials")

    if len(static_materials) > 1:
        for index, element in enumerate(static_materials):
            slot_name = str(element.get_editor_property("material_slot_name"))  # Convert to string
            
            for mat_name in mat_list:
                if slot_name == mat_name:
                    assigned_material = unreal.EditorAssetLibrary.load_asset(materials[mat_list.index(mat_name)])  # Load the assigned material
                    unreal.StaticMesh.set_material(loaded_mesh, index, assigned_material)
                    Preview_meshes.append(loaded_mesh)

    elif len(static_materials) == 1:
        for mat in materials:
            loaded_mat = unreal.EditorAssetLibrary.load_asset(mat)
            mat_name=loaded_mat.get_name()
            mat_name=get_last_part_with_number(mat_name)
            if mat_name.lower() in mesh_name.lower():
                print(mat_name)
                unreal.StaticMesh.set_material(loaded_mesh,0,loaded_mat)
                Preview_meshes.append(loaded_mesh)
                #print(f"{loaded_mesh}wiill be assigned at  index {index} of {loaded_mat}")
