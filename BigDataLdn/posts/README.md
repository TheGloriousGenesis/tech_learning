# Big Data London Conference

A detailed summary of the things I've learned during my time at BigDataLdn Confernce 2024!

tags: AI, platform, tools

## Business Value in AI
Multiple steps can be taken to ensure sustained sponsorship: [Microsofts AI strategy roadmap](https://info.microsoft.com/ww-landing-AI-Strategy-Roadmap-Navigating-the-stages-of-AI-value-creation.html)
- Find the strategic initiative of the company (company wild OKRs) and align with them. 
- Find what the business strategy is for the firm, acquisition Strategies 
  - Horizontal acquisition - buying competitors: 
    - Sales growth: Buy companies for their client/customer bases
    - Regional expansions: Enter new markets by acquiring local businesses in same sector with existing infrastructure (e.g offices).
    - Industry roll-up: Consolidate fragmented markets by buying smaller competitors to dominate market share.
    - Diversification: Reduce risk by buying companies in unrelated sectors (e.g tech company buying logistics company)
    - Full Service Expansion: Broaden offerings by acquiring complementary services (e.g hairdresser purchasing beauty salon).
  - Vertical acquisition - buying suppliers/distributors
    - Backward integration acquiring suppliers
    - Forward integration controlling distribution (e.g brewery owning pubs)
    - Balanced integration managing both production and distribution internally
  - Innovation & Product Development
    - Cutting edge R&D
    - New product launches
    - 
## Platforms
Platform tools, a one stop shop for creation, deployment, runtime (monitoring operations) are becoming more mainstream as people want a centralised place to maintain the full life cycle of a product as platforms, at their core, must enable data centralisation, and data centralisation is what people want. They dont want to use multiple tools. They want centralised asset management.

### Features of platform
- Data product request, management
- Search & Find data assets
- Metadata management
- Integrate with other products to explore analytics more
- Deals with consumer side movement:
	- Catalog
	- Quality checks
	- CI/CD
	- Governance
	- Lineage
- **FEATURE ADD**: Business usecase builder
- Integrate your outputs/analytics

### Tooling that supports platform (manage data product lifecycle)
- #DataContract[[BigDataLDN#DataContract]]
- Catalog lineage (similar to data lineage but for catalog entries): through versioning
- ==FEATURE ADD: We could have quality checks & Notifications when schema has changed (e.g column name or type) and the downstream impact. Then create notification on  GithubPR  to state X has changed and the upstream/downstream impact==

### Metrics
Platforms must include metrics at all points of the data product cycle:
- During deployment time (using the tool to execute pipelines and create deployment), collecting data surrounding user behaviour is beneficial. 
- At runtime (model actually executing), collecting data regarding how the data is interacting with the model - model drift, number of hits the model takes etc) ==what metrics are taken at runtime==

### Buy or create?
Creation use to bring about the innovation many companies require. But due to the influx of high quality software on the market that is specialised, the innovation is now happening on the business logic side (which falls in line with less custom code, more scalable well built sturdy components). Example: Palantir started with propertiary software, and later moved onto buying from competitors to improve their winning edge

## #Governance
There are now focuses on governance. People don't want to have to worry about whether they are compliant with the latest is regarding governance, so now separate platform have arisen to deal with it e.g Blindata etc. ==Maybe we could integrate with AI4DP to cover this section in MA?==

There are three types of governance:
- Compliance governance:
	- Data governance: framework that manages the availability, usability, integrity, and security of data used in AI systems. Ensure the right people have access to right data too.
- Ethical governance: Ensure responsible AI practices
- Operational governance: 
	- Model governance: How is the model behaving: lifecycle management of AI models. It ensures that models are developed, validated, deployed, monitored, and updated in a responsible manner
	- Managerial governance: who owns the model, who is accountable

Parts of governance also include good documentation, model observability (coda), vetted usecases (cortex)

## DataMesh
Lots of discussion around data mesh architecture

Is about weaving domains that deal with the data at different points of the data processing cycle

Data mesh is hard to implement, #DataContract ==can be used to aid instead==

## DataProduct
Another word for use case, kedroservice

## GraphRAG
Microsoft copilot uses GraphRAG!

Data in different parts of a company could use the same words but mean different things (different concepts/semantics). If you train a model on the corpus of data in your enterprise without a domain specific understanding on the words and their meaning, the output of the model will be nonsense. To create a data product that is interoperable across different domains in the firm the product must make sense at the following levels:
- semantic level
- product level
- physical asset
- technical metadata

Market volatility for GenAI can make future proofing solutions difficult (e.g due to lack of explainability)

Hence mixing knowledge Graphs (old ML method) with #GenAI (new AI model) can help deal with that. Knowledge graphs are people centric (as the people in the company, usually one person from each domain, must agree on the ontology). This is enterprise ontology, when used with LLMs,  helps with explainability issue of LLMs

#GraphRAG can improve LLMs (neojs) ==Include paper==

#knowledgemesh 
![[Pasted image 20240921223404.png]]
### Team set up
Using a enterprise ontology means there will be two teams when developing: The modelling team deals with knowledge graph modelling, and the data product team deals with the data product implementation
![[Pasted image 20240921223326.png]]

## #DataContract
Data contract is a data API

Why not just use APIs?   
Data contracts ensure the quality and format of the data, while API contracts define the technical interfaces required to access and integrate this data into various applications and systems.

Data quality is the main issue that still arises when using data products
- There tends to be 50:1 software engineers to data engineers, with 80% incidents originates from unexpected upstream data quality issues, 70% data development time spent on bespoke non-scaleable validation tasks
- Data contracts help catch issues prevalent in this image regarding **change management**, where rapid change in microservices could have affects further down the line without those changes being communicated:
![[Pasted image 20240920104228.png]]

Data contracts can also help enforce #Governance programmatically. It also helps consumers of the data see whats coming and reduce the reactive state of software engineers.

==POSSIBLE ADD: Possible change detection done on a S3 level to check if data matches contracts in application==

## #Metadata
There is a strong focus about metadata management. There is currently no industry standard for metadata management and everyone has their own way of implementing a solution. Its become important to be able to search and manage this additional data and utilise it in different areas of the company. Data catalogs like glue could be helpful to seeing how we can improve catalog service to be up to par with industry standard.

## #GenerativeAI vs #PredictiveAI
- Predictive: Using algorithms that output based on probabilistic models, or have defined boundaries to classify, usually trained on labelled data ==is unsupervised learning predictive?==
- Generative: Generates new data from trained dataset, predicts new items and data is not labelled.

## Papers and Surveys:

- The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed: https://www.rand.org/pubs/research_reports/RRA2680-1.html
- 2024 State of Analytics Engineering: https://www.getdbt.com/resources/reports/state-of-analytics-engineering-2024

### Interesting reads:
- Uber has more than 2200+ stateless microservices in production. Understanding what they set up in place to manage and deliver their product could be handy to mirror: 
	- https://www.uber.com/en-GB/blog/up-portable-microservices-ready-for-the-cloud/
	- https://www.uber.com/en-GB/blog/microservice-architecture/
	- https://www.infoq.com/news/2023/10/uber-up-cloud-microservices/

### Upcoming conferences:
- Super computer https://sc24.supercomputing.org/


___


### Azure Data Fabric

- **Microsoft Intelligent Data Platform:** Azure Data Fabric is part of Microsoft’s intelligent data platform, designed to facilitate seamless integration and management of data across various services.
- **OneLake Integration:** The platform’s OneLake feature communicates effortlessly with other CRM tools behind the scenes. It can also mirror data, ensuring users do not need to worry about the physical location of their data.
- **Integrated Governance:** Azure Data Fabric provides integrated governance, managing analytics and serving AI models while integrating with the entire suite of Microsoft products. However, users may find themselves locked into the Microsoft ecosystem after adoption.

### IBM WatsonX

- **Core Components:** IBM WatsonX is divided into three main components: **watsonx.ai**, **watsonx.data**, and **watsonx.governance**. Each component serves a distinct purpose, with watsonx.ai focusing on AI capabilities.
- **Unified AI Platform:** It offers a unified AI platform that utilizes decorators in Jupyter Notebooks. Users gain access to base models and tracking metrics for free, although custom models can be used with some limitations on benefits.
- **Extensibility:** WatsonX provides an extensible software development kit (SDK) for integration with other applications.
- **User-Friendly Interface:** The platform features a straightforward interface, supporting low-code development, making it accessible for users with varying levels of technical expertise.

### Dataiku

- **Unified AI Platform:** Dataiku is a unified AI platform catering to both low-code and no-code users, as well as power users, allowing them to create, deploy, and manage machine learning (ML), artificial intelligence (AI), and generative AI (GenAI) solutions.
- **Low-Code Features:** Users can easily drag and drop images and shapes to build their data pipelines. The platform also supports deployment and team collaboration.
- **Strong Integrations:** Dataiku offers strong extensibility with third-party tools and customer relationship management (CRM) systems. It maintains external partnerships, facilitating easy integration with various data sources.
- **User-Friendly Interface:** The platform is noted for its visually appealing and intuitive interface.

### Cloudera

- **Scalable and Secure Data Management:** Cloudera provides scalable and secure data management solutions that include portable, cloud-native data services. It is designed to support enterprises in managing their data effectively across different environments.

### AnyScale

- **Scalability Across Platforms:** AnyScale’s primary selling point is its ability to build applications that can run at any scale, from a personal laptop to large data centers.
- **ML Infrastructure Management:** The platform specializes in managing machine learning infrastructure. Companies like LiveEO, which has a technology stack similar to ours, have utilized AnyScale to effectively scale their workloads.

### IBM Cloud Pak

- **Enterprise-Grade Containerization:** IBM Cloud Paks are enterprise-grade, containerized software solutions that combine container images with capabilities for deployment in production use cases. They feature integrations for management and lifecycle operations.
- **Deployment Features:** Key features include pre-configured deployments based on product expertise, rolling upgrades, and comprehensive management of production workloads.

