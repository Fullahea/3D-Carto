from crewai import Task
from textwrap import dedent
from 任务prompt import Produce_DCM1,Produce_DCM2
from 任务prompt import Evaluate_DCM
from 任务prompt import Control_Process
class CartoTask():
    def produce_DCM(self,agent,userinput):
        return Task(
            description=dedent(Produce_DCM1+Produce_DCM2+userinput),
            agent=agent,
            expected_output="All you need to do is generate XML"
        )
    def evaluate_Generation(self,agent,context):
        return Task(
            description=dedent(Evaluate_DCM),
            expected_output="Generate one report about the evaluation",
            context=context,
            agent=agent
        )
    def control_Process(self,agent,context):
        return Task(
            description=dedent(Control_Process),
            context=context,
            expected_output="Only output the XML",
            agent=agent
        )