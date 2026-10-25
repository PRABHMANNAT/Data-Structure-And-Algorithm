import {el, note, button, download} from '/workbench/dom.js';
import {metrics, table, sequence} from '/workbench/results.js';
import {bars, graph, bits} from '/workbench/charts.js';

export function render(host,data) {
  host.append(metrics([['Accepted',data.stats.accepted],['Late / rejected',data.stats.rejected_late],['Watermark',data.stats.watermark],['Window total',data.total]]));
  host.append(bars(data.timeline.map(row=>row.total),data.timeline.map(row=>row.timestamp)));
  host.append(table(['Key','Event time','Status','Watermark','Window total'],data.timeline.map(row=>[row.key,row.timestamp,row.accepted?'Accepted':'Late',row.watermark,row.total])));
  host.append(el('h3',{},'Heavy hitters'),table(['Key','Estimated count'],data.leaders));
  host.append(note('The chart shows the exact rolling value total after each event. Heavy hitters estimate cumulative accepted event counts, not the current window. Rejected late events do not change either total.'));
}
