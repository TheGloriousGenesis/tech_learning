# C3

Types are the unit component of c3 that can be used across all points 

c3 type is agnostic description of potential complex object in the system

declarative by nature

 The C3 AI Type System serves as an abstraction layer that unifies all technologies under the same system. 
 
C3 Agentic AI Platform can be deployed with any cloud provider


## Types

### Core components

 The C3 AI Type System serves as an abstraction layer that unifies all technologies under the same system. Everything is a type
 (even cluster!)

| Name        | Description                                                                                                                                  |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Cluster     | logical abstraction of all software needed to deploy c3 ai on prem or cloud                                                                  |
| Environment | (similar to namespace in a multi-tenant environment) logical abstraction of part of cluster partitioned away for deploying specified applications |
| Application | ai/ml/genai model. Logical partition that users/devs interact with. Deployable piece of software                                             |


### For ML
| Name             | Description                                                        |
|------------------|--------------------------------------------------------------------|
| Feature store    | reuse features across different applications                       |
| Model registry   | Reuse pipelines (models) and share them                            |
| Environment      | configuration partition that can be single node or shared          |


### For feature engineering
| Name            | Description                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------|
| Canoncial types | inbound data schema validators (think pydantic)                                              |
| Transform       | Define transformations from one source to another (think of transformers in scikit learn way |

## Attributes 

- One can make types persistable using the `entity` keyword when defining the declaration of the type.
- One can obtain information from persistable types via the `eval` / `fetch` method. `eval` obtains the actual data in 
tabular format, whereas the `fetch` obtains the type representation of the data (allowing you to execute type methods on
on it)

### Inbuilt

There are some prebuilt types so that you do not have to reinvent the wheel

| Name             | Description                                                                  |
|------------------|------------------------------------------------------------------------------|
| Facility         | Similar to digital twin, maps physical processes (inputs to oil well)        |
| Asset/Sensor     | Model industrial processes                                                   |
| Alert/Work Order | When attribute of asset gets to certain level, this can be set up to trigger |
| MIModel          | generate predictions for assets                                              |
| MIPipeline       | stores all needed to run pipeline                                            |


![img_1.png](img_1.png)

## Architecture

C3 Cluster is the entry point to ai platform

Cluster contains environments and environments contain applications

Environments can either be Single node or shared node. In both cases theare must be a leader node and a task node. In the SNE case,
the single node acts as both the leader and task node. Environments are isolated and do not share with other environments
but do share processes/resource from main cluster

C3 AI utilise the following to speed up development:
- Asynchronicity: multiple jobs can be done at onces
- Parallelism: Same job can be split apart into smaller units and done at the same time
- Autoscaling: more or less resources allocated as needed 
- Queues: Organize related jobs to parallelize work and run asynchronous logic in the background


## Testing

Software engineering systems and machine learning systems differ in regards to testing and behaviour. 
In software engineering, one tests on the code and the behaviour is consistent, in ml systems you also need tests on the
data as the data changes the behaviour of the system.

![img.png](img.png) (reference: https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/)



feature definitions (stored)
feature materialisation (executed feature defintions on assets to create the data needed)




