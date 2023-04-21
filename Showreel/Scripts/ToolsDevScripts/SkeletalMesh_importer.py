import unreal
import os


    
def build_import_options(Skeletal_mesh_data,mat):

    options = unreal.FbxImportUI()
    options_editor_properties={
        'import_mesh': True,
        'automated_import_should_detect_type': False,
        'create_physics_asset':False,
        'import_textures': False,
        'import_materials': mat,
        'import_as_skeletal':True,
        'mesh_type_to_import': unreal.FBXImportType.FBXIT_SKELETAL_MESH,
        "skeletal_mesh_import_data": Skeletal_mesh_data,
    }

    options.set_editor_properties(options_editor_properties)
    return options

def build_skeletal_mesh_data():
    Skeletal_mesh_data= unreal.FbxSkeletalMeshImportData()
    vertex_color_options=unreal.VertexColorImportOption.OVERRIDE
    import_content_type=unreal.FBXImportContentType.FBXICT_ALL
    normal_gen_method= unreal.FBXNormalGenerationMethod.BUILT_IN

    Skeletal_mesh_import_properties = {
        'bake_pivot_in_vertex' : False,
        'compute_weighted_normals': True,
        'convert_scene': True,
        'convert_scene_unit': False,
        'import_content_type': import_content_type,
        'import_meshes_in_bone_hierarchy':True,
        'import_uniform_scale':1.0,
        'normal_generation_method': normal_gen_method,
        'reorder_material_to_fbx_order':True,
        'use_t0_as_ref_pose': True,
        'vertex_color_import_option': vertex_color_options
    }
    Skeletal_mesh_data.set_editor_properties(Skeletal_mesh_import_properties)

    return Skeletal_mesh_data

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
        'save':False
    }
    task.set_editor_properties(tasks_editor_properties)
    tasks.append(task)
    return tasks

def import_skeletal_mesh(tasks):
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    asset_tools.import_asset_tasks(tasks)

def execute_import_skeletal_mesh(game_path,filename):
    mesh_data = build_skeletal_mesh_data()
    mesh_options = build_import_options(mesh_data,mat)
    import_tasks = build_import_tasks(game_path, filename.replace(".fbx", ""), "/Game/ToolsDev/SkeletalMeshes/", mesh_options)
    import_skeletal_mesh(import_tasks)



def Import_From_Disk(asset_prefix):
    projectDir = unreal.Paths.project_dir()+ 'ExternalFiles'
    steps = 0
    matching_files=[]
    for folder,subfolders, files in os.walk(projectDir):
        if folder != projectDir:
            for f in files:
                if asset_prefix.lower() in f.lower():
                    steps +=1
                    # Skeletal_mesh=os.path.join(folder, f)
                    Skeletal_mesh= os.path.join(folder, f).replace('\\', '/')
                    matching_files.append((Skeletal_mesh,f))
                    
    return steps,matching_files


def create_slow_task():
    steps, matching_files = Import_From_Disk(asset_prefix)
    with unreal.ScopedSlowTask(steps,'Importing Assets...') as slow_task:
        slow_task.make_dialog(True)
        for i,(skeletal_mesh,f) in enumerate(matching_files):
            if slow_task.should_cancel():
                break
            slow_task.enter_progress_frame(1,f'Importing Assets {f} {i}/{steps}')
            execute_import_skeletal_mesh(skeletal_mesh,f)
            #unreal.EditorAssetLibrary.save_directory("/Game/ToolsDev/SkeletalMeshes/",only_if_is_dirty=True,recursive=True)
            unreal.EditorAssetLibrary.checkout_directory(("/Game/ToolsDev/SkeletalMeshes/",recursive=True))

Import_From_Disk(asset_prefix)
create_slow_task()
cbox_update = True
