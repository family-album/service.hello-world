def run():
    import xbmc
    #url = 'plugin://plugin.onedrive/?content_type=image'
    url = 'http://localhost:8586/source/OneDrive/'
    xbmc.executebuiltin('ActivateWindow(Pictures)')
    xbmc.executebuiltin(f'Container.Update({url})')

if __name__ == "__main__":
    run()