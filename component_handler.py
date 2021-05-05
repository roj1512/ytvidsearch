from constants import channel_element_key
from constants import playlist_element_key
from constants import shelf_element_key
from constants import video_element_key


class ComponentHandler:
    def _getVideoComponent(self, element, shelf_title=None):
        video = element[video_element_key]
        component = {
            'type':                           'video',
            'id':                              self._getValue(video, ['videoId']),
            'title':                           self._getValue(video, ['title', 'runs', 0, 'text']),
            'publishedTime':                   self._getValue(video, ['publishedTimeText', 'simpleText']),
            'duration':                        self._getValue(video, ['lengthText', 'simpleText']),
            'viewCount': {
                'text':                        self._getValue(video, ['viewCountText', 'simpleText']),
                'short':                       self._getValue(video, ['shortViewCountText', 'simpleText']),
            },
            'thumbnails':                      self._getValue(video, ['thumbnail', 'thumbnails']),
            'richThumbnail':                   self._getValue(video, ['richThumbnail', 'movingThumbnailRenderer', 'movingThumbnailDetails', 'thumbnails', 0]),
            'descriptionSnippet':              self._getValue(video, ['descriptionSnippet', 'runs']),
            'channel': {
                'name':                        self._getValue(video, ['ownerText', 'runs', 0, 'text']),
                'id':                          self._getValue(video, ['ownerText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
                'thumbnails':                  self._getValue(video, ['channelThumbnailSupportedRenderers', 'channelThumbnailWithLinkRenderer', 'thumbnail', 'thumbnails']),
            },
            'accessibility': {
                'title':                       self._getValue(video, ['title', 'accessibility', 'accessibilityData', 'label']),
                'duration':                    self._getValue(video, ['lengthText', 'accessibility', 'accessibilityData', 'label']),
            },
        }
        component['link'] = 'https://www.youtube.com/watch?v=' + \
            component['id']
        component['channel']['link'] = 'https://www.youtube.com/channel/' + \
            component['channel']['id']
        component['shelfTitle'] = shelf_title
        return component

    def _getChannelComponent(self, element: dict) -> dict:
        channel = element[channel_element_key]
        component = {
            'type':                           'channel',
            'id':                              self._getValue(channel, ['channelId']),
            'title':                           self._getValue(channel, ['title', 'simpleText']),
            'thumbnails':                      self._getValue(channel, ['thumbnail', 'thumbnails']),
            'videoCount':                      self._getValue(channel, ['videoCountText', 'runs', 0, 'text']),
            'descriptionSnippet':              self._getValue(channel, ['descriptionSnippet', 'runs']),
            'subscribers':                     self._getValue(channel, ['subscriberCountText', 'simpleText']),
        }
        component['link'] = 'https://www.youtube.com/channel/' + \
            component['id']
        return component

    def _getPlaylistComponent(self, element: dict) -> dict:
        playlist = element[playlist_element_key]
        component = {
            'type':                           'playlist',
            'id':                             self._getValue(playlist, ['playlistId']),
            'title':                          self._getValue(playlist, ['title', 'simpleText']),
            'videoCount':                     self._getValue(playlist, ['videoCount']),
            'channel': {
                'name':                       self._getValue(playlist, ['shortBylineText', 'runs', 0, 'text']),
                'id':                         self._getValue(playlist, ['shortBylineText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
            },
            'thumbnails':                     self._getValue(playlist, ['thumbnailRenderer', 'playlistVideoThumbnailRenderer', 'thumbnail', 'thumbnails']),
        }
        component['link'] = 'https://www.youtube.com/playlist?list=' + \
            component['id']
        component['channel']['link'] = 'https://www.youtube.com/channel/' + \
            component['channel']['id']
        return component

    def _getShelfComponent(self, element: dict) -> dict:
        shelf = element[shelf_element_key]
        return {
            'title':                           self._getValue(shelf, ['title', 'simpleText']),
            'elements':                        self._getValue(shelf, ['content', 'verticalListRenderer', 'items']),
        }

    def _getValue(self, source: dict, path):
        value = source
        for key in path:
            if type(key) is str:
                if key in value.keys():
                    value = value[key]
                else:
                    value = None
                    break
            elif type(key) is int:
                if len(value) != 0:
                    value = value[key]
                else:
                    value = None
                    break
        return value
