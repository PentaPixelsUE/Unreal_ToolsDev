import unreal
import os



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
    
                

def build_anim_import_options(skeleton_path):
    options = unreal.FbxImportUI()
    options.skeleton=unreal.load_asset(skeleton_path)
    options_editor_properties={
        'import_mesh': True,
        'automated_import_should_detect_type': False,
        'create_physics_asset':True,
        'import_textures': False,
        'import_materials': False,
        'mesh_type_to_import': unreal.FBXImportType.FBXIT_ANIMATION,
        
    }
    options.set_editor_properties(options_editor_properties)
    

    exported_time= unreal.FBXAnimationLengthImportType.FBXALIT_EXPORTED_TIME

    anim_editor_properties={
        'import_rotation': unreal.Rotator(0.0,0.0,0.0),
        'import_translation': unreal.Vector(0.0,0.0,0.0),
        'import_uniform_scale':1.0,
        'animation_length': exported_time,
        'remove_redundant_keys': False,
        'import_meshes_in_bone_hierarchy':True,
        'use_default_sample_rate':False,
        'import_bone_tracks':True,
        'delete_existing_morph_target_curves':False,
        'delete_existing_non_curve_custom_attributes':False,
        'do_not_import_curve_with_zero':True,
        'import_custom_attribute':True

    }
    options.anim_sequence_import_data.set_editor_properties(anim_editor_properties)
    return options

def build_import_tasks(filename: str, destination_name: str, destination_path: str, options):

    tasks = [] #Potential Cause for issues ? 
    task = unreal.AssetImportTask() # Contains data for a group of assets to import
    
    tasks_editor_properties = {
        'async_': True,
        'automated': True,
        "destination_name": destination_name,
        "destination_path": destination_path,
        "filename": filename,
        'options': options,
        'replace_existing':True,
        'save':True
    }
    task.set_editor_properties(tasks_editor_properties)
    tasks.append(task)
    return tasks

def import_animation(tasks):
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    asset_tools.import_asset_tasks(tasks)

def execute_import_animation_(game_path,filename,char):
    skeleton_path=check_files(char)
    mesh_options = build_anim_import_options(skeleton_path)
    import_tasks = build_import_tasks(game_path, filename.replace(".fbx", ""), "/Game/ToolsDev/Animations/", mesh_options)
    import_animation(import_tasks)


def Import_From_Disk(asset_prefix):
    projectDir = unreal.Paths.project_dir()+ 'ExternalFiles/'
    steps = 0
    matching_files=[]
    for folder,subfolders, files in os.walk(projectDir):
        if folder != projectDir:
            for f in files:
                if asset_prefix.lower() in f.lower():
                    steps +=1
                    animation_asset= os.path.join(folder, f).replace('\\', '/')
                    matching_files.append((animation_asset,f))
    return steps,matching_files

def create_slow_task():
    steps, matching_files = Import_From_Disk(asset_prefix)
    with unreal.ScopedSlowTask(steps,'Importing Assets...') as slow_task:
        slow_task.make_dialog(True)
        for i,(animation_asset,f) in enumerate(matching_files):
            if slow_task.should_cancel():
                break
            slow_task.enter_progress_frame(1,f'Importing Assets...{i}/{steps}')
            execute_import_animation_(animation_asset,f,char)


Import_From_Disk(asset_prefix)
create_slow_task()

