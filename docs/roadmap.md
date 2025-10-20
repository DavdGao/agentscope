# Roadmap

## Long-term Goals

Offering **agent-oriented programming (AOP)** as a new programming paradigm to organize the design and implementation of next-generation LLM-empowered applications.

## Short-term Goals

### [2025-10] AgentScope 1.0 Enhancements

Thanks for the community, and AgentScope 1.0 has received great feedback since its release. We are committed to
continuously improving AgentScope based on user feedback and evolving industry standards.
In the upcoming months, we plan to focus on the following enhancements:

- RAG
  - Integrate with popular vector databases (e.g., Milvus)
  - Support more advanced retrieval techniques (e.g., reranking)
- Short-term Memory
  - We have heard from community and decided to provide more flexible short-term memory implementations
- Tool Control
  - Support user confirmation/approval before tool execution
- Improve Implementation
  - Rewrite these three examples to be implemented in the existing framework of agentscope
    - Meta Planner
    - Deep Research
    - Browser-use
- Voice Agent
  - Voice agent is a very attractive scenario. We plan to provide native support for voice agents in AgentScope.
- Documentation
  - Add contribution guidelines for community involvement
  - [PLANNED] AgentScope design book, that provides in-depth explanations of the framework's architecture and design principles




### [2025-09] AgentScope 1.0 Roadmap

We are deeply grateful for the continuous support from the open-source community that has witnessed AgentScope's
growth. Throughout our journey, we have maintained **developer-centric transparency** as our core principle,
which will continue to guide our future development.

As the AI agent ecosystem rapidly evolves, we recognize the need to adapt AgentScope to meet emerging trends and
requirements. We are excited to announce the upcoming release of AgentScope v1.0.0, which marks a significant shift
towards deployment-focused and secondary development direction. This new version will provide comprehensive support for agent developers
with enhanced deployment capabilities and practical features. Specifically, the update will include:

- ✨New Features
  - 🛠️ Tool/MCP
    - Support both sync/async tool functions
    - Support streaming tool function
    - Support parallel execution of tool functions
    - Provide more flexible support for the MCP server

  - 💾 Memory
    - Enhance the existing short-term memory
    - Support long-term memory

  - 🤖 Agent
    - Provide powerful ReAct-based out-of-the-box agents

- 👨‍💻 Development
  - Provide enhanced AgentScope Studio with visual components for developing, tracing and debugging
  - Provide a built-in copilot for developing/drafting AgentScope applications

- 🔍 Evaluation
  - Provide built-in benchmarking and evaluation toolkit for agents
  - Support result visualization

- 🏗️ Deployment
  - Support asynchronous agent execution
  - Support session/state management
  - Provide sandbox for tool execution

Stay tuned for our detailed release notes and beta version, which will be available soon. Follow our GitHub
repository and official channels for the latest updates. We look forward to your valuable feedback and continued
support in shaping the future of AgentScope.
