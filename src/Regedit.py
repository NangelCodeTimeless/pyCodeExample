import winreg as reg
"""Using the library winreg"""


class Regedit:
    key = reg.HKEY_LOCAL_MACHINE
    sub_key = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"

    @classmethod
    def Run_Begin_Windows(cls, name_key, path_file):
        hkey = reg.OpenKey(cls.key, cls.sub_key, 0, access=reg.KEY_WRITE)
        reg.SetValueEx(hkey, name_key, 0, reg.REG_SZ, path_file)
        reg.CloseKey(hkey)
        print("Se agrego correctamente....")


    @classmethod
    def del_key(cls):
        pass


if __name__ == "__main__":
    path = "C:\\Users\\Nahum\\Desktop\\Riley.mp3"
    Regedit.Run_Begin_Windows("Favorito", path)





