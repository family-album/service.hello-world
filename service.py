def run():
    import xbmc
    import xbmcgui
    url = 'plugin://plugin.onedrive/?content_type=image'
    xbmc.executebuiltin(f'ActivateWindow(Videos,{url})')

if __name__ == "__main__":
    run()