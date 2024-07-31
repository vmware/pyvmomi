# Copyright (c) 2022-2024 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# Client security module.

import hashlib
import ssl

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


"""
Verify that a thumbprint matches a certificate

:param derCert: DER-encoded SSL certificate
:type derCert: str
:param thumbprint: SHA1/SHA256/SHA512 thumbprint
                   of an SSL certificate
:type thumbprint: str
:returns: None
:raises ThumbprintMismatchException
"""
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


"""
Verify that two PEM certificates match

:param actualCert: PEM-encoded SSL certificate
:type actualCert: str
:param expectedCert: PEM-encoded SSL certificate
:type actualCert: str
:returns: None
:raises CertificateMismatchException
"""
def VerifyCert(actualCert, expectedCert):
    actualCert = actualCert.strip()
    expectedCert = expectedCert.strip()
    if actualCert != expectedCert:
        raise CertificateMismatchException(expectedCert, actualCert)


class CertificateMismatchException(Exception):
    def __init__(self, expected, actual):
        Exception.__init__(self, "Certificate mismatch. Expected: \n{0}, "
                                 "actual: \n{1}".format(expected, actual))

        self.expected = expected
        self.actual = actual
