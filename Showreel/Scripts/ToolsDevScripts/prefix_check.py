import unreal
import os




def Import_From_Disk(asset_prefix):
    projectDir = unreal.Paths.project_dir() + 'ExternalFiles'
    for folder, subfolders, files in os.walk(projectDir):
        if folder != projectDir:
            for f in files:
                if asset_prefix.lower() in f.lower():
                    return True
    return False  # No match found

is_found = Import_From_Disk(asset_prefix)
if is_found:
    unreal.log_warning("Found Assets For Import")
else:
    unreal.log_warning("No Match Found")
