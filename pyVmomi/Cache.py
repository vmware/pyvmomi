# Copyright (c) 2008-2024 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# Cache decorator implementation

def Cache(fn):
    """ Function cache decorator """
    def fnCache(*args, **kwargs):
        """ Cache function """
        key = (args and tuple(args)
               or None, kwargs and frozenset(list(kwargs.items())) or None)
        if key not in fn.__cached__:
            fn.__cached__[key] = cache = fn(*args, **kwargs)
        else:
            cache = fn.__cached__[key]
        return cache

    def ResetCache():
        """ Reset cache """
        fn.__cached__ = {}

    setattr(fn, "__cached__", {})
    setattr(fn, "__resetcache__", ResetCache)
    fnCache.__name__ = fn.__name__
    fnCache.__doc__ = fn.__doc__
    fnCache.__dict__.update(fn.__dict__)
    return fnCache
