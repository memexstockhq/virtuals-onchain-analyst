# Virtuals Onchain Analyst

[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Chains](https://img.shields.io/badge/Chains-RH%20%7C%20BSC%20%7C%20EVM-lightgrey)](configs/)

**A Virtuals agent that reads onchain data**

Reference implementation of one Virtuals Protocol analyst persona: reads RH/BSC/EVM on-chain data, writes ticker briefs, posts signed verdicts.

## Quick start

```bash
git clone https://github.com/cervemone/virtuals-onchain-analyst.git
cd virtuals-onchain-analyst
pip install -r requirements.txt
python -m src.main --help
```

## Layout

```
  agent/
  tools/
  chains/
  prompts/
  storage/
  tests/
  docs/
  scripts/
  configs/
  examples/
  evaluations/
  integrations/
```

## Related

- `stock-token-index` — registry of tokenized equities
- `stock-analyst-agent` — the agent that consumes this repo
- `rh-stock-token-sdk` — SDK for Robinhood Chain stock tokens

## License

MIT
