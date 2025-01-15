def run():
    import xbmc
    import xbmcgui

    # Create a dialog window with "Hello, World!" message
    dialog = xbmcgui.Dialog()
    dialog.ok("Hello, World!", "Hello, World!")

    # Run the OneDrive addon and navigate to the images section
    addon_id = 'plugin.onedrive'
    url = f'plugin://{addon_id}/?action=images'
    xbmc.executebuiltin(f'RunPlugin({url})')

if __name__ == "__main__":
    run()