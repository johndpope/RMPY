from RMPY.rig import rigBase
import pymel.core as pm


class RigBaseSwitchModel(rigBase.BaseModel):
    def __init__(self):
        super(RigBaseSwitchModel, self).__init__()
        self.control = None
        self.reverse = None
        self.attribute_output = None
        self.attribute_output_false = None


class RigBaseSwitch(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        super(RigBaseSwitch, self).__init__(*args, **kwargs)
        self._model = RigBaseSwitchModel()
        self.control = None
        self.reverse = None
        self.attribute_output = None
        self.attribute_output_false = None
        self.attribute_name = 'switch'

    def initialize(self, *args, **kwargs):
        self.control = kwargs.pop('control', None)
        if self.control:
            self.control = self.rm.as_pymel_nodes(self.control)
        self.attribute_name = kwargs.pop('attribute_name', 'switch')
        self.reverse = pm.shadingNode('reverse', asUtility=True)
        self.name_convention.rename_name_in_format(self.reverse, name="reverse")
        self.attribute_output_false = self.reverse.outputX

    @property
    def control(self):
        return self._model.control

    @control.setter
    def control(self, value):
        self._model.control = value

    @property
    def attribute_output(self):
        return self._model.attribute_output

    @attribute_output.setter
    def attribute_output(self, value):
        self._model.attribute_output = value

    @property
    def attribute_output_false(self):
        return self._model.attribute_output_false

    @attribute_output_false.setter
    def attribute_output_false(self, value):
        self._model.attribute_output_false = value

    @property
    def reverse(self):
        return self._model.reverse

    @reverse.setter
    def reverse(self, value):
        self._model.reverse = value

    def set_control(self, **kwargs):
        self.control = kwargs.pop('control', self.control)
        self.attribute_name = kwargs.pop('attribute_name', self.attribute_name)

    def set_outputs(self):
        pass


if __name__ == '__main__':
    RigBaseSwitch()