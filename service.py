def run():
    import xbmc
    import xbmcgui

    # Create a dialog window with "Hello World" message
    dialog = xbmcgui.Dialog()
    dialog.ok("Hello World", "Hello World")

if __name__ == "__main__":
    run()