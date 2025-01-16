import xbmcgui
import debugpy
dialog = xbmcgui.Dialog()
try:
    debugpy.connect(5678)
    dialog.ok("debugpy", "Ok.")
except:
    dialog.ok("debugpy", "Ko.")
    pass
import xbmc
url = 'plugin://plugin.onedrive/'
xbmc.executebuiltin('ActivateWindow(Pictures)')
xbmc.executebuiltin(f'Container.Update({url})')