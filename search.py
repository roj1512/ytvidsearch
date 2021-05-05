import json
from typing import Union

from component_handler import ComponentHandler
from constants import *
from constants import channel_element_key
from constants import playlist_element_key
from constants import rich_item_key
from constants import shelf_element_key
from constants import video_element_key
from request_handler import RequestHandler


class SearchInternal(RequestHandler, ComponentHandler):
    response = None
    responseSource = []
    resultComponents = []

    def __init__(self, query: str, limit: int, language: str, region: str, searchPreferences: str):
        self.query = query
        self.limit = limit
        self.language = language
        self.region = region
        self.searchPreferences = searchPreferences
        self.continuationKey = None
        self._makeRequest()
        self._parseSource()

    def result(self, mode=ResultMode.dict):
        if mode == ResultMode.json:
            return json.dumps({'result': self.resultComponents}, indent=4)
        elif mode == ResultMode.dict:
            return {'result': self.resultComponents}

    def next(self):
        if self.continuationKey:
            self.response = None
            self.responseSource = None
            self.resultComponents = []
            self._makeRequest()
            self._parseSource()
            self._getComponents(*self.searchMode)
            return True
        else:
            return False

    def _getComponents(self, findVideos: bool, findChannels: bool, findPlaylists: bool) -> None:
        self.resultComponents = []
        for element in self.responseSource:
            if video_element_key in element.keys() and findVideos:
                self.resultComponents.append(self._getVideoComponent(element))
            if channel_element_key in element.keys() and findChannels:
                self.resultComponents.append(
                    self._getChannelComponent(element),
                )
            if playlist_element_key in element.keys() and findPlaylists:
                self.resultComponents.append(
                    self._getPlaylistComponent(element),
                )
            if shelf_element_key in element.keys() and findVideos:
                for shelfElement in self._getShelfComponent(element)['elements']:
                    self.resultComponents.append(
                        self._getVideoComponent(
                            shelfElement, shelf_title=self._getShelfComponent(element)[
                                'title'
                            ],
                        ),
                    )
            if rich_item_key in element.keys() and findVideos:
                richItemElement = self._getValue(
                    element, [rich_item_key, 'content'],
                )
                ''' Initial fallback handling for VideosSearch '''
                if video_element_key in richItemElement.keys():
                    videoComponent = self._getVideoComponent(richItemElement)
                    self.resultComponents.append(videoComponent)
            if len(self.resultComponents) >= self.limit:
                break


class VideosSearch(SearchInternal):
    def __init__(self, query: str, limit: int = 20, language: str = 'en', region: str = 'US'):
        self.searchMode = (True, False, False)
        super().__init__(query, limit, language, region, SearchMode.videos)
        self._getComponents(*self.searchMode)
