# High-Level Theoretical Derivation

本稿不讨论材料、热学、结构、控制等工程问题，只保留 MDDS 概念最核心的理论骨架。

目标只有一个：

> 在给定位移角 $\phi$ 时，推导维持该环所需的最小光压参数 $\beta_{\text{req}}$，并把它改写成允许的最大系统面密度曲线 $\sigma_{\max}(\phi)$。

---

## 1. Problem Statement

我们考虑一个节点：

- 与恒星中心距离固定为 $r$
- 位于恒星赤道面上方纬度 $\phi$
- 绕恒星自转轴做圆周运动，角速度为 $\omega$
- 太阳帆法线相对来光方向倾斜一个锥角 $\alpha$

我们要求该节点在固定 $r$ 和固定 $\phi$ 上长期维持圆形位移轨道。

这意味着要同时满足：

1. 竖直方向没有净加速度
2. 水平方向恰好提供圆周运动所需的向心加速度

---

## 2. Geometry and Kinematics

把位置写成柱坐标最直观。

若球坐标半径为 $r$、纬度为 $\phi$，则：

$$\rho = r\cos\phi,\qquad z = r\sin\phi$$

其中：

- $\rho$ 是围绕恒星轴旋转时的轨道半径
- $z$ 是离赤道面的高度

节点以角速度 $\omega$ 绕轴做圆周运动，因此其加速度只有水平方向向内的向心项：

$$a_c = \omega^2 \rho = \omega^2 r\cos\phi$$

为了与开普勒圆轨道对比，定义无量纲角速度比：

$$\nu \equiv \frac{\omega}{\sqrt{\mu/r^3}}$$

其中 $\mu = GM_\odot$。

于是向心加速度也可写成：

$$a_c = \nu^2 \frac{\mu}{r^2}\cos\phi$$

---

## 3. Gravity Decomposition

太阳引力大小为：

$$g = \frac{\mu}{r^2}$$

在柱坐标下分解为：

- 水平向内分量：

$$g_\rho = g\cos\phi$$

- 竖直向下分量：

$$g_z = g\sin\phi$$

所以，随着 $\phi$ 增大：

- 需要轨道或光压来抵消的竖直分量单调增加
- 可由圆周运动承担的水平部分按 $\cos\phi$ 下降

这正是“赤道宽松、高纬苛刻”的高层来源。

---

## 4. Ideal Sail Force Decomposition

定义光压参数：

$$\beta \equiv \frac{F_{\text{rad}}}{F_{\text{grav}}} = \frac{\sigma^*}{\sigma}$$

其中：

$$\sigma^* = \frac{L_\odot}{2\pi cGM_\odot} \approx 1.53\ \text{g/m}^2$$

是太阳系下的临界面密度常数。

对理想镜面帆，若帆法线与来光方向夹角为 $\alpha$，则光压加速度大小为：

$$a_{\text{SRP}} = \beta g \cos^2\alpha$$

由于力沿帆法线方向，其在“沿太阳方向”和“垂直太阳方向”的分量分别为：

$$a_{\parallel} = \beta g\cos^3\alpha$$
$$a_{\perp} = \beta g\cos^2\alpha\sin\alpha$$

其中：

- $a_{\parallel}$ 负责减轻水平向内引力负担
- $a_{\perp}$ 负责把节点抬离赤道面

这里采用的是与 statite / Dyson-bubble 一阶推导相同的**理想镜面**假设。对本稿而言，这样做是有意的：目标是先建立 MDDS 的闭式几何与动力学框架，而不是在第一篇框架论文中引入完整的光学非理想模型。

但需要明确的是，MDDS 对非理想光学的敏感性高于纯径向辐射支撑构型。对 Dyson bubble / statite 而言，非理想反射主要表现为径向推力折减；而对 MDDS 而言，吸收、漫反射与热再辐射不仅会降低有效推力大小，还会扰动合力方向，因为该构型依赖光压力在径向与离面方向上的特定分解。

这里还需要再加一个建模边界：本文主推导把反射薄膜视为唯一显式承受并利用光压的支撑表面。诸如太阳能电池板之类的 payload 表面，不在主方程里单独赋予额外光压分量，也不显式引入由此产生的受力偏移或姿态耦合；它们只在后续工程记账里通过总系统面密度 $\sigma_{\text{sys}}$ 间接体现。

因此，本稿后续得到的 $\beta_{\min}(\phi)$ 与 $\sigma_{\max}(\phi)$ 应理解为：

> **理想镜面、单主支撑表面假设下的主支撑曲线，而不是已经完成光学现实闭合与 payload 光压耦合后的最终工程曲线。**

---

## 5. Force-Balance Equations

### 5.1 Vertical equilibrium

节点高度固定，因此竖直方向净加速度必须为零。

于是光压的离面分量必须平衡引力的竖直分量：

$$\beta g\cos^2\alpha\sin\alpha = g\sin\phi$$

约去 $g$ 得：

$$\boxed{\beta \cos^2\alpha\sin\alpha = \sin\phi}$$

### 5.2 Horizontal equilibrium

在水平方向，引力向内分量并不需要完全由光压抵消，因为仍然允许轨道运动提供向心加速度。

也就是说：

$$g\cos\phi - \beta g\cos^3\alpha = a_c$$

代入 $a_c = \nu^2(\mu/r^2)\cos\phi = \nu^2 g\cos\phi$，约去 $g$，得：

$$\boxed{\beta \cos^3\alpha = \cos\phi(1-\nu^2)}$$

这两条式子就是 MDDS 理论的最核心方程组。

---

## 6. General Parametric Family

由竖直平衡式直接解出 $\beta$：

$$\boxed{\beta(\phi,\alpha) = \frac{\sin\phi}{\cos^2\alpha\sin\alpha}}$$

再把它代回水平平衡式，可得：

$$\frac{\sin\phi}{\cos^2\alpha\sin\alpha}\cos^3\alpha = \cos\phi(1-\nu^2)$$

整理得：

$$\sin\phi\cot\alpha = \cos\phi(1-\nu^2)$$

即：

$$\boxed{\nu^2(\phi,\alpha) = 1 - \frac{\tan\phi}{\tan\alpha}}$$

这两个公式给出了一般理论图景：

- 给定纬度 $\phi$
- 你选定一个帆角 $\alpha$
- 所需光压参数 $\beta$ 和轨道角速度比 $\nu$ 就被同时确定了

并且存在一个基本约束：

$$\nu^2 \ge 0 \quad \Rightarrow \quad \tan\alpha \ge \tan\phi$$

也就是：

$$\boxed{\alpha \ge \phi}$$

这说明纬度越高，所需帆角下限越高。

---

## 7. The Payload-Friendly Branch: Minimize Required Beta

如果我们的目标是：

> 在每个纬度上尽量允许更重的系统和更大的 payload

那么就要在给定 $\phi$ 下让所需 $\beta$ 最小，也就是最小化：

$$\beta(\phi,\alpha) = \frac{\sin\phi}{\cos^2\alpha\sin\alpha}$$

由于 $\sin\phi$ 与 $\alpha$ 无关，这等价于最大化：

$$f(\alpha)=\cos^2\alpha\sin\alpha$$

对其求导：

$$f'(\alpha)=\cos\alpha(\cos^2\alpha-2\sin^2\alpha)$$

排除平凡边界后，极值条件为：

$$\cos^2\alpha = 2\sin^2\alpha$$

即：

$$\tan^2\alpha = \frac{1}{2}$$

因此最优帆角为：

$$\boxed{\alpha_{\text{opt}} = \arctan\left(\frac{1}{\sqrt{2}}\right) \approx 35.264^\circ}$$

这个结果非常重要：

> 最优锥角与 $\phi$ 无关，它是整个低-$\beta$ 支撑分支的一个固定几何常数。

---

## 8. The Latitude Support Curve

在最优角下，

$$\cos^2\alpha_{\text{opt}}\sin\alpha_{\text{opt}}=\frac{2}{3\sqrt{3}}$$

代回一般式：

$$\beta_{\min}(\phi)=\frac{\sin\phi}{2/(3\sqrt{3})}$$

得到：

$$\boxed{\beta_{\min}(\phi)=\frac{3\sqrt{3}}{2}\sin\phi}$$

这就是我们真正想要的“纬度支撑曲线”。

它的物理意义非常清楚：

- 赤道附近：$\phi\to 0$，所以 $\beta_{\min}\to 0$
- 纬度升高：$\beta_{\min}$ 单调增加
- 越想抬高环，系统必须越轻

同时，把最优角代回角速度式：

$$\nu^2 = 1 - \sqrt{2}\tan\phi$$

即：

$$\boxed{\nu^2(\phi)=1-\sqrt{2}\tan\phi}$$

这说明：

- 在赤道处，$\nu\to 1$，退化为普通开普勒圆轨道
- 随着纬度升高，轨道角速度逐渐下降
- 位移越大，越需要更多光压、越少依赖轨道离心力

这里需要特别区分两种不同的“临界”含义。

第一种是**架构阈值**：

> 当系统自身已经达到 $\beta \ge 1$ 时，纯辐射支撑的 statite / Dyson-bubble 类构型就进入了可选设计空间。

这仍然是一个非常有意义的门槛，因为它表示“是否已经有资格完全放弃轨道支撑”。

如果仍然沿着本文当前这条 payload-friendly 支撑曲线来看，那么

$$\beta_{\min}(\phi)=1$$

对应的角度是：

$$\phi_{\beta=1}=\arcsin\left(\frac{2}{3\sqrt{3}}\right)\approx 22.638^\circ$$

而在这一点上，轨道支撑并没有消失，因为

$$\nu^2 = 1-\sqrt{2}\tan\phi_{\beta=1} \approx 0.410$$

即：

$$\nu \approx 0.640$$

所以，**对当前这条分支而言，$\beta = 1$ 只意味着“已经跨过了 bubble/statite 可选架构的门槛”，并不意味着“这条分支已经完全转入纯光压支撑”。**

但第二种是**当前这条低-$\beta$ payload-friendly 分支自身的终点**。

由

$$\nu^2(\phi)=1-\sqrt{2}\tan\phi$$

可知，当

$$\phi_c=\arctan\left(\frac{1}{\sqrt{2}}\right)\approx 35.264^\circ$$

时，正好有

$$\nu = 0$$

也就是：对这条特定分支而言，轨道支撑在此点完全消失。

再代回最小支撑曲线，可得：

$$\beta_{\min}(\phi_c)=1.5$$

因此：

- $\beta = 1$ 表示“纯辐射支撑架构开始成为可选方案”
- $\phi_c \approx 35.264^\circ$、$\beta = 1.5$ 表示“当前这条 payload-friendly displaced-orbit 分支走到自己的内部终点”

这两者不是同一个临界点。

为了避免混淆，可以把三个最重要的标记点并列成一张小表：

| 标记 | 条件 | 对应状态 | 物理意义 |
|------|------|----------|----------|
| 平面开普勒极限 | $\phi = 0$ | $\beta = 0,\ \nu = 1$ | 纯轨道支撑，没有离面位移 |
| bubble / statite 进入阈值 | $\beta = 1$（沿当前 payload-friendly 分支） | $\phi \approx 22.638^\circ,\ \nu \approx 0.640$ | 纯辐射支撑架构开始进入可选空间，但当前分支仍保留轨道支撑 |
| 当前分支内部终点 | $\nu = 0$ | $\phi_c \approx 35.264^\circ,\ \beta = 1.5$ | 当前这条 displaced-orbit 最优分支真正走到纯光压支撑端点 |

换句话说，**一旦材料已经达到 $\beta \ge 1$，你在架构上当然可以选择转向 bubble / statite；但如果你坚持沿着本文当前推导出的这条最优微位移分支继续走，那么它真正走到“完全不再依赖轨道支撑”的位置，是在 $\beta = 1.5$ 而不是 $\beta = 1$。**

---

## 9. Convert to the Critical Density Curve

因为：

$$\beta = \frac{\sigma^*}{\sigma}$$

所以给定纬度下允许的最大系统面密度为：

$$\sigma_{\max}(\phi)=\frac{\sigma^*}{\beta_{\min}(\phi)}$$

代入上式：

$$\boxed{\sigma_{\max}(\phi)=\frac{2\sigma^*}{3\sqrt{3}\sin\phi}}$$

这就是高层上最重要的工程接口。

它把动力学问题直接改写成一个材料/系统质量问题：

> 只要某个架构的总系统面密度 $\sigma_{\text{sys}}$ 低于 $\sigma_{\max}(\phi)$，它就可以在该纬度挂载有效 payload。

也就是说，判据只有一条：

$$\boxed{\sigma_{\text{sys}} < \sigma_{\max}(\phi)}$$

---

## 10. Useful Corollaries

在上面的统一判据之上，会自然长出两类不同的设计目标：

1. **最大有效载荷方向（payload-optimized branch）**

   给定纬度 $\phi$，希望所需 $\beta$ 最小，从而让允许的系统面密度 $\sigma_{\max}$ 最大。
   这正是前文求得 $\alpha_{\text{opt}}$ 与 $\beta_{\min}(\phi)$ 的物理意义：它们对应的是“在该纬度上给系统留下最大质量预算”的分支。

2. **同步约束方向（synchronization-constrained branch）**

   给定外部运行目标，例如与地球保持同角速度，或满足某个预设周期关系。
   这一方向不再单纯追求最大 $\sigma_{\max}$，而是追求更规则的运行组织、部署节律、通信窗口或系统编排。

更简洁地说：

> 前者最大化工程可行裕度，后者最大化运行上的规则性。

### 10.1 Maximum feasible latitude for a given system

若某个具体架构的总系统面密度为 $\sigma_{\text{sys}}$，则其最大可行纬度由

$$\sigma_{\text{sys}} = \sigma_{\max}(\phi_{\max})$$

给出：

$$\boxed{\phi_{\max} = \arcsin\left(\frac{2\sigma^*}{3\sqrt{3}\,\sigma_{\text{sys}}}\right)}$$

这就是“系统轻到什么程度，最多能被抬到多高”的直接映射。

### 10.2 Small-angle asymptotic form

当 $\phi \ll 1$（弧度制）时：

$$\sin\phi \approx \phi$$

于是：

$$\beta_{\min}(\phi)\approx \frac{3\sqrt{3}}{2}\phi$$

$$\sigma_{\max}(\phi)\approx \frac{2\sigma^*}{3\sqrt{3}\phi}$$

因此在高层近似上：

> 允许的系统面密度大致按 $1/\phi$ 下降。

这解释了为什么从 $0.5^\circ$ 到 $1^\circ$ 再到 $2^\circ$，可行窗口会缩得非常快。

### 10.3 Earth-synchronous variant

上面的推导默认：

- 位移环的球坐标半径固定为 $r$
- 然后让其角速度 $\omega$ 自行满足平衡

如果进一步要求：

> 该环与地球公转保持同角速度同步

即：

$$\omega = \omega_\oplus = \sqrt{\mu/a_\oplus^3}$$

其中 $a_\oplus = 1\ \text{AU}$。

则

$$\nu^2 = \frac{\omega_\oplus^2}{\mu/r^3} = \frac{\mu/a_\oplus^3}{\mu/r^3} = \left(\frac{r}{a_\oplus}\right)^3$$

把它代回一般关系

$$\nu^2(\phi,\alpha)=1-\frac{\tan\phi}{\tan\alpha}$$

得到同步轨道半径：

$$\boxed{r_{\text{sync}}(\phi,\alpha)=a_\oplus\left(1-\frac{\tan\phi}{\tan\alpha}\right)^{1/3}}$$

若仍取 payload-friendly 的最优分支

$$\alpha_{\text{opt}} = \arctan\left(\frac{1}{\sqrt{2}}\right)$$

则同步半径简化为：

$$\boxed{r_{\text{sync}}(\phi)=a_\oplus\left(1-\sqrt{2}\tan\phi\right)^{1/3}}$$

这里最关键的结论是：

> **地球同步约束不会改变最小 $\beta$ 曲线，也不会改变临界面密度曲线；它主要改变的是环的实际半径。**

也就是说：

- $\beta_{\min}(\phi)$ 不变
- $\sigma_{\max}(\phi)$ 不变
- 变化的是：环需要从 `1 AU` 略微缩到更内侧，才能保持与地球同角速度

这是一个很好的理论结果，因为它说明“同步化”不是额外的质量惩罚，主要是轨道几何上的修正。

从设计目标上看，这个同步变体可以被理解成：

> **在同一基础理论框架内，从“最大质量裕度”目标切换到了“最大运行规则性”目标。**

因此，MDDS 的理论框架并不只给出一个单独解，而是至少给出两类自然分支：

- 一个是以最小 $\beta$ 为目标的 **payload-friendly branch**
- 一个是以外部周期约束为目标的 **synchronization-constrained branch**

两者都服从同一套力平衡方程，只是优化目标不同。

### 10.4 Representative Earth-synchronous numbers

在最优低-$\beta$ 分支上：

| $\phi$ | $r_{\text{sync}}/1\text{AU}$ | inward shift | $z=r\sin\phi$ | $\beta_{\min}$ | $\sigma_{\max}$ |
|--------|-----------------------------:|-------------:|--------------:|---------------:|----------------:|
| $0.5^\circ$ | $0.99587$ | $6.18\times10^5$ km | $1.30\times10^6$ km | $0.02267$ | $67.48\ \text{g/m}^2$ |
| $1.0^\circ$ | $0.99170$ | $1.24\times10^6$ km | $2.59\times10^6$ km | $0.04534$ | $33.74\ \text{g/m}^2$ |
| $2.0^\circ$ | $0.98326$ | $2.50\times10^6$ km | $5.13\times10^6$ km | $0.09067$ | $16.87\ \text{g/m}^2$ |
| $3.0^\circ$ | $0.97466$ | $3.79\times10^6$ km | $7.63\times10^6$ km | $0.13597$ | $11.25\ \text{g/m}^2$ |
| $5.0^\circ$ | $0.95693$ | $6.44\times10^6$ km | $1.25\times10^7$ km | $0.22644$ | $6.76\ \text{g/m}^2$ |

从这些数可以看出：

- 对 `1°` 量级环，同步约束带来的半径修正只有不到 `1%`
- 离面高度仍然保持在几百万公里量级
- 真正主导可行性的仍然是 $\sigma_{\max}(\phi)$，而不是这点同步半径修正

因此在高层判断上可以这样说：

> 若目标是在 `1 AU` 附近与地球公转同角速度同步，则 MDDS 的理论要求几乎不变，只需把环放在略小于 `1 AU` 的位置。

---

## 11. Representative Numbers at 1 AU

取 $\sigma^*\approx 1.53\ \text{g/m}^2$：

### At $\phi = 0.5^\circ$

$$\beta_{\min}\approx 0.02266,\qquad \sigma_{\max}\approx 67.52\ \text{g/m}^2$$

### At $\phi = 1.0^\circ$

$$\beta_{\min}\approx 0.04534,\qquad \sigma_{\max}\approx 33.76\ \text{g/m}^2$$

### At $\phi = 2.0^\circ$

$$\beta_{\min}\approx 0.09062,\qquad \sigma_{\max}\approx 16.88\ \text{g/m}^2$$

这三个点已经足够说明这条曲线的形状：

- 从赤道向外一开始下降就很快
- `1°` 仍可能有工程窗口
- 到 `2°` 时质量预算已经非常紧

---

## 12. What This Derivation Means at High Level

从高层看，MDDS 的理论核心不应该再表述成“某个单独的 1° 环可不可行”，而应该表述成：

1. 先推导纬度支撑曲线 $\beta_{\min}(\phi)$
2. 再改写成临界面密度曲线 $\sigma_{\max}(\phi)$
3. 任意候选架构都对应一个系统面密度 $\sigma_{\text{sys}}$
4. 两者交点给出最大可行纬度 $\phi_{\max}$

于是整个问题就被统一成了一个非常干净的高层判据：

> **MDDS 是一个“纬度支撑曲线”和“系统面密度”之间的交点问题。**

从更抽象的动力学图景看，MDDS 还可以被理解成一族连接两种极限状态的采能构型：

- 当 $\phi = 0$ 时，支撑完全由轨道运动承担，对应平面开普勒 swarm 极限
- 随着 $\phi$ 增大，太阳光压逐步补充并部分替代轨道支撑
- 在这个意义上，MDDS 的更广义框架指向以辐射支撑为主导的 statite / bubble 端点

但这里必须加一个严格限定：

> **本稿显式求解的，是其中的低纬、低-$\beta$、圆形位移轨道分支。它可以被看作朝向辐射支撑端点的一段连续过渡，但并不意味着这条具体分支本身会无缝延伸到 $\phi\to 90^\circ$。**

因此，更准确的说法不是“当前这条解一直延伸到极区”，而是：

> **MDDS 提供了一个从纯开普勒支撑向更强辐射支撑逐步过渡的概念连续体，而本文分析的是这一连续体中的低纬可工程化分支。**

后续所有工程细节，无论是：

- PV 填充因子
- 反射膜面密度
- bus / deployment / control 质量
- 结构尺度律

本质上都只是在决定 $\sigma_{\text{sys}}$ 这条线落在哪里。

而动力学主问题，已经由本稿中的 $\beta_{\min}(\phi)$ 与 $\sigma_{\max}(\phi)$ 解决了第一层。

---

## 13. Progressive Deployment Interpretation

这套高层理论还有一个对 Dyson 计划尤其重要的含义：

> 它不只是一个“最终构型”，也是一个“可渐进展开”的部署框架。

原因在于，$\sigma_{\max}(\phi)$ 曲线天然给出了一个由易到难的扩张顺序：

1. **先从黄道附近开始**

   当 $\phi \approx 0$ 时：

   - $\beta_{\min} \to 0$
   - $\sigma_{\max} \to \infty$

   也就是说，赤道附近是整个体系中最宽松、最容易先做的区域。

2. **每个新节点一发出去就有独立价值**

   在低纬区域，节点几乎可以按普通或准普通太阳轨道工作。
   如果采用与地球同公转角速度同步的策略，则它们并不是“等待未来联网”的临时构件，而是立刻进入一个可运营的位置。

3. **再向更高纬度逐步扩张**

   随着材料、结构、控制、在轨制造能力改善，系统面密度 $\sigma_{\text{sys}}$ 下降，对应的最大可行纬度 $\phi_{\max}$ 上升，系统就能自然地从低纬带向更高纬带扩展。

因此，MDDS 的理论意义不只是：

- 如何支撑某个单独的位移环

更是：

- 如何定义一条从低纬、低门槛开始，逐渐走向分层 Dyson Swarm 的生长路径

这使它与很多“一步到位”的 Dyson 设想不同。对 MDDS 而言：

> 每一个中间阶段都可以是有用的，每一个已部署节点都可以成为未来更大星周基础设施的一部分。

从这个角度看，MDDS 不只是一个轨道动力学构型，也是一种 **Dyson-progressive architecture**。
