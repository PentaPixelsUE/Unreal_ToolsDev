import os
import unreal as ue



def SetImportTasks(filename,destination_path,options=None):
    task_properties = {
        "async_": True,
        "destination_name": "",
        "destination_path": destination_path,
        "filename": filename,
        "replace_existing": True,
        "save": True,
        "options": True,
    }
    task = ue.AssetImportTask()
    for prop, value in task_properties.items():
        setattr(task, f"set_editor_property_{prop}", value)

    return task

def SetStaticMeshData():
    ui = ue.FbxImportUI()

    properties = {
        'import_mesh': True,
        'import_as_skeletal': False,
        'import_materials': True,
        'import_textures': False,
    }
    ui.set_editor_properties(properties)

    import_data = {
        'import_translation': ue.Vector(50, 0.0, 0.0),
        'import_rotation': ue.Rotator(0.0, 0.0, 0.0),
        'import_uniform_scale': 1.0,
        'combine_meshes': True,
        'auto_generate_collision': True,
    }
    ui.static_mesh_import_data.set_editor_properties(import_data)

    return ui



if __name__ == '__main__':
    #Start with the project Directory
    projectDir = ue.Paths.project_dir()


    for folder,subfolders, files in os.walk(projectDir):
        if folder != projectDir:
            for f in files:
                if f.startswith("hat"):
                    #DEBUGGER :FOUND THE FILES 
                    static_path=f"Path: ", os.path.join(folder, f)
                    


    

             
            
        





