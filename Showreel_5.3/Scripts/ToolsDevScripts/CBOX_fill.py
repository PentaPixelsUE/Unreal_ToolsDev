
import unreal


def check_files(existing_names=[]):
    reg = unreal.AssetRegistryHelpers.get_asset_registry()
    eal = unreal.EditorAssetLibrary()
    dir_path = "/Game/ToolsDev/SkeletalMeshes"
    if eal.does_directory_exist(dir_path):
        assets = reg.get_assets_by_path(dir_path, recursive=True)
        for asset in assets:
            full_name = asset.get_full_name()
            path = full_name.split(' ')[-1]
            skelmesh = unreal.load_asset(path)
            data = unreal.SystemLibrary()
            name = data.get_object_name(skelmesh)
            if isinstance(skelmesh, unreal.SkeletalMesh):
                asset_name=name.split('_')[0]
                if asset_name not in existing_names:
                    existing_names.append(asset_name)
    return existing_names




existing_names=check_files()


char_cbox.clear_options()
for name in existing_names:
    char_cbox.add_option(name)