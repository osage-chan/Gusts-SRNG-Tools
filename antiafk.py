import vgamepad
from time import sleep

controller = vgamepad.VDS4Gamepad()
sleep(1)
print("Anti AFKing")
while True:
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
    sleep(2)