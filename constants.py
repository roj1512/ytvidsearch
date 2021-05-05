request_payload = {
    'context': {
        'client': {
            'clientName': 'WEB',
            'clientVersion': '2.20210224.06.00',
            'newVisitorCookie': True,
        },
        'user': {
            'lockedSafetyMode': False,
        },
    },
}
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'


video_element_key = 'videoRenderer'
channel_element_key = 'channelRenderer'
playlist_element_key = 'playlistRenderer'
shelf_element_key = 'shelfRenderer'
item_section_key = 'itemSectionRenderer'
continuation_item_key = 'continuationItemRenderer'
player_response_key = 'playerResponse'
rich_item_key = 'richItemRenderer'
search_key = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
content_path = [
    'contents', 'twoColumnSearchResultsRenderer',
    'primaryContents', 'sectionListRenderer', 'contents',
]
fallback_content_path = [
    'contents', 'twoColumnSearchResultsRenderer',
    'primaryContents', 'richGridRenderer', 'contents',
]
continuation_content_path = [
    'onResponseReceivedCommands',
    0, 'appendContinuationItemsAction', 'continuationItems',
]
continuation_key_path = [
    'continuationItemRenderer',
    'continuationEndpoint', 'continuationCommand', 'token',
]
playlist_info_path = [
    'response', 'sidebar',
    'playlistSidebarRenderer', 'items',
]
playlist_videos_path = [
    'response', 'contents', 'twoColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content',
    'sectionListRenderer', 'contents', 0, 'itemSectionRenderer', 'contents', 0, 'playlistVideoListRenderer', 'contents',
]
playlist_primary_info_key = 'playlistSidebarPrimaryInfoRenderer'
playlist_secondary_info_key = 'playlistSidebarSecondaryInfoRenderer'
playlist_video_key = 'playlistVideoRenderer'


class ResultMode:
    json = 0
    dict = 1


class SearchMode:
    videos = 'EgIQAQ%3D%3D'
    channels = 'EgIQAg%3D%3D'
    playlists = 'EgIQAw%3D%3D'


class VideoUploadDateFilter:
    lastHour = 'EgQIARAB'
    today = 'EgQIAhAB'
    thisWeek = 'EgQIAxAB'
    thisMonth = 'EgQIBBAB'
    thisYear = 'EgQIBRAB'


class VideoDurationFilter:
    short = 'EgQQARgB'
    long = 'EgQQARgC'


class VideoSortOrder:
    relevance = 'CAASAhAB'
    uploadDate = 'CAISAhAB'
    viewCount = 'CAMSAhAB'
    rating = 'CAESAhAB'
