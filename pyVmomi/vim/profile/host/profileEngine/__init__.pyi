from enum import Enum


class AnswerFileValidationInfo():


    class Status(Enum):
        success = "success"
        failed = "failed"
        failed_defaults = "failed_defaults"