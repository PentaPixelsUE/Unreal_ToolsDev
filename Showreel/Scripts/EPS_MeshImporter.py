import sys
import unreal
project_path= unreal.Paths.project_dir()
scritps_path = project_path + 'Scripts'

sys.path.append(scritps_path)
import MeshImporter
import importlib
importlib.reload(MeshImporter)