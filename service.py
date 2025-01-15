def run():
    import xbmc
    import xbmcgui

    # Create a dialog window with "Hello World" message
    dialog = xbmcgui.Dialog()
    dialog.ok("Hello World", "Hello World")

    # Ejecutar el addon de imágenes en la sección de imágenes
    xbmc.executebuiltin('RunAddon(plugin.onedrive, content=images)')

if __name__ == "__main__":
    run()