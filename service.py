def run():
    import xbmc
    import xbmcgui
    # Run the OneDrive addon and navigate to the images section
    url = 'plugin://plugin.onedrive/?content_type=image'
    xbmc.executebuiltin(f'Container.Update({url})')
if __name__ == "__main__":
    run()