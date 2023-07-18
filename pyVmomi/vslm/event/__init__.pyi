from enum import Enum


class VslmEvent():


    class VslmEventType(Enum):
        preFcdMigrateEvent = "preFcdMigrateEvent"
        postFcdMigrateEvent = "postFcdMigrateEvent"


class VslmEventInfo():


    class State(Enum):
        success = "success"
        error = "error"