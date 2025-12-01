import PyInstaller.__main__
import os
import customtkinter

# Get customtkinter path for add-data
ctk_path = os.path.dirname(customtkinter.__file__)

PyInstaller.__main__.run([
    'main.py',
    '--name=WindowsPortManager',
    '--onefile',
    '--noconsole',
    f'--add-data={ctk_path};customtkinter/',
    '--clean',
    '--uac-admin' # Request admin rights for the EXE itself
])
