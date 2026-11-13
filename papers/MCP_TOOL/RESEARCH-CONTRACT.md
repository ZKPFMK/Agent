# Research Contract

状态：`TEMPLATE`

这个文件必须在实现任何新 idea 之前冻结。修改时复制为 `RESEARCH-CONTRACT-v2.md`，并在 `DECISIONS.md` 记录修改原因。

## 1. 研究问题

```text
RQ1：
RQ2：
RQ3：
```

## 2. 范围

```text
时间范围：
攻击面：
目标系统：
攻击者能力：
不研究的对象：
允许的实验环境：
```

## 3. Hypothesis

```text
H1：
机制解释：
最接近的 prior work：
我们的 delta：
```

## 4. Baselines

```text
B0 naive attack：
B1 strongest known attack：
B2 simple defense：
B3 proposed defense/control：
```

## 5. Success signals

成功必须同时满足：

```text
S1：
S2：
S3：
```

每个成功信号都要指定：

```text
metric：
threshold：
comparison：
n：
seed：
```

## 6. Independent failure signals

失败信号不能只写“没有达到成功阈值”。至少检查：

```text
F1：naive baseline 已达到相同效果
F2：换模型或框架后效果消失
F3：换 seed 后效果消失
F4：攻击成功但 benign utility 显著下降
F5：证明大小、延迟或成本过高
F6：防御只在非自适应攻击下有效
F7：威胁模型要求不现实的权限
F8：结果无法复现
```

针对当前 idea 补充：

```text
F9：
F10：
```

## 7. Ablation expectations

| Ablation | 预期结果 | 如果没有出现意味着什么 |
|---|---|---|
| 去掉机制 A |  |  |
| 去掉机制 B |  |  |
| 替换路由/解析步骤 |  |  |
| 去掉跨工具交互 |  |  |
| 仅使用 naive payload |  |  |

## 8. 实验协议

```text
模型：
模型版本：
框架：
数据集：
数据 split：
temperature：
seed：
judge：
judge validation：
统计方法：
预算：
```

## 9. Kill criteria

满足以下任意条件，idea 自动返回 P6 或标记为 `refuted`：

```text
K1：
K2：
K3：
```

## 10. Claim contract

| Claim ID | 预注册 claim | 最小证据 | Kill switch | 状态 |
|---|---|---|---|---|
| C1 |  |  |  | open |
| C2 |  |  |  | open |

