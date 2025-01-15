def run():
    import xbmc
    xbmc.executebuiltin('ActivateWindow(Pictures)')
    xbmc.executebuiltin(f'Container.Update({url})')
if __name__ == "__main__":
    run()