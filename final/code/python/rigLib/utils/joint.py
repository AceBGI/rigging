"""
Joint utils
"""

import maya.cmds as mc

"""
lists joints hierarchy starting with top join
"""
def listHierarchy(topJoint, withEndJoints = True):
    listedJoints = mc.listRelatives(topJoint, type = "joint", ad = True)
    listedJoints.append(topJoint)
    listedJoints.reverse() # reorder list to have topJoint at top

    completeJoints = listedJoints[:] #make a copy of the listed Joints
    
    if withEndJoints == False:
        completeJoints = [j for j in listedJoints if mc.listRelatives(j, c = 1, type = 'joint')]

    return completeJoints
    