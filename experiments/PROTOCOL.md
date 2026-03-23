# Experiment Protocol

本文档定义数值实验的规范和流程。

---

## 实验目录结构

```
experiments/
├── PROTOCOL.md          # 本文件
└── runs/
    └── YYYYMMDD_name/   # 单次实验运行
        ├── README.md    # 实验描述
        ├── params.json  # 参数记录
        ├── results/     # 输出数据
        └── figures/     # 生成图表
```

---

## 实验记录规范

每次实验必须包含：

### 1. 假设 (Hypothesis)

明确陈述本次实验要验证或探索的问题。

> 例："当 φ 从 1° 增加到 5° 时，所需 β 的增长是否近似线性？"

### 2. 参数设置 (Parameters)

完整记录所有输入参数，使用 `params.json`:

```json
{
  "experiment_type": "parameter_sweep",
  "date": "2026-03-23",
  "parameters": {
    "r_au": 1.0,
    "phi_range_deg": [0.5, 5.0],
    "reflector_material": "kapton_al_1um",
    "pv_material": "cigs_flex"
  },
  "model_version": "v0.1"
}
```

### 3. 方法 (Method)

描述使用的模型、脚本、计算步骤。

### 4. 结果 (Results)

- 数值数据保存为 CSV 或 JSON
- 图表保存为 PNG/PDF（带源数据）
- 关键数值在 README 中列出

### 5. 结论 (Conclusion)

- 假设是否得到验证？
- 有何意外发现？
- 对论文/下一步实验的启示？

---

## 实验类型

### Type A: 参数扫描 (Parameter Sweep)

固定其他变量，扫描单一或多个参数的影响。

**典型问题**:
- β vs φ 关系验证
- 材料选择对可行设计空间的影响
- 热平衡温度 vs 距离

### Type B: 设计优化 (Design Optimization)

给定约束条件，寻找最优配置。

**典型问题**:
- 给定目标 β 和功率需求，最小化反射镜面积
- 最大化载荷/反射镜质量比

### Type C: 稳定性分析 (Stability Analysis)

分析扰动响应和长期稳定性。

**典型问题**:
- 轴向扰动的恢复时间
- 太阳风扰动的累积效应

### Type D: 对比研究 (Comparative Study)

与其他方案的定量比较。

**典型问题**:
- MDDS vs 传统戴森群的碰撞风险
- MDDS vs 戴森泡的载荷能力

---

## 可复现性要求

1. **随机种子**: 如使用随机数，必须固定并记录种子
2. **版本控制**: 记录模型代码版本（git commit hash）
3. **环境**: 记录 Python 版本和关键依赖版本
4. **独立验证**: 关键结果应能通过重新运行脚本复现

---

## 实验命名规范

格式: `YYYYMMDD_short_description`

例:
- `20260323_beta_phi_sweep`
- `20260325_material_comparison`
- `20260401_thermal_equilibrium`

---

## 从实验到论文

1. 实验结果先在 `experiments/runs/` 验证
2. 确认正确后，将关键图表复制到 `Paper/figures/results/`
3. 在论文草稿中引用具体实验（如 "see experiment `20260323_beta_phi_sweep`"）
4. 最终版本前清理中间实验，保留支撑论文结论的核心实验
