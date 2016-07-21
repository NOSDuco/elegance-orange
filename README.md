### Elegance Orange

Elegance Orange is an static orange Gnome Shell theme based off of the outdated theme Elegance Colors. This theme contains bug fixes, minor changes, and commits to bring it compatibility with the most recent version of Gnome Shell. 

### Requirements

GTK+ 3.14

Gnome Shell 3.12+

Roboto Medium Font (should faltback to default if not present)

Python 3.0 (Only for automated installation)

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
```
python install.py    
```
Theme will now be installed into your 'gnome-shell' themes directory.

To set the theme, choose the theme via the Gnome Tweak Tool, or run the following command:
```
gsettings set org.gnome.shell.extensions.user-theme name 'elegance-orange'
```
### Bugs, Fixes, and Suggestions

Please submit [here](https://github.com/nosduco/elegance-orange/issues).
