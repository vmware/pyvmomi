pyvmomi
------------
.. |downloads| image:: https://img.shields.io/pypi/dm/pyvmomi.svg
    :target: https://pypi.python.org/pypi/pyvmomi/
.. |py-version| image:: https://img.shields.io/pypi/pyversions/pyVmomi

|downloads| |py-version|

pyVmomi is the Python SDK for the VMware vSphere Management API that allows you to rapidly build solutions integrated with VMware ESXi and vCenter Server.
For accessing features from the `vSphere Automation APIs <https://developer.vmware.com/apis/vsphere-automation/latest/>`_
(REST), please refer to the `VMware vSphere Automation SDK for Python <https://github.com/vmware/vsphere-automation-sdk-python/>`_.

.. contents:: Table of Contents
   :depth: 1
   :local:
   :backlinks: none

Getting Started
================
To get started, see the
`getting started guide <http://vmware.github.io/pyvmomi-community-samples/#getting-started>`_.
You'll need `Python <https://www.python.org/downloads/>`_,
`pip <https://pip.pypa.io/en/latest/installation/>`_, and the
`samples project <http://vmware.github.io/pyvmomi-community-samples/>`_.

Installing
==========
The master is code that is in development, official releases are tagged and
posted to `pypi <https://pypi.python.org/pypi/pyvmomi/>`_

* The official release is available using pip, just run
  ``pip install --upgrade pyvmomi``.
* To install the version in `github <https://github.com/vmware/pyvmomi>`_ use
  ``python setup.py develop`` for development install or
  ``python setup.py install``.
* To install `github's version <https://github.com/vmware/pyvmomi>`_ with sso support, just run
  ``pip install -e ".[sso]"`` inside project's home folder.

Testing
=======
Unit tests can be invoked by using the `tox <https://testrun.org/tox/>`_ command. You may have to
configure multiple python interpreters so that you can test in all the
environments listed in ``tox.ini`` or you will have to run ``tox`` with the
``-e`` flag to run only in your version of python. For example, if you only
have Python 2.7 then ``tox -e py27`` will limit your test run to Python 2.7.

Contributing
============
* Research `open issues <https://github.com/vmware/pyvmomi/issues?q=is%3Aopen+is%3Aissue>`_
* Follow the `contribution standards <https://github.com/vmware/pyvmomi/wiki/Contributions>`_

Documentation
=============
For general language neutral documentation of vSphere Management API see:

* `Release Notes <https://docs.vmware.com/en/VMware-vSphere/8.0/rn/pyvmomi-sdk-80-release-notes.html>`_
* `vSphere Web Services API Doc <https://developer.broadcom.com/xapis/vsphere-web-services-api/latest/>`_

Python Support
==============
* pyVmomi supports Python 3.4+

Versioning
====================
pyVmomi: **X.Y.Z.U.P**

vCenter-related:
**X.Y** - (Major release), **Z** - (Update release), **U** - (Patch)

pyVmomi-related:
**P** - (pyVmomi patches)

Compatibility Policy
====================
pyVmomi maintains minimum backward compatibility with the previous
*four* releases of *vSphere* and it's own previous four releases.
Compatibility with much older versions may continue to work but will
not be actively supported.

For example, version v6.0.0 is most compatible with vSphere 6.0, 5.5, 5.1 and
5.0. Initial releases compatible with a version of vSphere will bare a naked
version number of v6.0.0 indicating that version of pyVmomi was released
simultaneously with the *GA* version of vSphere with the same version number.

Support
====================
Support details can be referenced under the **SDK and API Support for Commercial and Enterprise Organizations** section at `Broadcom Developer Portal <https://developer.broadcom.com/support>`_.

For community support, please open a `Github issue <https://github.com/vmware/pyvmomi/issues>`_ or start a `Discussion <https://github.com/vmware/pyvmomi/discussions>`_.

Related Projects
================
* VMware vSphere Automation SDK for Python: https://github.com/vmware/vsphere-automation-sdk-python
* Samples Project: https://github.com/vmware/pyvmomi-community-samples

Have fun!
