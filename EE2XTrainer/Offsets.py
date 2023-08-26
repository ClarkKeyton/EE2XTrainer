import pymem
from pymem import Pymem

def OpenProcessEE2X():
    pm = Pymem("EE2X.exe")
    return pm
def GetBaseAddress():
    return OpenProcessEE2X().base_address
class Offsets:
    points_ptraddr = GetBaseAddress() + 0x0094D82
    pointsoffset_addr = 0xD4
    resourcesaddr = GetBaseAddress() + 0x0062F8E8
    uraniumoffset = 0x37C
    goldoffset = 0x368
    foodoffset = 0x2DC
    woodoffset = 0x2F0
    stoneoffset = 0x304
    oilrig1offset = 0x24
    oilrig2offset = 0x14C
    oiladdress = GetBaseAddress() + 0x009D4C08