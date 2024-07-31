import os

from crewai import Crew, Process
from textwrap import dedent
from agents import CartoAgents
from tasks import CartoTask


from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]=os.getenv("OPENAI_MODEL_NAME")


class CartoCrew:
    def __init__(self,userinput):
        self.input=userinput
    def run(self):
        #多个agents和tasks实例化
        agents=CartoAgents()
        tasks=CartoTask()
        #具体agent、task实例化
        produce_agent=agents.produce_DCM_agent()
        evaluate_agent=agents.evaluate_DCM_agent()
        manager=agents.manager_agent()
        #有了相关任务函数类，来实现具体任务
        produce=tasks.produce_DCM(
            produce_agent,self.input
        )
        evaluate=tasks.evaluate_Generation(
            evaluate_agent,[produce]
        )
        control=tasks.control_Process(
            manager,[produce,evaluate]
        )
        #用crew流程来实现，目前是顺序
        crew=Crew(
            agents=[produce_agent,evaluate_agent,manager],
            tasks=[produce,evaluate,control],
            # manager_llm=manager,
            verbose=True
        )
        result=crew.kickoff()
        return result


if __name__ == "__main__":
    userinput= input(
        dedent("""
        请输入语句：
    """))
    do = CartoCrew(userinput)
    result = do.run()
    print("\n\n########################")
    print("zzz")
    print("123")
    print(result)