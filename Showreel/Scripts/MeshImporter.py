import os
import unreal as ue





                


def staticmeshimportparams(Fbx_static_mesh_import_data):
    ui_import= ue.FbxImportUI()
    task_properties = {
        'import_mesh': True,
        'import_as_skeletal': False,
        'import_materials': True,
        'import_textures': False,
        'static_mesh_import_data':Fbx_static_mesh_import_data
    }
    ui_import.set_editor_properties(task_properties)
    return ui_import


def fbximportdata():
    import_data= ue.FbxAssetImportData()
    fbx_import_data = {
        'convert_scene': True,
        'import_translation': ue.Vector(0.0,0.0,0.0),
        'import_rotation':ue.Rotator(0.0,0.0,0.0),
        'import_uniform_scale': 100   
        } 
    import_data.set_editor_properties(fbx_import_data)
    return import_data


def StaticMeshImportData():
    Fbx_static_mesh_import_data= ue.FbxStaticMeshImportData()
    fbx_import_properties = {
        'combine_meshes':True,
        'remove_degenerates':True,
        'generate_lightmap_u_vs':True,
        'auto_generate_collision':False,
        'build_nanite':True,
        'combine_meshes':True
    
    }

    Fbx_static_mesh_import_data.set_editor_properties(fbx_import_properties)

    return Fbx_static_mesh_import_data


def ImportTasks(filename,file_path,options=None):
    tasks = []
    task = ue.AssetImportTask()
    
    task_properties = {
        'async_':True,
        'automated':True,
        'destination_name':filename,
        'destination_path':file_path,
        'options':options
    }
    task.set_editor_properties(task_properties)
    tasks.append(task)
    return tasks


#Start with the project Directory
projectDir = ue.Paths.project_dir()
assetTools = ue.AssetToolsHelpers.get_asset_tools()
destination_path= '/Game/ToolsDev/StaticMeshes'

for folder,subfolders, files in os.walk(projectDir):
    if folder != projectDir:
        for f in files:
            if f.startswith("hat"):
                #DEBUGGER :FOUND THE FILES 
                static_mesh=f"Path: ", os.path.join(folder, f)
                print(static_mesh) 
                # create asset import data object        
                assetImportData = ue.AssetImportData()
                # set assetImportData attributes
                mesh_data = StaticMeshImportData()
                mesh_opts= staticmeshimportparams(mesh_data) 
                import_tasks=ImportTasks(str(f),destination_path,mesh_opts)
                assetTools.import_asset_tasks(import_tasks)