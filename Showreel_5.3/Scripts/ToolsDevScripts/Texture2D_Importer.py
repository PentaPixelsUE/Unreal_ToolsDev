import unreal
import os




file_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".exr", ".hdr", ".tga","tiff","tif")


def import_textures(asset_prefix,file_extensions):
   
    projectDir = unreal.Paths.project_dir() + 'ExternalFiles'
    
    def get_file_path(folder, name):
        return os.path.join(folder, name).replace('\\', '/')

    def get_file_name(name):
        return os.path.splitext(name)[0]

    def get_file_ext(name):
        return os.path.splitext(name)[1]
    
    matching_files=[]
    steps = 0
    for folder, subfolders, files in os.walk(projectDir):
        if folder != projectDir:
            for f in files:
                if asset_prefix.lower() in f.lower() and f.lower().endswith(file_extensions):
                    steps += 1
                    full_path = get_file_path(folder, f)
                    name = get_file_name(f)
                    extension = get_file_ext(f)
                    matching_files.append((full_path,name))
    return steps,matching_files

                   

def create_slow_task():
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    steps,matching_files = import_textures(asset_prefix)
    with unreal.ScopedSlowTask(steps, 'Importing Textures...') as slow_task:
        unreal.log_warning(matching_files)
        slow_task.make_dialog(True)
        for i, (full_path,name) in enumerate(matching_files):
            unreal.log_warning(name)
            if slow_task.should_cancel():
                break
            slow_task.enter_progress_frame(1, f'Importing {name} {i}/{steps}')
            task = unreal.AssetImportTask()
            task.destination_path = '/Game/ToolsDev/Textures'
            task.destination_name = name
            task.filename = str(full_path)
            task.replace_existing = True
            task.save = False
            asset_tools.import_asset_tasks([task])  

                             
 
import_textures(asset_prefix,file_extensions)
create_slow_task()


