# 定义了几个具有不同能力的agents

from agents.agents import DEFAULT_AGENT, get_agent, get_all_agent_info

__all__ = ["get_agent", "get_all_agent_info", "DEFAULT_AGENT"]

"""
这个 __init__.py 文件是一个包初始化文件，它的主要作用是：

1. 包定义：
- 将所在目录定义为一个 Python 包
- 使得目录中的模块可以被导入

2. 接口暴露：
- 通过 __all__ 明确定义了包的公共接口
- 只暴露三个特定的对象：
  * DEFAULT_AGENT：默认代理
  * get_agent：获取代理的函数
  * get_all_agent_info：获取所有代理信息的函数

3. 使用示例：
```python
# 可以这样使用
from agents import get_agent, DEFAULT_AGENT
# 或者
from agents import *  # 只会导入 __all__ 中列出的三个对象
```

这种设计提供了良好的封装性和接口清晰性，使包的使用更加简单和可控。它遵循了 Python 的最佳实践，通过明确的接口定义来控制包的使用方式。

"""
