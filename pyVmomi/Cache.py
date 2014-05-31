# VMware vSphere Python SDK
# Copyright (c) 2008-2013 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module implements the cache decorator
"""
__author__ = "VMware, Inc."


def cache(function):
    """Function cache Decorator"""

    def function_cache(*args, **kwargs):
        """cache function"""
        key = (args and tuple(args) or None,
               kwargs and frozenset(kwargs.items()) or None)
        if key not in function.__cached__:
            function.__cached__[key] = mycache = function(*args, **kwargs)
        else:
            mycache = function.__cached__[key]
        return mycache

    def reset_cache():
        """Reset the cache"""
        function.__cached__ = {}

    setattr(function, "__cached__", {})
    setattr(function, "__resetcache__", reset_cache)
    function_cache.__name__ = function.__name__
    function_cache.__doc__ = function.__doc__
    function_cache.__dict__.update(function.__dict__)
    return function_cache
