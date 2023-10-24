import unreal
#Define the directory containing your Skeletal Meshes
Skelmesh_dir = "/Game/ToolsDev/SkeletalMeshes/"
#List Skeletal Mesh assets
skelmeshes = unreal.EditorAssetLibrary.list_assets(directory_path=Skelmesh_dir, recursive=True, include_folder=False)
#Create empty lists to store the meshes, skeletons, and section IDs to merge
meshes_to_merge = []
#Iterate over the Skeletal Mesh assets and add them to the lists to merge
for mesh_path in skelmeshes:
    #Load each Skeletal Mesh asset
    mesh = unreal.EditorAssetLibrary.load_asset(mesh_path)

    # If the asset is a Skeletal Mesh, add it to the list of meshes to merge
    if isinstance(mesh, unreal.SkeletalMesh):
        
        meshes_to_merge.append(mesh)
        mappings=mesh.get_editor_property("asset_import_data")
        # Get the Skeleton associated with the Skeletal Mesh
        #skeleton = mesh.get_editor_property("skeleton")

        # Add the Skeleton to the list of skeletons to merge
    elif isinstance(mesh,unreal.Skeleton):
        skeleton=mesh#get the last skeleton
# Create a SkeletalMeshMergeParams object
#class unreal.SkeletalMeshMergeParams(mesh_section_mappings: 
# None = [], uv_transforms_per_mesh: None = [], 
# meshes_to_merge: None = [],
#  strip_top_lods: int = 0,
#  needs_cpu_access: bool = False,
#  skeleton_before: bool = False,
#  skeleton: Skeleton = Ellipsis)¶
skelprop=unreal.InterchangeGenericCommonSkeletalMeshesAndAnimationsProperties
skel_mesh_merge_params = unreal.SkeletalMeshMergeParams(
    mesh_section_mappings=[],  # Use an empty list for mesh_section_mappings
    uv_transforms_per_mesh=[],  # Use an empty list for uv_transforms_per_mesh
    meshes_to_merge=meshes_to_merge,
    strip_top_lods=0,
    needs_cpu_access=False,
    skeleton_before=True,
    skeleton=skeleton,
)
# Merge the Skeletal Meshes
merged_mesh = unreal.SkeletalMergingLibrary.merge_meshes(skel_mesh_merge_params)