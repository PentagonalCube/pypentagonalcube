"""

    s e t t i n g s
    Settings
    ===================

    :description:
    A file to hold onto the settings/configuration for the package.

"""
#
#   :code:
from .utils import read_from_environment

PYPENTAGONALCUBE_DEBUG_LEVEL = read_from_environment(
    variable_name="PYPENTAGONALCUBE_DEBUG",
    default_value="error"
)

PYPENTAGONALCUBE_CACHE_SECONDS = read_from_environment(
    variable_name="PYPENTAGONALCUBE_CACHE_SECONDS",
    default_value=60 * 15,  # 15 minutes,
    cast_to_type=float
)
