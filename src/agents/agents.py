from dataclasses import dataclass
# 已编译的状态图
from langgraph.graph.state import CompiledStateGraph

from agents.bg_task_agent.bg_task_agent import bg_task_agent
from agents.chatbot import chatbot
from agents.research_assistant import research_assistant
from schema import AgentInfo

DEFAULT_AGENT = "research-assistant"


@dataclass
class Agent:
    description: str
    graph: CompiledStateGraph


agents: dict[str, Agent] = {
    "chatbot": Agent(description="一个简单的聊天机器人。", graph=chatbot),
    "research-assistant": Agent(
        description="一个具有网页搜索和计算器功能的研究助手。", graph=research_assistant
    ),
    "bg-task-agent": Agent(description="一个背景任务代理。", graph=bg_task_agent),
}


def get_agent(agent_id: str) -> CompiledStateGraph:
    return agents[agent_id].graph


def get_all_agent_info() -> list[AgentInfo]:
    return [
        AgentInfo(key=agent_id, description=agent.description) for agent_id, agent in agents.items()
    ]


"""
这段代码实现了一个 Agent 管理系统，主要用于处理不同类型的 AI 代理。以下是详细解释：

1. 核心组件：
- Agent 类：使用 @dataclass 装饰器定义的数据类，包含描述和编译图两个属性
- agents 字典：注册了三种类型的代理：
  * 基础聊天机器人
  * 具备搜索和计算功能的研究助手
  * 后台任务处理代理

2. 功能接口：
- get_agent()：通过 ID 获取特定代理的图结构
- get_all_agent_info()：获取所有已注册代理的信息列表

3. 设计特点：
- 使用工厂模式实现代理的创建和管理
- 采用字典作为简单的注册机制
- 通过 dataclass 简化了数据类的定义，提高代码可读性
- 默认使用研究助手作为主要代理

这种设计允许系统灵活地管理和切换不同类型的 AI 代理，便于扩展和维护。每个代理都有其特定的功能和用途，可以根据需求选择合适的代理来处理不同的任务。

"""
