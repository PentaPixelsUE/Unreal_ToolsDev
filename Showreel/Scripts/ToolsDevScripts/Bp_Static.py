import unreal



eal=unreal.EditorAssetLibrary()


def check_files():
    dir_path='/Game/ToolsDev/SkeltalMeshes/'
    if eal.does_directory_exist(dir_path):
        unreal.log_warning("WE HAVE SHIT ")
        return True
    else:
        unreal.log_warning("No Such File or Directory")


check_files()



def create_an_actor_blueprint(asset_prefix)

    package_path = '/Game/ToolsDev/SkeletalMeshes/'