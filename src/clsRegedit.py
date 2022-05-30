from win32api import RegOpenKeyEx, RegSetValueEx,RegCloseKey,RegDeleteValue,RegCreateKey
from win32con import KEY_WRITE, HKEY_LOCAL_MACHINE, REG_SZ, KEY_ALL_ACCESS
import os  

"""using the library win32api """


class RegEdit:
    ''' Clase RegEdit agrega un archivo para ejecutarlo al inicio de windows''' 
    def __init__(self):
        self.key_reg = HKEY_LOCAL_MACHINE
        self.sub_key = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
    ''' El metodo addValueKey() necesita permisos de ADMINSTRADOR'''
    def addValueKey(self, appName, value_key, type_data=REG_SZ):
        open_key = RegOpenKeyEx(self.key_reg, self.sub_key, 0, KEY_WRITE)
        RegSetValueEx(open_key, appName, 0, type_data, self.get_path_file(value_key))
        RegCloseKey(open_key)
        print("Clave {} fue creada correctamente".format(appName))
    ''' El metodo delKey() necesita permisos de ADMINSTRADOR'''
    def delKey(self, appname):
        open_key = RegOpenKeyEx(self.key_reg, self.sub_key, 0, KEY_WRITE)
        RegDeleteValue(open_key, appname)
        RegCloseKey(open_key)
        print("Clave {} fue borrada correctamente".format(appname))

    @classmethod
    def get_path_file(cls, nameFile):
        path_relative = ".." + "\\" + nameFile
        path_absolute = os.path.abspath(path_relative)
        return path_absolute


if __name__ == "__main__":
    nombre_app = "Musica Favorita"
    value = "favorito.mp3"
    obj = RegEdit()
    # obj.delKey(nombre_app)
    obj.addValueKey(nombre_app, value)
