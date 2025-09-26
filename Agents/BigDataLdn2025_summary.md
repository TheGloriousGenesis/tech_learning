## Tips and tricks for how to get better results from LLM+MCP conversations

Before you would need to prompt a llm which will then reply. Now the reply goes through an agent before it is returned to user

Context is king!

Tip - Use markdown files to describe what you want to achieve. Very long
context and describe all steps is better than docstrings and writing in code! both should be done haha.

Tip - Focus on error messages! Be descriptive and recovery messages on what to
do next in error messages

Tip - Self healing loops (do iteration checks on format and quality of what is produced (have a critic) then execute or return results to user)

Blueprints are the new code!

Have MCP server read sql and write ai readable descriptions

Agent controller (master agent) have access to MCP

## Agents of Change -- Will AI Agents Be the Next Hype Bubble, or Transform Companies Forever? 

Governance (stack traceability even integration to  GitHub to see where the problem occurs)

Maia Context files to generate pipelines (instead of) Structure

Get the data and build something that works

Set up training (what it does and what it doesn't do)

Writing detail prompts

## Machine Scale vs. Human Scale: The Looming Crisis in Data Engineering

Maia

A2A

Exposes data from central team

Collaborative working (can generate pipelines that look like your code,
also can work with pipelines already generated)

Senior engineer working like tech lead

Commit documentation

## Agentic AI Architecture - how to use LLMs at enterprise scale

Genai platform architecture: You have tracking and monitoring, inference, tuning, CICD. 
Tracking and monitoring: includes logs and metrics that feeds into a monitoring dashboard period.
Inference: includes an application that has a store of prompt templates, which term is a combination of prompt construction augmentation model scoring and some post processing results are then returned to the application.
Tuning: includes source data being provided to the system to curate context (this can be provided in documents or even better as RAG) which is then stored in the vector store which helps augment prompts with additional information. alongside this, the underlining model undergoes fine tuning which is based on a foundational model being tailored to this given business usecase

Agent AI architecture / Multi-agent Patterns:
1. Refinement/reflection agent
2. Prompt chaining of tasks (finance analyst agent: data -> trend analysis)
3. Routing (this requests need specialised agent e.g customer support requests should be handled by retail chatbot )
4. Parallelisation
5. Orchestror/Planner (big agent that summarises all info from other agent)


An Agent consist of:
- brains (LLM) 
- memory (Context - history of prompts/answers) 
- tools (for actions)

To create a good agent/prompt you must tell the agent/prompt what it is! Describe it's Role, Goal, Behaviour, Purpose

Create Agent personas: Tuned and trained to have a certain role

Best practices with agents:
- Define clear contracts
- enable agent discovery
- apply versioning, 
- evolution communication of new versions 
- implement monitoring (obtain metrics, this is important!)
- allow polyglot language / systems

Agents are autonomous, modular, loosely coupled, scalable, distributed -
similar to common patterns we have now: microservices, object orientated, service oriented architecture
Agents are the new microservices


## Can MCP be more than just the latest way to codify our stubbornly opinionated data egos?

Keboola

## From Dev to MVP in Less Than 30 Days: Real-World Lessons from Databricks

Engineers Have strong narrative : 1 page slide so people can promote you
MVP

Log blockers and risks

Think legislation, third party, proprietary software have measurable
metrics

Ship core functionality first. Polish later

Time, revenue and risk (translate tech to business wins)

Regular check ups in finance legal security


## FastMCP: Model Context Pragmatism Prefect built FastMCP

Aaazzam VP of product

### Why MCP:

Humans are orchestrators - we are the integration layer

Solving cross coordination problems

Nowadays the workplace is the LLM interfaces

Great for one shot atomic pass but not good context. They can only
orchestrator what they can access

How do i bring context to LLM interfaces Trying Inject business logic to
UI

We are trying to offload our tasks to LLM (humans are orchestrators but now we want to offload to llms!)

Orchestrator requires Workflows Resources Tools Who is asking (state)

Context makes capabilities dynamic! What you can do depends on what
information you can provide

### Why not REST? 

API's have fixed capabilities and are stateless

For LLM you need runtime discovery, bidirectional communication to communicate state
Eg someone who logs in to a service will now change the state of what's available for user to use

MCP is orchestration protocol

They allow stateful bidirectional interaction (rpc) of things
(capability discovery)

Protocol Resource Tools

MCP allows one central contract instead of many plugins

Open source tool to test out fastmcp servers deployed : FastMCP cloud - by Prefect

### What MCP doesn't have

MCP: is opinionated about state , Ecosystem and Deployments

currently many mcp servers are used as static tool servers because being dynamic is hard

1.  State is hard to do. Priority externalising session state. Protocol
    built for single server serving single session. What breaks: pod death equals a loss of context hence the 
    reason it can't scale horizontally. when a server crashes a user can lose 20 minutes of work for example. 
    the problem is mCP service assumes statefullness but modern infrastructure assume statelessness. 
    The solution to this is to externalise session state to a Redis or database, design service to be ephemeral,
    build resumable operations, accept that horizontal scaling was not designed for MCP services.

2.  MCP compatible Clients lagging behind. To work with client limitations, ship advanced features with fallbacks and 
    if possible prioritise building per client MCP capabilities; for example have a tool that lists the resources as well as resources defined in MCP (e.g resources -> `list_resources`)

3.  Observability is hard. Observability workarounds include building service side logging that captures context, track which tools get called within a session to proxy intent, or author a feedback tool or Qwargs in tools function argument that the agent can populate e/g `user_intent: str | None`.
    This will look like product analytics, using client telemetry in the future to guild development.

### What's MCP has figured out and what you should/shouldn't be doing

1. Do not burn tokens on decision making. 
2. MCP Anti pattern is dumping your API. E.g dont expose `get_customer() + get_orders() + check_status()`, expose `investigate_customer_issues()`. You are increasing decision space, you must reduce it. If you don't can lead to poor tool selection!
3. MCP pattern - Hyper curating: cut down the decisions. Describe workflows and when
    to use it. Think about the Agent story vs User story. Design for agent thinking! Curate obsessively. Flatten decision tree. Dynamic
    namespacing of tools whilst clients interact with the system can help so agent is only shown what it needs (different tools for different roles/states)
4. MCP Pattern - internal expertise engines pattern: Encode your top performers workflows!
5. Pre plan every path, dont make the llm figure out sequencing
6. MCP Pattern - Cross system orchestration: across different systems internally to communicate in one centralised place - the MCP server (solve
48 browser tab problem). This hides complexity from llm and maintains consistency across systems
7. MCP Pattern - Investifate assistant: Gather and reconcile fragmented data. Returns synthesized context not raw data. This handles correlation complexity!



## Knowledge Graphs as a Reasoning Engine: Deploying Agents To Uncover Deep Insights in Your Connected Data 

Reasoning is the cognitive process of deriving knowledge from evidence

LLM limited to data they have been trained on, RAG offers solution and retrieves info

With the new graph reasoning agent what occurs is the orchestrator, which is a language model, has access to a state graph. 
The language model also has access to tools via MCP in which it can call in order to execute certain functionality.


## Small Language Models Beginners course

Small language model (SLM): at or below 12 billion parameters
Large language model (LLM): above 12 billion
NOTE: Above is rough estimations that can be modified depending on business need


SLM: use for specialist models
LLM: use for generalist models, complex reasoning

Pros SLM:

- Cost, power (paper - large language models: significant cost)

### Developing agents:

Read Open AI has a practical guide to building agents

Start with baseline - what does good look like

Choose best model that does that

Read Nvidia small langue models are the future of agent ai

Keep LLM for orchestrator/reasoning of complex task, SLM for specialise agents/ small tasks



#### Quantization 
Chose quantization level to save money too. 
Quantization describes level of detail the weights of the LM are saved as. 
Better Quantization can sometimes cost less money, be faster and have better performance (good for inference endpoints)

E.g Q4 quantization (8 times smaller, good for edge devices, local)

Tip: don't go below q4 in many cases

#### Distillation 

Description : Have teacher model train student model. Can save money

### Choose your deployment pattern

#### Local deployment 

Utilise redits, local llama LLM community

ensure you have good hardware as well

To utilise quantised models ollama and LM studio is helpful to read the llama.Cpp files

Oollama needs to be manually configured in windows machines to use the correct GPU

In oollama you have to create custom model file to obtain model of
quantize level you want

After you create model, you can select and copilot

Can use continue.dev too

Ollama and LM studio provide great engines to run small language models on local hardware.
This route provides maximum privacy and works off-line but requires investment in equipment and maintenance

#### Managed cloud platform

- data stays in tenant
- use AWS sagemaker and jumpstart

- Using databricks example utilisation : use huggingface cli to download model in uc volume, then use python wrapper
(using transformers), declare unity catalog and deploy (serverless
endpoint) 

- leverage the cloud to access a wide way of models securely keeping data within your company tenant. this requires setting up deployment pipelines and supporting any custom points made

#### Cloud api access

Pay by token

could deprecate old api endpoints, be careful!

using huggingface interface API playground

As context increases, token increases, money increases

Start with performance, baseline then challenger,

Always look at the license

Use the instruct version of the model if available

## Must read articles and guides

- Book: Hidden technical debt in machine learning systems (similar issues to what we see in agents today too)
- GDS Agent: A graph Algorithmic Reasoning agent (first LLM that can do reason on graphs: e.g user will ask NL question and the agent understands the implicit graph base nature of the question, selects correct graph algorithm, executes it on the knowledge graph, obtains accurate grounded answer)
- OpenAI agent development practical guide (With agent development: establish a baseline to measure perfomance, iterate on accuracy, optimise for efficency)
- Nvidia Language models are the future of agentic AI (use small language models to reduce latency and infrastructure cost, implement modular design where small language models are used for routine tasks and reserve large models for complex reasoning, rapid specialisation find tune agile small language models for specific tasks to enable faster iteration)

## Companies of high interest

### Matillion - Maia

They have created a platform called Maia which looks to augment the data engineer role (and even slightly the data scientist role) regarding generating pipelines.

They have context files which they use to create pipelines from natural language. In these context files, They describe heavily the business landscape,
the data landscape, security standards and how to generate each section of the pipeline: pipeline context, data sources, business rules that are associated with that pipeline.
They translate business language into data pipeline language in that manner. 

AGENT AUGMENTATION TASK: Look into Maia's context files they use to generate complex pipelines using natural language and give a brief description. State pros and cons and current usecases.

### Prefect - Preface

Prefect is a workflow orchestration framework built for building python pipelines. By adding wrappers to code, information is exposed on the dashboard.

They also have some open source infrastructure generation 

Repository: https://github.com/PrefectHQ/Prefect

AGENT AUGMENTATION TASK: Look into Prefect and describe their infrastructure generation capabilities, the pros and cons and current usecases

