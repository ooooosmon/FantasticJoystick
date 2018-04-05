# from pymouse import PyMouse
# from pykeyboard import PyKeyboard

import wx
import keyboard as kb

import gui
import joystick as jk


class Master:

    # def detect_buttons_and_axes(self, joystick):
    #     canRun = {
    #         "win+tab": True
    #     }

    #     btn = joystick.GetJoystickButtonStatusBoolean
    #     if len(joystick.joystickButtonsStatus) <= 0:
    #         return

    #     global canRun

    #     def _get_can_run(key):
    #         return canRun[key]

    #     def _set_can_run(key, value):
    #         if canRun[key] is not None:
    #             canRun[key] = value

    #     _key_win_tab = "win+tab"
    #     if btn(0) and btn(1) and _get_can_run(_key_win_tab):
    #         kb.press_keys([kb.windows_l_key, kb.tab_key])
    #         _set_can_run(_key_win_tab, False)
    #         return
    #     elif not btn(0) and not btn(1):
    #         _set_can_run(_key_win_tab, True)
    #     if btn(3):
    #         kb.press_key(kb.windows_l_key)
    #         kb.release_key(kb.windows_l_key)
    #         returnQS

    def register_hot_key(self, hotkey, trigger):
        kb.add_hotkey(hotkey, trigger)

    # get now pressed key and show to the text ctrl component
    def get_current_press_key(self, e, text_ctrl, frame):
        cur_key = kb.read_hotkey(False)
        frame.set_static_text_label(text_ctrl, cur_key)
        print(cur_key)

    def bind_event(self, component, event_type, fc_event):
        component.Bind(event_type, fc_event)

    def unbind_event(self, component, event_type):
        component.Unbind(event_type)

    def _main(self):
        # define basic variable
        app = wx.App()
        frame = gui.MyFrame()
        joystick = jk.Joystick(frame)

        # prepare
        frame.prepare(self.bind_event, self, joystick)

        # start
        frame.start()
        joystick.start()
        app.MainLoop()

        # STOP - this program will stop when user click close button

    def run(self):
        # program enter point
        self._main()

master = Master()
if __name__ == "__main__":
    master.run()
