import unittest
from transit_simulator.simulator import Simulator
class SimulatorTests(unittest.TestCase):
 def test_advances_clock_and_counts_processed_events(self):
  sim=Simulator();sim.schedule(3,"arrival","x");seen=[];sim.run_until(5,lambda e:seen.append(e.payload))
  self.assertEqual((seen,sim.clock,sim.metrics.summary()["event_arrival"]),(["x"],5,1))
 def test_advances_time_without_events(self):
  sim=Simulator();sim.run_until(8,lambda event:None);self.assertEqual(sim.clock,8)
