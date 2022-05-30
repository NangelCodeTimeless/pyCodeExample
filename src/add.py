import os
from winreg import ConnectRegistry, OpenKey, QueryValueEx, KEY_ALL_ACCESS, REG_EXPAND_SZ, SetValueEx, CloseKey, \
  HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER

import win32con
import win32gui


def AppendWindowsPath(path):
  def AddPathInRegistry(HKEY, reg_path, new_path):
    reg = None
    key = None
    try:
      reg = ConnectRegistry(None, HKEY)
      key = OpenKey(reg, reg_path, 0, KEY_ALL_ACCESS)
      path_string, type_id = QueryValueEx(key, 'PATH')
      path_list = [f.strip("\r\n") for f in  path_string.split(';') if f]

      if new_path in path_list:
        print(new_path + " is already in %PATH%")
        return "ALREADY_IN_ENVIRONMENT"

      print("Adding " + new_path + " to %PATH%")
      SetValueEx(key, 'PATH', 0, REG_EXPAND_SZ, path_string + ";" + new_path)
      return "UPDATED_PATH"
    except Exception as e:
      print("ERROR while executing registry edit with " + str(HKEY) + "/" + reg_path)
      return "ERROR"
    finally:
      if key: CloseKey(key)
      if reg: CloseKey(reg)


  # Add the path to the current machine
  result_machine = \
    AddPathInRegistry(HKEY_LOCAL_MACHINE,
                      r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
                      path)

  # Update the path for the current user.
  result_user = \
    AddPathInRegistry(HKEY_CURRENT_USER, r'Environment', path)

  if ("UPDATED_PATH" in result_machine) or ("UPDATED_PATH" in result_user):
    # Updates Environment.
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment') (os.environ["PATH"])


AppendWindowsPath(r'c:\Users\Nahum')