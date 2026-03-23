# Closure Protocol

本文档定义任务和工作阶段的闭环标准。

---

## 闭环原则

根据 AGENTS.md (Constitution):

> Conversational completion is not closure; session work closes only when absorbed into durable state or explicitly handed off.

工作只有在以下情况才算真正完成：
1. 结果已吸收到规范位置（canonical location）
2. 或显式移交给下一阶段

---

## 闭环检查清单

### 代码变更

- [ ] 代码已提交到 git
- [ ] 相关文档已更新（如 README, STATUS）
- [ ] 如涉及新功能，已添加到 ROADMAP 或标记完成
- [ ] 测试通过（如有）

### 实验完成

- [ ] 实验记录完整（假设、参数、结果、结论）
- [ ] 数据已保存到 `experiments/runs/`
- [ ] 关键图表已生成并保存
- [ ] 结论已反馈到模型或论文

### 论文章节

- [ ] 草稿已保存到 `Paper/drafts/`
- [ ] 依赖的模型/计算已完成
- [ ] 图表已生成并放入 `Paper/figures/`
- [ ] Paper/README.md 状态已更新

### 研究里程碑

- [ ] 所有子任务已完成或显式延期
- [ ] STATUS.md 已更新
- [ ] ROADMAP.md 进度已更新
- [ ] 下一步行动已明确

---

## 临时状态处理

临时状态（session notes, 草稿, 脚手架）必须：

1. **吸收**: 内容移入规范位置，删除临时文件
2. **或标记**: 明确延期原因和计划处理时间
3. **或删除**: 如果不再需要

不允许临时状态无限期存在。

---

## Session 闭环

每个工作 session 结束前：

1. 检查是否有未保存的重要状态
2. 确保可复现：他人（或未来的自己）能从 repo 状态继续
3. 更新 STATUS.md 如有显著进展
4. 如有待办事项，记录到相关文档或 ROADMAP

---

## 审计触发

以下情况触发闭环审计：

- Session 开始时（检查上次遗留）
- 请求关闭任务时
- 达到里程碑时
- 发现重复摩擦时（friction pattern）
