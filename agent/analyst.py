"""The onchain analyst agent."""
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class TickerBrief:
    ticker: str
    price: float
    rsi: float
    sentiment: str
    verdict: str

class OnchainAnalyst:
    def __init__(self, chains: Dict[str, str]):
        self.chains = chains  # chain -> rpc

    def analyze(self, ticker: str) -> TickerBrief:
        price = self._price(ticker)
        rsi = self._rsi(ticker)
        return TickerBrief(ticker, price, rsi, "neutral", "HOLD")

    def _price(self, ticker: str) -> float:
        return 0.0

    def _rsi(self, ticker: str) -> float:
        return 50.0
