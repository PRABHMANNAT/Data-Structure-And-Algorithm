# Error bounds

For epsilon `e` and failure probability `δ`, the sketch width is `ceil(euler/e)`
and depth is `ceil(log(1/δ))`. A point estimate is at most the true count plus
approximately `e` times all inserted mass with probability `1-δ`.
