from os.path import expanduser, exists
from os import makedirs, getcwd
from distutils.dir_util import copy_tree

HOME_DIR = expanduser("~")
THEME_DIR = HOME_DIR + "/.themes/"
THEME_NAME = "elegance-orange"
INSTALL_DIR = THEME_DIR + THEME_NAME

if not exists(INSTALL_DIR):
    makedirs(INSTALL_DIR)
    
print("Copying files...")
try:
    copy_tree(getcwd() + "/" + THEME_NAME, INSTALL_DIR)
    print("Theme installed!")
except OSError as exc:
    print("Failed to install theme!")
