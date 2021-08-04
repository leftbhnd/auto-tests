class AsrMsg:
    def __init__(self, text, uuid):
        self.text = text
        self.uuid = uuid


class ClickMsg:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class FaseMsg:
    def __init__(self, type, id, facemask, score):
        self.type = type
        self.id = id
        self.facemask = facemask
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
        self._buttons = [0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                         ]

    def upVolume(self):
        # X LB
        self._buttons[3] = 1
        self._buttons[6] = 1
        return {'axes': self._axes, 'buttons': self._buttons}

    def downVolume(self):
        # X LT
        self._buttons[3] = 1
        self._axes[5] = -1.0
        return {'axes': self._axes, 'buttons': self._buttons}

    def upMic(self):
        # X RB
        self._buttons[3] = 1
        self._buttons[7] = 1
        return {'axes': self._axes, 'buttons': self._buttons}

    def downMic(self):
        # X RT
        self._buttons[3] = 1
        self._axes[4] = -1.0
        return {'axes': self._axes, 'buttons': self._buttons}

    def phraseMode(self):
        # back Y
        self._buttons[15] = 1
        self._buttons[4] = 1
        return {'axes': self._axes, 'buttons': self._buttons}

    def nextPhrase(self):
        # Y RT
        self._buttons[4] = 1
        self._axes[4] = -1.0
        return {'axes': self._axes, 'buttons': self._buttons}

    def previosePhrase(self):
        # Y RB
        self._buttons[4] = 1
        self._buttons[7] = 1
        return {'axes': self._axes, 'buttons': self._buttons}

    def autoMode(self):
        # back start
        self._buttons[15] = 1
        self._buttons[11] = 1
        return {'axes': self._axes, 'buttons': self._buttons}
