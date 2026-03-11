![CI](https://github.com/mxn2020/minions-portfolio-manager-workspace/actions/workflows/ci.yml/badge.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# minions-portfolio-manager

**Agent to manage global hierarchies, ecosystems, and projects**

Built on the [Minions SDK](https://github.com/mxn2020/minions).

---

## Quick Start

```bash
# TypeScript / Node.js
npm install @minions-portfolio-manager/sdk minions-sdk

# Python
pip install minions-portfolio-manager

# CLI (global)
npm install -g @minions-portfolio-manager/cli
```

---

## CLI

```bash
# Show help
portfolio-manager --help
```

---

## Python SDK

```python
from minions_portfolio_manager import create_client

client = create_client()
```

---

## Project Structure

```
minions-portfolio-manager/
  packages/
    core/           # TypeScript core library (@minions-portfolio-manager/sdk on npm)
    python/         # Python SDK (minions-portfolio-manager on PyPI)
    cli/            # CLI tool (@minions-portfolio-manager/cli on npm)
  apps/
    web/            # Playground web app
    docs/           # Astro Starlight documentation site
    blog/           # Blog
  examples/
    typescript/     # TypeScript usage examples
    python/         # Python usage examples
```

---

## Development

```bash
# Install dependencies
pnpm install

# Build all packages
pnpm run build

# Run tests
pnpm run test

# Type check
pnpm run lint
```

---

## Documentation

- Docs: [portfolio-manager.minions.help](https://portfolio-manager.minions.help)
- Blog: [portfolio-manager.minions.blog](https://portfolio-manager.minions.blog)
- App: [portfolio-manager.minions.wtf](https://portfolio-manager.minions.wtf)

---

## License

[MIT](LICENSE)
