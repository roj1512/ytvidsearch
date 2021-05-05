import { keyable } from "./interfaces";

export const getValue = (source: keyable, path: Array<string | number>) => {
  let value = source;
  let key;

  for (let i in path) {
    key = path[i];
    if (typeof key === "string") {
      if (key in value) {
        value = value[key];
      } else {
        value = null;
        break;
      }
    } else if (typeof key === "number") {
      if (value.length !== 0) {
        value = value[key];
      } else {
        value = null;
        break;
      }
    }
  }

  return value;
};
