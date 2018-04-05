import wx


class MyFrame(wx.Frame):
    triggerInputTimes = -8

    def __init__(self):
        wx.Frame.__init__(self, None, size=(1024, 768))

        panel = wx.Panel(self)
        panel.SetBackgroundColour((255, 255, 0))

        sizer = wx.GridBagSizer(0, 0)

        # def add_joystick_status_component():
        # add_joystick_status_component()

        self._create_and_setup_status_component(panel)
        self._create_and_setup_add_hotkey_component(panel)
        self._create_and_setup_hotkey_list_component(panel)
        self._add_component_to_sizer(sizer)
        # self.textCtrl = wx.TextCtrl(panel)
        # sizer.Add(self.textCtrl, pos=(0, 6), flag=wx.ALL, border=5)

        panel.SetSizerAndFit(sizer)
        self.Centre()

    # create some label to show joystick input status
    def _create_and_setup_status_component(self, parent):
        # button 0
        self.lblBtn0 = wx.StaticText(parent, wx.ID_ANY, "X", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn0.Wrap(-1)
        self.lblBtnStatus0 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus0.Wrap(-1)

        # button 1
        self.lblBtn1 = wx.StaticText(parent, wx.ID_ANY, "A", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn1.Wrap(-1)
        self.lblBtnStatus1 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus1.Wrap(-1)

        # button 2
        self.lblBtn2 = wx.StaticText(parent, wx.ID_ANY, "B", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn2.Wrap(-1)
        self.lblBtnStatus2 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus2.Wrap(-1)

        # button 3
        self.lblBtn3 = wx.StaticText(parent, wx.ID_ANY, "Y", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn3.Wrap(-1)
        self.lblBtnStatus3 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus3.Wrap(-1)

        # button 4
        self.lblBtn4 = wx.StaticText(parent, wx.ID_ANY, "Left Bumper", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn4.Wrap(-1)
        self.lblBtnStatus4 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus4.Wrap(-1)

        # button 5
        self.lblBtn5 = wx.StaticText(parent, wx.ID_ANY, "Right Bumper", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn5.Wrap(-1)
        self.lblBtnStatus5 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus5.Wrap(-1)

        # button 6
        self.lblBtn6 = wx.StaticText(parent, wx.ID_ANY, "Left Trigger", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn6.Wrap(-1)
        self.lblBtnStatus6 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus6.Wrap(-1)

        # button 7
        self.lblBtn7 = wx.StaticText(parent, wx.ID_ANY, "Right Trigger", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn7.Wrap(-1)
        self.lblBtnStatus7 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus7.Wrap(-1)

        # button 8
        self.lblBtn8 = wx.StaticText(parent, wx.ID_ANY, "Back", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn8.Wrap(-1)
        self.lblBtnStatus8 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus8.Wrap(-1)

        # button 9
        self.lblBtn9 = wx.StaticText(parent, wx.ID_ANY, "Start", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn9.Wrap(-1)
        self.lblBtnStatus9 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus9.Wrap(-1)

        # button 10
        self.lblBtn10 = wx.StaticText(parent, wx.ID_ANY, "Left Stick", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn10.Wrap(-1)
        self.lblBtnStatus10 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus10.Wrap(-1)

        # button 11
        self.lblBtn11 = wx.StaticText(parent, wx.ID_ANY, "Right Stick", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn11.Wrap(-1)
        self.lblBtnStatus11 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus11.Wrap(-1)

        # button 12
        self.lblBtn12 = wx.StaticText(parent, wx.ID_ANY, "Guide", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn12.Wrap(-1)
        self.lblBtnStatus12 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus12.Wrap(-1)

        # button 13
        self.lblBtn13 = wx.StaticText(parent, wx.ID_ANY, "Touchpad", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtn13.Wrap(-1)
        self.lblBtnStatus13 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblBtnStatus13.Wrap(-1)

        # hat 0 | -1
        self.lblHat0 = wx.StaticText(parent, wx.ID_ANY, "Left", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblHat0.Wrap(-1)
        self.lblHatStatus0 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblHatStatus0.Wrap(-1)

        # hat 1 | 1
        self.lblHat1 = wx.StaticText(parent, wx.ID_ANY, "Right", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblHat1.Wrap(-1)
        self.lblHatStatus1 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblHatStatus1.Wrap(-1)

        # hat 2 | -1
        self.lblHat2 = wx.StaticText(parent, wx.ID_ANY, "Up", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblHat2.Wrap(-1)
        self.lblHatStatus2 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblHatStatus2.Wrap(-1)

        # hat 3 | 1
        self.lblHat3 = wx.StaticText(parent, wx.ID_ANY, "Down", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblHat3.Wrap(-1)
        self.lblHatStatus3 = wx.StaticText(parent, wx.ID_ANY, "False", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblHatStatus3.Wrap(-1)

        # axes 0
        self.lblAxis0 = wx.StaticText(parent, wx.ID_ANY, "LS x axis")
        self.lblAxis0.Wrap(-1)
        self.lblAxisStatus0 = wx.StaticText(parent, wx.ID_ANY, str(-1.0))
        self.lblAxisStatus0.Wrap(-1)

        # axes 1
        self.lblAxis1 = wx.StaticText(parent, wx.ID_ANY, "LS y axis")
        self.lblAxis1.Wrap(-1)
        self.lblAxisStatus1 = wx.StaticText(parent, wx.ID_ANY, str(-1.0))
        self.lblAxisStatus1.Wrap(-1)

        # axes 2
        self.lblAxis2 = wx.StaticText(parent, wx.ID_ANY, "RS x axis")
        self.lblAxis2.Wrap(-1)
        self.lblAxisStatus2 = wx.StaticText(parent, wx.ID_ANY, str(-1.0))
        self.lblAxisStatus2.Wrap(-1)

        # axes 3
        self.lblAxis3 = wx.StaticText(parent, wx.ID_ANY, "RS y axis")
        self.lblAxis3.Wrap(-1)
        self.lblAxisStatus3 = wx.StaticText(parent, wx.ID_ANY, str(-1.0))
        self.lblAxisStatus3.Wrap(-1)

        # axes 4
        self.lblAxis4 = wx.StaticText(parent, wx.ID_ANY, "Right Trigger")
        self.lblAxis4.Wrap(-1)
        self.lblAxisStatus4 = wx.StaticText(parent, wx.ID_ANY, str(-1.0))
        self.lblAxisStatus4.Wrap(-1)

        # axes 5
        self.lblAxis5 = wx.StaticText(parent, wx.ID_ANY, "Left Trigger")
        self.lblAxis5.Wrap(-1)
        self.lblAxisStatus5 = wx.StaticText(parent, wx.ID_ANY, str(-1.0))
        self.lblAxisStatus5.Wrap(-1)

    def _create_and_setup_add_hotkey_component(self, parent):
        # input hotkey
        self.lblInputHotKey = wx.StaticText(parent, wx.ID_ANY, "Hotkey", wx.DefaultPosition, wx.DefaultSize, 0)
        self.tcInputHotkey = wx.TextCtrl(parent, wx.ID_ANY, "None", wx.DefaultPosition, wx.DefaultSize, 0)

        # trigger key what you want
        self.lblTriggerKey = wx.StaticText(parent, wx.ID_ANY, "Trigger Key", wx.DefaultPosition, wx.DefaultSize, 0)
        self.tcTriggerkey = wx.TextCtrl(parent, wx.ID_ANY, "None", wx.DefaultPosition, wx.DefaultSize, 0)

        # ok and cancel button
        self.btnCreateHotkeyOkay = wx.Button(parent, wx.ID_ANY, "Okay", wx.DefaultPosition, wx.DefaultSize, 0)
        self.btnCreateHotkeyCancel = wx.Button(parent, wx.ID_ANY, "Cancel", wx.DefaultPosition, wx.DefaultSize, 0)

    def _create_and_setup_hotkey_list_component(self, parent):
        pass

    # add this component into sizer to display on the window
    def _add_component_to_sizer(self, sizer):
        buttons_label_start_col_num = 0
        buttons_label_start_row_num = 0

        def add_status_component():
            # button 0
            sizer.Add(self.lblBtn0, pos=(buttons_label_start_row_num + 0, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus0, pos=(buttons_label_start_row_num + 0, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 1
            sizer.Add(self.lblBtn1, pos=(buttons_label_start_row_num + 1, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus1, pos=(buttons_label_start_row_num + 1, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 2
            sizer.Add(self.lblBtn2, pos=(buttons_label_start_row_num + 2, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus2, pos=(buttons_label_start_row_num + 2, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 3
            sizer.Add(self.lblBtn3, pos=(buttons_label_start_row_num + 3, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus3, pos=(buttons_label_start_row_num + 3, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 4
            sizer.Add(self.lblBtn4, pos=(buttons_label_start_row_num + 4, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus4, pos=(buttons_label_start_row_num + 4, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 5
            sizer.Add(self.lblBtn5, pos=(buttons_label_start_row_num + 5, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus5, pos=(buttons_label_start_row_num + 5, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 6
            sizer.Add(self.lblBtn6, pos=(buttons_label_start_row_num + 6, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus6, pos=(buttons_label_start_row_num + 6, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 7
            sizer.Add(self.lblBtn7, pos=(buttons_label_start_row_num + 7, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus7, pos=(buttons_label_start_row_num + 7, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 8
            sizer.Add(self.lblBtn8, pos=(buttons_label_start_row_num + 8, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus8, pos=(buttons_label_start_row_num + 8, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 9
            sizer.Add(self.lblBtn9, pos=(buttons_label_start_row_num + 9, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus9, pos=(buttons_label_start_row_num + 9, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 10
            sizer.Add(self.lblBtn10, pos=(buttons_label_start_row_num + 10, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus10, pos=(buttons_label_start_row_num + 10, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 11
            sizer.Add(self.lblBtn11, pos=(buttons_label_start_row_num + 11, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus11, pos=(buttons_label_start_row_num + 11, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 12
            sizer.Add(self.lblBtn12, pos=(buttons_label_start_row_num + 12, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus12, pos=(buttons_label_start_row_num + 12, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # button 13
            sizer.Add(self.lblBtn13, pos=(buttons_label_start_row_num + 13, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblBtnStatus13, pos=(buttons_label_start_row_num + 13, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # hat 0 | -1
            sizer.Add(self.lblHat0, pos=(buttons_label_start_row_num + 14, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblHatStatus0, pos=(buttons_label_start_row_num + 14, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # hat 1 | 1
            sizer.Add(self.lblHat1, pos=(buttons_label_start_row_num + 15, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblHatStatus1, pos=(buttons_label_start_row_num + 15, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # hat 2 | -1
            sizer.Add(self.lblHat2, pos=(buttons_label_start_row_num + 16, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblHatStatus2, pos=(buttons_label_start_row_num + 16, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # hat 3 | 1
            sizer.Add(self.lblHat3, pos=(buttons_label_start_row_num + 17, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblHatStatus3, pos=(buttons_label_start_row_num + 17, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # axis 0
            sizer.Add(self.lblAxis0, pos=(buttons_label_start_row_num + 18, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblAxisStatus0, pos=(buttons_label_start_row_num + 18, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # axis 1
            sizer.Add(self.lblAxis1, pos=(buttons_label_start_row_num + 19, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblAxisStatus1, pos=(buttons_label_start_row_num + 19, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # axis 2
            sizer.Add(self.lblAxis2, pos=(buttons_label_start_row_num + 20, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblAxisStatus2, pos=(buttons_label_start_row_num + 20, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # axis 3
            sizer.Add(self.lblAxis3, pos=(buttons_label_start_row_num + 21, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblAxisStatus3, pos=(buttons_label_start_row_num + 21, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # axis 4
            sizer.Add(self.lblAxis4, pos=(buttons_label_start_row_num + 22, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblAxisStatus4, pos=(buttons_label_start_row_num + 22, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

            # axis 5
            sizer.Add(self.lblAxis5, pos=(buttons_label_start_row_num + 23, buttons_label_start_col_num + 0), flag=wx.ALL, border=5)
            sizer.Add(self.lblAxisStatus5, pos=(buttons_label_start_row_num + 23, buttons_label_start_col_num + 1), flag=wx.ALL, border=5)

        def add_create_hotkey_component():
            sizer.Add(self.lblInputHotKey, pos=(0, 3), flag=wx.ALL, border=5)
            sizer.Add(self.tcInputHotkey, pos=(0, 4), flag=wx.ALL, border=5)
            sizer.Add(self.lblTriggerKey, pos=(1, 3), flag=wx.ALL, border=5)
            sizer.Add(self.tcTriggerkey, pos=(1, 4), flag=wx.ALL, border=5)
            sizer.Add(self.btnCreateHotkeyOkay, pos=(2, 3), flag=wx.ALL | wx.EXPAND, border=5)
            sizer.Add(self.btnCreateHotkeyCancel, pos=(2, 4), flag=wx.ALL | wx.EXPAND, border=5)

        def add_hotkey_list():
            pass

        add_status_component()
        add_create_hotkey_component()
        add_hotkey_list()

    def _bind_basic_event(self, bind_evt, master, joystick):
        # to break the joystick infinity loop then close the whole program
        bind_evt(self, wx.EVT_CLOSE, lambda e: self._on_close(e, joystick))

        # bind any event here...
        bind_evt(self.tcInputHotkey, wx.EVT_KEY_DOWN, lambda e: master.get_current_press_key(e, self.tcInputHotkey, self))
        bind_evt(self.tcTriggerkey, wx.EVT_KEY_DOWN, lambda e: master.get_current_press_key(e, self.tcTriggerkey, self))

    def prepare(self, bind_evt, master, joystick):
        self._bind_basic_event(bind_evt, master, joystick)

    def start(self):
        self.Show()

    def set_static_text_label(self, component, value="ERROR"):
        component.SetLabel(value)
        self.triggerInputTimes += 1
        # print("Trigger Times: %s" %self.triggerInputTimes)

    # EVENT

    def _on_close(self, e, joystick):
        joystick.stop()
        self.Destroy()

    def _on_key_press(self, e):
        pass
