### Elegance Orange

Elegance Orange is an static orange Gnome Shell theme based off of the outdated theme Elegance Colors. This theme contains bug fixes, minor changes, and commits to bring it compatibility with the most recent version of Gnome Shell. 

### Requirements

GTK+ 3.14

Gnome Shell 3.12+

Roboto Medium Font (should faltback to default if not present)

Python 3.0+ (Only for automated installation)

###Installation

Clone the repository in a temporary directory:
```
git clone https://github.com/nosduco/elegance-orange.git
```
Change into the directory:
```
cd elegance-orange
```
Run automated python installer:
(If you wish to install manually, follow the method beyond this section.)
```
python install.py    
```
Theme will now be installed into your 'gnome-shell' themes directory.

To set the theme, choose the theme via the Gnome Tweak Tool, or run the following command:
```
gsettings set org.gnome.shell.extensions.user-theme name 'elegance-orange'
```

###Manual Installation


Clone the repository in a temporary directory:
```
git clone https://github.com/nosduco/elegance-orange.git
```
Change into the directory:
```
cd elegance-orange
```
Two methods exist beyond this point:

####Method One

Create a zip and load the zip from Gnome Tweak Tool.

Zip the file either using a file explorer or the command below:
```
zip -r elegance-orange.zip elegance-orange

```

Open Gnome Tweak Tool, navigate to Appearance, and under the "Shell theme" line select to open a theme/zip and choose the zip in the current directory.

Proceed to then select it from the drop down menu.

####Method Two

Copy all the files to the theme directory manually.

(Will add later)

### Bugs, Fixes, and Suggestions

Please submit [here](https://github.com/nosduco/elegance-orange/issues).
