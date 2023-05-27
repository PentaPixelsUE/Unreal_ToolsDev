import unreal
import os

def Import_From_Disk(asset_prefix):
    # Get the project directory
    projectDir = unreal.Paths.project_dir() + 'ExternalFiles'
    
    # Check if asset prefix is empty
    if not asset_prefix:
        unreal.log_warning("Asset Prefix is Empty")
        return False
    
    # Walk through the directory tree
    for folder, subfolders, files in os.walk(projectDir):
        # Exclude the top-level directory
        if folder != projectDir:
            # Iterate over files in the current folder
            for f in files:
                # Check if the asset prefix is present in the filename (case-insensitive)
                if asset_prefix.lower() in f.lower():
                    unreal.log_warning("Found Assets For Import")
                    return True
    
    # No match found
    unreal.log_warning("No Match Found")
    return False

# Call the function with an asset prefix
asset_prefix = "my_asset"
Import_From_Disk(asset_prefix)
