import os
import xml.etree.ElementTree as ET
from crewai import Agent, Task, Crew, Process


# 自定义函数：解析用户输入
def parse_input(user_input):
    # 简单的示例解析逻辑
    parsed_info = {"name": "Example", "value": user_input}
    return parsed_info


# 自定义函数：转换为XML格式
def convert_to_xml(parsed_info):
    root = ET.Element("root")
    for key, value in parsed_info.items():
        child = ET.SubElement(root, key)
        child.text = value
    return ET.tostring(root, encoding='unicode')


# 自定义函数：执行解析任务
def perform_parse_task(task_prompt):
    parsed_info = parse_input(task_prompt)
    xml_output = convert_to_xml(parsed_info)
    return xml_output


# 自定义函数：执行评价任务
def perform_evaluate_task(xml_output):
    # 简单的示例评价逻辑
    errors = []
    try:
        root = ET.fromstring(xml_output)
        if root.find("name") is None or root.find("value") is None:
            errors.append("XML格式不正确或缺少必要信息")
    except ET.ParseError:
        errors.append("XML解析失败")

    if errors:
        evaluation = {"status": "失败", "errors": errors}
    else:
        evaluation = {"status": "成功", "message": "XML符合预期"}

    return evaluation


# 定义智能体
parser_agent = Agent(
    name="解析模块智能体",
    role="解析用户输入",
    goal="从自然语言输入中提取关键信息并生成XML",
    backstory="你是一名语言解析和数据格式化专家，擅长从文本中提取重要信息并将其转换为XML格式。",
    verbose=True
)

evaluator_agent = Agent(
    name="评价智能体",
    role="评价生成的XML",
    goal="确保生成的XML符合预期标准",
    backstory="你是一名质量控制专家，负责检查和评价XML输出的质量。",
    verbose=True
)

manager_agent = Agent(
    name="经理人智能体",
    role="控制流程",
    goal="协调解析和评价过程，并根据评价结果进行调整",
    backstory="你是一名项目经理，负责确保项目按计划顺利进行。",
    verbose=True
)

# 定义任务
parse_task = Task(
    name="解析任务",
    description="解析用户输入的自然语言，并提取以下关键信息：姓名和值，并将其转换为XML格式。",
    expected_output="生成的XML文件。",
    agent=parser_agent
)

evaluate_task = Task(
    name="评价任务",
    description="评价解析任务生成的XML，确保其符合以下标准：XML格式是否正确，提取的信息是否完整。",
    expected_output="评价报告或反馈。",
    agent=evaluator_agent
)


# 自定义控制流程
def control_process(user_input, max_attempts=3):
    for attempt in range(max_attempts):
        print(f"尝试 {attempt + 1}: 执行解析任务")
        xml_output = perform_parse_task(user_input)
        print(f"解析任务结果: {xml_output}")

        print(f"尝试 {attempt + 1}: 执行评价任务")
        evaluation = perform_evaluate_task(xml_output)
        print(f"评价任务结果: {evaluation}")

        if evaluation["status"] == "成功":
            return xml_output, evaluation
        else:
            print("评价不通过，重新执行解析任务。")

    return xml_output, evaluation


# 创建并启动团队
agents = [parser_agent, evaluator_agent, manager_agent]
tasks = [parse_task, evaluate_task]

crew = Crew(agents=agents, tasks=tasks, process=Process.sequential)
user_input = "示例输入文本"

# 执行控制任务
final_output, final_evaluation = control_process(user_input)
print(f"最终输出: {final_output}")
print(f"最终评价: {final_evaluation}")
