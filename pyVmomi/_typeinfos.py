# **********************************************************
# Copyright (c) 2005-2023 VMware, Inc.
# **********************************************************

import sys


def load_typeinfos():
    try:
        from . import _typeinfo_core
    except ImportError:
        pass

    try:
        from . import _typeinfo_eam
    except ImportError:
        pass

    try:
        from . import _typeinfo_pbm
    except ImportError:
        pass

    try:
        from . import _typeinfo_query
    except ImportError:
        pass

    try:
        from . import _typeinfo_sms
    except ImportError:
        pass

    try:
        from . import _typeinfo_vim
    except ImportError:
        pass

    try:
        from . import _typeinfo_vslm
    except ImportError:
        pass


# VmomiJSONEncoder was originally part of VmomiSupport and not a separate module.
# This insertion into VmomiSupport is for backwards compatibility.
from .VmomiJSONEncoder import VmomiJSONEncoder
from .VmomiJSONEncoder import templateOf
VmomiSupport = sys.modules['pyVmomi.VmomiSupport']
setattr(VmomiSupport, 'VmomiJSONEncoder', VmomiJSONEncoder)
setattr(VmomiSupport, 'templateOf', templateOf)
