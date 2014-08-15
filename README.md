[![Build Status](https://travis-ci.org/vmware/pyvmomi.svg?branch=master)](https://travis-ci.org/vmware/pyvmomi) 
[![Downloads](https://pypip.in/download/pyvmomi/badge.png)](https://pypi.python.org/pypi/pyvmomi/)

pyVmomi is the Python SDK for the VMware vSphere API that allows you to manage ESX, ESXi, and vCenter.

Getting Started
================
To get started, check out the samples project at http://vmware.github.io/pyvmomi-community-samples/

* community discussion on IRC freenode.net channels [#pyvmomi and #pyvmomi-dev](http://webchat.freenode.net/?channels=#pyvmomi,#pyvmomi-dev)
* community email is on [nabble](http://pyvmomi.2338814.n4.nabble.com)

Installing
==========
The master is code that is in development, official releases are tagged and posted to [pypi](https://pypi.python.org/pypi/pyvmomi/).

* The official release is availabe using pip, just run `pip install pyvmomi`. 
* To install the version in [github](https://github.com/vmware/pyvmomi) use `python setup.py develop` for development install or `python setup.py install`. 

Contributing
============
* Research [open issues](https://github.com/vmware/pyvmomi/issues?q=is%3Aopen+is%3Aissue)
* Follow the [contribution standards](https://github.com/vmware/pyvmomi/wiki/Contributions)
* Coordinate with [other developers](http://webchat.freenode.net/?channels=#pyvmomi,#pyvmomi-dev) on the project.

Other Languages
===============
There are other bindings of this API in other languages. See:

* **vijava** (Java): http://vijava.sourceforge.net/
* **rbvmomi** (Ruby): https://github.com/vmware/rbvmomi
* **vSphere SDK for Perl** (non-free): https://my.vmware.com/group/vmware/details?downloadGroup=VSP510-SDKPERL-510&productId=285

Documentation
=============
For general language neutral documentation of vSphere Management API see:
http://pubs.vmware.com/vsphere-55/index.jsp#com.vmware.wssdk.apiref.doc/right-pane.html

Python Support
==============
* pyVmomi 5.5.0_2014.1 and later support Python 2.6, 2.7, 3.3 and 3.4
* pyVmomi 5.5.0 and below support Python 2.6 and 2.7

Compatibility Policy
====================
pyVmomi versions are marked **vSphere version** _separator_ **release version**. Pyvmomi maintains minimum backward compatibility
with the previous _four_ releases of *vSphere* and it's own previous four releases. Compatibility with much older versions may
continue to work but will not be actively supported.

For example, version **v5.5.0**_2014.1 is most compatible with vSphere 5.5, 5.1, 5.0, and 4.1 and was the first release in
2014. Initial releases compatible with a version of vSphere will bare a naked version number of **v5.5.0** indicating that
version of pyVmomi was released simultaneously with the *GA* version of vSphere with the same version number.

Releases
========
* [5.1.0](https://github.com/vmware/pyvmomi/tree/v5.1.0)
* [5.5.0](https://github.com/vmware/pyvmomi/tree/v5.5.0) [release notes](https://github.com/vmware/pyvmomi/compare/v5.1.0...v5.5.0)
* [5.5.0_2014.1](https://github.com/vmware/pyvmomi/tree/v5.5.0_2014.1) [release notes](https://github.com/vmware/pyvmomi/compare/v5.5.0...5.5.0_2014.1)
* Next release in progress [5.5.0_2014.2](https://github.com/vmware/pyvmomi/issues?milestone=2&state=open)

Related Projects
================
* Feature Incubator: [pyvmomi-tools](https://github.com/vmware/pyvmomi-tools)
* Samples Project: [pyvmomi-community-samples](https://github.com/vmware/pyvmomi-community-samples)

Have fun!
