# Testing Protocol

本文档定义代码和模型的验证标准。

---

## 测试层级

### Level 1: 单位分析 (Dimensional Analysis)

所有物理方程必须通过量纲检查。

```python
# Example: verify σ* has units of kg/m²
# σ* = L / (2π c G M)
# [W] / ([m/s] [m³/(kg·s²)] [kg])
# = [kg·m²/s³] / [m/s · m³/(kg·s²) · kg]
# = [kg·m²/s³] / [m⁴/s³]
# = [kg/m²] ✓
```

### Level 2: 极限情况 (Limiting Cases)

模型在物理极限应给出合理结果：

| 极限 | 预期行为 |
|------|----------|
| φ → 0 | β → 0, 退化为开普勒轨道 |
| β → 1 | 完全悬浮，无需轨道速度 |
| r → ∞ | 光压 → 0, β_required → sin(φ) |
| σ → σ* | β → 1 |

### Level 3: 文献对标 (Literature Validation)

与 McInnes (1999) 及其他参考文献的结果比较：

- [ ] 临界面密度 σ* ≈ 1.53 g/m² 
- [ ] 位移轨道方程与 McInnes 公式一致
- [ ] 材料数据与公开规格相符

### Level 4: 数值验证 (Numerical Tests)

```python
# tests/test_orbital.py

def test_sigma_star():
    """Verify critical areal density."""
    from models.orbital import SIGMA_STAR
    assert abs(SIGMA_STAR * 1000 - 1.53) < 0.01  # g/m²

def test_beta_phi_small_angle():
    """For small φ, β ≈ sin(φ)."""
    from models.orbital import DisplacedOrbit
    orbit = DisplacedOrbit(r_au=1.0, phi_deg=1.0)
    beta = orbit.required_beta()
    expected = np.sin(np.radians(1.0))
    assert abs(beta - expected) / expected < 0.01

def test_displacement_calculation():
    """Verify vertical displacement at 1 AU, 1°."""
    from models.orbital import DisplacedOrbit
    orbit = DisplacedOrbit(r_au=1.0, phi_deg=1.0)
    d_km = orbit.vertical_displacement()
    # Expected: 1 AU * sin(1°) ≈ 2.6e6 km
    assert 2.5e6 < d_km < 2.7e6
```

---

## 运行测试

```bash
# 从项目根目录
python -m pytest tests/ -v

# 单个模块
python -m pytest tests/test_orbital.py -v

# 带覆盖率
python -m pytest tests/ --cov=models
```

---

## 持续验证

### 提交前检查

1. 所有测试通过
2. 单位分析无误
3. 极限情况合理

### 新增功能

每个新模型/函数应包含：
- Docstring with expected behavior
- At least one unit test
- Verification against known result (if applicable)

---

## 已知限制

记录模型的已知限制和适用范围：

| 模型 | 限制 | 适用范围 |
|------|------|----------|
| DisplacedOrbit | 小角度近似 | φ < 10° |
| DisplacedOrbit | 忽略太阳风 | 一级估算 |
| SystemBudget | 假设完美反射 | 保守估计 |

---

## 测试目录结构

```
tests/
├── __init__.py
├── test_orbital.py       # 轨道动力学测试
├── test_mass_budget.py   # 质量预算测试
└── test_thermal.py       # 热力学测试
```
