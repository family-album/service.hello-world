def run():
    import xbmc
    import xbmcgui

    # Create a dialog window with "Hello, World!" message
    dialog = xbmcgui.Dialog()
    dialog.ok("Hello, World!", "Hello, World!")

    # Run the OneDrive addon and navigate to the images section
    url = 'plugin://plugin.onedrive/?content_type=image'
    xbmc.executebuiltin('ActivateWindow(Pictures)')
    xbmc.executebuiltin(f'Container.Update({url})')

if __name__ == "__main__":
    run()