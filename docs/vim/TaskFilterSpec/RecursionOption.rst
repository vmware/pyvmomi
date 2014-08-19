vim.TaskFilterSpec.RecursionOption
==================================
  This option specifies how to select tasks based on child relationships in the inventory hierarchy. If a managed entity has children, their tasks can be retrieved with this filter option.
  :contained by: `vim.TaskFilterSpec <vim/TaskFilterSpec.rst>`_

  :type: `vim.TaskFilterSpec.RecursionOption <vim/TaskFilterSpec/RecursionOption.rst>`_

  :name: all

values:
--------

self
   Returns tasks that pertain only to the specified managed entity, and not its children.

children
   Returns tasks pertaining to child entities only. Excludes tasks pertaining to the specified managed entity itself.

all
   Returns tasks pertaining either to the specified managed entity or to its child entities.
