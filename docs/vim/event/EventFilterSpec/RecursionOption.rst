vim.event.EventFilterSpec.RecursionOption
=========================================
  This option specifies how to select events based on child relationships in the inventory hierarchy. If a managed entity has children, their events can be retrieved with this filter option.
  :contained by: `vim.event.EventFilterSpec <vim/event/EventFilterSpec.rst>`_

  :type: `vim.event.EventFilterSpec.RecursionOption <vim/event/EventFilterSpec/RecursionOption.rst>`_

  :name: all

values:
--------

self
   Returns events that pertain only to the specified managed entity, and not its children.

children
   Returns events pertaining to child entities only. Excludes events pertaining to the specified managed entity itself.

all
   Returns events pertaining either to the specified managed entity or to its child entities.
