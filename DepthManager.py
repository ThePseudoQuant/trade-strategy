
import requests
import time

class DepthManager:
    def __init__(self, market):
        self.market = market
        self.bids = {}
        self.asks = {}
        self.poll_market_interval()

    def poll_market_interval(self):
        # This will run the poll_market method every 3 seconds
        while True:
            self.poll_market()
            time.sleep(3)

    def poll_market(self):
        res = requests.get(f'https://public.coindcx.com/market_data/orderbook?pair={self.market}')
        depth = res.json()
        self.bids = depth['bids']
        self.asks = depth['asks']

    def get_relevant_depth(self):
        highest_bid = -100
        lowest_ask = 10000000

        for bid_price in self.bids.keys():
            if float(bid_price) > highest_bid:
                highest_bid = float(bid_price)

        for ask_price in self.asks.keys():
            if float(ask_price) < lowest_ask:
                lowest_ask = float(ask_price)

        return {
            'highest_bid': highest_bid,
            'lowest_ask': lowest_ask
        }

# Example usage:
# depth_manager = DepthManager('BTC/INR')
# depth_manager.poll_market()
# print(depth_manager.get_relevant_depth())
