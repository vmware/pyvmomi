"""
Copyright (c) 2021-2022 VMware, Inc.

This module handles pyVmomi features states
"""
from collections import namedtuple
from . import _assert_not_initialized

# pyVmomi features along with their default states.
# e.g., 'newFeature': False
_features = {
}

Features = namedtuple('Features', _features.keys())
flags = Features(**_features)


def _init():
    global flags
    flags = Features(**_features)


def get_feature_names():
    return _features.keys()


def set_feature_state(feature_name, state):
    _assert_not_initialized()
    if feature_name not in _features:
        raise AttributeError("Feature '{0}' is not supported!".format(feature_name))
    if not isinstance(feature_name, str):
        raise TypeError("Feature name should be string!")
    if not isinstance(state, bool):
        raise TypeError("Feature state should be boolean!")

    _features[feature_name] = state
