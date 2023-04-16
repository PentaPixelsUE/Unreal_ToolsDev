import unreal



eal=unreal.EditorAssetLibrary()


def check_files():
    dir_path='/Game/ToolsDev/SkeltalMeshes/Beach_Body.Beach_Body'
    unreal.log_warning(eal.does_directory_exist(dir_path))


check_files()
