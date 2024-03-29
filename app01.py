import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
os.environ["OPENAI_API_KEY"] = "sk-"
os.environ["SERPER_API_KEY"] = ""
# 创建搜索工具
search_tool = SerperDevTool()

# 定义代理
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI and data science',
    tools=[search_tool],
    allow_delegation=True,
    backstory="I am a seasoned research analyst with over 10 years of experience..."
)

writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about AI and data science', 
    tools=[search_tool],
    allow_delegation=False,
    backstory="I am a talented writer passionate about telling stories that inspire and educate."
)

# 定义任务
research_task = Task(
    description="Identify the next big trend in AI and data science...",
    agent=researcher,
    expected_output="A detailed report on the next major trend in AI and data science, including its potential impact, key drivers, and challenges."
)

write_task = Task(
    description="Compose an insightful article on AI and data science advancements...",
    agent=writer,
    expected_output="A well-written and engaging article discussing the latest advancements in AI and data science, suitable for publication in a tech magazine."
)

# 创建队伍
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

# 启动队伍
result = crew.kickoff()