import unreal
import os




def Import_From_Disk(asset_prefix):
    projectDir = unreal.Paths.project_dir() + 'ExternalFiles'
    if not asset_prefix:
        unreal.log_warning("Asset Prefix is Empty")
        return False
    for folder, subfolders, files in os.walk(projectDir):
        if folder != projectDir:
            for f in files:
                if asset_prefix.lower() in f.lower():
                    unreal.log_warning("Found Assets For Import")
                    return True
    unreal.log_warning("No Match Found")
    return False  # No match found

    

Import_From_Disk(asset_prefix)