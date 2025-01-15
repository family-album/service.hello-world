def run():
    import xbmc
    import xbmcgui
    url = f'plugin://plugin.onedrive/?content_type=image'
    xbmc.executebuiltin(f'RunPlugin("{url}")')

if __name__ == "__main__":
    run()