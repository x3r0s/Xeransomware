from cx_Freeze import setup, Executable
import sys

# exclude unneeded packages. More could be added. Has to be changed for
# other programs.
build_exe_options = {"excludes": ["tkinter", "PyQt4.QtSql", "sqlite3", 
                                  "scipy.lib.lapack.flapack",
                                  "PyQt4.QtNetwork",
                                  "PyQt4.QtScript",
                                  "numpy.core._dotblas", 
                                  "PyQt5"],
                     "optimize": 2}

# Information about the program and build command. Has to be adjusted for
# other programs
setup(
    name="XLocker",                           # Name of the program
    version="0.1",                              # Version number
    description="@Vanxis",                # Description
    options = {"build_exe": build_exe_options}, # <-- the missing line
    executables=[Executable("XLocker.py",     # Executable python file
                            base = ("Win32GUI" if sys.platform == "win32" 
                            else None))],
)