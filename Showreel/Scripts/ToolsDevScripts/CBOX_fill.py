
import unreal



def check_files(existing_names=[]):
    reg = unreal.AssetRegistryHelpers.get_asset_registry()
    eal = unreal.EditorAssetLibrary()
    dir_path = '/Game/ToolsDev/SkeletalMeshes/'
    first_names = existing_names

    if eal.does_directory_exist(dir_path):
        assets = reg.get_assets_by_path(dir_path, recursive=False)
        for asset in assets:
            name = asset.asset_name
            first_name = str(name).split('_')[0]
            if first_name not in first_names:
                first_names.append(first_name)
                

    else:
        print("Directory does not exist.")
        return []

    unique_first_names = list(set(first_names))
    return unique_first_names

existing_names= check_files()


for char in existing_names:
    if char in existing_names:
        char_cbox.add_option(char)
           

