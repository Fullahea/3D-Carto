from crewai.utilities.token_counter_callback import TokenCalcHandler
from crewai import  Process
class TokenTrackingProcess(Process):
    def __init__(self, tasks):
        self.tasks = tasks
        self.total_tokens = 0

    def execute(self, inputs):
        results = []
        for task in self.tasks:
            token_handler = TokenCalcHandler(task.agent.llm.model_name)
            task.agent.llm.callbacks = [token_handler]
            result = task.execute(inputs)
            results.append(result)
            task_tokens = token_handler.total_tokens
            self.total_tokens += task_tokens
            print(f"Task '{task.description}' used {task_tokens} tokens.")
        print(f"Total token usage: {self.total_tokens}")
        return results