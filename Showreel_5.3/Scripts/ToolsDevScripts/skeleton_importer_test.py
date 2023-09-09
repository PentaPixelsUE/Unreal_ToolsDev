

# def check_files():
#     reg = unreal.AssetRegistryHelpers.get_asset_registry()
#     eal = unreal.EditorAssetLibrary()
#     rig_h=unreal.RigHierarchy()
#     bones=[]
#     dir_path = "/Game/ToolsDev/SkeletalMeshes"
#     if eal.does_directory_exist(dir_path):
#         assets = reg.get_assets_by_path(dir_path, recursive=True)
#         for asset in assets:
#             full_name = asset.get_full_name()
#             path = full_name.split(' ')[-1]
#             skelmesh = unreal.load_asset(path)
#             if isinstance(skelmesh, unreal.Skeleton):
#                 tree = skelmesh.get_editor_property("bone_tree")
#                 for bone in tree:
#                     bones.append(rig_h.acquire_editor_element_handle())

                    

#     return bones

# bones = check_files()

# pprint.pprint(bones)

import unreal
import pprint

blueprint = unreal.load_object(name = '/Game/ToolsDev/SkeletalMeshes/Beach_Body_CtrlRig.Beach_Body_CtrlRig', outer = None)
hierarchy = blueprint.hierarchy
bones=hierarchy.get_bones()
for bone in bones:
    pprint.pprint(bone)



