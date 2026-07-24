import subprocess
import os
import maya.cmds as mc

def install_maya_package(package_name, maya_version, target_directory=None):
    """
    Installs a Python package for Maya using mayapy and pip.

    Args:
        package_name (str): The name of the package to install.
        maya_version (str): The version of Maya (e.g., "2026").
        target_directory (str, optional): The installation directory.
                                          If None, installs to the version-specific site-packages.
    """

    # Locate mayapy based on your operating system
    if os.name == 'nt':  # Windows
        mayapy_path = f"C:\\Program Files\\Autodesk\\Maya{maya_version}\\bin\\mayapy.exe"
    elif os.uname().sysname == 'Darwin':  # macOS
        mayapy_path = f"/Applications/Autodesk/maya{maya_version}/Maya.app/Contents/bin/mayapy"
    else:  # Linux
        mayapy_path = f"/usr/autodesk/Maya{maya_version}/bin/mayapy"

    # Check if mayapy exists
    if not os.path.exists(mayapy_path):
        print(f"Error: mayapy not found at {mayapy_path}. Please check your Maya installation path and version.")
        return

    # Construct the pip install command
    command = [mayapy_path, "-m", "pip", "install", package_name]

    if target_directory:
        command.extend(["--target", target_directory])
    else:
        # Install to the version-specific site-packages by default
        if os.name == 'nt':  # Windows
            command.extend(["--target", f"C:\\Users\\{os.getlogin()}\\Documents\\maya\\{maya_version}\\scripts\\site-packages"]) #
        elif os.uname().sysname == 'Darwin':  # macOS
            command.extend(["--target", f"$HOME/Library/Preferences/Autodesk/maya/{maya_version}/scripts/site-packages"]) #
        else:  # Linux
            command.extend(["--target", f"$HOME/maya/{maya_version}/scripts/site-packages"]) #


    try:
        print(f"Installing {package_name} for Maya {maya_version}...")
        subprocess.run(command, check=True)
        print(f"{package_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")

if __name__ == "__main__":
    package_to_install = "numpy"  # Replace with the desired package name
    maya_version = mc.about(v=True)
    install_maya_package(package_to_install, maya_version)
    
    package_to_install = "sympy"  # Replace with the desired package name
    maya_version = mc.about(v=True)
    install_maya_package(package_to_install, maya_version)

    # You can also specify a custom target directory if needed:
    # install_maya_package("requests", maya_version="2026", target_directory="/path/to/my/custom/packages")
