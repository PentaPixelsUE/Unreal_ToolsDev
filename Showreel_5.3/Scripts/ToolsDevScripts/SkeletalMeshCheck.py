import unreal

eal = unreal.EditorAssetLibrary()
dir_path = "/Game/ToolsDev/SkeletalMeshes"
exist=eal.does_directory_exist(dir_path) and eal.does_directory_have_assets(dir_path)
hasanim=exist
