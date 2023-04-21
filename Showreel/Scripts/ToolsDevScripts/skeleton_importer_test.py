import unreal
import pprint



def check_files(char):
    reg = unreal.AssetRegistryHelpers.get_asset_registry()
    eal = unreal.EditorAssetLibrary()
    skeletons=[]
    dir_path = "/Game/ToolsDev/SkeletalMeshes"
    if eal.does_directory_exist(dir_path):
        assets = reg.get_assets_by_path(dir_path, recursive=True)
        for asset in assets:
            full_name = asset.get_full_name()
            path = full_name.split(' ')[-1]
            skelmesh = unreal.load_asset(path)
            if isinstance(skelmesh, unreal.Skeleton):
                skeleton_name = skelmesh.get_name()
                if char in skeleton_name:
                    return path
    
                
    

skeletons = check_files(char)

pprint.pprint(skeletons)
