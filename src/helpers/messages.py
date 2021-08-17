class AsrTtsMsg:
    def __init__(self, text, uuid):
        self.text = text
        self.uuid = uuid


class ClickMsg:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class FaceMsg:
    def __init__(self, type, is_tracking, id, track_id, score):
        self.type = type
        self.is_tracking = is_tracking
        self.id = id
        self.track_id = track_id
        self.score = score


class InteractionMsg:
    def __init__(self, state, reason):
        self.state = state
        # reason's type: Speech = 0, Face = 1, Click = 2, Hark = 3
        self.reason = reason


class JoyCmdMsg:
    def __init__(self):
        '''
        axes = [0.0, 0.0, 0.0, 0.0, RT, LT]
        buttons = [A, B, 0, X, Y, 0, LB, RB, 0, 0, 0, start, 0, 0, 0, back, 0, up, right, down, left]
        '''
        self._axes = [0.0, 0.0, 0.0, 0.0, 1.0, 1.0]
        self._buttons = [
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]

    def upVolume(self):
        # X LB
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[3], first_press_buttons[6] = 1, 1

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[3], second_press_buttons[6] = 1, 0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def downVolume(self):
        # X LT
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[3], first_press_axes[5] = 1, -1.0

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[3], second_press_axes[5] = 1, 1.0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def upMic(self):
        # X RB
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[3], first_press_buttons[7] = 1, 1

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[3], second_press_buttons[7] = 1, 0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def downMic(self):
        # X RT
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[3], first_press_axes[4] = 1, -1.0

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[3], second_press_axes[4] = 1, 1.0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def phraseMode(self):
        # back Y
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[15], first_press_buttons[4] = 1, 1

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[15], second_press_buttons[4] = 1, 0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def nextPhrase(self):
        # Y RT
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[4], first_press_axes[4] = 1, -1.0

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[4], second_press_axes[4] = 1, 1.0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def previousPhrase(self):
        # Y RB
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[4], first_press_buttons[7] = 1, 1

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[4], second_press_buttons[7] = 1, 0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]

    def autoMode(self):
        # back start
        first_press_axes, first_press_buttons = list(
            self._axes), list(self._buttons)
        first_press_buttons[15], first_press_buttons[11] = 1, 1

        second_press_axes, second_press_buttons = list(
            self._axes), list(self._buttons)
        second_press_buttons[15], second_press_buttons[11] = 1, 0

        return [
            {'axes': first_press_axes, 'buttons': first_press_buttons},
            {'axes': second_press_axes, 'buttons': second_press_buttons},
            {'axes': self._axes, 'buttons': self._buttons}
        ]
