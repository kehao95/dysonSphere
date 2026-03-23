# Development Guide

本文档定义项目的开发工作流和约定。

---

## 工作流程

### 1. 数学建模

数学模型位于 `models/` 目录：

```
models/
├── README.md           # 模型总览和符号定义
├── orbital/            # 轨道动力学
│   ├── displaced_orbit.py
│   └── stability.py
├── thermal/            # 热力学
│   └── equilibrium.py
└── mass_budget/        # 质量预算
    ├── materials.py    # 材料数据库
    └── calculator.py   # 系统β计算
```

### 2. 数值实验

实验遵循 `experiments/PROTOCOL.md` 定义的规范。

每次实验运行记录于 `experiments/runs/` 目录，包含：
- 假设 (hypothesis)
- 参数设置 (parameters)
- 结果 (results)
- 结论 (conclusion)

### 3. 论文写作

论文相关材料位于 `Paper/` 目录，遵循 `Paper/README.md` 定义的工作流。

---

## 符号约定

全局符号定义于 `models/README.md`，保持单一权威来源。

| Symbol | Name | SI Unit |
|--------|------|---------|
| $\beta$ | Lightness number | dimensionless |
| $\sigma$ | Areal density | kg/m² |
| $\sigma^*$ | Critical areal density | kg/m² (≈1.53 g/m² for Sun) |
| $\phi$ | Displacement angle | rad or deg |
| $r$ | Orbital radius | m or AU |
| $L_\odot$ | Solar luminosity | W |
| $M_\odot$ | Solar mass | kg |

---

## 代码约定

### 语言选择

- **Python 3.10+**: 数值计算、可视化
- **LaTeX**: 论文排版
- **Markdown**: 文档

### 依赖管理

使用 `requirements.txt` 或 `pyproject.toml` 管理 Python 依赖。

核心依赖（预期）：
- `numpy` — 数值计算
- `scipy` — 科学计算
- `matplotlib` — 可视化
- `astropy` — 天文常数和单位

### 代码风格

- 遵循 PEP 8
- 函数和类需有 docstring
- 物理量使用明确的单位注释或 `astropy.units`

---

## 文档约定

### Markdown

- 使用 GitHub Flavored Markdown
- 数学公式使用 `$...$`（行内）和 `$$...$$`（块级）
- 图表引用格式：`![description](path/to/figure.png)`

### 版本控制

- Commit message 简洁描述变更
- 重大变更更新 `STATUS.md`
- 里程碑完成更新 `ROADMAP.md`

---

## 质量保证

### 数学验证

- 单位分析（dimensional analysis）必须通过
- 极限情况（limiting cases）必须符合物理直觉
- 与文献结果对标（where applicable）

### 代码验证

- 核心函数需有单元测试
- 数值结果需可复现（固定随机种子、记录参数）

---

## 参考资料位置

| 类型 | 位置 |
|------|------|
| 文献 PDF | `docs/references/` |
| 论文 BibTeX | `Paper/references.bib` |
| 材料数据 | `models/mass_budget/materials.py` |
