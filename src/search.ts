import { encode } from "querystring";
import fetch from "node-fetch";
import { requestPayload, userAgent, searchKey } from "./constants";

export const search = async (query) => {
  const body = JSON.stringify({
    ...requestPayload,
    query: query,
    client: { hl: "en", gl: "us" },
  });
  const response = await fetch(
    `https://www.youtube.com/youtubei/v1/search?${encode({ key: searchKey })}`,
    {
      headers: {
        "Content-Type": "application/json; charset=utf-8",
        "Content-Length": body.length.toString(),
        "User-Agent": userAgent,
      },
      body: body,
      method: "POST",
    }
  );
  return await response.json();
};
