import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host,data) {
  const ratio=data.input_bytes?`${(data.archive_bytes/data.input_bytes*100).toFixed(1)}%`:'—';
  host.append(metrics([['Input bytes',data.input_bytes],['Archive bytes',data.archive_bytes],['Size ratio',ratio],['Round trip',data.verified?'Verified':'Failed']]));
  host.append(el('h3',{},'Most frequent bytes'),bars(data.frequencies.map(row=>row[1]),data.frequencies.map(row=>'0x'+row[0].toString(16).padStart(2,'0'))));
  host.append(button('Download .huf archive ↓',()=>{
    const bytes=Uint8Array.from(atob(data.archive),ch=>ch.charCodeAt(0));
    const url=URL.createObjectURL(new Blob([bytes],{type:'application/octet-stream'}));
    const link=el('a',{href:url,download:'fieldnotes.huf'});link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  },'text-button'));
  host.append(el('details',{},el('summary',{},'Inspect decompressed text'),el('pre',{},data.decoded)));
  host.append(note('A ratio above 100% means the archive is larger. Huffman headers can outweigh savings on short inputs. Frequencies are UTF-8 bytes, not characters.'));
}
