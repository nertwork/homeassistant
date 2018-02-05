from requests import get

DOMAIN = 'public_ip'

def setup(hass, config):
    my_ip = get('https://api.ipify.org').text
    hass.states.set('public_ip.Public_IPv4', my_ip)

    return True
