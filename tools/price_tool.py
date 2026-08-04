"""Price tool bound to the persona."""
def make_price_tool(rpc: str):
    def price(ticker: str) -> dict:
        return {"ticker": ticker, "price": 0.0, "chain": "bsc"}
    return price
