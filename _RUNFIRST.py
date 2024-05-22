import shutil
import os
input("Thank's for using Gust's SRNG Macros.\nRunning this will re-initialise EVERYHTHING. Including your configs.\nAre you sure you wanna continue? (CTRL+C, or close this window to stop.): ")
print("Copying default config...")
if not os.path.exists("config/"):
    os.mkdir("config")
for conf in os.listdir("depend/defaultconfigs/"):
    fn = f"_config_{conf.split('.')[0]}.py"
    print(fn)
    shutil.copy("depend/defaultconfigs/" + conf,"config/" + fn)
print("Done.")
input("Press enter to exit: ")