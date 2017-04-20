"""
main module for komodo dragon rig setup

"""

import maya.cmds as mc
from rigLib.base import control
from rigLib.base import module

sceneScale = 1.0

#this path will have to change for each computer setup ***********************************
mainProjectPath = 'C:/Users/ace-b/Source/Repos/rigging/final/assets'
modelFilePath = '%s/%s/model/%s_model.mb'
builderSceneFilePath = '%s/%s/builder/%s_builder.mb'

rootJnt = 'root1_jnt'

"""
main function to build character rig
"""
def build(characterName):
    mc.file( new = True, f = True) # make sure the scene is clean

    # make base
    baseRig = module.Base(characterName = characterName, scale = sceneScale)

    # import model
    modelFile = modelFilePath % (mainProjectPath, characterName, characterName)
    mc.file( modelFile, i = 1)

    # import builder scene
    builderFile = builderSceneFilePath % ( mainProjectPath, characterName, characterName )
    mc.file( builderFile, i = 1)

    # parent model
    modelGrp = '%s_model_grp' % characterName
    mc.parent( modelGrp, baseRig.modelGrp )
    
    # parent skeleton
    mc.parent( rootJnt, baseRig.jointsGrp )

