#!/usr/bin/env python
"""
Copyright (c) 2022 VMware, Inc.

This module is the python vmomi client security module.
"""
__author__ = "VMware, Inc"

import hashlib

_isSha1Enabled = True
_isSha256Enabled = True
_isSha512Enabled = True


def SetSha1Enabled(state):
    global _isSha1Enabled
    _isSha1Enabled = state


def SetSha256Enabled(state):
    global _isSha256Enabled
    _isSha256Enabled = state


def SetSha512Enabled(state):
    global _isSha512Enabled
    _isSha512Enabled = state


def VerifyCertThumbprint(derCert, thumbprint):
    thumbprint_len = len(thumbprint)
    if thumbprint_len == 40 and _isSha1Enabled:
        sha = hashlib.sha1()
    elif thumbprint_len == 64 and _isSha256Enabled:
        sha = hashlib.sha256()
    elif thumbprint_len == 128 and _isSha512Enabled:
        sha = hashlib.sha512()
    else:
        raise ThumbprintMismatchException(thumbprint,
                                          '<unsupported algo>')
    sha.update(derCert)
    shaDigest = sha.hexdigest().lower()
    if shaDigest != thumbprint:
        raise ThumbprintMismatchException(thumbprint, shaDigest)


class ThumbprintMismatchException(Exception):
    def __init__(self, expected, actual):
        Exception.__init__(self, "SHA thumbprint mismatch. Expected: `{0}`, "
                                 "actual: `{1}`".format(expected, actual))

        self.expected = expected
        self.actual = actual
