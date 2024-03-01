class Switch:
    def __init__(self, device):
        self.device = device

    def press(self):
        self.device.turn_on()

class LightBulb:
    def turn_on(self):
        pass

switch = Switch(LightBulb())
switch.press()
