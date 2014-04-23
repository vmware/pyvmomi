pyVmomi is a Python SDK for the VMware vSphere API that allows you to
manipulate ESX, ESXi, and vCenter using scripts.

To get started, check out the examples in `sample/poweronvm.py` and
`sample/getallvms.py`.

You can install this as a package. Just run `python setup.py bdist_egg`
and then use `pip` or `easy_install` to deploy it on your system.

There are other bindings of this API in other languages. See:

* **vijava** (Java): http://vijava.sourceforge.net/
* **rbvmomi** (Ruby): https://github.com/vmware/rbvmomi
* **vSphere SDK for Perl** (non-free): https://my.vmware.com/group/vmware/details?downloadGroup=VSP510-SDKPERL-510&productId=285

Supported Versions of Python
* python version 2.6 and above

Supported Versions of vSphere
* version 2.0 and above

Version compatibility policy
* every release of pyVmomi is backwards compatible with every preceding release
