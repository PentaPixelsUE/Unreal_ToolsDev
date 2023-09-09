import unreal


def create_blueprint(asset_skelmeshes_map):  
    subobject_datasys = unreal.SubobjectDataSubsystem()
    subob_data_bp_factory_lib=unreal.SubobjectDataBlueprintFunctionLibrary()      
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class", unreal.Actor)
    for asset_name, component_skelmeshes in asset_skelmeshes_map.items():
        for component_name, skelmesh in component_skelmeshes.items():
            blueprint = asset_tools.create_asset(asset_name, '/Game/ToolsDev/Blueprints', None, factory)

            subsystem = unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
            root_data_handle = subsystem.k2_gather_subobject_data_for_blueprint(blueprint)[0]
            
            sub_handle, fail_reason = subsystem.add_new_subobject(
                unreal.AddNewSubobjectParams(
                    parent_handle=root_data_handle,
                    new_class=unreal.SkeletalMeshComponent,
                    blueprint_context=blueprint
                )
            )

            if not fail_reason.is_empty():
                raise Exception(f"Failed to add sub-object {component_name} to blueprint {asset_name}: {fail_reason}")
            
            subobject_datasys.rename_subobject(sub_handle,component_name)
            component_data= subobject_datasys.k2_find_subobject_data_from_handle(sub_handle)
            sub_handle_object= subob_data_bp_factory_lib.get_object(component_data,even_if_pending_kill=False)
            unreal.SkeletalMeshComponent.set_skeletal_mesh_asset(sub_handle_object,skelmesh)
            

    return blueprint


def check_files():
    reg = unreal.AssetRegistryHelpers.get_asset_registry()
    eal = unreal.EditorAssetLibrary()
    dir_path = "/Game/ToolsDev/SkeletalMeshes"
    asset_skelmeshes_map = {}
    if eal.does_directory_exist(dir_path):
        assets = reg.get_assets_by_path(dir_path, recursive=True)
        for asset in assets:
            full_name = asset.get_full_name()
            path = full_name.split(' ')[-1]
            skelmesh = unreal.load_asset(path)
            data = unreal.SystemLibrary()
            name = data.get_object_name(skelmesh)
            if isinstance(skelmesh, unreal.SkeletalMesh):
                asset_name, component_name = name.split("_")
                if asset_name not in asset_skelmeshes_map:
                    asset_skelmeshes_map[asset_name] = {}
                asset_skelmeshes_map[asset_name][component_name] = skelmesh

        return asset_skelmeshes_map
    else:
        print("Directory does not exist.")
        return {}

# Example usage:
asset_skelmeshes_map = check_files()
create_blueprint(asset_skelmeshes_map)
for asset_name, component_skelmeshes in asset_skelmeshes_map.items():
    print("Skeletal Meshes for asset {}: ".format(asset_name))
    for component_name, skelmesh in component_skelmeshes.items():
        print("  Component {}: {}".format(component_name, skelmesh))


# for asset_name, component_names in asset_component_map.items():
#     blueprint = create_blueprint(asset_name, component_names,skelmeshes)
#     print(f"Created blueprint {asset_name} with {len(component_names)} components.")
