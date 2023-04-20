import sys
import unreal
project_path= unreal.Paths.project_dir()
scripts_path = project_path + 'Scripts/ToolsDevScripts/'

sys.path.append(scripts_path)
import Bp_Skel
import importlib
importlib.reload(Bp_Skel)