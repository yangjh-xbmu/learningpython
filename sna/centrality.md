# 中心性、权力与瓶颈

## 样本数据

LiveJournal 是一家在俄罗斯和东欧地区受欢迎的博客网站，它提供了简单的API接口可用于数据挖掘。

### 从LiveJournal获得数据

下面的代码将利用LiveJournal的API接口，获得指定用户的朋友关系：

```python
import sys
import os
import networkx as net
import urllib.request


def read_lj_friends(g, name):
    response=urllib.request.urlopen('http://www.livejournal.com/misc/fdata.bml?user='+name)
    for line in response.readlines():
        if line.startswith(b'#'): continue 
        
        parts=line.split()
        
        if len(parts)==0: continue
        
        if parts[0]=='<': 
            g.add_edge(parts[1],name)
        else:
            g.add_edge(name,parts[1])
```

上述函数的第一个参数g，为图对象，由节点、边与代表朋友的人名构成；另一个参数name，为用户名，将查询该用户在LiveJournal网站中的朋友信息（即关注和被关注）。

### 滚雪球抽样

人类对社会网络存在“可观测性的界限”（Horizon of Observability）,我们能很好地感知到谁是朋友，但是我们对朋友的朋友、朋友的朋友的朋友的认知水平会迅速下降，我们几乎对朋友的朋友的朋友几乎一无所知。

基于上述现象，我们通常会限制搜索到二级水平（朋友的朋友），为围绕中心者的社会网络提供一个相当完整的图。要达到上述目的，我们可以采用滚雪球抽样法：

1. 开始于一个中心节点
2. 获得中心节点的朋友
3. 对于每一个朋友：对他们的朋友进行抽样
4. 对于朋友的朋友，对他们的朋友进行抽样
5. 以此类推

Python的滚雪球抽样，可用递归来实现：

```python
def snowball_sampling(g, center, max_depth=1, current_depth=0, taboo_list=[]):
    print(center, current_depth, max_depth, taboo_list)

    if current_depth == max_depth:
        print('out of depth')
        return taboo_list
    if center in taboo_list:
        print('taboo')
        return taboo_list
    else:
        taboo_list.append(center) 

    read_lj_friends(g, center)

    for node in g.neighbors(center):
        taboo_list = snowball_sampling(g, node, current_depth=current_depth+1, max_depth=max_depth, taboo_list=taboo_list)

    return taboo_list
```

### 保存数据到本地文件

保存文件可以使用Pajek的文本格式：

```python
net.write_pajek(g,'lj_friend.net')
```

## 中心性

分析社会网络的主要方法是测量它的权力、影响力，即**中心性**。

### 网络中谁更重要

中心性的含义通常首先看“它的依赖”，它取决于连接的节点是否有信息交换或者职责关系，取决于对所需的权力和影响力的认知作为输出。

### 发现“名人”

程度中心性（degree centrality），节点度（node degree）简单来说，就是所有与它有关的连接数量。程度中心度高，还要看联系及关系的性质。但无论如何，程度中心性是理解社会网络的一项非常有用的测量指标。

### 发现八卦传播者

### 发现传播瓶颈或社会桥梁

### 整合

### 谁是灰衣主教

### PageRank



## 中心性测量不能告诉我们什么

中心度测量不能告诉我们人们为什么在争论中的站队，是什么力量使得网络连接在一起，又是什么离间了他们。对于上述问题，我们必须深入节点层面的测量指标，通过三元组，可以挖掘出更大的派系和聚类。
