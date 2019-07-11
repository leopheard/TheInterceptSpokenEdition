from xbmcswift2 import Plugin, xbmcgui
from resources.lib import theinterceptspokenedition

plugin = Plugin()

URL0 = "http://api.spokenlayer.com/feed/channel/v1-intercept-news2-ext/3c9929b72538c12bd92ac6762f8d798b9d4e8cdca7692ea74f466061d01816cb"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(20000), 
            'path': plugin.url_for('spoken_edition'),
            'thumbnail': "http://media.spokenlayer.com/cover-art/2016/10/01/the-intercept-v2-10-1-1400x1400.png"},
        {
            'label': plugin.get_string(20001), 
            'path': plugin.url_for('spoken_edition1'),
            'thumbnail': "http://media.spokenlayer.com/cover-art/2016/10/01/the-intercept-v2-10-1-1400x1400.png"},
    ]

    return items

@plugin.route('/spoken_edition/')
def spoken_edition():
    """
    contains playable podcasts listed as just-in
    """
    soup0 = theinterceptspokenedition.get_soup0(URL0)
    
    playable_podcast0 = theinterceptspokenedition.get_playable_podcast0(soup0)
    
    items = theinterceptspokenedition.compile_playable_podcast0(playable_podcast0)

    return items

@plugin.route('/spoken_edition1/')
def spoken_edition1():
    """
    contains playable podcasts listed as just-in
    """
    soup0 = theinterceptspokenedition.get_soup0(URL0)
    
    playable_podcast01 = theinterceptspokenedition.get_playable_podcast01(soup0)
    
    items = theinterceptspokenedition.compile_playable_podcast01(playable_podcast01)

    return items


if __name__ == '__main__':
    plugin.run()
