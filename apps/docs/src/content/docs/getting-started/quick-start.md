---
title: Quick Start
description: Get up and running with Minions Portfolio-manager in minutes
---

## TypeScript

```typescript
import { createClient } from '@minions-portfolio-manager/sdk';

const client = createClient();
console.log('Version:', client.version);
```

## Python

```python
from minions_portfolio_manager import create_client

client = create_client()
print(f"Version: {client['version']}")
```

## CLI

```bash
portfolio-manager info
```
