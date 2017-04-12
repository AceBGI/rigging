"""
module for making rig controls 
"""

import maya.cmds as mc

class Control():
    
    """
    class for building rig control
    """
    
    def __init__(
                 self,
                 prefix = 'new',
                 scale = 1.0,
                 translateTo = '',
                 rotateTo = '',
                 parent = '',
                 shape = 'circle',
                 lockChannels = ['s','v']
                 ):
        
        
   
            
        ctrlObject = mc.circle( n = prefix + '_ctl', ch = False, normal = [1, 0, 0], radius = scale )[0]
        ctrlOffset = mc.group( n = prefix + 'Offset_grp', em = 1 )
        mc.parent( ctrlObject, ctrlOffset )
        
        # color control
        ctrlShape = mc.listRelatives(ctrlObject, s = 1)[0]
        mc.setAttr(ctrlShape + '.ove', 1)
        
        # colors: 6 = blue, 13 = red, 22 = yellow
        if prefix.startswith("l_") | prefix.startswith("L_") | prefix.startswith("left") | prefix.startswith("Left"): #blue
            mc.setAttr(ctrlShape + '.ovc', 6) # .ovc = override color
        elif prefix.startswith("r_") | prefix.startswith("R_") | prefix.startswith("right") | prefix.startswith("Right"): #red
            mc.setAttr(ctrlShape + '.ovc', 13)
        else:
            mc.setAttr(ctrlShape + '.ovc', 22) #yellow
        
        # translate control
        
        if mc.objExists( translateTo ):
            
            mc.delete( mc.pointConstraint( translateTo, ctrlOffset ) )
        
        # rotate control
        
        if mc.objExists( rotateTo ):
            
            mc.delete( mc.orientConstraint( rotateTo, ctrlOffset ) )
        
        # parent control
        
        if mc.objExists( parent ):
            
            mc.parent( ctrlOffset, parent )
        
        # lock control channels
        
        singleAttributeLockList = []
        
        for item in lockChannels:
            
            if item in ['t','r','s']:
                
                for axis in ['x','y','z']:
                    
                    at = item + axis
                    singleAttributeLockList.append( at )
            
            else:
                
                singleAttributeLockList.append( item )
        
        for at in singleAttributeLockList:
            
            mc.setAttr( ctrlObject + '.' + at, l = 1, k = 0 )
        
        
        # add public members
        
        self.C = ctrlObject
        self.Off = ctrlOffset
        
        
        
        
                    
                    
        
        
        
        
        
        
        
        
        
        
        
       
        
        
        
