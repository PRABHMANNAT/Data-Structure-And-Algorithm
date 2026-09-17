import unittest
from advanced_delivery_network.delivery_network.errors import DeliveryNetworkError, UnknownStopError
class ErrorTests(unittest.TestCase):
    def test_specific_errors_are_domain_errors(self):
        self.assertTrue(issubclass(UnknownStopError, DeliveryNetworkError))
if __name__ == "__main__": unittest.main()
