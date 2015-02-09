"""
Script managing all the default paths to the scripts
"""

import sys

def addPath(sysPath):
    sysPath.append("./Manipulation")
    sysPath.append("./Features")
    sysPath.append("./Submissions")
    sysPath.append("./Data")

    return sysPath
