from threading import Thread
from time import sleep

import gi
gi.require_version("Gst", "1.0")

from gi.repository import Gst, GLib, GObject


Gst.init()

main_loop = GLib.MainLoop()
main_loop_thread = Thread(target=main_loop.run)
main_loop_thread.start()

pipeline = Gst.parse_launch("udpsrc address=230.230.230.230 ! fakesink")
sink = pipeline.get_by_name("fakesink0")
pad = sink.get_static_pad("sink")
caps = pad.get_current_caps()

pipeline.set_state(Gst.State.PLAYING)
try:
    while True:
        sleep(0.1)
        print(caps)
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
print("over")
main_loop.quit()
main_loop_thread.join()