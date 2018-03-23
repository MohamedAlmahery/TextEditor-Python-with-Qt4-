#coding=utf-8

from cx_Freeze import setup, Executable

includes = ["atexit"] 

buildOptions = dict(
    create_shared_zip=False,
    append_script_to_exe=True,
    includes=includes
)

executables = [
    Executable(
        script='TextEditor.py',
        targetName='Text Editor.exe',
        base="Win32GUI" # THIS ONE IS IMPORTANT FOR GUI APPLICATION
    )
]

setup(
    name="Text Editor",
    version="1.0",
    description="",
    options=dict(build_exe=buildOptions),
    executables=executables
)
