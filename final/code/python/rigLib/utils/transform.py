"""
functions to manipulate and create transforms
"""

import maya.cmds as mc
from . import name

"""
make offset group for given object
"""
""" pramaters
object: transform object to get offset group
prefix: string, prfix is name of new offset group

"""
def makeOffsetGrp(object, prefix = ""):
    if not prefix:
        prefix = name.removeSuffix(object)

    offsetGrp = mc.group(n = prefix + 'offset_grp', em = 1)
    objectParents = mc.listRelatives(object, p = 1) # returns a list of parents / relatives
    
    # if there object has any parents then parent offsetGrp to the top relative in the list index [0]
    if objectParents:
        mc.parent(offsetGrp, objectParents[0]) 
    
    #match object transform
    mc.delete(mc.parentConstraint(object, offsetGrp))
    mc.delete(mc.scaleConstraint(object, offsetGrp))

    mc.parent(object, offsetGrp) # parent object under offset group
    
    return offsetGrp