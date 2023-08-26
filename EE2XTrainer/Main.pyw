import dearpygui.dearpygui as d
import Hack as EE2Hack
import Offsets as addr_ee2x
from pymem import Pymem
def OILHack():
    oil_real_offsets = EE2Hack.GetAddressWithOffsets(addr_ee2x.GetBaseAddress() + addr_ee2x.Offsets.oiladdress, offsets=[addr_ee2x.Offsets.oilrig1offset, addr_ee2x.Offsets.oilrig2offset])
    EE2Hack.OpenProcessEE2X().write_int(oil_real_offsets, int(d.get_value("OILRIG_VALUE")))
class DearPyGui_Main:
    def Main():
        d.create_context()

        with d.window(tag="EE2XHack_WindowMain"):
            d.add_text("Hello, It's My First External Trainer for Empire Earth 2... Enjoy!!!", color=[155, 76, 76, 255])
            d.add_slider_int(label="SET OIL VALUE", min_value=0, max_value=700000, tag="OILRIG_VALUE")
            d.add_button(label="SET VALUE TO OIL", callback=OILHack)
        d.create_viewport(title='EE2X Trainer by ClarkKeyton', width=855, height=920)
        d.setup_dearpygui()
        d.show_viewport()
        d.set_primary_window("EE2XHack_WindowMain", True)
        d.start_dearpygui()
        d.destroy_context()
if __name__ == "__main__":
    DearPyGui_Main.Main()