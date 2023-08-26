from pymem import Pymem
from pymem.ptypes import RemotePointer
from Offsets import *
def GetAddressWithOffsets(base, offsets):
    remote_pointer = RemotePointer(OpenProcessEE2X().process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(OpenProcessEE2X().process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset