# main.py
from ota import OTAUpdater


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/brendandburns/micropython-ota')
    # We're already connected so no need to pass the real passwords
    ota_updater.download_and_install_update_if_available('wifi-ssid', 'wifi-password')


def start():
    from main.app import run
    run()

def boot():
    download_and_install_update_if_available()
    start()


boot()