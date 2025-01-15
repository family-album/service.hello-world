def run():
    import xbmc
    import xbmcgui

    # Create a dialog window with "Hello, World!" message
    dialog = xbmcgui.Dialog()
    dialog.ok("Hello, World!", "Hello, World!")

    # Run the OneDrive addon and navigate to the images section
    url = 'plugin://plugin.onedrive/?content_type=image&action=_list_drive&drive_id=759B0A50C8ABEB97'
    xbmc.executebuiltin(f'RunPlugin("{url}")')

if __name__ == "__main__":
    run()