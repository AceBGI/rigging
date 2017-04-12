"""
By Alex Eakle
control module for making rig controls

"""
import maya.cmds as mc

class Control():
    """
    class for building rig control
    """
    def __init__(self, 
                 prefix = 'new', 
                 scale = 1.0, 
                 translateTo = '',
                 rotateTo = '',
                 parent = '',
                 lockChannels = ['s','v']
                 ):
        ctrlObject = mc.circle( n = prefix + '_ctrl', ch = False, normal = [1,0,0], radius = scale )[0]
        ctrlOffset = mc.group(n = prefix + 'offset_grp', em = 1 )# keep chanels clean
        mc.parent(ctrlObject, ctrlOffset); # parents object controler to a ofset

        """
         translate control 
        """

        if mc.objExists( translateTo ):
            mc.delete( ms.pointConstraint(translateTo, ctrlOffset)) # moves controler object to referrence object

        """
         rotate control 
        """

        if mc.objExists( rotateTo ):
            mc.delete( ms.orientConstraint(rotateTo, ctrlOffset)) # rotate controler object to  match referrence objects rotation


        """
         parent control 
        """

        if mc.objExists( parent ):
            mc.parent( ctrlObject, parent )
