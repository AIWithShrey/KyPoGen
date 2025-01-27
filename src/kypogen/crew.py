from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv, find_dotenv

@CrewBase
class Kypogen():
    """Kyverno Policy Generation and Validation Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def policy_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['policy_generator'],
            verbose=True,
        )

    @agent
    def policy_validator(self) -> Agent:
        return Agent(
            config=self.agents_config['policy_validator'],
            #tools=[tool],
            verbose=True,
        )

    @task
    def generate_policy(self) -> Task:
        return Task(
            config=self.tasks_config['generate_policy'],
            agent=self.policy_generator()
        )

    @task 
    def validate_policy(self) -> Task:
        return Task(
            config=self.tasks_config['validate_policy'],
            agent=self.policy_validator(),
            output_file='output/report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.policy_generator(), self.policy_validator()],
            tasks=[self.generate_policy(), self.validate_policy()],
            verbose=True,
        )