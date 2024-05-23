import vgamepad
from time import sleep

controller = vgamepad.VDS4Gamepad()
def galaw():
    controller.right_joystick_float(0.25,-0.25)
    controller.update()
    sleep(0.1)
    controller.right_joystick_float(0,0)
    controller.update()
    sleep(0.1)
    controller.right_joystick_float(-0.25,0.25)
    controller.update()
    sleep(0.1)
    controller.right_joystick_float(0,0)
    controller.update()