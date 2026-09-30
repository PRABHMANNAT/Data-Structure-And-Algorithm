export const $ = selector => document.querySelector(selector);
export const announcement = message => { $("#announcement").textContent=message; };
export const inputFor = key => document.querySelector(`[data-key="${key}"]`);
