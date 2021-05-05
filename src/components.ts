import { getValue } from "./helpers";
import { video } from "./constants";
import { keyable } from "./interfaces";

export const getVideoComponent = (element: any): keyable => {
  const _video = element[video];
  const component = {
    _: video,
    id: getValue(_video, ["videoId"]),
    title: getValue(_video, ["title", "runs", 0, "text"]),
    publishedTime: getValue(_video, ["publishedTimeText", "simpleText"]),
    duration: getValue(_video, ["lengthText", "simpleText"]),
    viewCount: {
      text: getValue(_video, ["viewCountText", "simpleText"]),
      short: getValue(_video, ["shortViewCountText", "simpleText"]),
    },
    thumbnails: getValue(_video, ["thumbnail", "thumbnails"]),
    richThumbnail: getValue(_video, [
      "richThumbnail",
      "movingThumbnailRenderer",
    ]),
    descriptionSnippet: getValue(_video, ["descriptionSnippet", "runs"]),
    channel: {
      name: getValue(_video, ["ownerText", "runs", 0, "text"]),
      id: getValue(_video, [
        "ownerText",
        "runs",
        0,
        "navigationEndpoint",
        "browserEndpoint",
        "browseId",
      ]),
      thumbnails: getValue(_video, [
        "channelThumbnailSupportedRenderers",
        "channelThumbnailWithLinkRenderer",
        "thumbnail",
        "thumbnails",
      ]),
      accessibility: {
        title: getValue(_video, [
          "title",
          "accessibility",
          "accessibilityData",
          "label",
        ]),
        duration: getValue(_video, [
          "lengthText",
          "accessibility",
          "accessibilityData",
          "label",
        ]),
      },
    },
  };

  component["url"] = `https://youtu.be/${component.id}`;
  component.channel[
    "url"
  ] = `https://www.youtube.com/channel/${component.channel.id}`;

  return component;
};
