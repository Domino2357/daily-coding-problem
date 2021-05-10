"""
This question was asked by Facebook.

You run an e-commerce website and want to record the last N order ids in a log.
 Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""


class OrderRecorder:
    def __init__(self, maximal_number_of_orders):
        self.orders = []
        self.maximal_number_of_orders = maximal_number_of_orders

    def record(self, order_id):
        if len(order_id) < self.maximal_number_of_orders:
            self.orders.append(order_id)
        else:
            # queue in the next item in FIFO order
            del self.orders[0]
            self.orders.append(order_id)

    def get_last(self, i):
        if i <= self.maximal_number_of_orders:
            return self.orders[-(i - 1)]
