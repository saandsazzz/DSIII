# DSIII

## 人物属性对各面板能力的影响

黑魂3中通过消耗灵魂来升级人物，每一级可以选择提高一点属性值，这些属性值的提高会加强人物的面板能力，本章通过对升级后的面板能力变化进行分析（分析过程见xxx），总结出各个属性对于各个面板能力的影响。

属性一共有九个：**生命力、集中力、持久力、体力、力气、敏捷、智力、信仰、运气**。

本章计算的面板能力包括：**防御力**（物理、防打击、防斩击、防突刺、魔力、火、雷、暗）**、抵抗力**（出血、毒、寒气、咒死）**、血量、专注值、精力、装备重量、寻宝能力、记忆空格**。

首先可以将各面板分为两类，一类面板能力会受到多个属性的影响，另一类面板能力只会受到单个属性影响。

### 多个属性影响

#### 防御力

防御力有两类，一类是物理：包括**物理防御力、防打击防御力、防斩击防御力、防突刺防御力**；

​                           一类是属性：包括**魔力、火、雷、暗**。

任何一个属性的增加都会造成所有的防御力增加，并且增加幅度基本一致

但是对于物理防御力，体力和力气两个属性有额外的增加幅度。

对于属性防御力，每一个都有一个对应的属性会有额外的增加幅度（不同属性防御力幅度一致）。

（魔力——智力，火——力气，雷——持久力，暗——信仰）

#### 抵抗力

抵抗力的成长类似与属性防御力。

首先任何一个属性的增加都会造成所有的防御力增加，并且增加幅度一致（与防御力的不一致）。

其次每一个抵抗力都有一个对应的属性会有额外的增加幅度（属性值30以后才会有，不同抵抗力幅度一致）。

（出血——持久力，毒——体力，寒气——生命力，咒死——运气）

#### 总结计算公式

根据防御力和抵抗力的增长特点，可以将各面板能力与属性值的关系通过一个通式和函数表来表示。
$$
y_j=\sum_1^9f_{ij}(x_i)
$$
式中x<sub>i</sub>表示各属性值，y<sub>j</sub>表示各面板能力，具体如下表所示，f<sub>ij</sub>根据下表对应查得。

<h3 align = "center">防御力与抵抗力计算函数表</h3>

| <span style="display:inline-block;width:100px"> </span> | <span style="display:inline-block;width:100px">物理(y<sub>1</sub>)</span> | <span style="display:inline-block;width:100px">防打击(y<sub>2</sub>)</span> | <span style="display:inline-block;width:100px">防斩击(y<sub>3</sub>)</span> | <span style="display:inline-block;width:100px">防突刺(y<sub>4</sub>)</span> | <span style="display:inline-block;width:100px">魔力(y<sub>5</sub>)</span> | <span style="display:inline-block;width:100px">火(y<sub>6</sub>)</span> | <span style="display:inline-block;width:100px">雷(y<sub>7</sub>)</span> | <span style="display:inline-block;width:100px">暗(y<sub>8</sub>)</span> | <span style="display:inline-block;width:100px">出血(y<sub>9</sub>)</span> | <span style="display:inline-block;width:100px">毒(y<sub>10</sub>)</span> | <span style="display:inline-block;width:100px">寒气(y<sub>11</sub>)</span> | <span style="display:inline-block;width:100px">咒死(y<sub>12</sub>)</span> |
| :------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 生命力（x<sub>1</sub>）                                 | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | function6                                                    | 0                                                            |
| 集中力（x<sub>2</sub>）                                 | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            |
| 持久力（x<sub>3</sub>）                                 | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | function5                                                    | 0                                                            | function6                                                    | 0                                                            | 0                                                            | 0                                                            |
| 体力（x<sub>4</sub>）                                   | function3                                                    | function3                                                    | function3                                                    | function3                                                    | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | function6                                                    | 0                                                            | 0                                                            |
| 力气（x<sub>5</sub>）                                   | function4                                                    | function4                                                    | function4                                                    | function4                                                    | 0                                                            | function5                                                    | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            |
| 敏捷（x<sub>6</sub>）                                   | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            |
| 智力（x<sub>7</sub>）                                   | 0                                                            | 0                                                            | 0                                                            | 0                                                            | function5                                                    | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            |
| 信仰（x<sub>8</sub>）                                   | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | function5                                                    | 0                                                            | 0                                                            | 0                                                            | 0                                                            |
| 运气（x<sub>9</sub>）                                   | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | 0                                                            | function6                                                    |
| 总和（x<sub>10</sub>）                                  | function1                                                    | function1                                                    | function1                                                    | function1                                                    | function1                                                    | function1                                                    | function1                                                    | function1                                                    | function2                                                    | function2                                                    | function2                                                    | function2                                                    |

#### 各函数公式

通过对各函数分离取整等操作，得到了每一个函数的通式。

这里的6个函数都是分段直线函数，并且在分析时总结出这里的各曲线都是通过确定一些整点然后连接得到的。

以下列出各函数的关键转折点以及其曲线图。

**function1：属性总和增加对防御力的影响**

关键点：（1，40），（150，100），（170，110），（240，120），（891，150）

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/function1_curve.png)



**function2：属性总和增加对抵抗力的影响**

关键点：（1，90），（150，120），（190，160），（240，175），（891，200）

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/function2_curve.png)



**function3：体力增加对防御力的额外影响**

关键点：（0，0），（15，5），（25，22），（40，40），（99，60）

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/function3_curve.png)



**function4：力气对防御力的额外影响**

关键点：（0，0），（30，10），（40，15），（60，30），（99，40）

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/function4_curve.png)



**function5：对应属性对属性防御力的额外影响**

关键点：（0，0），（30，20），（40，40），（60，70），（99，100）

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/function5_curve.png)



**function6：对应属性对抵抗力的额外影响**

关键点：（0，0），（30，0），（40，30），（60，40），（99，50）

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/function6_curve.png)



### 单个属性影响

其余的**血量、专注值、精力、装备重量、寻宝能力、记忆空格**都由单个属性值决定。

（血量——生命力，专注值——集中力，精力——持久力，装备重量——体力，寻宝能力——运气，记忆空格——集中力）

这里**装备重量和寻宝能力**都是**线性增加**，**记忆空格**随着集中力的增加**阶梯式增长**。

而血量、专注值和精力的变化比较复杂，不再是前面的分段直线，部分段为曲线。

曲线应当都是对几个固定点进行插值补充，类似与Hermit插值的方法进行补充，而且插值的方法能够保证函数在插值段是单增函数

由于小数取整等影响，而且部分点的数据完全不符合多项式函数的，难以反推出符合所有值的通式。（计算器中直接存入了99个对应的值）

#### 血量

提高生命力会增加血量，增幅在15、16点生命力时达到最高，15点到27点之间增长幅度依旧可观，27点到50点增长幅度明显减少，50点之后达到最小。

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/HP_curve.png)

#### 专注值

提高集中力会增加专注值，增幅在35点集中力前都是在一直增加，35点之后到99增幅明显减少。

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/FP_curve.png)

#### 精力

提高持久力会增加精力，增幅在40点持久力之前都很可观，40以后到99增幅明显减少。

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/Stamina_curve.png)

#### 装备重量

提高体力会增加装备重量，整体呈线性。

起点：（0，40）	终点：（99，139）

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/EquipmentLoad_curve.png)

#### 寻宝能力

提高运气会增加寻宝能力，整体呈线性。

起点：（0，100）	终点：（99，199）

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/ItemDiscovery_curve.png)

#### 记忆空格

提高集中力会增加记忆空格的数量，在固定阶梯处记忆空格增加，最多为10个。

增长节点：（10，14，18，24，30，40，50，60，80，99）

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/AttunementSlots_curve.png)



### 升级需要灵魂数

升级会提升人物面板能力，同时也需要消耗游戏内货币——灵魂来进行升级。

等级越高，升级需要的灵魂数随之增加，这里升级消耗的灵魂数与等级之间的关系为多项式函数关系

分为两段，10级以前与11级以后，10级以前直接二次函数拟合即可满足所有点。

11级以后用4次函数拟合后基本所有点都落在拟合的4次函数上，函数通式为：

![1](http://latex.codecogs.com/gif.latex?\begin{cases}0.12*level^2+16*level+657.4\\\\-1e^{-12}*level^4+0.02*level^3+3.12*level^2+111.78*level-786.2\\\\\end{cases})

等级:1~10

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/SoulsToNextLevel_curve_1To10.png)

等级:11~802

![Alt text](https://github.com/saandsazzz/DSIII/blob/main/image/SoulsToNextLevel_curve_11To802.png)

### 人物属性计算器

整理所有公式，使用Python中Pyqt5制作了一个简易的人物属性计算器，对不同出身下人物升级后的面板以及所消耗的灵魂数进行计算。

计算器打包在**人物计算器.exe**中，py代码在文件夹中。
