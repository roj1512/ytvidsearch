export const requestPayload = {
  context: {
    client: {
      clientName: "WEB",
      clientVersion: "2.20210224.06.00",
      newVisitorCookie: true,
    },
    user: {
      lockedSafetyMode: false,
    },
  },
};

export const userAgent =
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36";

export const video = "videoRenderer";
export const channel = "channelRenderer";
export const playlist = "playlistRenderer";
export const shelf = "shelfRenderer";
export const itemSection = "itemSectionRenderer";
export const continuationItem = "continuationItemRenderer";
export const playerResponse = "playerResponse";
export const richItem = "richItemRenderer";

export const searchKey = "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8";

export const contentPath = [
  "contents",
  "twoColumnSearchResultsRenderer",
  "primaryContents",
  "sectionListRenderer",
  "contents",
];

export const fallbackContentPath = [
  "contents",
  "twoColumnSearchResultsRenderer",
  "primaryContents",
  "richGridRenderer",
  "contents",
];

export const continuationContentPath = [
  "onResponseReceivedCommands",
  0,
  "appendContinuationItemsAction",
  "continuationItems",
];

export const continuationKeyPath = [
  "continuationItemRenderer",
  "continuationEndpoint",
  "continuationCommand",
  "token",
];

export const playlistInfoPath = [
  "response",
  "sidebar",
  "playlistSidebarRenderer",
  "items",
];

export const playlistVideosPath = [
  "response",
  "contents",
  "twoColumnBrowseResultsRenderer",
  "tabs",
  0,
  "tabRenderer",
  "content",
  "sectionListRenderer",
  "contents",
  0,
  "itemSectionRenderer",
  "contents",
  0,
  "playlistVideoListRenderer",
  "contents",
];

export const playlistPrimaryInfo = "playlistSidebarPrimaryInfoRenderer";
export const playlistSecondaryInfo = "playlistSidebarSecondaryInfoRenderer";
export const playlistVideo = "playlistVideoRenderer";

export class ResultMode {
  json = 0;
  dict = 1;
}

export class SearchMode {
  videos = "EgIQAQ%3D%3D";
  channels = "EgIQAg%3D%3D";
  playlists = "EgIQAw%3D%3D";
}

export class VideoUploadDateFilter {
  lastHour = "EgQIARAB";
  today = "EgQIAhAB";
  thisWeek = "EgQIAxAB";
  thisMonth = "EgQIBBAB";
  thisYear = "EgQIBRAB";
}

export class VideoDurationFilter {
  short = "EgQQARgB";
  long = "EgQQARgC";
}

export class VideoSortOrder {
  relevance = "CAASAhAB";
  uploadDate = "CAISAhAB";
  viewCount = "CAMSAhAB";
  rating = "CAESAhAB";
}
