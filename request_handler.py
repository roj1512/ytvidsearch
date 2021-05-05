import copy
import json
from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen

from component_handler import ComponentHandler
from constants import content_path
from constants import continuation_content_path
from constants import continuation_item_key
from constants import continuation_key_path
from constants import fallback_content_path
from constants import item_section_key
from constants import request_payload
from constants import search_key
from constants import user_agent


class RequestHandler(ComponentHandler):
    def _makeRequest(self) -> None:
        ''' Fixes #47 '''
        requestBody = copy.deepcopy(request_payload)
        requestBody['query'] = self.query
        requestBody['client'] = {
            'hl': self.language,
            'gl': self.region,
        }
        if self.searchPreferences:
            requestBody['params'] = self.searchPreferences
        if self.continuationKey:
            requestBody['continuation'] = self.continuationKey
        requestBodyBytes = json.dumps(requestBody).encode('utf_8')
        request = Request(
            'https://www.youtube.com/youtubei/v1/search' + '?' + urlencode({
                'key': search_key,
            }),
            data=requestBodyBytes,
            headers={
                'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': len(requestBodyBytes),
                'User-Agent': user_agent,
            },
        )
        try:
            self.response = urlopen(request).read().decode('utf_8')
        except:
            raise Exception('ERROR: Could not make request.')

    def _parseSource(self) -> None:
        try:
            if not self.continuationKey:
                responseContent = self._getValue(
                    json.loads(self.response), content_path,
                )
            else:
                responseContent = self._getValue(
                    json.loads(
                        self.response,
                    ), continuation_content_path,
                )
            if responseContent:
                for element in responseContent:
                    if item_section_key in element.keys():
                        self.responseSource = self._getValue(
                            element, [item_section_key, 'contents'],
                        )
                    if continuation_item_key in element.keys():
                        self.continuationKey = self._getValue(
                            element, continuation_key_path,
                        )
            else:
                self.responseSource = self._getValue(
                    json.loads(self.response), fallback_content_path,
                )
                self.continuationKey = self._getValue(
                    self.responseSource[-1], continuation_key_path,
                )
        except:
            raise Exception('ERROR: Could not parse YouTube response.')
