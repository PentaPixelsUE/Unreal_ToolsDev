import sys
import unreal
project_path= unreal.Paths.project_dir()
scritps_path = project_path + 'Scripts/ToolsDevScripts'

sys.path.append(scritps_path)
import prefix_check
import importlib
importlib.reload(prefix_check)