import sys

for p in sys.path:
    print p
    
codePath = 'C:/Users/u0584599/Source/Repos/rigging/final/code/python'

if not codePath is sys.path:
    sys.path.append(codePath)

import rigLib 

c = rigLib.base.control.Control()
