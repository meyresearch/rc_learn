"""
RC_learn
A tool to learn in an unsupervised fashion slow reaction coordinates in molecular dynamics
"""

# Add imports here
from .rc_learn import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
