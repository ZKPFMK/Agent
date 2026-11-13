# Claims

| id | claim | proposer | status | falsifier evidence | evidence refs |
|---|---|---|---|---|---|

规则：

- 新 claim 先登记，再实现；
- 初始状态必须是 `open`；
- 只有 `survived` 或带明确窄化表述的 `weakened` 才能进入论文；
- 被 `refuted` 的 claim 不能通过换措辞重新进入论文；
- 每个 claim 必须有 kill switch。

