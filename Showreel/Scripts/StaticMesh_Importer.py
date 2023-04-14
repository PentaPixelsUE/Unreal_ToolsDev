import unreal
import os


def build_import_tasks(filename: str, destination_name: str, destination_path: str, options):
    tasks = []
    task = unreal.AssetImportTask() # Contains data for a group of assets to import
    
    task.set_editor_property('async_', True)
    task.set_editor_property('automated', True)
    task.set_editor_property("destination_name", destination_name)
    task.set_editor_property("destination_path", destination_path)
    task.set_editor_property("filename", filename)
    task.set_editor_property('options', options)
    task.set_editor_property('replace_existing',True)
    task.set_editor_property('save',True)
    tasks.append(task)
    return tasks

def build_import_options(static_mesh_data):
    options = unreal.FbxImportUI()
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('create_physics_asset',False)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', False)
    options.set_editor_property('import_as_skeletal', False)
    options.set_editor_property("static_mesh_import_data", static_mesh_data)
    return options


def build_static_mesh_data():
    static_mesh_data = unreal.FbxStaticMeshImportData()
    static_mesh_data_properties ={
        'build_nanite':True,
        'auto_generate_collision': False,
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
    import_tasks = build_import_tasks(game_path, filename, "/Game/ToolsDev/StaticMeshes/", mesh_options)
    import_static_mesh(import_tasks)




projectDir = unreal.Paths.project_dir()+ 'ExternalFiles'

destination_path= unreal.Paths.project_content_dir() + '/ToolsDev/ImportedMeshes/'
found_files=[]
for folder,subfolders, files in os.walk(projectDir):
    if folder != projectDir:
        for f in files:
            if f.startswith("hat_"):
                static_mesh=os.path.join(folder, f)
                static_mesh = os.path.join(folder, f).replace('\\', '/')
                execute_import_static_mesh(static_mesh,str(f))
                