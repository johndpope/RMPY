import pymel.core as pm
from RMPY.rig import rigIK
from RMPY.rig import rigFK
from RMPY.rig import rigBase
from RMPY.rig import rigSingleJoint
from RMPY.rig import constraintSwitch
import RMPY.core.main as rm


class RigIkFkModel(rigBase.BaseModel):
    def __init__(self):
        super(RigIkFkModel, self).__init__()
        self.ik_rig = None
        self.fk_rig = None
        self.switch_control_rig = None
        self.ik_fk_switch = None


class RigIkFk(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        super(RigIkFk, self).__init__(*args, **kwargs)
        self._model = RigIkFkModel()
        self.root = None
        self.tip = None
        self.joints = []
        self.reset_joints = []

    @property
    def ik_rig(self):
        if self._model.ik_rig is None:
            self._model.ik_rig = rigIK.IKRig(rig_system=self.rig_system)
        return self._model.ik_rig

    @property
    def fk_rig(self):
        if self._model.fk_rig is None:
            self._model.fk_rig = rigFK.RigFK(rig_system=self.rig_system)
        return self._model.fk_rig

    @property
    def switch_control_rig(self):
        if self._model.switch_control_rig is None:
            self._model.switch_control_rig = rigSingleJoint.RigSingleJoint(rig_system=self.rig_system)
        return self._model.switch_control_rig

    @property
    def ik_fk_switch(self):
        if self._model.ik_fk_switch is None:
            self._model.ik_fk_switch = constraintSwitch.ConstraintSwitch(rig_system=self.rig_system)
        return self._model.ik_fk_switch

    def create_point_base(self, *creation_points, **kwargs):
        super(RigIkFk, self).create_point_base(*creation_points, **kwargs)
        self.root = pm.group(empty=True)
        self.root.setParent(self.rig_system.kinematics)

        self.name_convention.rename_name_in_format(self.root, name='mainMover')

        self.ik_rig.create_point_base(*creation_points, control_orientation='world', last_joint_follows_control=False)

        self.fk_rig.create_point_base(*creation_points, orient_type='point_orient')

        self.switch_control_rig.create_point_base(creation_points[-1], name='switch', type='box')

        self.ik_fk_switch.build(self.ik_rig.joints, self.fk_rig.joints, control=self.switch_control_rig.controls[0],
                                attribute_name='IkFkSwitch')

        self.fk_rig.set_parent(self.root)
        self.ik_rig.set_parent(self.root)
        self.tip = self.ik_fk_switch.outputs[-1]

        for each_token in self.ik_rig.controls_dict:
            self.ik_fk_switch.attribute_output_a >> self.ik_rig.controls_dict[each_token].visibility

        for each_control in self.fk_rig.controls:
            self.ik_fk_switch.attribute_output_b >> each_control.visibility
        # pm.parentConst'raint(self.fk_limb.controls[0], self.ik_limb.reset_controls['poleVector'], mo=True)
        # pm.parentConstraint(self.fk_limb.controls[0], self.ik_limb.reset_controls['ikHandleSecondary'], mo=True)
        pm.parentConstraint(self.fk_rig.controls[0], self.ik_rig.root_joints, mo=True)

        self.joints = self.switch_control_rig.joints
        self.reset_joints = self.switch_control_rig.reset_joints



if __name__ == '__main__':
    root_arm = pm.ls('R_leg01_reference_pnt')[0]
    arm_root_points = rm.descendents_list(root_arm)[:3]
    print arm_root_points
    arm_rig = RigIkFk()
    arm_rig.create_point_base(*arm_root_points)



