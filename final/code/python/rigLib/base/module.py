"""
module for making top rig structure and rig module 
"""

import maya.cmds as mc

sceneObjectType = 'rig'

from . import control


class Base():
    
    """
    class for building top rig structure
    """
    """ paramaters:
    characterNmae: str, character name
    scale: float, general scale of the rig
    """
    
    def __init__(
                 self,
                 characterName = 'new',
                 scale = 1.0,
                 ):
        
        self.topGrp = mc.group( n = characterName + '_rig_grp', em = 1 )
        self.rigGrp = mc.group( n = 'rig_grp', em = 1, p = self.topGrp )
        self.modelGrp = mc.group( n = 'model_grp', em = 1, p = self.topGrp )
        
        characterNameAt = 'characterName'
        sceneObjectTypeAt = 'sceneObjectType'
        
        for at in [ characterNameAt, sceneObjectTypeAt ]:  
            mc.addAttr( self.topGrp, ln = at, dt = 'string' )
        
        mc.setAttr( self.topGrp + '.' + characterNameAt, characterName, type = 'string', l = 1 )
        mc.setAttr( self.topGrp + '.' + sceneObjectTypeAt, sceneObjectType, type = 'string', l = 1 )
        
        
        # make global control
        
        global1Ctrl = control.Control( 
                                     prefix = 'global1',
                                     scale = scale * 20,
                                     parent = self.rigGrp,
                                     lockChannels = ['v']
                                     )
        
        global2Ctrl = control.Control( 
                                     prefix = 'global2',
                                     scale = scale * 18,
                                     parent = global1Ctrl.C,
                                     lockChannels = ['s', 'v']
                                     )

        self._flatternGloabalCtrlShape(global1Ctrl.C);
        self._flatternGloabalCtrlShape(global2Ctrl.C);
        
        for axis in ['y', 'z']:
            mc.connectAttr(global1Ctrl.C + '.sx', global1Ctrl.C + '.s' + axis)
            mc.setAttr(global1Ctrl.C + '.s' + axis, k = 0)

        # more groups
        self.jointsGrp = mc.group( n = 'joints_grp', em = 1, p = global2Ctrl.C )
        self.modulesGrp = mc.group( n = 'modules_grp', em = 1, p = global2Ctrl.C )
        self.partGrp = mc.group( n = 'parts_grp', em = 1, p = self.rigGrp )
        mc.setAttr(self.partGrp + '.it', l = 1)

    def _flatternGloabalCtrlShape(self, ctrlObject):
        ctrlShapes = mc.listRelatives(ctrlObject, s = 1, type = 'nurbsCurve')
        clust = mc.cluster(ctrlShapes)[1]
        mc.setAttr(clust + '.rz', 90)
        mc.delete(ctrlShapes, ch = 1)


class Module():
    
    """
    class for building Module rig structure
    """
    """ paramaters:
    pregix: str, prefix to name new objects
    baseObject: copy or instance of 'base.module.Base' class
    """
    def __init__(
                 self,
                 prefix = 'new',
                 baseObject = None
                 ):
        
        
        self.topGrp = mc.group( n = prefix + 'Module_grp', em = 1 )
        self.controlGrp = mc.group( n = prefix + 'Controls_grp', em = 1, p = self.topGrp )
        self.jointGrp = mc.group( n = prefix + 'Joints_grp', em = 1, p = self.topGrp )
        self.partGrp = mc.group( n = prefix + 'Parts_grp', em = 1, p = self.topGrp )
        self.partsNoTransGrp = mc.group( n = prefix + 'partsNoTrans_grp', em = 1, p = self.topGrp )

        mc.setAttr(self.partsNoTransGrp + '.it', 0, l = 1)

        if(baseObject):
            mc.parent(self.topGrp, baseObject.modulesGrp)