import vgamepad
from time import sleep

controller = vgamepad.VDS4Gamepad()
sleep(1)
while True:
    controller.right_joystick_float(-0.01,0)
    controller.update()
    sleep(0.1)
    controller.right_joystick_float(0,0)
    controller.update()
    sleep(0.1)
    controller.right_joystick_float(0.01,0)
    controller.update()
    sleep(0.1)
    controller.right_joystick_float(0,0)
    controller.update()
    sleep(1)