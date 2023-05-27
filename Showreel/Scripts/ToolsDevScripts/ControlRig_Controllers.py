#WIP


#TESTING IF WE CAN AUTOMATE THE CONTROL RIG CREATION FOR CONTROLS IN A LOOP


#TEST WITH A PREDEFINED LIST OF CTRL NAMES (LATER WE WILL USE A SCRIPT TO READ ALL THE BONES AND )
################################################################################################################
bone_ctrl_names = ['Root_ctrl', 'Body_ctrl', 'Arm_ctrl', 'Leg_ctrl']

def create_control(control_name, parent_name=None):
    control_settings = unreal.RigControlSettings()
    control_settings.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
    control_settings.control_type = unreal.RigControlType.EULER_TRANSFORM
    control_settings.display_name = 'None'
    control_settings.draw_limits = True
    control_settings.shape_color = unreal.LinearColor(1.0, 0.0, 0.0, 1.0)
    control_settings.shape_name = 'Default'
    control_settings.shape_visible = True
    control_settings.is_transient_control = False
    control_settings.limit_enabled = [unreal.RigControlLimitEnabled(False, False)] * 9
    control_settings.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.0, 0.0, 0.0], rotation=[0.0, 0.0, 0.0], scale=[0.0, 0.0, 0.0]))
    control_settings.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.0, 0.0, 0.0], rotation=[0.0, 0.0, 0.0], scale=[0.0, 0.0, 0.0]))
    control_settings.primary_axis = unreal.RigControlAxis.X

    if parent_name:
        hierarchy_controller.add_control(control_name, parent_name, control_settings, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.0, 0.0, 0.0], rotation=[0.0, 0.0, 0.0], scale=[1.0, 1.0, 1.0])))
    else:
        hierarchy_controller.add_control(control_name, '', control_settings, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.0, 0.0, 0.0], rotation=[0.0, 0.0, 0.0], scale=[1.0, 1.0, 1.0])))


for control_name in bone_ctrl_names:
    create_control(control_name)
################################################################################################################


#FULL CTRLS CREATION IN A CTRLRIG BP
import unreal



blueprint = unreal.load_object(name = '/Game/ToolsDev/SkeletalMeshes/Beach_Body_CtrlRig.Beach_Body_CtrlRig', outer = None)
hierarchy = blueprint.hierarchy
hierarchy_controller = hierarchy.get_controller()
library = blueprint.get_local_function_library()
library_controller = blueprint.get_controller(library)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_root_ctrl = unreal.RigControlSettings()
control_settings_root_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_root_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_root_ctrl.display_name = 'None'
control_settings_root_ctrl.draw_limits = True
control_settings_root_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_root_ctrl.shape_name = 'Default'
control_settings_root_ctrl.shape_visible = True
control_settings_root_ctrl.is_transient_control = False
control_settings_root_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_root_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_root_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_root_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Root_ctrl', '', control_settings_root_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Root_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Root_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Root_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Root_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Root_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_body_ctrl = unreal.RigControlSettings()
control_settings_body_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_body_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_body_ctrl.display_name = 'None'
control_settings_body_ctrl.draw_limits = True
control_settings_body_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_body_ctrl.shape_name = 'Default'
control_settings_body_ctrl.shape_visible = True
control_settings_body_ctrl.is_transient_control = False
control_settings_body_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_body_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_body_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_body_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Body_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Root_ctrl'), control_settings_body_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Body_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Body_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Body_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Body_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Body_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_hips_ctrl = unreal.RigControlSettings()
control_settings_hips_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_hips_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_hips_ctrl.display_name = 'None'
control_settings_hips_ctrl.draw_limits = True
control_settings_hips_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_hips_ctrl.shape_name = 'Default'
control_settings_hips_ctrl.shape_visible = True
control_settings_hips_ctrl.is_transient_control = False
control_settings_hips_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_hips_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_hips_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_hips_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Hips_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Body_ctrl'), control_settings_hips_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Hips_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Hips_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Hips_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Hips_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Hips_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_abdomen_ctrl = unreal.RigControlSettings()
control_settings_abdomen_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_abdomen_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_abdomen_ctrl.display_name = 'None'
control_settings_abdomen_ctrl.draw_limits = True
control_settings_abdomen_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_abdomen_ctrl.shape_name = 'Default'
control_settings_abdomen_ctrl.shape_visible = True
control_settings_abdomen_ctrl.is_transient_control = False
control_settings_abdomen_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_abdomen_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_abdomen_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_abdomen_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Abdomen_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Hips_ctrl'), control_settings_abdomen_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Abdomen_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Abdomen_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Abdomen_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Abdomen_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Abdomen_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_torso_ctrl = unreal.RigControlSettings()
control_settings_torso_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_torso_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_torso_ctrl.display_name = 'None'
control_settings_torso_ctrl.draw_limits = True
control_settings_torso_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_torso_ctrl.shape_name = 'Default'
control_settings_torso_ctrl.shape_visible = True
control_settings_torso_ctrl.is_transient_control = False
control_settings_torso_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_torso_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_torso_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_torso_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Torso_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Abdomen_ctrl'), control_settings_torso_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Torso_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Torso_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Torso_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Torso_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Torso_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_chest_ctrl = unreal.RigControlSettings()
control_settings_chest_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_chest_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_chest_ctrl.display_name = 'None'
control_settings_chest_ctrl.draw_limits = True
control_settings_chest_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_chest_ctrl.shape_name = 'Default'
control_settings_chest_ctrl.shape_visible = True
control_settings_chest_ctrl.is_transient_control = False
control_settings_chest_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_chest_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_chest_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_chest_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Chest_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Torso_ctrl'), control_settings_chest_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Chest_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Chest_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Chest_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Chest_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Chest_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_neck_ctrl = unreal.RigControlSettings()
control_settings_neck_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_neck_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_neck_ctrl.display_name = 'None'
control_settings_neck_ctrl.draw_limits = True
control_settings_neck_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_neck_ctrl.shape_name = 'Default'
control_settings_neck_ctrl.shape_visible = True
control_settings_neck_ctrl.is_transient_control = False
control_settings_neck_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_neck_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_neck_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_neck_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Neck_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Chest_ctrl'), control_settings_neck_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Neck_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Neck_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Neck_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Neck_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Neck_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_head_ctrl = unreal.RigControlSettings()
control_settings_head_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_head_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_head_ctrl.display_name = 'None'
control_settings_head_ctrl.draw_limits = True
control_settings_head_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_head_ctrl.shape_name = 'Default'
control_settings_head_ctrl.shape_visible = True
control_settings_head_ctrl.is_transient_control = False
control_settings_head_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_head_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_head_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_head_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Head_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Neck_ctrl'), control_settings_head_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Head_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Head_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Head_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Head_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Head_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_head_end_ctrl = unreal.RigControlSettings()
control_settings_head_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_head_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_head_end_ctrl.display_name = 'None'
control_settings_head_end_ctrl.draw_limits = True
control_settings_head_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_head_end_ctrl.shape_name = 'Default'
control_settings_head_end_ctrl.shape_visible = True
control_settings_head_end_ctrl.is_transient_control = False
control_settings_head_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_head_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_head_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_head_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Head_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Head_ctrl'), control_settings_head_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Head_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Head_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Head_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Head_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Head_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_shoulder_l_ctrl = unreal.RigControlSettings()
control_settings_shoulder_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_shoulder_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_shoulder_l_ctrl.display_name = 'None'
control_settings_shoulder_l_ctrl.draw_limits = True
control_settings_shoulder_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_shoulder_l_ctrl.shape_name = 'Default'
control_settings_shoulder_l_ctrl.shape_visible = True
control_settings_shoulder_l_ctrl.is_transient_control = False
control_settings_shoulder_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_shoulder_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_shoulder_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_shoulder_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Shoulder_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Chest_ctrl'), control_settings_shoulder_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_upper_arm_l_ctrl = unreal.RigControlSettings()
control_settings_upper_arm_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_upper_arm_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_upper_arm_l_ctrl.display_name = 'None'
control_settings_upper_arm_l_ctrl.draw_limits = True
control_settings_upper_arm_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_upper_arm_l_ctrl.shape_name = 'Default'
control_settings_upper_arm_l_ctrl.shape_visible = True
control_settings_upper_arm_l_ctrl.is_transient_control = False
control_settings_upper_arm_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_upper_arm_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_upper_arm_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_upper_arm_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('UpperArm_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_L_ctrl'), control_settings_upper_arm_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_lower_arm_l_ctrl = unreal.RigControlSettings()
control_settings_lower_arm_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_lower_arm_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_lower_arm_l_ctrl.display_name = 'None'
control_settings_lower_arm_l_ctrl.draw_limits = True
control_settings_lower_arm_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_lower_arm_l_ctrl.shape_name = 'Default'
control_settings_lower_arm_l_ctrl.shape_visible = True
control_settings_lower_arm_l_ctrl.is_transient_control = False
control_settings_lower_arm_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_lower_arm_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_arm_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_arm_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('LowerArm_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_L_ctrl'), control_settings_lower_arm_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_wrist_l_ctrl = unreal.RigControlSettings()
control_settings_wrist_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_wrist_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_wrist_l_ctrl.display_name = 'None'
control_settings_wrist_l_ctrl.draw_limits = True
control_settings_wrist_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_wrist_l_ctrl.shape_name = 'Default'
control_settings_wrist_l_ctrl.shape_visible = True
control_settings_wrist_l_ctrl.is_transient_control = False
control_settings_wrist_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_wrist_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_wrist_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_wrist_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Wrist_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_L_ctrl'), control_settings_wrist_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_index1_l_ctrl = unreal.RigControlSettings()
control_settings_index1_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_index1_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_index1_l_ctrl.display_name = 'None'
control_settings_index1_l_ctrl.draw_limits = True
control_settings_index1_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_index1_l_ctrl.shape_name = 'Default'
control_settings_index1_l_ctrl.shape_visible = True
control_settings_index1_l_ctrl.is_transient_control = False
control_settings_index1_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_index1_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index1_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index1_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Index1_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_L_ctrl'), control_settings_index1_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_index2_l_ctrl = unreal.RigControlSettings()
control_settings_index2_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_index2_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_index2_l_ctrl.display_name = 'None'
control_settings_index2_l_ctrl.draw_limits = True
control_settings_index2_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_index2_l_ctrl.shape_name = 'Default'
control_settings_index2_l_ctrl.shape_visible = True
control_settings_index2_l_ctrl.is_transient_control = False
control_settings_index2_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_index2_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index2_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index2_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Index2_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_L_ctrl'), control_settings_index2_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_index3_l_ctrl = unreal.RigControlSettings()
control_settings_index3_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_index3_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_index3_l_ctrl.display_name = 'None'
control_settings_index3_l_ctrl.draw_limits = True
control_settings_index3_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_index3_l_ctrl.shape_name = 'Default'
control_settings_index3_l_ctrl.shape_visible = True
control_settings_index3_l_ctrl.is_transient_control = False
control_settings_index3_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_index3_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index3_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index3_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Index3_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_L_ctrl'), control_settings_index3_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_index4_l_ctrl = unreal.RigControlSettings()
control_settings_index4_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_index4_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_index4_l_ctrl.display_name = 'None'
control_settings_index4_l_ctrl.draw_limits = True
control_settings_index4_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_index4_l_ctrl.shape_name = 'Default'
control_settings_index4_l_ctrl.shape_visible = True
control_settings_index4_l_ctrl.is_transient_control = False
control_settings_index4_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_index4_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index4_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index4_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Index4_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_L_ctrl'), control_settings_index4_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_index4_l_end_ctrl = unreal.RigControlSettings()
control_settings_index4_l_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_index4_l_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_index4_l_end_ctrl.display_name = 'None'
control_settings_index4_l_end_ctrl.draw_limits = True
control_settings_index4_l_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_index4_l_end_ctrl.shape_name = 'Default'
control_settings_index4_l_end_ctrl.shape_visible = True
control_settings_index4_l_end_ctrl.is_transient_control = False
control_settings_index4_l_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_index4_l_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index4_l_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index4_l_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Index4_L_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_L_ctrl'), control_settings_index4_l_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_middle1_l_ctrl = unreal.RigControlSettings()
control_settings_middle1_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_middle1_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_middle1_l_ctrl.display_name = 'None'
control_settings_middle1_l_ctrl.draw_limits = True
control_settings_middle1_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_middle1_l_ctrl.shape_name = 'Default'
control_settings_middle1_l_ctrl.shape_visible = True
control_settings_middle1_l_ctrl.is_transient_control = False
control_settings_middle1_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_middle1_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle1_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle1_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Middle1_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_L_ctrl'), control_settings_middle1_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_middle2_l_ctrl = unreal.RigControlSettings()
control_settings_middle2_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_middle2_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_middle2_l_ctrl.display_name = 'None'
control_settings_middle2_l_ctrl.draw_limits = True
control_settings_middle2_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_middle2_l_ctrl.shape_name = 'Default'
control_settings_middle2_l_ctrl.shape_visible = True
control_settings_middle2_l_ctrl.is_transient_control = False
control_settings_middle2_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_middle2_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle2_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle2_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Middle2_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_L_ctrl'), control_settings_middle2_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_middle3_l_ctrl = unreal.RigControlSettings()
control_settings_middle3_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_middle3_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_middle3_l_ctrl.display_name = 'None'
control_settings_middle3_l_ctrl.draw_limits = True
control_settings_middle3_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_middle3_l_ctrl.shape_name = 'Default'
control_settings_middle3_l_ctrl.shape_visible = True
control_settings_middle3_l_ctrl.is_transient_control = False
control_settings_middle3_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_middle3_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle3_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle3_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Middle3_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_L_ctrl'), control_settings_middle3_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_middle4_l_ctrl = unreal.RigControlSettings()
control_settings_middle4_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_middle4_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_middle4_l_ctrl.display_name = 'None'
control_settings_middle4_l_ctrl.draw_limits = True
control_settings_middle4_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_middle4_l_ctrl.shape_name = 'Default'
control_settings_middle4_l_ctrl.shape_visible = True
control_settings_middle4_l_ctrl.is_transient_control = False
control_settings_middle4_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_middle4_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle4_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle4_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Middle4_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_L_ctrl'), control_settings_middle4_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_middle4_l_end_ctrl = unreal.RigControlSettings()
control_settings_middle4_l_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_middle4_l_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_middle4_l_end_ctrl.display_name = 'None'
control_settings_middle4_l_end_ctrl.draw_limits = True
control_settings_middle4_l_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_middle4_l_end_ctrl.shape_name = 'Default'
control_settings_middle4_l_end_ctrl.shape_visible = True
control_settings_middle4_l_end_ctrl.is_transient_control = False
control_settings_middle4_l_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_middle4_l_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle4_l_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle4_l_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Middle4_L_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_L_ctrl'), control_settings_middle4_l_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_ring1_l_ctrl = unreal.RigControlSettings()
control_settings_ring1_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_ring1_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_ring1_l_ctrl.display_name = 'None'
control_settings_ring1_l_ctrl.draw_limits = True
control_settings_ring1_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_ring1_l_ctrl.shape_name = 'Default'
control_settings_ring1_l_ctrl.shape_visible = True
control_settings_ring1_l_ctrl.is_transient_control = False
control_settings_ring1_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_ring1_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring1_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring1_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Ring1_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_L_ctrl'), control_settings_ring1_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_ring2_l_ctrl = unreal.RigControlSettings()
control_settings_ring2_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_ring2_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_ring2_l_ctrl.display_name = 'None'
control_settings_ring2_l_ctrl.draw_limits = True
control_settings_ring2_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_ring2_l_ctrl.shape_name = 'Default'
control_settings_ring2_l_ctrl.shape_visible = True
control_settings_ring2_l_ctrl.is_transient_control = False
control_settings_ring2_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_ring2_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring2_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring2_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Ring2_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_L_ctrl'), control_settings_ring2_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_ring3_l_ctrl = unreal.RigControlSettings()
control_settings_ring3_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_ring3_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_ring3_l_ctrl.display_name = 'None'
control_settings_ring3_l_ctrl.draw_limits = True
control_settings_ring3_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_ring3_l_ctrl.shape_name = 'Default'
control_settings_ring3_l_ctrl.shape_visible = True
control_settings_ring3_l_ctrl.is_transient_control = False
control_settings_ring3_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_ring3_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring3_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring3_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Ring3_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_L_ctrl'), control_settings_ring3_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_ring4_l_ctrl = unreal.RigControlSettings()
control_settings_ring4_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_ring4_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_ring4_l_ctrl.display_name = 'None'
control_settings_ring4_l_ctrl.draw_limits = True
control_settings_ring4_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_ring4_l_ctrl.shape_name = 'Default'
control_settings_ring4_l_ctrl.shape_visible = True
control_settings_ring4_l_ctrl.is_transient_control = False
control_settings_ring4_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_ring4_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring4_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring4_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Ring4_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_L_ctrl'), control_settings_ring4_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_ring4_l_end_ctrl = unreal.RigControlSettings()
control_settings_ring4_l_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_ring4_l_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_ring4_l_end_ctrl.display_name = 'None'
control_settings_ring4_l_end_ctrl.draw_limits = True
control_settings_ring4_l_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_ring4_l_end_ctrl.shape_name = 'Default'
control_settings_ring4_l_end_ctrl.shape_visible = True
control_settings_ring4_l_end_ctrl.is_transient_control = False
control_settings_ring4_l_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_ring4_l_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring4_l_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring4_l_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Ring4_L_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_L_ctrl'), control_settings_ring4_l_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pinky1_l_ctrl = unreal.RigControlSettings()
control_settings_pinky1_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pinky1_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pinky1_l_ctrl.display_name = 'None'
control_settings_pinky1_l_ctrl.draw_limits = True
control_settings_pinky1_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pinky1_l_ctrl.shape_name = 'Default'
control_settings_pinky1_l_ctrl.shape_visible = True
control_settings_pinky1_l_ctrl.is_transient_control = False
control_settings_pinky1_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pinky1_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky1_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky1_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Pinky1_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_L_ctrl'), control_settings_pinky1_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pinky2_l_ctrl = unreal.RigControlSettings()
control_settings_pinky2_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pinky2_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pinky2_l_ctrl.display_name = 'None'
control_settings_pinky2_l_ctrl.draw_limits = True
control_settings_pinky2_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pinky2_l_ctrl.shape_name = 'Default'
control_settings_pinky2_l_ctrl.shape_visible = True
control_settings_pinky2_l_ctrl.is_transient_control = False
control_settings_pinky2_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pinky2_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky2_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky2_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Pinky2_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_L_ctrl'), control_settings_pinky2_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pinky3_l_ctrl = unreal.RigControlSettings()
control_settings_pinky3_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pinky3_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pinky3_l_ctrl.display_name = 'None'
control_settings_pinky3_l_ctrl.draw_limits = True
control_settings_pinky3_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pinky3_l_ctrl.shape_name = 'Default'
control_settings_pinky3_l_ctrl.shape_visible = True
control_settings_pinky3_l_ctrl.is_transient_control = False
control_settings_pinky3_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pinky3_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky3_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky3_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Pinky3_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_L_ctrl'), control_settings_pinky3_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pinky4_l_ctrl = unreal.RigControlSettings()
control_settings_pinky4_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pinky4_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pinky4_l_ctrl.display_name = 'None'
control_settings_pinky4_l_ctrl.draw_limits = True
control_settings_pinky4_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pinky4_l_ctrl.shape_name = 'Default'
control_settings_pinky4_l_ctrl.shape_visible = True
control_settings_pinky4_l_ctrl.is_transient_control = False
control_settings_pinky4_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pinky4_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky4_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky4_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Pinky4_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_L_ctrl'), control_settings_pinky4_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pinky4_l_end_ctrl = unreal.RigControlSettings()
control_settings_pinky4_l_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pinky4_l_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pinky4_l_end_ctrl.display_name = 'None'
control_settings_pinky4_l_end_ctrl.draw_limits = True
control_settings_pinky4_l_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pinky4_l_end_ctrl.shape_name = 'Default'
control_settings_pinky4_l_end_ctrl.shape_visible = True
control_settings_pinky4_l_end_ctrl.is_transient_control = False
control_settings_pinky4_l_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pinky4_l_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky4_l_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky4_l_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Pinky4_L_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_L_ctrl'), control_settings_pinky4_l_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_thumb1_l_ctrl = unreal.RigControlSettings()
control_settings_thumb1_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_thumb1_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_thumb1_l_ctrl.display_name = 'None'
control_settings_thumb1_l_ctrl.draw_limits = True
control_settings_thumb1_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_thumb1_l_ctrl.shape_name = 'Default'
control_settings_thumb1_l_ctrl.shape_visible = True
control_settings_thumb1_l_ctrl.is_transient_control = False
control_settings_thumb1_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_thumb1_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb1_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb1_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Thumb1_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_L_ctrl'), control_settings_thumb1_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_thumb2_l_ctrl = unreal.RigControlSettings()
control_settings_thumb2_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_thumb2_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_thumb2_l_ctrl.display_name = 'None'
control_settings_thumb2_l_ctrl.draw_limits = True
control_settings_thumb2_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_thumb2_l_ctrl.shape_name = 'Default'
control_settings_thumb2_l_ctrl.shape_visible = True
control_settings_thumb2_l_ctrl.is_transient_control = False
control_settings_thumb2_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_thumb2_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb2_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb2_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Thumb2_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_L_ctrl'), control_settings_thumb2_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_thumb3_l_ctrl = unreal.RigControlSettings()
control_settings_thumb3_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_thumb3_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_thumb3_l_ctrl.display_name = 'None'
control_settings_thumb3_l_ctrl.draw_limits = True
control_settings_thumb3_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_thumb3_l_ctrl.shape_name = 'Default'
control_settings_thumb3_l_ctrl.shape_visible = True
control_settings_thumb3_l_ctrl.is_transient_control = False
control_settings_thumb3_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_thumb3_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb3_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb3_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Thumb3_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_L_ctrl'), control_settings_thumb3_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_thumb3_l_end_ctrl = unreal.RigControlSettings()
control_settings_thumb3_l_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_thumb3_l_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_thumb3_l_end_ctrl.display_name = 'None'
control_settings_thumb3_l_end_ctrl.draw_limits = True
control_settings_thumb3_l_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_thumb3_l_end_ctrl.shape_name = 'Default'
control_settings_thumb3_l_end_ctrl.shape_visible = True
control_settings_thumb3_l_end_ctrl.is_transient_control = False
control_settings_thumb3_l_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_thumb3_l_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb3_l_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb3_l_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Thumb3_L_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_L_ctrl'), control_settings_thumb3_l_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_shoulder_r_ctrl = unreal.RigControlSettings()
control_settings_shoulder_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_shoulder_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_shoulder_r_ctrl.display_name = 'None'
control_settings_shoulder_r_ctrl.draw_limits = True
control_settings_shoulder_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_shoulder_r_ctrl.shape_name = 'Default'
control_settings_shoulder_r_ctrl.shape_visible = True
control_settings_shoulder_r_ctrl.is_transient_control = False
control_settings_shoulder_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_shoulder_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_shoulder_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_shoulder_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Shoulder_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Chest_ctrl'), control_settings_shoulder_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_upper_arm_r_ctrl = unreal.RigControlSettings()
control_settings_upper_arm_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_upper_arm_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_upper_arm_r_ctrl.display_name = 'None'
control_settings_upper_arm_r_ctrl.draw_limits = True
control_settings_upper_arm_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_upper_arm_r_ctrl.shape_name = 'Default'
control_settings_upper_arm_r_ctrl.shape_visible = True
control_settings_upper_arm_r_ctrl.is_transient_control = False
control_settings_upper_arm_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_upper_arm_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_upper_arm_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_upper_arm_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('UpperArm_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Shoulder_R_ctrl'), control_settings_upper_arm_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_lower_arm_r_ctrl = unreal.RigControlSettings()
control_settings_lower_arm_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_lower_arm_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_lower_arm_r_ctrl.display_name = 'None'
control_settings_lower_arm_r_ctrl.draw_limits = True
control_settings_lower_arm_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_lower_arm_r_ctrl.shape_name = 'Default'
control_settings_lower_arm_r_ctrl.shape_visible = True
control_settings_lower_arm_r_ctrl.is_transient_control = False
control_settings_lower_arm_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_lower_arm_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_arm_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_arm_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('LowerArm_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperArm_R_ctrl'), control_settings_lower_arm_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_wrist_r_ctrl = unreal.RigControlSettings()
control_settings_wrist_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_wrist_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_wrist_r_ctrl.display_name = 'None'
control_settings_wrist_r_ctrl.draw_limits = True
control_settings_wrist_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_wrist_r_ctrl.shape_name = 'Default'
control_settings_wrist_r_ctrl.shape_visible = True
control_settings_wrist_r_ctrl.is_transient_control = False
control_settings_wrist_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_wrist_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_wrist_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_wrist_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Wrist_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerArm_R_ctrl'), control_settings_wrist_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_index1_r_ctrl = unreal.RigControlSettings()
control_settings_index1_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_index1_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_index1_r_ctrl.display_name = 'None'
control_settings_index1_r_ctrl.draw_limits = True
control_settings_index1_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_index1_r_ctrl.shape_name = 'Default'
control_settings_index1_r_ctrl.shape_visible = True
control_settings_index1_r_ctrl.is_transient_control = False
control_settings_index1_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_index1_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index1_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index1_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Index1_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_R_ctrl'), control_settings_index1_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_index2_r_ctrl = unreal.RigControlSettings()
control_settings_index2_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_index2_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_index2_r_ctrl.display_name = 'None'
control_settings_index2_r_ctrl.draw_limits = True
control_settings_index2_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_index2_r_ctrl.shape_name = 'Default'
control_settings_index2_r_ctrl.shape_visible = True
control_settings_index2_r_ctrl.is_transient_control = False
control_settings_index2_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_index2_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index2_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index2_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Index2_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index1_R_ctrl'), control_settings_index2_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_index3_r_ctrl = unreal.RigControlSettings()
control_settings_index3_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_index3_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_index3_r_ctrl.display_name = 'None'
control_settings_index3_r_ctrl.draw_limits = True
control_settings_index3_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_index3_r_ctrl.shape_name = 'Default'
control_settings_index3_r_ctrl.shape_visible = True
control_settings_index3_r_ctrl.is_transient_control = False
control_settings_index3_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_index3_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index3_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index3_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Index3_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index2_R_ctrl'), control_settings_index3_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_index4_r_ctrl = unreal.RigControlSettings()
control_settings_index4_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_index4_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_index4_r_ctrl.display_name = 'None'
control_settings_index4_r_ctrl.draw_limits = True
control_settings_index4_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_index4_r_ctrl.shape_name = 'Default'
control_settings_index4_r_ctrl.shape_visible = True
control_settings_index4_r_ctrl.is_transient_control = False
control_settings_index4_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_index4_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index4_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index4_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Index4_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index3_R_ctrl'), control_settings_index4_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_index4_r_end_ctrl = unreal.RigControlSettings()
control_settings_index4_r_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_index4_r_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_index4_r_end_ctrl.display_name = 'None'
control_settings_index4_r_end_ctrl.draw_limits = True
control_settings_index4_r_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_index4_r_end_ctrl.shape_name = 'Default'
control_settings_index4_r_end_ctrl.shape_visible = True
control_settings_index4_r_end_ctrl.is_transient_control = False
control_settings_index4_r_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_index4_r_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index4_r_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_index4_r_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Index4_R_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_R_ctrl'), control_settings_index4_r_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Index4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_middle1_r_ctrl = unreal.RigControlSettings()
control_settings_middle1_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_middle1_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_middle1_r_ctrl.display_name = 'None'
control_settings_middle1_r_ctrl.draw_limits = True
control_settings_middle1_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_middle1_r_ctrl.shape_name = 'Default'
control_settings_middle1_r_ctrl.shape_visible = True
control_settings_middle1_r_ctrl.is_transient_control = False
control_settings_middle1_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_middle1_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle1_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle1_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Middle1_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_R_ctrl'), control_settings_middle1_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_middle2_r_ctrl = unreal.RigControlSettings()
control_settings_middle2_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_middle2_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_middle2_r_ctrl.display_name = 'None'
control_settings_middle2_r_ctrl.draw_limits = True
control_settings_middle2_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_middle2_r_ctrl.shape_name = 'Default'
control_settings_middle2_r_ctrl.shape_visible = True
control_settings_middle2_r_ctrl.is_transient_control = False
control_settings_middle2_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_middle2_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle2_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle2_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Middle2_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle1_R_ctrl'), control_settings_middle2_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_middle3_r_ctrl = unreal.RigControlSettings()
control_settings_middle3_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_middle3_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_middle3_r_ctrl.display_name = 'None'
control_settings_middle3_r_ctrl.draw_limits = True
control_settings_middle3_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_middle3_r_ctrl.shape_name = 'Default'
control_settings_middle3_r_ctrl.shape_visible = True
control_settings_middle3_r_ctrl.is_transient_control = False
control_settings_middle3_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_middle3_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle3_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle3_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Middle3_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle2_R_ctrl'), control_settings_middle3_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_middle4_r_ctrl = unreal.RigControlSettings()
control_settings_middle4_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_middle4_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_middle4_r_ctrl.display_name = 'None'
control_settings_middle4_r_ctrl.draw_limits = True
control_settings_middle4_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_middle4_r_ctrl.shape_name = 'Default'
control_settings_middle4_r_ctrl.shape_visible = True
control_settings_middle4_r_ctrl.is_transient_control = False
control_settings_middle4_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_middle4_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle4_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle4_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Middle4_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle3_R_ctrl'), control_settings_middle4_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_middle4_r_end_ctrl = unreal.RigControlSettings()
control_settings_middle4_r_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_middle4_r_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_middle4_r_end_ctrl.display_name = 'None'
control_settings_middle4_r_end_ctrl.draw_limits = True
control_settings_middle4_r_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_middle4_r_end_ctrl.shape_name = 'Default'
control_settings_middle4_r_end_ctrl.shape_visible = True
control_settings_middle4_r_end_ctrl.is_transient_control = False
control_settings_middle4_r_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_middle4_r_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle4_r_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_middle4_r_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Middle4_R_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_R_ctrl'), control_settings_middle4_r_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Middle4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_ring1_r_ctrl = unreal.RigControlSettings()
control_settings_ring1_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_ring1_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_ring1_r_ctrl.display_name = 'None'
control_settings_ring1_r_ctrl.draw_limits = True
control_settings_ring1_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_ring1_r_ctrl.shape_name = 'Default'
control_settings_ring1_r_ctrl.shape_visible = True
control_settings_ring1_r_ctrl.is_transient_control = False
control_settings_ring1_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_ring1_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring1_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring1_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Ring1_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_R_ctrl'), control_settings_ring1_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_ring2_r_ctrl = unreal.RigControlSettings()
control_settings_ring2_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_ring2_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_ring2_r_ctrl.display_name = 'None'
control_settings_ring2_r_ctrl.draw_limits = True
control_settings_ring2_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_ring2_r_ctrl.shape_name = 'Default'
control_settings_ring2_r_ctrl.shape_visible = True
control_settings_ring2_r_ctrl.is_transient_control = False
control_settings_ring2_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_ring2_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring2_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring2_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Ring2_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring1_R_ctrl'), control_settings_ring2_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_ring3_r_ctrl = unreal.RigControlSettings()
control_settings_ring3_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_ring3_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_ring3_r_ctrl.display_name = 'None'
control_settings_ring3_r_ctrl.draw_limits = True
control_settings_ring3_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_ring3_r_ctrl.shape_name = 'Default'
control_settings_ring3_r_ctrl.shape_visible = True
control_settings_ring3_r_ctrl.is_transient_control = False
control_settings_ring3_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_ring3_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring3_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring3_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Ring3_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring2_R_ctrl'), control_settings_ring3_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_ring4_r_ctrl = unreal.RigControlSettings()
control_settings_ring4_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_ring4_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_ring4_r_ctrl.display_name = 'None'
control_settings_ring4_r_ctrl.draw_limits = True
control_settings_ring4_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_ring4_r_ctrl.shape_name = 'Default'
control_settings_ring4_r_ctrl.shape_visible = True
control_settings_ring4_r_ctrl.is_transient_control = False
control_settings_ring4_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_ring4_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring4_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring4_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Ring4_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring3_R_ctrl'), control_settings_ring4_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_ring4_r_end_ctrl = unreal.RigControlSettings()
control_settings_ring4_r_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_ring4_r_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_ring4_r_end_ctrl.display_name = 'None'
control_settings_ring4_r_end_ctrl.draw_limits = True
control_settings_ring4_r_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_ring4_r_end_ctrl.shape_name = 'Default'
control_settings_ring4_r_end_ctrl.shape_visible = True
control_settings_ring4_r_end_ctrl.is_transient_control = False
control_settings_ring4_r_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_ring4_r_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring4_r_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_ring4_r_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Ring4_R_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_R_ctrl'), control_settings_ring4_r_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Ring4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pinky1_r_ctrl = unreal.RigControlSettings()
control_settings_pinky1_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pinky1_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pinky1_r_ctrl.display_name = 'None'
control_settings_pinky1_r_ctrl.draw_limits = True
control_settings_pinky1_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pinky1_r_ctrl.shape_name = 'Default'
control_settings_pinky1_r_ctrl.shape_visible = True
control_settings_pinky1_r_ctrl.is_transient_control = False
control_settings_pinky1_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pinky1_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky1_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky1_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Pinky1_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_R_ctrl'), control_settings_pinky1_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pinky2_r_ctrl = unreal.RigControlSettings()
control_settings_pinky2_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pinky2_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pinky2_r_ctrl.display_name = 'None'
control_settings_pinky2_r_ctrl.draw_limits = True
control_settings_pinky2_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pinky2_r_ctrl.shape_name = 'Default'
control_settings_pinky2_r_ctrl.shape_visible = True
control_settings_pinky2_r_ctrl.is_transient_control = False
control_settings_pinky2_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pinky2_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky2_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky2_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Pinky2_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky1_R_ctrl'), control_settings_pinky2_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pinky3_r_ctrl = unreal.RigControlSettings()
control_settings_pinky3_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pinky3_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pinky3_r_ctrl.display_name = 'None'
control_settings_pinky3_r_ctrl.draw_limits = True
control_settings_pinky3_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pinky3_r_ctrl.shape_name = 'Default'
control_settings_pinky3_r_ctrl.shape_visible = True
control_settings_pinky3_r_ctrl.is_transient_control = False
control_settings_pinky3_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pinky3_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky3_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky3_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Pinky3_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky2_R_ctrl'), control_settings_pinky3_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pinky4_r_ctrl = unreal.RigControlSettings()
control_settings_pinky4_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pinky4_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pinky4_r_ctrl.display_name = 'None'
control_settings_pinky4_r_ctrl.draw_limits = True
control_settings_pinky4_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pinky4_r_ctrl.shape_name = 'Default'
control_settings_pinky4_r_ctrl.shape_visible = True
control_settings_pinky4_r_ctrl.is_transient_control = False
control_settings_pinky4_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pinky4_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky4_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky4_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Pinky4_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky3_R_ctrl'), control_settings_pinky4_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pinky4_r_end_ctrl = unreal.RigControlSettings()
control_settings_pinky4_r_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pinky4_r_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pinky4_r_end_ctrl.display_name = 'None'
control_settings_pinky4_r_end_ctrl.draw_limits = True
control_settings_pinky4_r_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pinky4_r_end_ctrl.shape_name = 'Default'
control_settings_pinky4_r_end_ctrl.shape_visible = True
control_settings_pinky4_r_end_ctrl.is_transient_control = False
control_settings_pinky4_r_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pinky4_r_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky4_r_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pinky4_r_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Pinky4_R_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_R_ctrl'), control_settings_pinky4_r_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Pinky4_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_thumb1_r_ctrl = unreal.RigControlSettings()
control_settings_thumb1_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_thumb1_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_thumb1_r_ctrl.display_name = 'None'
control_settings_thumb1_r_ctrl.draw_limits = True
control_settings_thumb1_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_thumb1_r_ctrl.shape_name = 'Default'
control_settings_thumb1_r_ctrl.shape_visible = True
control_settings_thumb1_r_ctrl.is_transient_control = False
control_settings_thumb1_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_thumb1_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb1_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb1_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Thumb1_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Wrist_R_ctrl'), control_settings_thumb1_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_thumb2_r_ctrl = unreal.RigControlSettings()
control_settings_thumb2_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_thumb2_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_thumb2_r_ctrl.display_name = 'None'
control_settings_thumb2_r_ctrl.draw_limits = True
control_settings_thumb2_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_thumb2_r_ctrl.shape_name = 'Default'
control_settings_thumb2_r_ctrl.shape_visible = True
control_settings_thumb2_r_ctrl.is_transient_control = False
control_settings_thumb2_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_thumb2_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb2_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb2_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Thumb2_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb1_R_ctrl'), control_settings_thumb2_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_thumb3_r_ctrl = unreal.RigControlSettings()
control_settings_thumb3_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_thumb3_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_thumb3_r_ctrl.display_name = 'None'
control_settings_thumb3_r_ctrl.draw_limits = True
control_settings_thumb3_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_thumb3_r_ctrl.shape_name = 'Default'
control_settings_thumb3_r_ctrl.shape_visible = True
control_settings_thumb3_r_ctrl.is_transient_control = False
control_settings_thumb3_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_thumb3_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb3_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb3_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Thumb3_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb2_R_ctrl'), control_settings_thumb3_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_thumb3_r_end_ctrl = unreal.RigControlSettings()
control_settings_thumb3_r_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_thumb3_r_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_thumb3_r_end_ctrl.display_name = 'None'
control_settings_thumb3_r_end_ctrl.draw_limits = True
control_settings_thumb3_r_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_thumb3_r_end_ctrl.shape_name = 'Default'
control_settings_thumb3_r_end_ctrl.shape_visible = True
control_settings_thumb3_r_end_ctrl.is_transient_control = False
control_settings_thumb3_r_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_thumb3_r_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb3_r_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_thumb3_r_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Thumb3_R_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_R_ctrl'), control_settings_thumb3_r_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Thumb3_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_upper_leg_l_ctrl = unreal.RigControlSettings()
control_settings_upper_leg_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_upper_leg_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_upper_leg_l_ctrl.display_name = 'None'
control_settings_upper_leg_l_ctrl.draw_limits = True
control_settings_upper_leg_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_upper_leg_l_ctrl.shape_name = 'Default'
control_settings_upper_leg_l_ctrl.shape_visible = True
control_settings_upper_leg_l_ctrl.is_transient_control = False
control_settings_upper_leg_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_upper_leg_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_upper_leg_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_upper_leg_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('UpperLeg_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Body_ctrl'), control_settings_upper_leg_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_lower_leg_l_ctrl = unreal.RigControlSettings()
control_settings_lower_leg_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_lower_leg_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_lower_leg_l_ctrl.display_name = 'None'
control_settings_lower_leg_l_ctrl.draw_limits = True
control_settings_lower_leg_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_lower_leg_l_ctrl.shape_name = 'Default'
control_settings_lower_leg_l_ctrl.shape_visible = True
control_settings_lower_leg_l_ctrl.is_transient_control = False
control_settings_lower_leg_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_lower_leg_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_leg_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_leg_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('LowerLeg_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_L_ctrl'), control_settings_lower_leg_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_lower_leg_l_end_ctrl = unreal.RigControlSettings()
control_settings_lower_leg_l_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_lower_leg_l_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_lower_leg_l_end_ctrl.display_name = 'None'
control_settings_lower_leg_l_end_ctrl.draw_limits = True
control_settings_lower_leg_l_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_lower_leg_l_end_ctrl.shape_name = 'Default'
control_settings_lower_leg_l_end_ctrl.shape_visible = True
control_settings_lower_leg_l_end_ctrl.is_transient_control = False
control_settings_lower_leg_l_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_lower_leg_l_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_leg_l_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_leg_l_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('LowerLeg_L_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_L_ctrl'), control_settings_lower_leg_l_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_upper_leg_r_ctrl = unreal.RigControlSettings()
control_settings_upper_leg_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_upper_leg_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_upper_leg_r_ctrl.display_name = 'None'
control_settings_upper_leg_r_ctrl.draw_limits = True
control_settings_upper_leg_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_upper_leg_r_ctrl.shape_name = 'Default'
control_settings_upper_leg_r_ctrl.shape_visible = True
control_settings_upper_leg_r_ctrl.is_transient_control = False
control_settings_upper_leg_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_upper_leg_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_upper_leg_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_upper_leg_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('UpperLeg_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Body_ctrl'), control_settings_upper_leg_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_lower_leg_r_ctrl = unreal.RigControlSettings()
control_settings_lower_leg_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_lower_leg_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_lower_leg_r_ctrl.display_name = 'None'
control_settings_lower_leg_r_ctrl.draw_limits = True
control_settings_lower_leg_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_lower_leg_r_ctrl.shape_name = 'Default'
control_settings_lower_leg_r_ctrl.shape_visible = True
control_settings_lower_leg_r_ctrl.is_transient_control = False
control_settings_lower_leg_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_lower_leg_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_leg_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_leg_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('LowerLeg_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='UpperLeg_R_ctrl'), control_settings_lower_leg_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_lower_leg_r_end_ctrl = unreal.RigControlSettings()
control_settings_lower_leg_r_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_lower_leg_r_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_lower_leg_r_end_ctrl.display_name = 'None'
control_settings_lower_leg_r_end_ctrl.draw_limits = True
control_settings_lower_leg_r_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_lower_leg_r_end_ctrl.shape_name = 'Default'
control_settings_lower_leg_r_end_ctrl.shape_visible = True
control_settings_lower_leg_r_end_ctrl.is_transient_control = False
control_settings_lower_leg_r_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_lower_leg_r_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_leg_r_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_lower_leg_r_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('LowerLeg_R_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_R_ctrl'), control_settings_lower_leg_r_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='LowerLeg_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_foot_l_ctrl = unreal.RigControlSettings()
control_settings_foot_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_foot_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_foot_l_ctrl.display_name = 'None'
control_settings_foot_l_ctrl.draw_limits = True
control_settings_foot_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_foot_l_ctrl.shape_name = 'Default'
control_settings_foot_l_ctrl.shape_visible = True
control_settings_foot_l_ctrl.is_transient_control = False
control_settings_foot_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_foot_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_foot_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_foot_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Foot_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Root_ctrl'), control_settings_foot_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_foot_l_end_ctrl = unreal.RigControlSettings()
control_settings_foot_l_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_foot_l_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_foot_l_end_ctrl.display_name = 'None'
control_settings_foot_l_end_ctrl.draw_limits = True
control_settings_foot_l_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_foot_l_end_ctrl.shape_name = 'Default'
control_settings_foot_l_end_ctrl.shape_visible = True
control_settings_foot_l_end_ctrl.is_transient_control = False
control_settings_foot_l_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_foot_l_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_foot_l_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_foot_l_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Foot_L_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_L_ctrl'), control_settings_foot_l_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pt_l_ctrl = unreal.RigControlSettings()
control_settings_pt_l_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pt_l_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pt_l_ctrl.display_name = 'None'
control_settings_pt_l_ctrl.draw_limits = True
control_settings_pt_l_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pt_l_ctrl.shape_name = 'Default'
control_settings_pt_l_ctrl.shape_visible = True
control_settings_pt_l_ctrl.is_transient_control = False
control_settings_pt_l_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pt_l_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pt_l_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pt_l_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('PT_L_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Root_ctrl'), control_settings_pt_l_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_L_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_L_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pt_l_end_ctrl = unreal.RigControlSettings()
control_settings_pt_l_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pt_l_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pt_l_end_ctrl.display_name = 'None'
control_settings_pt_l_end_ctrl.draw_limits = True
control_settings_pt_l_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pt_l_end_ctrl.shape_name = 'Default'
control_settings_pt_l_end_ctrl.shape_visible = True
control_settings_pt_l_end_ctrl.is_transient_control = False
control_settings_pt_l_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pt_l_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pt_l_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pt_l_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('PT_L_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_L_ctrl'), control_settings_pt_l_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_L_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_L_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_foot_r_ctrl = unreal.RigControlSettings()
control_settings_foot_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_foot_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_foot_r_ctrl.display_name = 'None'
control_settings_foot_r_ctrl.draw_limits = True
control_settings_foot_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_foot_r_ctrl.shape_name = 'Default'
control_settings_foot_r_ctrl.shape_visible = True
control_settings_foot_r_ctrl.is_transient_control = False
control_settings_foot_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_foot_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_foot_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_foot_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Foot_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Root_ctrl'), control_settings_foot_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_foot_r_end_ctrl = unreal.RigControlSettings()
control_settings_foot_r_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_foot_r_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_foot_r_end_ctrl.display_name = 'None'
control_settings_foot_r_end_ctrl.draw_limits = True
control_settings_foot_r_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_foot_r_end_ctrl.shape_name = 'Default'
control_settings_foot_r_end_ctrl.shape_visible = True
control_settings_foot_r_end_ctrl.is_transient_control = False
control_settings_foot_r_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_foot_r_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_foot_r_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_foot_r_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('Foot_R_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_R_ctrl'), control_settings_foot_r_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Foot_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pt_r_ctrl = unreal.RigControlSettings()
control_settings_pt_r_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pt_r_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pt_r_ctrl.display_name = 'None'
control_settings_pt_r_ctrl.draw_limits = True
control_settings_pt_r_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pt_r_ctrl.shape_name = 'Default'
control_settings_pt_r_ctrl.shape_visible = True
control_settings_pt_r_ctrl.is_transient_control = False
control_settings_pt_r_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pt_r_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pt_r_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pt_r_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('PT_R_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='Root_ctrl'), control_settings_pt_r_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_R_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_R_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])), unreal.RigControlValueType.CURRENT)
control_settings_pt_r_end_ctrl = unreal.RigControlSettings()
control_settings_pt_r_end_ctrl.animation_type = unreal.RigControlAnimationType.ANIMATION_CONTROL
control_settings_pt_r_end_ctrl.control_type = unreal.RigControlType.EULER_TRANSFORM
control_settings_pt_r_end_ctrl.display_name = 'None'
control_settings_pt_r_end_ctrl.draw_limits = True
control_settings_pt_r_end_ctrl.shape_color = unreal.LinearColor(1.000000, 0.000000, 0.000000, 1.000000)
control_settings_pt_r_end_ctrl.shape_name = 'Default'
control_settings_pt_r_end_ctrl.shape_visible = True
control_settings_pt_r_end_ctrl.is_transient_control = False
control_settings_pt_r_end_ctrl.limit_enabled = [unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False), unreal.RigControlLimitEnabled(False, False)]
control_settings_pt_r_end_ctrl.minimum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pt_r_end_ctrl.maximum_value = unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000]))
control_settings_pt_r_end_ctrl.primary_axis = unreal.RigControlAxis.X
hierarchy_controller.add_control('PT_R_end_ctrl', unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_R_ctrl'), control_settings_pt_r_end_ctrl, unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[1.000000,1.000000,1.000000])))
hierarchy.set_control_shape_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MINIMUM)
hierarchy.set_control_value(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_R_end_ctrl'), unreal.RigHierarchy.make_control_value_from_euler_transform(unreal.EulerTransform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,0.000000],scale=[0.000000,0.000000,0.000000])), unreal.RigControlValueType.MAXIMUM)
hierarchy.set_control_offset_transform(unreal.RigElementKey(type=unreal.RigElementType.CONTROL, name='PT_R_end_ctrl'), unreal.Transform(location=[0.000000,0.000000,0.000000],rotation=[0.000000,0.000000,-0.000000],scale=[1.000000,1.000000,1.000000]), True, True)