"""

    l o g
    Log
    ===================

    :description:
    A python file to wrap the default logger into an easy include in any project.

"""
#
#   :builtins:
import logging

#
#   :code:
from .settings import PYPENTAGONALCUBE_DEBUG_LEVEL
from .exceptions import InvalidLoggingLevelException

#
#   :statics:
#   Define our logging format.
LOGGING_FORMAT = "[%(asctime)s.%(msecs)03d] %(levelname)s : %(message)s"
LOGGING_DATE_FORMAT = '%Y/%m/%d %H:%M:%S'

#
#   Define the mapping of our logging levels.
LEVELS_MAPPING = {
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "critical": logging.CRITICAL,
    "debug": logging.DEBUG,
    "info": logging.INFO
}

#
#   Ok, handle the environment level and convert it via a dictionary.
logging_level = LEVELS_MAPPING.get(PYPENTAGONALCUBE_DEBUG_LEVEL)
if not logging_level:
    raise InvalidLoggingLevelException(
        f"error, invalid logging level in environment @ "
        f"'PYPENTAGONALCUBE_DEBUG' = '{PYPENTAGONALCUBE_DEBUG_LEVEL}',"
        f" valid options: '{list(LEVELS_MAPPING.keys())}'"
    )

#
#   Ok, now configure our logger dynamically.
logging.basicConfig(
    format=LOGGING_FORMAT,
    datefmt=LOGGING_DATE_FORMAT,
    level=logging_level
)


