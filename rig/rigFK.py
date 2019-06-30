import pymel.core as pm
from RMPY.rig import baseRig


class RigFKModel(baseRig.BaseModel):
    def __init__(self):
        super(RigFKModel, self).__init__()


class RigFK(baseRig.BaseRig):
    def __init__(self, *args, **kwargs):
        super(RigFK, self).__init__(*args, **kwargs)

    def create_point_base(self, *args, **kwargs):
        reset_joints, joint_list = self.create.joints.point_base(*args, **kwargs)
        self.reset_joints.append(reset_joints)
        self.reset_joints.setParent(self.rig_system.joints)
        self.joints.append(joint_list)

        for index, eachJoint in enumerate(joint_list[:-1]):
            reset_group, control = self.create.control.point_base(eachJoint, **kwargs)
            self.reset_controls.append(reset_group)
            self.controls.append(control)
            if index == 0:
                reset_group.setParent = self.rig_system.controls
            else:
                pm.parent(reset_group, self.controls[index-1])

            pm.parentConstraint(control, eachJoint, mo=False)
            pm.scaleConstraint(control, eachJoint, mo=False)

