.. image:: https://travis-ci.org/vmware/pyvmomi.svg?branch=v5.5.0_2014.1
    :target: https://travis-ci.org/vmware/pyvmomi
    :alt: Build Status

.. image:: https://pypip.in/download/pyvmomi/badge.png
    :target: https://pypi.python.org/pypi/pyvmomi/
    :alt: Downloads

pyVmomi is the Python SDK for the VMware vSphere API that allows you to manage 
ESX, ESXi, and vCenter.

Getting Started
================
To get started, check out the samples project at:

*  http://vmware.github.io/pyvmomi-community-samples/

* community discussion on IRC freenode.net channels `#pyvmomi and #pyvmomi-dev <http://webchat.freenode.net/?channels=#pyvmomi,#pyvmomi-dev>`_

* community email is on `nabble <http://pyvmomi.2338814.n4.nabble.com>`_

Installing
==========
The master is code that is in development, official releases are tagged and 
posted to `pypi <https://pypi.python.org/pypi/pyvmomi/>`_

* The official release is available using pip, just run 
  ``pip install --upgrade pyvmomi``. 
* To install the version in `github <https://github.com/vmware/pyvmomi>`_ use 
  ``python setup.py develop`` for development install or 
  ``python setup.py install``. 

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
* Coordinate with `other developers <http://webchat.freenode.net/?channels=#pyvmomi,#pyvmomi-dev>`_ on the project.

Documentation
=============
For general language neutral documentation of vSphere Management API see: 

* `vSphere WS SDK API Docs <http://pubs.vmware.com/vsphere-55/topic/com.vmware.wssdk.apiref.doc/right-pane.html>`_

Python Support
==============
* pyVmomi 5.5.0-2014.1 and later support Python 2.6, 2.7, 3.3 and 3.4
* pyVmomi 5.5.0 and below support Python 2.6 and 2.7

Compatibility Policy
====================
pyVmomi versions are marked vSphere_version-release . Pyvmomi maintains minimum 
backward compatibility with the previous _four_ releases of *vSphere* and it's 
own previous four releases. Compatibility with much older versions may continue 
to work but will not be actively supported.

For example, version v5.5.0-2014.1 is most compatible with vSphere 5.5, 5.1, 
5.0, and 4.1 and was the first release in 2014. Initial releases compatible with
a version of vSphere will bare a naked version number of v5.5.0 indicating that 
version of pyVmomi was released simultaneously with the *GA* version of vSphere 
with the same version number.

Releases
========
* `5.5.0-2014.1.1 <https://github.com/vmware/pyvmomi/tree/v5.5.0-2014.1.1>`_
   release notes https://github.com/vmware/pyvmomi/releases/tag/v5.5.0-2014.1.1 
* `5.5.0-2014.1 <https://github.com/vmware/pyvmomi/tree/v5.5.0-2014.1>`_
   release notes https://github.com/vmware/pyvmomi/releases/tag/v5.5.0-2014.1
* `5.5.0 <https://github.com/vmware/pyvmomi/tree/v5.5.0>`_
* `5.1.0 <https://github.com/vmware/pyvmomi/tree/v5.1.0>`_ 
   release notes https://github.com/vmware/pyvmomi/releases/tag/v5.1.0

Related Projects
================
* Feature Incubator: pyvmomi-tools https://github.com/vmware/pyvmomi-tools
* Samples Project: https://github.com/vmware/pyvmomi-community-samples

Have fun!
