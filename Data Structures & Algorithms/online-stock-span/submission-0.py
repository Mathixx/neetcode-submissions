class StockSpanner:

    def __init__(self):
        # Stack stores tuples of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # Check previous prices in the stack.
        # If the previous price is less than or equal to the current price,
        # we "merge" it into the current day's span.
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
        
        # Push the current price and its calculated span onto the stack
        self.stack.append((price, span))
        
        return span
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)