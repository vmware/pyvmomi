
vmodl.query.PropertyCollector.Change
====================================
  Describes a change to a property.
:extends: vmodl.DynamicData_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Property or nested property to which the change applies. Nested properties are specified by paths; for example,
        * foo.bar
        * foo.arProp["key val"]
        * foo.arProp["key val"].baz
        * 
    op (`vmodl.query.PropertyCollector.Change.Op <vmodl/query/PropertyCollector/Change/Op.rst>`_):

       Change operation for the property. Valid values are:addThe property is a collection and the change inserts an element into the collection.removeThe property is a collection and the change deletes an element from the collection.assignThe change is a new value for the property.indirectRemoveThe property was removed because a containing property was removed or unset
    val (`object <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       New value for the property when "op" is either "add" or "assign".
