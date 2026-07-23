# README #

XROMM_MayaTools are a set of maya-embedded-language (.mel) and python scripts along with a Maya shelf toolbar for XROMM workflow processes. David Baier, Professor of Biology at Providence College is the primary developer, with substantial contributions from Steve Gatesy and Armita Manafzadeh. All three should be acknowledged in all publications using XROMM MayaTools. Inertial axes and center of mass calculations were adopted from Matlab scripts from Joseph J. Crisco's lab. Please see * [INRTAxes wiki page](https://github.com/XROMMPackages/xromm_mayatools/wiki/INRTAxes) for citations if you use INRTAxes or CoM tools. 

XROMM_MayaTools are used to calculate marker centroids from CTscans, animate XROMM data, import X-ray camera reconstructions, create joint coordinate systems and export XROMM data.
***
# Download [XROMM_MayaTools_v2.2.6.zip](https://github.com/user-attachments/files/30157275/XROMM_MayaTools_v2.2.6.zip) #
***
# Installation of MEL scripts and XROMM Shelf #

Download the zip folder, unzip and place the XROMM_MayaTools_v2.2.6 folder in a storage location of your choosing.

Open maya, click the gear icon next to the shelves, and select load shelf

Navigate to the location that you saved the files and select shelf_XROMM_tools_v2.2.6.mel

Click the setpath button on the newly loaded shelf

Choose the "scripts" directory from the XROMM_MayaTools_v2.2.6 Folder

You should see a Set Path window that shows your chosen path in the user defined MAYA_SCRIPT_PATHS as well as lists of locations where maya looks for 


# Installation for versions 2.2.3 and older #
CLOSE MAYA BEFORE INSTALLATION

## Windows10 ##
Move shelf_XROMM_tools.mel to the following directory: 

* My_Documents\maya\mayaVersion(e.g. 2017)\prefs\shelves

Move the .mel files from the XROMM scripts folder into the following directory: 

* My_Documents\maya\scripts

as above, move the scripts, not the folder
 

## Mac OS X ##
Move shelf_XROMM_tools.mel to the following directory: 

* Macintosh HD/Users/Your_User_Account/Library/Preferences/Autodesk/maya/mayaVersion(e.g. 2012)/prefs/shelves
* if the Library is not visible, click the gear icon and select show libraries.

Move the .mel files from the XROMM scripts folder into the following directory: 

* Macintosh HD/Users/User_Account/Library/Preferences/Autodesk/maya/mayaVersion(e.g. 2012)/scripts

MOVE THE SCRIPTS NOT THE FOLDER. Maya does not look in the subfolders of this directory.
***
***
**XROMM_MayaTools development is supported by the US National Science Foundation through an Advances in Biological Informatics grant to PI Elizabeth Brainerd and CoPIs Stephen Gatesy and David Baier.**
