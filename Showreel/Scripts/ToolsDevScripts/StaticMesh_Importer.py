import unreal
import os


def build_import_tasks(filename: str, destination_name: str, destination_path: str, options):
    tasks = []
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

def build_import_options(static_mesh_data):
    options = unreal.FbxImportUI()
    options_editor_properties={
        'import_mesh': True,
        'create_physics_asset':False,
        'import_textures': False,
        'import_materials': False,
        'import_as_skeletal':False,
        "static_mesh_import_data": static_mesh_data,
    }

    options.set_editor_properties(options_editor_properties)
    return options


def build_static_mesh_data():
    static_mesh_data = unreal.FbxStaticMeshImportData()
    static_mesh_data_properties ={
        'build_nanite':True,
        'auto_generate_collision': True,
        'convert_scene' : True
    }
    static_mesh_data.set_editor_properties(static_mesh_data_properties)
 
    return static_mesh_data

def import_static_mesh(tasks):
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    asset_tools.import_asset_tasks(tasks)


def execute_import_static_mesh(game_path,filename):
    mesh_data = build_static_mesh_data()
    mesh_options = build_import_options(mesh_data)
    import_tasks = build_import_tasks(game_path, filename.replace(".fbx", ""), "/Game/ToolsDev/StaticMeshes/", mesh_options)
    import_static_mesh(import_tasks)

def import_from_disk(asset_prefix):
    projectDir = unreal.Paths.project_dir() + 'ExternalFiles'
    steps = 0
    matching_files = []
    for folder, subfolders, files in os.walk(projectDir):
        if folder != projectDir:
            for f in files:
                if asset_prefix.lower() in f.lower():
                    steps += 1
                    static_mesh = os.path.join(folder, f).replace('\\', '/')
                    matching_files.append((static_mesh, f))
    return steps, matching_files

def create_slow_task():
    steps, matching_files = import_from_disk(asset_prefix)
    with unreal.ScopedSlowTask(steps, 'Importing Assets...') as slow_task:
        slow_task.make_dialog(True)
        for i, (static_mesh, f) in enumerate(matching_files):
            if slow_task.should_cancel():
                break
            slow_task.enter_progress_frame(1, f'Importing Assets... {i}/{steps}')
            execute_import_static_mesh(static_mesh, f)

import_from_disk(asset_prefix)
create_slow_task()


