import unreal




def build_import_tasks(filename: str, destination_name: str, destination_path: str, options):
    tasks = []
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property("destination_name", destination_name)
    task.set_editor_property("destination_path", destination_path)
    task.set_editor_property("filename", filename)
    task.set_editor_property('options', options)
    tasks.append(task)
    return tasks



def build_import_options(static_mesh_data):
    options = unreal.FbxImportUI()
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', False)
    options.set_editor_property('import_as_skeletal', False)
    options.set_editor_property("static_mesh_import_data", static_mesh_data)
    return options


def build_static_mesh_data():
    static_mesh_data = unreal.FbxStaticMeshImportData()
    static_mesh_data.set_editor_property("build_nanite", False)
    static_mesh_data.set_editor_property("auto_generate_collision", False)
    return static_mesh_data


def execute_import_static_mesh(game_path):
    mesh_data = build_static_mesh_data()
    mesh_options = build_import_options(mesh_data)
    import_tasks = build_import_tasks(game_path, "name", "/Game/ImportFolder", mesh_options)
    assetimport_static_mesh(import_tasks)

execute_import_static_mesh(r"C:\Users\deonw\OneDrive\Desktop\Import_Static_Mesh_Test.FBX")