#描述代理行为
from crewai import Agent

class CartoAgents():

    def produce_DCM_agent(self):
        return Agent(
            role='Parsing user input',
            goal=f'Extract key information from the user_input according to the rules and generate the right XML.',
            backstory=f"""The generation rules and examples of the XML file will be given in the tasks. You need to 
                      understand both rules and examples so that you can extract the right key information from user 
                      input. """,
            max_iter=10,
            verbose=True
        )
    def evaluate_DCM_agent(self):
        return Agent(
            role='Evaluate the generation according to the scoring standard',
            goal='Ensure that the generated XML meets the expected standards',
            backstory=f"""You can understand the rules of how to evaluate the XML correctness. Consider with the 
                      examples, give the suitable score report""",
            verbose=True
        )
    def manager_agent(self):
        return Agent(
            role='Coordinate agents in this program',
            goal="""Make sure the parsing and conversion process runs smoothly and check the final result.""",
            backstory=f"""You are the manager of this program, ensure that the analytical generation and evaluation 
            processes run smoothly, and check the final results.""",
            # llm='gpt-4',
            verbose=True
        )
