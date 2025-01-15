def run():
    import xbmc
    addon_id = 'plugin.onedrive'
    url = f'plugin://{addon_id}/'
    xbmc.executebuiltin(f'RunPlugin({url}?content_type=images)')
if __name__ == "__main__":
    run()