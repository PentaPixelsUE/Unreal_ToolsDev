import unreal

# Define the directory containing your Skeletal Meshes
Skelmesh_dir = "/Game/ToolsDev/SkeletalMeshes/"

# List Skeletal Mesh assets
skelmeshes = unreal.EditorAssetLibrary.list_assets(directory_path=Skelmesh_dir, recursive=True, include_folder=False)

# Create empty lists to store the meshes, skeletons, and section IDs to merge
meshes_to_merge = []



# Iterate over the Skeletal Mesh assets and add them to the lists to merge
for mesh_path in skelmeshes:
    # Load each Skeletal Mesh asset
    mesh = unreal.EditorAssetLibrary.load_asset(mesh_path)

    # If the asset is a Skeletal Mesh, add it to the list of meshes to merge
    if isinstance(mesh, unreal.SkeletalMesh):
        meshes_to_merge.append(mesh)

        # Get the Skeleton associated with the Skeletal Mesh
        #skeleton = mesh.get_editor_property("skeleton")

        # Add the Skeleton to the list of skeletons to merge
    elif isinstance(mesh, unreal.Skeleton):
        skeleton=mesh

        # Add the section ID to the list of section IDs to merge
        

# # Create a SkeletonMergeParams object
# skeleton_merge_params = unreal.SkeletonMergeParams(
#     skeletons_to_merge=skeletons_to_merge,
#     merge_sockets=False,
#     merge_virtual_bones=False,
#     merge_curve_names=False,
#     merge_blend_profiles=False,
#     merge_anim_slot_groups=False,
#     check_skeletons_compatibility=False
# )

# # Merge the skeletons
# merged_skeleton = unreal.SkeletalMergingLibrary.merge_skeletons(skeleton_merge_params)

# Create a SkeletalMeshMergeParams object
#class unreal.SkeletalMeshMergeParams(mesh_section_mappings: None = [], uv_transforms_per_mesh: None = [], meshes_to_merge: None = [], strip_top_lods: int = 0, needs_cpu_access: bool = False, skeleton_before: bool = False, skeleton: Skeleton = Ellipsis)¶
skel_mesh_merge_params = unreal.SkeletalMeshMergeParams(
    mesh_section_mappings=[],  # Use an empty list for mesh_section_mappings
    uv_transforms_per_mesh=[],  # Use an empty list for uv_transforms_per_mesh
    meshes_to_merge=meshes_to_merge,
    strip_top_lods=0,
    needs_cpu_access=False,
    skeleton_before=True 
)


# Merge the Skeletal Meshes
merged_mesh = unreal.SkeletalMergingLibrary.merge_meshes(skel_mesh_merge_params)

# # Create a new Skeletal Mesh asset
asset_tools=unreal.AssetToolsHelpers.get_asset_tools()
new_skelmesh = asset_tools.create_asset(
    "MergedSkeletalMesh",
    Skelmesh_dir,
    unreal.SkeletalMesh,
    None,
    "TEST"
)


