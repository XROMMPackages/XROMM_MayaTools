# README #

XROMM_MayaTools are a set of maya-embedded-language (.mel) and python scripts along with a Maya shelf toolbar for XROMM workflow processes. David Baier, Professor of Biology at Providence College is the primary developer, with substantial contributions from Steve Gatesy and Armita Manafzedeh who should be acknowledged in all publications using XROMM MayaTools. The inertialAxes tool is modified from Matlab scripts that were developed and generously shared by Joseph Crisco and others. If you use the INRTAxes, please cite Joseph J. Crisco, James C. Coburn, Douglas C. Moore, Mohammad A. Upal,2005, Carpal bone size and scaling in men versus in women, The Journal of Hand Surgery, 30(1)35-42 and D. C. Moore; J. J. Crisco; T. G. Trafton; E. L. Leventhal, 2007, A digital database of wrist bone anatomy and carpal kinematics, Journal of Biomechanics 40(11):2537-2542 and references therein (Eberly et al., 1991; Gonzalez-Ochoa et al., 1998; Messner and Taylor, 1980)


XROMM_MayaTools are used to calculate marker centroids from CTscans, animate XROMM data, import X-ray camera reconstructions, create joint coordinate systems, export XROMM data, and aid in analyzing XROMM data. See also https://github.com/XROMMPackages/xromm_other_mel_scripts for a collection of additional XROMM tools by various developers.
***
# Download [XROMM_MayaTools_2.2.5](https://github.com/XROMMPackages/xromm_mayatools/releases/) #
***
# Installation of MEL scripts and XROMM Shelf #
v. 2.2.5 has a new installation method

Download the zip folder, unzip and place the XROMM_MayaTools_2.2.5 folder in a storage location of your choosing.

Open maya, click the gear icon next to the shelves, and select load shelf

Navigate to the location that you saved the files and select shelf_XROMM_tools_2_2_5.mel

Click the setpath button on the newly loaded shelf

Choose the "scripts" directory from the XROMM_MayaTools_2.2.5 Folder

You should see a Set Path window that shows your chosen path in the user defined MAYA_SCRIPT_PATHS as well as lists of locations where maya looks for 


# Installation for versions 2.2.3 and older #
CLOSE MAYA BEFORE INSTALLATION

## Windows10 ##
Move shelf_XROMM_tools.mel to the following directory: 

* My_Documents\maya\mayaVersion(e.g. 2017)\prefs\shelves

Move the .mel files from the XROMM scripts folder into the following directory: 

* My_Documents\maya\scripts

as above, move the scripts, not the folder
 
## Windows XP ##
Move shelf_XROMM_tools.mel to the following directory: 

* C:\Documents and Settings\User_Account\My Documents\maya\mayaVersion(e.g. 2012)\prefs\shelves

Move the .mel files from the XROMM scripts folder into the following directory: 

* C:\Documents and Settings\User_Account\My Documents\maya\scripts

MOVE THE SCRIPTS NOT THE FOLDER. Maya does not look in the subfolders of this directory.

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
