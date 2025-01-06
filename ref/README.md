Workload redirector
-------------------

VM owner request project
Project is created on some cluster

Destinations
- red
- mgmt
- hubN

Route
- `/login` -> mgmt
- `/api` -> red, mock?
- `/api/<version>/namespaces` -> red, relay LIST
- `/api/<version>/namespaces/` -> hubN
- `/apis` -> red, mock?
- `/apis/<group>/<version>/<namespace>` -> hubN
- `/*` -> 404

Assumption
- Valid bearer token / creds in mgmt + hubN

Question
- How valid token / creds in all clusters? auth or distribute token?
