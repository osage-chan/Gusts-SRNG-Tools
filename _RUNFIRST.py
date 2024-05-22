import shutil
input("Thank's for using Gust's SRNG Macros.\nRunning this will re-initialise EVERYHTHING. Including your configs.\nAre you sure you wanna continue? (CTRL+C, or close this window to stop.): ")
print("Copying default config...")
shutil.copy("depend/defaultconfig.py","_config.py")
print("Done.")
input("Press enter to exit: ")