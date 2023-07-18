from pyVmomi import vim, vmodl, vslm


class SyncFault(VslmFault):
    @property
    def id(self) -> vim.vslm.ID: ...
    @id.setter
    def id(self, value: vim.vslm.ID):
        self._id = value


class VslmFault(vmodl.MethodFault):
    @property
    def msg(self) -> str: ...
    @msg.setter
    def msg(self, value: str):
        self._msg = value