def run():
    import xbmc
    url = 'plugin://plugin.onedrive/?content_type=image'
    xbmc.executebuiltin('ActivateWindow(Pictures)')
    xbmc.executebuiltin(f'Container.Update({url})')

if __name__ == "__main__":
    run()