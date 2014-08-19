
vmodl.query.PropertyCollector.Filter
====================================
  The `PropertyFilter <vmodl/query/PropertyCollector/Filter.rst>`_ managed object type defines a filter that controls the properties for which a `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ detects incremental changes. Filters are subordinate objects; they are part of the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ and do not have independent lifetimes. A Filter is automatically destroyed when the session on which it was created is closed or the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ on which it was created is destroyed.




Attributes
----------
    spec (`vmodl.query.PropertyCollector.FilterSpec <vmodl/query/PropertyCollector/FilterSpec.rst>`_):
       Specifications for this filter.
    partialUpdates (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       Flag to indicate if a change to a nested property reports only the nested change or the entire specified property value. If the value is true, a change reports only the nested property. If the value is false, a change reports the enclosing property named in the filter.


Methods
-------


DestroyPropertyFilter():
   Destroys this filter.This operation can be called explicitly, or it can take place implicitly when the session that created the filter is closed.


  Privilege:



  Args:


  Returns:
    None
         


