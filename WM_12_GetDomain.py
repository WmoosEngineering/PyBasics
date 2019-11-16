# -*- coding: utf-8 -*-
"""
@author:  Wmoos
@company: Wmoos Engineering 
@e-mail:  victor.vimos@wmoos.com
@country: Quito-Ecuador
"""

def GetDomain(correo):
    return correo.split("@")[-1]


print(GetDomain('user@domain.com'))
