import unreal



eal=unreal.EditorAssetLibrary()


def check_files():
    dir_path='/Game/ToolsDev/SkeletalMeshes/'
    if eal.does_directory_exist(dir_path) and eal.does_directory_have_assets(dir_path+'/'):
        unreal.log_warning("WE HAVE SHIT ")
        
        return True
    else: 
        unreal.log_warning("The Are No Skeletons to animate")
        return False
        
    


skel=check_files()
