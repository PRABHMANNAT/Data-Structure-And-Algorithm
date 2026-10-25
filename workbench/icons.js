/** Small line icons; labels live on the surrounding interactive controls. */
const paths={
  search:'M20 20l-5-5 M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0',
  grid:'M3 3h7v7H3z M14 3h7v7h-7z M3 14h7v7H3z M14 14h7v7h-7z',
  bookmark:'M6 3h12v18l-6-4-6 4z',
  star:'m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2-5.6-3-5.6 3 1.1-6.2L3 9.6l6.2-.9z',
  arrow:'M5 12h14 M13 6l6 6-6 6',
  chevron:'m6 9 6 6 6-6',
  close:'m6 6 12 12 M18 6 6 18',
  code:'m8 6-6 6 6 6 M16 6l6 6-6 6 M14 3l-4 18',
};
export function icon(name) {
  const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
  for(const [key,value] of Object.entries({viewBox:'0 0 24 24',width:18,height:18,fill:'none',stroke:'currentColor','stroke-width':1.6,'stroke-linecap':'round','stroke-linejoin':'round','aria-hidden':'true',focusable:'false'}))svg.setAttribute(key,String(value));
  const path=document.createElementNS(svg.namespaceURI,'path');path.setAttribute('d',paths[name]||paths.arrow);svg.append(path);return svg;
}
