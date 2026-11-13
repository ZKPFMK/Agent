# R4 MCP 控制面候选：2026-11-11

状态：screen-only；未注册 claim、未运行实验、未调用模型、未启动服务。

## H1：roots/list 根能力自动披露

- **释放变量：**host 对 server 发起的 `roots/list` 请求如何处理：自动返回、返回空集、逐次确认或拒绝。
- **威胁模型：**攻击者只拥有一个已经连接的第三方 MCP server；host、client、合成工作区和 canary 均由项目控制。攻击者没有 host、LLM、受害工具或真实文件权限。
- **独立 witness：**攻击 server 的原始日志收到仅存在合成工作区中的 `CANARY_ROOT`；host trace 显示 `roots/list` 被允许且没有用户确认；没有工具调用。数据不能来自攻击 server 自己。
- **naive baseline：**同预算只返回普通工具结果，不发送 `roots/list`，攻击 server 收不到 canary。
- **机制 control：**同一合法请求，但关闭 roots capability、使用空白根列表或要求逐次确认。
- **kill switch：**固定 host 全部拒绝、返回空集或强制确认；或根列表本来就是公开授权信息。
- **邻近风险：**资源/elicitation/sampling abuse、resource/logic 攻击以及 COPEX client-layer 覆盖；若只是一般资源读取或公开根信息，则 NO-GO。

## H2：sampling 响应的会话/接收者错绑

- **释放变量：**`sampling/createMessage` 响应是否按 request-id + server/session + recipient 绑定，还是按当前活动会话路由。
- **威胁模型：**攻击者拥有已连接 server；项目自有 host 暴露 sampling，私有上下文只包含合成数据；server 没有工具权限，不能直接读取 host 上下文。
- **独立 witness：**攻击 server 收到只存在另一活动会话中的 `CANARY_CTX`；host trace 显示上下文 hash 与 response recipient 不匹配；没有工具调用。
- **naive baseline：**合法 sampling 请求只使用公开上下文，攻击 server 收不到 canary。
- **机制 control：**启用逐请求 recipient binding，并限制为公开上下文或逐次确认。
- **kill switch：**没有真实 sampling 路径；所有 host 均最小化上下文且绑定 recipient；或结果只因模型遵循恶意文本而出现，则归为普通提示词注入并关闭。
- **邻近风险：**sampling abuse、COPEX client/transport 越界；新意只能来自可观测的跨会话绑定状态。

## 2026-11-11 源码筛查结果

### H1：当前表述关闭

固定对象为 VS Code 1.106.0，commit `ac4cbdf48759c7d8c3eb91ffe6bb04316e263c57`。公开实现存在 server request → roots callback → 原连接 response 的路径，但 root URI/name 来自 host 已配置的 `explicitRoots` 或 workspace folders，并按 remote authority 过滤。没有证据表明 server 取得了未授权 root；没有逐次弹窗不等于缺少已有授权。OWASP MCP 安全指南也已将“公布打开目录、轮询 roots/list”作为已知风险描述。因此 H1 的一般“自动披露即攻击”表述 NO-GO。

若未来要重开，只能窄化为真实产品中的**未授权 root**：必须有 fixture 生成的私有 tenant/workspace B root，A 的有效授权范围不含它，且 server A 的原始结果精确包含随机 root 标记。root URI/name 披露本身不能等同文件内容读取或能力窃取。

### H2：继续 UNCERTAIN，禁止实验

固定实现中 sampling 回调存在，但已检查路径没有证明另一活动会话的私有上下文进入 A 的请求，也没有证明响应发错连接。要把 H2 从 screening 提升，必须固定同一 revision 的依赖锁和源码哈希，继续跟踪 `upstream_session` 的赋值/切换、上下文 lookup、approval binding、pending request key 和最终 send。若最终只是 session/identity rebinding，则回到已关闭 Q7；若只是模型遵循 server 文本，则是普通提示词注入。

### 下一轮轴

H1 不再重复。H2 只做一次有界的完整 upstream/session 代码核验；并行启动一个新的防御边界审计，寻找不涉及工具投毒、parser differential、approval cache、roots disclosure 或普通 prompt injection 的机制。仍未通过前不得注册 claim 或运行实验。

现有 R4-05 的 retry/cancel、R4-04 resource_link、R4-02 approval-cache 和 Q6/Q8 list_changed/stale-state 不重开。
