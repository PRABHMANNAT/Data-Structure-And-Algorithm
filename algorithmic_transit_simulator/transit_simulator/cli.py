import argparse
from .json_io import load_network
from .router import EarliestArrivalRouter
def main(argv=None):
 parser=argparse.ArgumentParser(description="Plan an earliest-arrival transit journey")
 parser.add_argument("network");parser.add_argument("origin");parser.add_argument("destination");parser.add_argument("departure",type=int)
 args=parser.parse_args(argv);journey=EarliestArrivalRouter(load_network(args.network)).route(args.origin,args.destination,args.departure)
 if not journey: print("No journey found");return 1
 print(f"arrival={journey.arrival} fare={journey.fare} legs={','.join(c.id for c in journey.connections)}");return 0
if __name__=="__main__":raise SystemExit(main())
