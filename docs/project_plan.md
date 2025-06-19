# Project Title: Delineo Data Analysis: AI-Augmented Counterfactual Analysis of Infection Chains 

## Goal: 

To develop an AI-powered framework for identifying and analyzing critical moments in infection simulations where small changes in behavior or policy could have significantly altered outcomes. The project aims to optimize the simulation pipeline, structure the data effectively, and apply clustering and causal analysis methods to uncover insights from counterfactual scenarios.

## Method: 

Simulation Optimization: Refactoring and enhancing the simulator for efficiency and modularity.
Structuring the Data: Organize simulation output (infection chains, agent states, policies) into analyzable formats.
Insight Extraction: Use AI techniques (for eg: clustering, counterfactual modeling, causal inference) to detect and analyze impactful deviations.

## Role of AI in the project: 

AI helps identify moments when a policy change could lead to significantly different results 

## Deliverables: 

**“Sparser” program:** Program to figure out which simulation runs (with which parameters and values) would have the biggest impact. 
**Counterfactual Analysis Framework:** a system to test “what if” questions for policy changes
**Clustering and flagging system:** Groups of similar infection patterns identified, AI highlights scenarios where changes have a big impact 


## Weekly Plan: 
Week 1 (done by 15 June) : Simulator logging 
\* Identifying bottlenecks in the simulation pipeline.
\* Adding logging to capture relevant simulation metadata (time of infection, source agent, policy state).
\* Get simulator’s “output” 

Week 2 (done by 22 June): Data Schema Design & Extraction
\* Designing a data format to be used for clustering
\* Extracting and storing simulation outputs in structured formats (e.g., JSON, CSV, or a lightweight database like SQLite).
\* Validating the integrity of stored data across simulation runs.

Week 3 (done by 29 June): Start developing “sparser”
\* write a simple code to run multiple scenarios (e.g., exhaustive parameter exploration--can improve in 1, 2)
\* Identifying points in time or agent behavior where alternate actions could be tested.
\* Building infrastructure to re-run simulations with small parameter tweaks.

Week 4 (done by 6 July): 
\* Making script to identify which parameter tweaks (like additional masking, closing a certain space down etc.) would be the most useful 
\* develop a "parameter estimation" so that we can estimate what the input params should be so the results is in the desired neighbourhood. Fine tune afterwards

Week 5 (done by 13 July): Clustering & Exploratory Analysis:
\* Using KMeans, DBSCAN, or AgglomerativeClustering to identify similar infection chain patterns or agent behaviors.
\* Applying PCA or TSNE to visualize high-dimensional simulation outputs.

Week 6 (done by 20 July): Causal Inference Techniques:
\* Using EconML's DML (Double Machine Learning) or CausalForestDML to estimate the effect of a specific behavior or policy change on infection rates.
LinearDML if we want interpretable treatment effects (e.g., "mask wearing reduces infections by 12%").
\* These methods work very well with simulation data where we know the treatment/control and outcome.

Week 7 (done by 27 July): Flagging System:
\* Using classification models (RandomForestClassifier, LogisticRegression) to build an ML system that predicts whether a scenario is a "high-impact counterfactual."

Week 8 (done by 3 Aug): 
\* Building a simple rule-based or ML-powered flagging system to highlight simulations with significant counterfactuals.

Week 9 (done by Aug 10): Summary statistics 
\* Generating natural-language or tabular summaries of findings (e.g., “Changing Agent A’s mask-wearing behavior reduced total infections by 20%”).

Week 10 (done by Aug 17): Final Evaluation & Report
\* Evaluating the framework using test scenarios.
\* Creating a concise, well-visualized report showcasing the framework, methods, and key insights.
\* Demo 

Project to be completed by 17 August. 

### More things to consider: 
\* Trade-offs in interventions (economic and other kinds of impact of lockdowns, more masking etc.) 
\* Increasing simulation speed and efficiency 
\* Fine-tuning parameter estimation and sparser module 
\* Model testing and validation 










