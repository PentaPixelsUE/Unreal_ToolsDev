import unreal
from Material_Assign import Materials
mel = unreal.MaterialEditingLibrary
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
eal = unreal.EditorAssetLibrary

# Read ALL textures
Tex_Dir = "/Game/Shaders/Textures/"
MA_Dir = "/Game/Shaders/Materials/"
Mesh_Dir="/Game/Shaders/Models/"
textures = eal.list_assets(directory_path=Tex_Dir, recursive=True, include_folder=False)

# Create a dictionary to store the texture categories
texture_categories = {}

for tex in textures:
    loaded_tex = unreal.load_asset(tex)
    tex_name = loaded_tex.get_name()
    # Split the texture name at "_"
    parts = tex_name.split("_")

    if len(parts) > 1:
        # Extract the part before the last "_"
        prefix = '_'.join(parts[:-1])

        # Extract the last part and remove "BaseColor" from it
        suffix = parts[-1]

        # Initialize or update the texture category in the dictionary
        if prefix not in texture_categories:
            texture_categories[prefix] = [suffix]
        else:
            texture_categories[prefix].append(suffix)

# for prefix, suffixes in texture_categories.items():
#     warning=(f"{prefix} has {', '.join(suffixes)}")
#     unreal.log_warning(warning)
posx=-800
for prefix, suffixes in texture_categories.items():
    # Create a new material for each prefix
    
    new_mat = asset_tools.create_asset(asset_name='MA_' + prefix, package_path=MA_Dir, asset_class=unreal.Material, factory=unreal.MaterialFactoryNew())

    # Iterate through the suffixes (texture types)
    posy=0

    for suffix in suffixes:
        
        
        # Create a material expression for the texture sample
        create_expression = unreal.MaterialEditingLibrary.create_material_expression
        texture_sample = create_expression(new_mat, unreal.MaterialExpressionTextureSample,posx,posy)

        # Set the sampler type to NORMAL
        if "Normal"in suffix:
            texture_sample.sampler_type = unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL

        # Construct the expected texture name for this suffix
        expected_tex_name = prefix + "_" + suffix

        # Find and load the corresponding texture
        for tex in textures:
            loaded_tex = unreal.load_asset(tex)
            tex_name = loaded_tex.get_name()

            if tex_name == expected_tex_name:
                # Assign the loaded texture to the texture sample expression
                texture_sample.texture = loaded_tex

                # Connect the texture sample expression to the appropriate material property based on the suffix
                if "BaseColor" in suffix:
                    unreal.MaterialEditingLibrary.connect_material_property(texture_sample, '', unreal.MaterialProperty.MP_BASE_COLOR)
                elif "Roughness" in suffix:
                    unreal.MaterialEditingLibrary.connect_material_property(texture_sample, '', unreal.MaterialProperty.MP_ROUGHNESS)
                elif "Metallic" in suffix:
                    unreal.MaterialEditingLibrary.connect_material_property(texture_sample, '', unreal.MaterialProperty.MP_METALLIC)
                elif "Normal" in suffix:
                    unreal.MaterialEditingLibrary.connect_material_property(texture_sample, '', unreal.MaterialProperty.MP_NORMAL)
        posy+=500
    mel.recompile_material(new_mat)
    eal.save_loaded_asset(new_mat)
      


for mat in Materials:   
    unreal.reload(mat)
