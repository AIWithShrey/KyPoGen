# Kypogen Crew

Welcome to the Kypogen Crew project, powered by [crewAI](https://crewai.com). This project demonstrates the automated generation of Kyverno policies using AI agents. The KyPoGen Crew is a collection of AI agents that work together to generate Kyverno policies and validate them against a hypothetic Kubernetes cluster.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

If using other LLM providers, add the respective API keys to the `.env` file.

**Add your `GEMINI_API_KEY` into the `.env` file**

- Modify `src/kypogen/config/agents.yaml` to define your agents
- Modify `src/kypogen/config/tasks.yaml` to define your tasks
- Modify `src/kypogen/crew.py` to add your own logic, tools and specific args
- Modify `src/kypogen/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the KyPoGen Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `policy.yaml` and `report.md` file with the output of the agent generated policies and the report of the validation.

## Understanding Your Crew

The KyPoGen Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding crewAI:
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)
