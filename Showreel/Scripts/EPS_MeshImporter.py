#This code is to be put in the Excute python script node in the editor utility widget to execute the .py file
#
#
#
##### EPS => Execute Python Script node
import sys
import unreal
project_path= unreal.Paths.project_dir()
scritps_path = project_path + 'Scripts'

sys.path.append(scritps_path)