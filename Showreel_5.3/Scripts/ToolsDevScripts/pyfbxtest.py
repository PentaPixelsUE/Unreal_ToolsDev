import fbx as pyfbx

# Load the FBX file
fbx_path = 'D:\Projects\Showreel_2023\Showreel\ExternalFiles\Modular_Characters\King\King_Body.fbx'
fbx = pyfbx.FBX(fbx_path)

# Get the root node of the hierarchy
root_node = fbx.get_root()

# Define a recursive function to print the hierarchy
def print_hierarchy(node, indent=0):
    print(' ' * indent + node.get_name())
    for child in node.get_children():
        print_hierarchy(child, indent + 2)

# Print the hierarchy starting from the root node
print_hierarchy(root_node)

# Clean up
fbx.cleanup()
