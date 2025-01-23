from cx_Freeze import setup, Executable

files = ['assets','databaseProducts.db','pys6_msgBoxes']

exe = Executable(script="app.py", base="win32GUI")

setup(
    name="Inventario PlanetMovil",
    version="5.0",
    description="Inventario y contabilidad",
    author="Diego Martinez",
    author_email='diegomartinez1101@gmail.com',
    options={'build_exe': {'include_files': files}},

    executables=[exe],
    packages=['assets','databaseProducts.db','pys6_msgBoxes']
)

# python setup.py build_exe --zip-include-packages=encodings,PySide6 -----COMANDO PARA CREAR .EXE

# pyinstaller --onefile --add-data "assets;assets" --add-data "pys6_msgBoxes;pys6_msgBoxes" app.py ----COMANDO PARA CREAR .EXE

