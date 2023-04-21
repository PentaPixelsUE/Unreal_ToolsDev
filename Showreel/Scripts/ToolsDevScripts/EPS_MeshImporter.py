import sys
import unreal
project_path= unreal.Paths.project_dir()
scripts_path = project_path + 'Scripts/ToolsDevScripts/'

sys.path.append(scripts_path)
import skeleton_importer_test
import importlib
importlib.reload(skeleton_importer_test)