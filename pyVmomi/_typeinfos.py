# **********************************************************
# Copyright (c) 2005-2022 VMware, Inc.
# **********************************************************

import sys

typeinfos = [
    'core',
    'eam',
    'pbm',
    'query',
    'sms',
    'vim',
]

# Deprecated
# VmomiJSONEncoder was originally part of VmomiSupport and not a separate module.
# This insertion into VmomiSupport is for backwards compatibility.
from .VmomiJSONEncoder import VmomiJSONEncoder
from .VmomiJSONEncoder import templateOf
VmomiSupport = sys.modules['pyVmomi.VmomiSupport']
setattr(VmomiSupport, 'VmomiJSONEncoder', VmomiJSONEncoder)
setattr(VmomiSupport, 'templateOf', templateOf)
