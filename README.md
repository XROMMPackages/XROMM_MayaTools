# README #

XROMM_MayaTools are a set of maya-embedded-language (.mel) and python scripts along with a Maya shelf toolbar for XROMM workflow processes. David Baier, Professor of Biology at Providence College is the primary developer, with substantial contributions from Steve Gatesy and Armita Manafzedeh who should be acknowledged in all publications using XROMM MayaTools. Inertial axes and center of mass calculations were adopted from Matlab scripts from Joseph J. Crisco's lab. Please see xromm.py script header for citations if you use these tools. 


XROMM_MayaTools are used to calculate marker centroids from CTscans, animate XROMM data, import X-ray camera reconstructions, create joint coordinate systems, export XROMM data, and aid in analyzing XROMM data. See also https://github.com/XROMMPackages/xromm_other_mel_scripts for a collection of additional XROMM tools by various developers.
***
# Download [XROMM_MayaTools_2.2.5](https://github.com/XROMMPackages/xromm_mayatools/releases/) #
***
# Installation of MEL scripts and XROMM Shelf #

Download the zip folder, unzip and place the XROMM_MayaTools_2.2.5 folder in a storage location of your choosing.

Open maya, click the gear icon next to the shelves, and select load shelf

Navigate to the location that you saved the files and select shelf_XROMM_tools_2.2.6.mel

Click the setpath button on the newly loaded shelf

Add path to both MAYA_SCRIPT_PATHS and PYTHONPATH.
Choose the "scripts" directory from the XROMM_MayaTools_2.2.6 Folder

# Installation for versions 2.2.3 and older #
CLOSE MAYA BEFORE INSTALLATION

## Windows ##
Move shelf_XROMM_tools.mel to the following directory: 

* C:\Users\<Username>\Documents\maya\scripts

## MacOS ##

Move the .mel files from the XROMM scripts folder into the following directory: 

*/Users/<Username>/Library/Preferences/Autodesk/maya/scripts

 
***
***
**XROMM_MayaTools development is supported by the US National Science Foundation through an Advances in Biological Informatics grant to PI Elizabeth Brainerd and CoPIs Stephen Gatesy and David Baier.**
