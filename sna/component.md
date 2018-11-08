# 派系、聚类和组元

中心性分析，主要是在个体层面进行分析。对社会网络的分析单元，还可以是子图和聚类特征。

## 组元和子图

**子图**(subgraph)是由一个网络的部分节点及这些节点之间的连接构成的。任意一组节点可以构成子图。

**组元**(component)是网络中相互分割的部分。

许多真实的网络中，尤其是那些通过随机抽样搜集到的网络数据，存在很多组元。

### 使用Python分析组元

NetworkX中提供了`connected_component_subgraphs()`方法计算网络中存在的组元，这个命令可以根据各个相互关联的组元返回其响应的图对象的数组生成器。

```python
import networkx as net
import matplotlib.pyplot as pyplot

e = net.read_pajek("egypt_retweets.net")

print('埃及革命推特转发网络的长度为：', len(e))
print('埃及革命推特转发网络中的组元数量：', sum(1 for _ in net.connected_component_subgraphs(e)))
```

我们需要剔除一定的组元规模，如组元规模小于10的情况：

```python
x = [len(c) for c in net.connected_component_subgraphs(e) if len(c) > 10]
print(x)
```

结果输出为：

```python
[17762, 64, 16, 13, 11, 11, 14, 16]
```

表明在转发网络中存在一个巨大的组元（超过17000）。

### 网络中的岛屿

有一种分析网络的技术称为“岛屿方法”（the island method）,这种方法尤其适合分析权重网络，如推特转发网络。使用“岛屿方法”意味着大的组元将被分割为小的组元，并且具有最多转发量的区域可以各自称为被单独分析的组元。

使用岛屿方法的关键是，确定合理的“水平面高度”，这个命令使用一个门槛数值（也就是说水平面高度）对图进行操作，使得权重超过该门槛值的边保存下来，移除剩余的边。

## 子图——自我中心网

## 三元组

## 分层聚类

## 三元组、网络密度和冲突
