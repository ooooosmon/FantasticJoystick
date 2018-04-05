import pygame


class _BasicComponentStatusStructure:
    components = None
    status = None

    def __init__(self):
        if self.components is None:
            self.components = []
        if self.status is None:
            self.status = []


class _JoystickHats:
    components = None

    INDEX_LEFT = 0
    INDEX_RIGHT = 1
    INDEX_UP = 2
    INDEX_DOWN = 3

    def __init__(self):
        if self.components is None:
            self.components = []

    status = {
        "current": (0, 0),

        "left": False,
        "right": False,
        "up": False,
        "down": False,

        "pre_left": True,
        "pre_right": True,
        "pre_up": True,
        "pre_down": True
    }


class Joystick:
    PRESSSED_COLOR = (59, 145, 40)
    RELEASED_COLOR = (0, 0, 0)

    done = False

    joystickButtons = _BasicComponentStatusStructure()
    joystickAxes = _BasicComponentStatusStructure()
    joystickHats = _JoystickHats()

    frame = None
    # fcDetectJoystickInput = DetectJoystickInput

    def __init__(self, frame):
        self.frame = frame
        pygame.init()
        pygame.joystick.init()

        self.add_all_joystick_button(self.frame)
        self.add_all_joystick_hat(self.frame)
        self.add_all_joystick_axis(self.frame)

    def start(self, *funcs):
        self.done = False
        self.loop()

    def loop(self, *funcs):
        while not self.done:
            for event in pygame.event.get():
                pass

            joystick_count = pygame.joystick.get_count()
            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()

                # button
                temp_list = []
                buttons = joystick.get_numbuttons()
                for btn in range(buttons):
                    button = joystick.get_button(btn)
                    temp_list.append(button)

                buttons = self.joystickButtons
                if self.compare_list_difference(temp_list, buttons.status):
                    buttons.status.clear()
                    for j in range(len(temp_list)):
                        buttons.status.append(temp_list[j])

                # hat
                temp_list = (0, 0)
                hats = joystick.get_numhats()
                for j in range(hats):
                    hat = joystick.get_hat(j)
                    temp_list = hat

                hats = self.joystickHats
                if self.compare_list_difference(temp_list, hats.status["current"]):
                    hats.status["current"] = temp_list

                hats.status["pre_left"]   = hats.status["left"]
                hats.status["pre_right"]  = hats.status["right"]
                hats.status["pre_up"]     = hats.status["up"]
                hats.status["pre_down"]   = hats.status["down"]

                if (hats.status["current"] == (-1, 0) or
                        hats.status["current"] == (-1, -1) or
                        hats.status["current"] == (-1, 1)):
                    # in condition
                    hats.status["left"] = True
                elif (hats.status["current"] != (-1, 0) or
                        hats.status["current"] != (-1, -1) or
                        hats.status["current"] != (-1, 1)):
                    # in condition
                    hats.status["left"] = False
                if (hats.status["current"] == (1, 0) or
                        hats.status["current"] == (1, -1) or
                        hats.status["current"] == (1, 1)):
                    # in condition
                    hats.status["right"] = True
                elif (hats.status["current"] != (1, 0) or
                        hats.status["current"] != (1, -1) or
                        hats.status["current"] != (1, 1)):
                    # in condition
                    hats.status["right"] = False
                if (hats.status["current"] == (0, 1) or
                        hats.status["current"] == (-1, 1) or
                        hats.status["current"] == (1, 1)):
                    # in condition
                    hats.status["up"] = True
                elif (hats.status["current"] != (0, 1) or
                        hats.status["current"] != (-1, 1) or
                        hats.status["current"] != (1, 1)):
                    # in condition
                    hats.status["up"] = False
                if (hats.status["current"] == (0, -1) or
                        hats.status["current"] == (-1, -1) or
                        hats.status["current"] == (1, -1)):
                    # in condition
                    hats.status["down"] = True
                elif (hats.status["current"] != (0, -1) or
                        hats.status["current"] != (-1, -1) or
                        hats.status["current"] != (1, -1)):
                    # in condition
                    hats.status["down"] = False

                # axis
                axes = joystick.get_numaxes()
                self.joystickAxes.status.clear()
                for a in range(axes):
                    axis = joystick.get_axis(a)
                    self.joystickAxes.status.append(axis)

            # self.fcDetectJoystickInput()
            for i in range(len(funcs)):
                funcs[i](self)
            self.set_buttons_status_display(self.frame)
            self.set_hats_status_display(self.frame)
            self.set_axes_status_display(self.frame)

    def stop(self):
        self.__addition_condition_to_close()

    def add_all_joystick_button(self, frame):
        components = self.joystickButtons.components
        components.append(frame.lblBtnStatus0)
        components.append(frame.lblBtnStatus1)
        components.append(frame.lblBtnStatus2)
        components.append(frame.lblBtnStatus3)
        components.append(frame.lblBtnStatus4)
        components.append(frame.lblBtnStatus5)
        components.append(frame.lblBtnStatus6)
        components.append(frame.lblBtnStatus7)
        components.append(frame.lblBtnStatus8)
        components.append(frame.lblBtnStatus9)
        components.append(frame.lblBtnStatus10)
        components.append(frame.lblBtnStatus11)
        components.append(frame.lblBtnStatus12)
        components.append(frame.lblBtnStatus13)

    def add_all_joystick_hat(self, frame):
        components = self.joystickHats.components
        components.append(frame.lblHatStatus0)  # left
        components.append(frame.lblHatStatus1)  # right
        components.append(frame.lblHatStatus2)  # up
        components.append(frame.lblHatStatus3)  # down

    def add_all_joystick_axis(self, frame):
        components = self.joystickAxes.components
        components.append(frame.lblAxisStatus0)
        components.append(frame.lblAxisStatus1)
        components.append(frame.lblAxisStatus2)
        components.append(frame.lblAxisStatus3)
        components.append(frame.lblAxisStatus4)
        components.append(frame.lblAxisStatus5)

    def compare_list_difference(self, l1, l2):
        if len(l1) != len(l2):
            return True  # l1 and l2 is difference
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return True
        # print("there are same")
        return False

    # button
    def get_joystick_button_status_integer(self, index):
        return 1 if self.joystickButtons.status[index] == 1 else 0

    def get_joystick_button_dtatus_boolean(self, index):
        return True if self.joystickButtons.status[index] == 1 else False

    def get_joystick_button_status_string(self, index):
        return "True" if self.joystickButtons.status[index] == 1 else "False"

    # hat
    def get_joystick_hat_status(self):
        return self.joystickHats.status["current"]

    # axis
    def get_joystick_axis_status(self, index):
        return self.joystickAxes.status[index]

    def get_joystick_axis_status_boolean(self, index):
        if index >= 0 and index <= 3:
            if self.joystickAxes.status[index] > 0.1:
                return True
            else:
                return False
        elif index == 4 or index == 5:
            if self.joystickAxes.status[index] > -1.0:
                return True
            else:
                return False

    def set_buttons_status_display(self, frame):
        buttons = self.joystickButtons
        if len(buttons.components) <= 0:
            return
        for i in range(len(buttons.components)):
            status = self.get_joystick_button_status_string(i)
            if buttons.components[i].Label != status:
                frame.set_static_text_label(buttons.components[i], status)
                buttons.components[i].SetForegroundColour(self.PRESSSED_COLOR if status == "True" else self.RELEASED_COLOR)

    def set_hats_status_display(self, frame):
        if len(self.joystickHats.components) <= 0:
            return

        for i in range(len(self.joystickHats.components)):
            hats = self.joystickHats

            LEFT   = hats.INDEX_LEFT   # noqa
            RIGHT  = hats.INDEX_RIGHT  # noqa
            UP     = hats.INDEX_UP     # noqa
            DOWN   = hats.INDEX_DOWN   # noqa

            if (hats.status["left"] is True and
               (hats.status["left"] is not hats.status["pre_left"])):
                # code behavior
                frame.set_static_text_label(hats.components[LEFT], "True")
                hats.components[LEFT].SetForegroundColour(self.PRESSSED_COLOR)
            elif (hats.status["left"] is False and
                 (hats.status["left"] is not hats.status["pre_left"])):
                # code behavior
                frame.set_static_text_label(hats.components[LEFT], "False")
                hats.components[LEFT].SetForegroundColour(self.RELEASED_COLOR)
            if (hats.status["right"] is True and
               (hats.status["right"] is not hats.status["pre_right"])):
                # code behavior
                frame.set_static_text_label(hats.components[RIGHT], "True")
                hats.components[RIGHT].SetForegroundColour(self.PRESSSED_COLOR)
            elif (hats.status["right"] is False and
                 (hats.status["right"] is not hats.status["pre_right"])):
                # code behavior
                hats.components[RIGHT].SetLabel("False")
                frame.set_static_text_label(hats.components[RIGHT], "False")
                hats.components[RIGHT].SetForegroundColour(self.RELEASED_COLOR)
            if (hats.status["up"] is True and
               (hats.status["up"] is not hats.status["pre_up"])):
                # code behavior
                frame.set_static_text_label(hats.components[UP], "True")
                hats.components[UP].SetForegroundColour(self.PRESSSED_COLOR)
            elif (hats.status["up"] is False and
                 (hats.status["up"] is not hats.status["pre_up"])):
                # code behavior
                frame.set_static_text_label(hats.components[UP], "False")
                hats.components[UP].SetForegroundColour(self.RELEASED_COLOR)
            if (hats.status["down"] is True and
               (hats.status["down"] is not hats.status["pre_down"])):
                # code behavior
                frame.set_static_text_label(hats.components[DOWN], "True")
                hats.components[DOWN].SetForegroundColour(self.PRESSSED_COLOR)
            elif (hats.status["down"] is False and
                 (hats.status["down"] is not hats.status["pre_down"])):
                # code behavior
                frame.set_static_text_label(hats.components[DOWN], "False")
                hats.components[DOWN].SetForegroundColour(self.RELEASED_COLOR)

    def set_axes_status_display(self, frame):
        axes = self.joystickAxes
        if len(axes.components) <= 0:
            return
        for i in range(len(axes.components)):
            status = round(self.get_joystick_axis_status(i), 1)
            if abs(status - 0) < 0.01:
                status = 0
            if axes.components[i].Label != str(status):
                frame.set_static_text_label(axes.components[i], str(status))

    def __addition_condition_to_close(self):
        self.done = True
        print("stop")

    def detect_joystick_nput():
        pass
