import unreal
import re


mel = unreal.MaterialEditingLibrary
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
eal = unreal.EditorAssetLibrary

# Read ALL textures
Tex_Dir = "/Game/Shaders/Textures/"
MA_Dir = "/Game/Shaders/Materials/"
Mesh_Dir = "/Game/Shaders/Models/"
textures = eal.list_assets(directory_path=Tex_Dir, recursive=True, include_folder=False)
meshes = unreal.EditorAssetLibrary.list_assets(directory_path=Mesh_Dir, recursive=True, include_folder=False)
# Create a dictionary to store the texture categories
texture_categories = {}
steps=0


def get_last_part_with_number(sop):
    # Convert the sop tuple to a string
    sop_str = str(sop)

    # Perform the split operation on the string
    parts = sop_str.split("_")

    for i in range(len(parts) - 1, -1, -1):
        if re.search(r'\d', parts[i]):
            return "_".join(parts[i-1:])

    # If no part with a number is found, return the entire last part
    return parts[-1]





for tex in textures:
    loaded_tex = unreal.load_asset(tex)
    tex_name = loaded_tex.get_name()
    # Split the texture name at "_"
    parts = tex_name.split("_")

    if len(parts) > 1:
        # Extract the part before the last "_"
        prefix = '_'.join(parts[:-1])

        # Extract the last part
        suffix = parts[-1]

        # Initialize or update the texture category in the dictionary
        if prefix not in texture_categories:
            texture_categories[prefix] = [suffix]
        else:
            texture_categories[prefix].append(suffix)



for prefix, suffixes in texture_categories.items():
    print( f"{prefix} has {', '.join(suffixes)}")
  

    


def create_master_material(texture_directory, material_directory):
    master_texture_dir = texture_directory + '/Base_Textues'
    posy = 0
    posx = -800
    new_mat = asset_tools.create_asset(asset_name='MASTER_MATERIAL', package_path=material_directory, asset_class=unreal.Material, factory=unreal.MaterialFactoryNew())
    new_mat.set_editor_property("BlendMode",unreal.BlendMode.BLEND_MASKED)
    textures = eal.list_assets(directory_path=master_texture_dir, recursive=True, include_folder=False)
    
    for tex in textures:
        loaded_tex = unreal.load_asset(tex)
        tex_name = loaded_tex.get_name()

        if "Normal" in tex_name:
            # Create a new material expression for each texture (inside the loop)

            create_expression = unreal.MaterialEditingLibrary.create_material_expression
            texture_sample = create_expression(new_mat, unreal.MaterialExpressionTextureSampleParameter2D, posx, posy)

            static_switch_param=create_expression(new_mat,unreal.MaterialExpressionStaticSwitchParameter,posx+400,posy)
            static_switch=create_expression(new_mat,unreal.MaterialExpressionStaticSwitch,posx+400,posy+400)

            texture_sample.set_editor_property("parameter_name", tex_name)
            static_switch.set_editor_property("default_value",False)
            texture_sample.texture = loaded_tex
            texture_sample.set_editor_property("SamplerType", unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)
            static_switch_param.set_editor_property("parameter_name",tex_name)
           
            

            unreal.MaterialEditingLibrary.connect_material_expressions(texture_sample,'',static_switch,'')
            unreal.MaterialEditingLibrary.connect_material_expressions(texture_sample,'',static_switch_param,'True')
            unreal.MaterialEditingLibrary.connect_material_expressions(static_switch,'',static_switch_param,'False')

            
            unreal.MaterialEditingLibrary.connect_material_property(static_switch_param, '', unreal.MaterialProperty.MP_NORMAL)
            


        else:
            # Create a new material expression for each texture (inside the loop)
            create_expression = unreal.MaterialEditingLibrary.create_material_expression
            texture_sample = create_expression(new_mat, unreal.MaterialExpressionTextureSampleParameter2D, posx, posy)
            texture_sample.texture = loaded_tex
            texture_sample.set_editor_property("parameter_name", tex_name)
            static_switch_param=create_expression(new_mat,unreal.MaterialExpressionStaticSwitchParameter,posx+400,posy)
            static_switch=create_expression(new_mat,unreal.MaterialExpressionStaticSwitch,posx+400,posy+400)
           
            
            static_switch.set_editor_property("default_value",False)
            static_switch_param.set_editor_property("parameter_name",tex_name)
            
        
            
            unreal.MaterialEditingLibrary.connect_material_expressions(texture_sample,'',static_switch,'')
            unreal.MaterialEditingLibrary.connect_material_expressions(texture_sample,'',static_switch_param,'True')
            unreal.MaterialEditingLibrary.connect_material_expressions(static_switch,'',static_switch_param,'False')

            if "basecolor" in tex_name.lower():
                unreal.MaterialEditingLibrary.connect_material_property(static_switch_param, '', unreal.MaterialProperty.MP_BASE_COLOR)
            elif "Roughness" in tex_name:
                unreal.MaterialEditingLibrary.connect_material_property(static_switch_param, '', unreal.MaterialProperty.MP_ROUGHNESS)
            elif "Metallic" in tex_name:
                unreal.MaterialEditingLibrary.connect_material_property(static_switch_param, '', unreal.MaterialProperty.MP_METALLIC)   
            elif "Opacity" in tex_name:
                unreal.MaterialEditingLibrary.connect_material_property(static_switch_param, '', unreal.MaterialProperty.MP_OPACITY_MASK)
            elif "Specular" in tex_name:
                unreal.MaterialEditingLibrary.connect_material_property(static_switch_param, '', unreal.MaterialProperty.MP_SPECULAR)
        posy += 500
    return new_mat


def create_material_instances(texture_categories, mat_dir, master):
 
    

    for prefix, suffixes in texture_categories.items():
            
        # Construct the instance material name based on the prefix
        instance_mat_name = f'MA_Inst_{prefix}'
        instance_mat_new = asset_tools.create_asset(asset_name=instance_mat_name, package_path=mat_dir, asset_class=unreal.MaterialInstanceConstant, factory=None)
        instance_mat_new.set_editor_property("parent", master)
     
        
        matching_textures = [tex for tex in textures if prefix in tex ]
    
        matching_textures.reverse()

        for tex in matching_textures:
            loaded_tex = unreal.load_asset(tex)
            tex_name = loaded_tex.get_name()
            
            # Determine the appropriate suffix based on the texture name
            for suffix in suffixes:
                if suffix in tex_name:
                    print(f"TEXTURE NAME = {tex_name}+ SUFFIX = {suffix} LOADED TEXTURE = {loaded_tex}")
            
                    mel.set_material_instance_static_switch_parameter_value(instance_mat_new, suffix, True, unreal.MaterialParameterAssociation.GLOBAL_PARAMETER)
                    
                    mel.set_material_instance_texture_parameter_value(instance_mat_new, suffix, loaded_tex)
                    
   
            # Break the inner loop after assigning the texture to the correct suffix
                    break
    return instance_mat_new
      
   
              
    
    

    





new_mat=create_master_material(Tex_Dir, MA_Dir)

create_material_instances(texture_categories,MA_Dir,new_mat)

