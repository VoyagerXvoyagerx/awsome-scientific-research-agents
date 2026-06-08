# Awesome Research Agents

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 精心整理的科研AI智能体与技能集合，覆盖从灵感产生到影响力分析的全研究生命周期。
> 
> **精选项目数量**：80+ | **分类**：6大方向 | **最后更新**：2026年6月

---

## 📖 目录

- [Awesome Research Agents](#awesome-research-agents)
  - [📖 目录](#-目录)
  - [🤖 Auto Research（端到端自动科研）](#-auto-research端到端自动科研)
  - [💡 Idea Generation（科研选题与idea生成）](#-idea-generation科研选题与idea生成)
  - [🧪 Experiment（实验设计与执行）](#-experiment实验设计与执行)
  - [✍️ Writing（论文写作与润色）](#️-writing论文写作与润色)
  - [📊 Scientific Visualization（科学画图与可视化）](#-scientific-visualization科学画图与可视化)
  - [📈 Impact Analysis（论文影响力分析）](#-impact-analysis论文影响力分析)
  - [📚 相关资源](#-相关资源)
    - [综合综述](#综合综述)
    - [关键论文](#关键论文)
  - [🤝 如何贡献](#-如何贡献)
  - [📜 许可证](#-许可证)

---

## 🤖 Auto Research（端到端自动科研）

> 覆盖从灵感产生、文献综述、实验设计、代码编写到论文写作的完整科研流程的自动化系统。

| 缩写 | 描述 | 类型 | Stars | Paper | 链接 |
|------|------|------|:------------:|-------|------|
| autoresearch | Andrej Karpathy的自主ML研究代理，让AI在单GPU上自动运行实验并改进模型 | agent | ![GitHub stars](https://img.shields.io/github/stars/karpathy/autoresearch?style=flat-square&logo=github) | - | [GitHub](https://github.com/karpathy/autoresearch) |
| AI-Scientist | 首个端到端自动化科学发现系统，自动生成研究想法、实验、论文和同行评审 | agent | ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=flat-square&logo=github) | [Nature 2024](https://modelscope.cn/papers/2408.06292/) | [GitHub](https://github.com/SakanaAI/AI-Scientist) |
| AutoResearchClaw | 全自主、自进化的23阶段研究流水线，从想法到论文一键生成 | agent | ![GitHub stars](https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2605.22662/) | [GitHub](https://github.com/aiming-lab/AutoResearchClaw) / [Demo](https://openclaw.ai) |
| AgentLab | 端到端自主研究工作流，多Agent协作（PhD/Postdoc/ML Engineer/Professor）协助人类研究者 | agent | ![GitHub stars](https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2501.04227/) | [GitHub](https://github.com/SamuelSchmidgall/AgentLaboratory) / [Demo](https://agentlaboratory.github.io) |
| AI-Researcher | 完全自主的科学创新系统，覆盖文献综述到论文撰写的完整研究管线 | agent | ![GitHub stars](https://img.shields.io/github/stars/hkuds/ai-researcher?style=flat-square&logo=github) | [NeurIPS 2025](https://modelscope.cn/papers/2505.18705/) | [GitHub](https://github.com/hkuds/ai-researcher) / [Demo](https://novix.science/chat) |
| EvoScientist | 自进化多Agent AI科学家系统，6个子Agent协作并通过持久记忆和技能进化实现端到端科研 | agent | ![GitHub stars](https://img.shields.io/github/stars/EvoScientist/EvoScientist?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2603.08127/) | [GitHub](https://github.com/EvoScientist/EvoScientist) / [Skill](https://skillsllm.com/skill/evoscientist) / [Demo](https://evoscientist.ai) |
| DeepScientist | 本地优先的自主研究工作室，通过贝叶斯优化和研究发现记忆推进前沿科学 | agent | ![GitHub stars](https://img.shields.io/github/stars/ResearAI/DeepScientist?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2509.26603/) | [GitHub](https://github.com/ResearAI/DeepScientist) / [Demo](https://deepscientist.cc) |
| CORAL | 轻量级多Agent自进化基础设施，支持异步执行和共享持久记忆 | agent | ![GitHub stars](https://img.shields.io/github/stars/Human-Agent-Society/CORAL?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2604.01658/) | [GitHub](https://github.com/Human-Agent-Society/CORAL) / [Docs](https://docs.coralxyz.com) |
| Robin | 首个集成文献搜索与数据分析的多Agent系统，实现半自主科学发现（Lab-in-the-Loop） | agent | ![GitHub stars](https://img.shields.io/github/stars/Future-House/robin?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2505.13400/) | [GitHub](https://github.com/Future-House/robin) |
| CycleResearcher | 通过迭代偏好训练框架，让开源LLM自动进行研究并模拟同行评审 | agent | ![GitHub stars](https://img.shields.io/github/stars/zhu-minjun/Researcher?style=flat-square&logo=github) | [ICLR 2025](https://modelscope.cn/papers/2411.00816/) | [GitHub](https://github.com/zhu-minjun/Researcher) / [Demo](https://wengsyx.github.io/Researcher) |
| SciMaster | 通用工具增强推理Agent，在Humanity's Last Exam上达到SOTA 32.1% | agent | ![GitHub stars](https://img.shields.io/github/stars/sjtu-sai-agents/X-Master?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2507.05241/) | [GitHub](https://github.com/sjtu-sai-agents/X-Master) / [Demo](https://scimaster.bohrium.com) |
| VirSci | 基于真实科学数据的多Agent科学协作系统，模拟真实科研团队的协作过程 | agent | ![GitHub stars](https://img.shields.io/github/stars/InternScience/Virtual-Scientists?style=flat-square&logo=github) | [ACL 2025](https://modelscope.cn/papers/2410.09403/) | [GitHub](https://github.com/InternScience/Virtual-Scientists) / [Demo](https://open-sciencelab.github.io/Virtual-Scientists) |
| MLR-Copilot | 基于LLM代理的自主机器学习研究框架，自动生成并实现研究想法 | agent | ![GitHub stars](https://img.shields.io/github/stars/du-nlp-lab/MLR-Copilot?style=flat-square&logo=github) | [arXiv 2024](https://modelscope.cn/papers/2408.14033/) | [GitHub](https://github.com/du-nlp-lab/MLR-Copilot) / [HF Space](https://huggingface.co/spaces/du-lab/MLR-Copilot) |

**补充项目**（无GitHub仓库但有重要学术价值）：
- **Baby-AIGS** (AIGS): 多Agent全流程AI生成科学系统，通过显式证伪机制实现科学发现 — [Paper](https://modelscope.cn/papers/2411.11910/) / [Demo](https://agent-force.github.io/AIGS/)
- **AI Co-Scientist** (Google): 基于Gemini 2.0的多Agent科学协作者 — [Paper](https://modelscope.cn/papers/2502.18864/)
- **ResearchTown**: 人类研究社区的模拟器 — [ICML 2025](https://modelscope.cn/papers/2412.17767/)

---

## 💡 Idea Generation（科研选题与idea生成）

> 专注于科研早期阶段——产生新颖研究想法、假设生成和选题辅助的AI工具。

| 缩写 | 描述 | 类型 | Stars | Paper | 链接 |
|------|------|------|:------------:|-------|------|
| AutoSci | Wiki-centric全生命周期AI研究平台，包含/ideate、/novelty、/review等完整skill集合 | agent/skill | ![GitHub stars](https://img.shields.io/github/stars/skyllwt/AutoSci?style=flat-square&logo=github) | - | [GitHub](https://github.com/skyllwt/AutoSci) / 内置skills |
| SciAgents | 通过多Agent智能图推理实现自动化科学发现，基于知识图谱的生物启发式群智 | agent | ![GitHub stars](https://img.shields.io/github/stars/lamm-mit/SciAgentsDiscovery?style=flat-square&logo=github) | [Advanced Materials](https://modelscope.cn/papers/2409.05556/) | [GitHub](https://github.com/lamm-mit/SciAgentsDiscovery) |
| CoI | Chain-of-Ideas：将文献组织为链式结构反映研究渐进发展，增强LLM构思能力 | agent | ![GitHub stars](https://img.shields.io/github/stars/DAMO-NLP-SG/CoI-Agent?style=flat-square&logo=github) | [arXiv 2024](https://modelscope.cn/papers/2410.13185/) | [GitHub](https://github.com/DAMO-NLP-SG/CoI-Agent) / [HF Space](https://huggingface.co/spaces/DAMO-NLP-SG/CoI_Agent) |
| SciPIP | 基于LLM的科学论文idea提议器，多粒度文献检索和双路径idea生成策略 | agent | ![GitHub stars](https://img.shields.io/github/stars/cheerss/SciPIP?style=flat-square&logo=github) | [arXiv 2024](https://modelscope.cn/papers/2410.23166/) | [GitHub](https://github.com/cheerss/SciPIP) / [HF Space](https://huggingface.co/spaces/lihuigu/SciPIP) |
| ResearchAgent | 基于科学文献的迭代式研究idea生成，利用多Agent review/refinement提高想法质量 | agent | ![GitHub stars](https://img.shields.io/github/stars/JinheonBaek/ResearchAgent?style=flat-square&logo=github) | [NAACL 2025](https://modelscope.cn/papers/2404.07738/) | [GitHub](https://github.com/JinheonBaek/ResearchAgent) |
| ResearchGPT | 端到端CS研究工作流基准测试与训练框架，构建CS-54k数据集 | agent | ![GitHub stars](https://img.shields.io/github/stars/wph6/ResearchGPT?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2510.20279/) | [GitHub](https://github.com/wph6/ResearchGPT) |
| Deep-Ideation | 在科学概念网络上设计LLM Agent生成新颖研究idea，explore-expand-evolve工作流 | agent | ![GitHub stars](https://img.shields.io/github/stars/kyZhao-1/Deep-Ideation?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2511.02238/) | [GitHub](https://github.com/kyZhao-1/Deep-Ideation) |
| IdeaForge | 通过对抗多Agent辩论生成研究idea，3-agent（Critic-Proposer-Judge）循环迭代优化 | agent | ![GitHub stars](https://img.shields.io/github/stars/makemebitter/ideaforge?style=flat-square&logo=github) | - | [GitHub](https://github.com/makemebitter/ideaforge) / 内置26 skill files |
| HypER | 基于文献的假设生成与蒸馏，带有来源追溯功能 | agent | ![GitHub stars](https://img.shields.io/github/stars/rosnikv/HypER?style=flat-square&logo=github) | [EMNLP 2025](https://modelscope.cn/papers/2506.12937/) | [GitHub](https://github.com/rosnikv/HypER) |

**补充项目**（无GitHub仓库但有重要学术价值）：
- **Nova**: 迭代式规划和搜索方法，增强LLM生成idea的新颖性和多样性 — [ACL 2025](https://modelscope.cn/papers/2410.14255/)
- **IdeaSynth**: 通过演化与组合idea facets并基于文献反馈迭代开发研究idea — [CHI 2025](https://modelscope.cn/papers/2410.04025/)
- **MOOSE-Chem**: 用于重新发现化学科学假设的LLM — [ICLR 2025](https://modelscope.cn/papers/2410.07076/)
- **LiveIdeaBench**: 评估LLMs科学创造力和idea生成能力的综合基准 — [arXiv 2024](https://modelscope.cn/papers/2412.17596/)

---

## 🧪 Experiment（实验设计与执行）

> 帮助研究人员设计实验、执行实验、分析实验数据的AI工具，包括AutoML、实验跟踪、超参优化等。

| 缩写 | 描述 | 类型 | Stars | Paper | 链接 |
|------|------|------|:------------:|-------|------|
| RD-Agent | 微软开源的自动化研发Agent，覆盖数据科学、量化金融、Kaggle竞赛、LLM微调等场景 | agent | ![GitHub stars](https://img.shields.io/github/stars/microsoft/RD-Agent?style=flat-square&logo=github) | [Tech Report](https://aka.ms/RD-Agent-Tech-Report) | [GitHub](https://github.com/microsoft/RD-Agent) / [Demo](https://rdagent.azurewebsites.net/) |
| AI-Scientist-v2 | 基于Agentic Tree Search的升级版，不依赖人类模板，可跨ML领域通用化探索 | agent | ![GitHub stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2504.08066/) | [GitHub](https://github.com/SakanaAI/AI-Scientist-v2) |
| MLE-bench | OpenAI开源的评估ML Agent在机器学习工程任务上表现的基准测试框架 | agent | ![GitHub stars](https://img.shields.io/github/stars/openai/mle-bench?style=flat-square&logo=github) | [arXiv 2024](https://modelscope.cn/papers/2410.07095/) | [GitHub](https://github.com/openai/mle-bench) |
| AIDE | 将ML工程视为代码优化问题，通过树搜索在代码空间中自动探索和优化解决方案 | agent | ![GitHub stars](https://img.shields.io/github/stars/WecoAI/aideml?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2502.13138/) | [GitHub](https://github.com/WecoAI/aideml) |
| MLGym | Meta推出的Gym风格框架和基准测试，用于评估和训练AI研究Agent | agent | ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/MLGym?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2502.14499/) | [GitHub](https://github.com/facebookresearch/MLGym) |
| CURIE | 面向严谨自动化科学实验的AI Agent框架，含实验严谨性引擎和多Agent协作 | agent | ![GitHub stars](https://img.shields.io/github/stars/Just-Curieous/Curie?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2502.16069/) | [GitHub](https://github.com/Just-Curieous/Curie) / [Demo](https://www.just-curieous.com/) |
| MLAgentBench | 评估语言Agent在ML实验任务上端到端表现的基准测试套件 | agent | ![GitHub stars](https://img.shields.io/github/stars/snap-stanford/MLAgentBench?style=flat-square&logo=github) | [arXiv 2023](https://modelscope.cn/papers/2310.03302/) | [GitHub](https://github.com/snap-stanford/MLAgentBench) |
| DS-Agent | 基于案例推理(CBR)的自动化数据科学Agent，开发阶段100%成功率 | agent | ![GitHub stars](https://img.shields.io/github/stars/guosyjlu/DS-Agent?style=flat-square&logo=github) | [ICML 2024](https://modelscope.cn/papers/2402.17453/) | [GitHub](https://github.com/guosyjlu/DS-Agent) |
| AutoReproduce | 多Agent框架，通过Paper Lineage算法自动复现论文实验 | agent | ![GitHub stars](https://img.shields.io/github/stars/AI9Stars/AutoReproduce?style=flat-square&logo=github) | [ACL 2026](https://modelscope.cn/papers/2505.20662/) | [GitHub](https://github.com/AI9Stars/AutoReproduce) |

**补充项目**（无GitHub仓库）：
- **AlphaEvolve** (Google DeepMind): 进化式编码Agent，使用Gemini模型自动发现和优化算法，突破4×4矩阵乘法56年纪录 — [arXiv 2025](https://modelscope.cn/papers/2505.04507/) / [Blog](https://deepmind.google/blog/alphaevolve-impact/)

---

## ✍️ Writing（论文写作与润色）

> 帮助研究人员写作、润色、修改学术论文的AI工具，包括文献综述生成、论文写作、引用验证等。

| 缩写 | 描述 | 类型 | Stars | Paper | 链接 |
|------|------|------|:------------:|-------|------|
| DeerFlow | 字节跳动开源的SuperAgent框架，支持深度研究、代码执行和创作 | agent | ![GitHub stars](https://img.shields.io/github/stars/bytedance/deer-flow?style=flat-square&logo=github) | - | [GitHub](https://github.com/bytedance/deer-flow) / [Demo](https://deerflow.tech) |
| STORM | 斯坦福开源的知识整理系统，通过多视角问题生成和检索研究生成带引用的完整报告 | agent | ![GitHub stars](https://img.shields.io/github/stars/stanford-oval/storm?style=flat-square&logo=github) | [NAACL 2024](https://modelscope.cn/papers/2402.14207/) | [GitHub](https://github.com/stanford-oval/storm) / [Demo](https://storm.genie.stanford.edu) |
| ARS | Claude Code学术研究技能套件，覆盖从文献调研到论文发表的全流程 | skill | ![GitHub stars](https://img.shields.io/github/stars/Imbad0202/academic-research-skills?style=flat-square&logo=github) | - | [GitHub](https://github.com/Imbad0202/academic-research-skills) / 内置Claude Code技能 |
| GPT-R | 基于LLM的自主深度研究代理，支持网络和本地文档研究，生成带引用的详细报告 | agent | ![GitHub stars](https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=flat-square&logo=github) | - | [GitHub](https://github.com/assafelovic/gpt-researcher) / [Skill Install](https://github.com/assafelovic/gpt-researcher) / [Demo](https://gptr.dev) |
| ODR | LangChain开源深度研究代理，支持多种模型提供商、搜索工具和MCP服务器 | agent | ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/open_deep_research?style=flat-square&logo=github) | - | [GitHub](https://github.com/langchain-ai/open_deep_research) |
| PaperQA2 | 面向科学文献的高精度RAG系统，支持科学问答、摘要生成和矛盾检测 | agent | ![GitHub stars](https://img.shields.io/github/stars/Future-House/paper-qa?style=flat-square&logo=github) | [arXiv 2024](https://modelscope.cn/papers/2409.13740/) | [GitHub](https://github.com/Future-House/paper-qa) / [Docs](https://futurehouse.gitbook.io/futurehouse-cookbook) |
| CSW | 科学写作工具，结合深度研究与格式化输出，支持论文/报告/基金申请 | skill | ![GitHub stars](https://img.shields.io/github/stars/K-Dense-AI/claude-scientific-writer?style=flat-square&logo=github) | - | [GitHub](https://github.com/K-Dense-AI/claude-scientific-writer) / 内置Claude Code技能 / [Demo](https://k-dense.ai) |
| OpenDraft | 开源AI论文草稿生成器，19个专业代理协作，支持验证引用并导出PDF/Word/LaTeX | agent | ![GitHub stars](https://img.shields.io/github/stars/federicodeponte/opendraft?style=flat-square&logo=github) | - | [GitHub](https://github.com/federicodeponte/opendraft) / [Demo](https://openpaper.dev) |
| LatteReview | 低代码Python包，通过AI智能体自动化系统性文献综述流程 | agent | ![GitHub stars](https://img.shields.io/github/stars/PouriaRouzrokh/LatteReview?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2501.05468/) | [GitHub](https://github.com/PouriaRouzrokh/LatteReview) / [Docs](https://pouriarouzrokh.github.io/LatteReview) |

---

## 📊 Scientific Visualization（科学画图与可视化）

> 帮助研究人员生成科学图表、数据可视化、论文插图的AI工具，包括自动生成图表、科学绘图等。

| 缩写 | 描述 | 类型 | Stars | Paper | 链接 |
|------|------|------|:------------:|-------|------|
| PaperBanana | 多Agent学术插图自动化生成框架，从文本描述生成出版级图表和统计图 | agent | ![GitHub stars](https://img.shields.io/github/stars/dwzhu-pku/PaperBanana?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2601.23265/) | [GitHub](https://github.com/dwzhu-pku/PaperBanana) / [Demo](https://dwzhu-pku.github.io/PaperBanana/) |
| AIDS-Team | AI驱动的数据科学团队Agent库，包含数据可视化、清洗、建模等多个Agent | agent | ![GitHub stars](https://img.shields.io/github/stars/business-science/ai-data-science-team?style=flat-square&logo=github) | - | [GitHub](https://github.com/business-science/ai-data-science-team) |
| PlotSense | AI驱动的数据可视化助手，提供智能图表推荐和自然语言解释 | agent | ![GitHub stars](https://img.shields.io/github/stars/PlotSenseAI/PlotSense?style=flat-square&logo=github) | - | [GitHub](https://github.com/PlotSenseAI/PlotSense) |
| MatPlotAgent | 清华NLP提出的模型无关LLM Agent框架，自动化科学数据可视化 | agent | ![GitHub stars](https://img.shields.io/github/stars/thunlp/MatPlotAgent?style=flat-square&logo=github) | [ACL 2024](https://modelscope.cn/papers/2402.11453/) | [GitHub](https://github.com/thunlp/MatPlotAgent) / [Skill](https://github.com/lingzhi227/agent-research-skills/tree/main/skills/figure-generation) |
| ARS-Viz | 包含31个学术研究技能的Claude Code技能包，含科学图表生成skill | skill | ![GitHub stars](https://img.shields.io/github/stars/lingzhi227/agent-research-skills?style=flat-square&logo=github) | - | [GitHub](https://github.com/lingzhi227/agent-research-skills) / [Skill](https://github.com/lingzhi227/agent-research-skills/tree/main/skills/figure-generation) |
| CoDA | Google Research多Agent协作数据可视化框架，将自然语言查询转为出版级图表 | agent | ![GitHub stars](https://img.shields.io/github/stars/google-research/agentic-visualization?style=flat-square&logo=github) | [ICLR 2026](https://modelscope.cn/papers/2510.03194/) | [GitHub](https://github.com/google-research/agentic-visualization) / [Demo](https://coda-agent.github.io/CoDA/) |
| VisCoder | 针对Python可视化代码生成微调的开源大语言模型，支持自我纠错 | agent | ![GitHub stars](https://img.shields.io/github/stars/TIGER-AI-Lab/VisCoder?style=flat-square&logo=github) | [EMNLP 2025](https://modelscope.cn/papers/2506.03930/) | [GitHub](https://github.com/TIGER-AI-Lab/VisCoder) / [Demo](https://tiger-ai-lab.github.io/VisCoder) |
| DiagramAgent | CVPR 2025文本到图表生成与编辑框架，支持流程图、架构图等 | agent | ![GitHub stars](https://img.shields.io/github/stars/DiagramAgent/DiagramAgent_official?style=flat-square&logo=github) | [CVPR 2025](https://modelscope.cn/papers/2411.11916/) | [GitHub](https://github.com/DiagramAgent/DiagramAgent_official) / [Demo](https://diagramagent.github.io/) |
| VIS-Shepherd | 基于MLLM的可视化评价与反馈模型，为LLM生成的可视化提供自动评估 | agent | ![GitHub stars](https://img.shields.io/github/stars/bopan3/VIS-Shepherd?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2506.13326/) | [GitHub](https://github.com/bopan3/VIS-Shepherd) |
| Plot-Skill | AI技能文件：生成出版级ggplot2/plotnine图表，矢量PDF输出 | skill | ![GitHub stars](https://img.shields.io/github/stars/dazhiyang/scientific-plotting-skill?style=flat-square&logo=github) | - | [GitHub](https://github.com/dazhiyang/scientific-plotting-skill) / [Skill](https://github.com/dazhiyang/scientific-plotting-skill/blob/main/SKILL.md) |
| ChatVis | 科学可视化Agent和Benchmark，从自然语言生成ParaView可视化Python脚本 | agent | ![GitHub stars](https://img.shields.io/github/stars/tpeterka/ChatVis?style=flat-square&logo=github) | [arXiv 2024](https://modelscope.cn/papers/2410.11863/) | [GitHub](https://github.com/tpeterka/ChatVis) |

**补充项目**（无GitHub仓库但有重要学术价值）：
- **PlotGen**: 多Agent LLM科学数据可视化框架，通过多模态反馈迭代优化图表质量 — [WWW 2025](https://modelscope.cn/papers/2502.00988/)
- **SASAV**: 首个完全自主且零提示的科学可视化Agent工作流 — [arXiv 2025](https://modelscope.cn/papers/2604.03406/) / [Demo](https://selfdirectedscivisagent.github.io)

---

## 📈 Impact Analysis（论文影响力分析）

> 帮助研究人员分析论文影响力、引用趋势、学术网络、研究趋势等的AI工具。

| 缩写 | 描述 | 类型 | Stars | Paper | 链接 |
|------|------|------|:------------:|-------|------|
| S2-MCP | FastMCP服务器实现，提供对Semantic Scholar API的全面访问（16个工具） | skill | ![GitHub stars](https://img.shields.io/github/stars/zongmin-yu/semantic-scholar-fastmcp-mcp-server?style=flat-square&logo=github) | - | [GitHub](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server) / [Tools](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server/blob/main/TOOLS.md) |
| Argo | 开源交互式文献可视化探索工具，基于Semantic Scholar实时数据 | tool | ![GitHub stars](https://img.shields.io/github/stars/poloclub/argo-scholar?style=flat-square&logo=github) | [arXiv 2021](https://modelscope.cn/papers/2110.14060/) | [GitHub](https://github.com/poloclub/argo-scholar) / [Demo](https://poloclub.github.io/argo-scholar) |
| S2-Skills | S2优先的发现引擎，提供Claude Code技能和MCP服务器 | skill | ![GitHub stars](https://img.shields.io/github/stars/zongmin-yu/semantic-scholar-skills?style=flat-square&logo=github) | - | [GitHub](https://github.com/zongmin-yu/semantic-scholar-skills) / [Skills](https://github.com/zongmin-yu/semantic-scholar-skills/tree/main/skills) |

**商业/学术平台**（无GitHub仓库但有重要价值）：

| 缩写 | 描述 | 类型 | Stars | Paper | 链接 |
|------|------|------|-------|----------|
| Elicit | AI研究助手，自动化文献综述和数据提取，覆盖1.38亿+论文 | agent | [Blog](https://elicit.org/blog) | [Website](https://elicit.org) |
| RR | "学术界的Spotify"，基于引文的文献映射和可视化工具 | agent | [Docs](https://researchrabbit.notion.site/) | [Website](https://researchrabbitapp.com) |
| CP | 可视化论文关系图谱，基于引用相似性发现相关研究 | tool | [About](https://www.connectedpapers.com/about) | [Website](https://www.connectedpapers.com) |
| Consensus | AI学术搜索引擎，搜索2亿+论文并提供Consensus Meter分析 | agent | [Help](https://help.consensus.app/) | [Website](https://consensus.app) |
| SciSpace | AI驱动的研究助手，支持文献综述、PDF交互、写作辅助 | agent | - | [Website](https://typeset.io) |
| FH | AI科学发现平台，包含Crow/Falcon/Owl/Phoenix等多个研究Agent | agent平台 | [Research](https://futurehouse.org/research) | [Website](https://futurehouse.org) |
| scite | 智能引文分析工具，显示引文上下文并分类支持/反驳/提及 | tool | [QSS 2020](https://doi.org/10.1162/qss_a_00146) | [Website](https://scite.ai) |
| MIRAI | 深度学习框架，使用标题和摘要预测论文5年引用影响力 | model | [arXiv 2025](https://modelscope.cn/papers/2606.05443/) | [Demo](https://predict-paper-impact.vercel.app) |
| Undermind | AI深度研究助手，自主迭代搜索并分析数百篇学术文献 | agent | [About](https://undermind.ai/about) | [Website](https://undermind.ai) |
| OpenAlex-MCP | OpenAlex MCP服务器，为AI代理提供学术数据访问接口 | skill | - | [HF Space](https://huggingface.co/spaces/skazo4nick/openalex-mcp-tool) |
| S2-Graph | 综合MCP服务器，提供文献发现、引文网络和作者分析 | skill | ![GitHub stars](https://img.shields.io/github/stars/alperenkocyigit/semantic-scholar-graph-api?style=flat-square&logo=github) | [GitHub](https://github.com/alperenkocyigit/semantic-scholar-graph-api) |

---

## 📚 相关资源

### 综合综述
- [awesome-ai-auto-research](https://github.com/worldbench/awesome-ai-auto-research) - AI Auto-Research综合调研
- [awesome-researchclaw](https://github.com/SUSTech-GenAI/awesome-researchclaw) - Research Agent overview
- [awesome-autoresearch](https://github.com/alvinreal/awesome-autoresearch) - 自主研究系统列表
- [Awesome-scientific-idea-generation](https://github.com/Superbooming/Awesome-scientific-idea-generation) - LLM科学idea生成论文列表
- [LLM-SCI-GEN](https://github.com/Paureel/LLM-SCI-GEN) - 科学假设生成论文集合
- [Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents](https://modelscope.cn/papers/2503.24047/) - 2025年科学智能综述

### 关键论文
- [Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://modelscope.cn/papers/2603.08127/) (2026)
- [AI-Generated Hypotheses and the Emergence of Autonomous Scientific Discovery](https://pubs.acs.org/doi/10.1021/acsmaterialslett.6c00224) (2026)
- [Towards End-to-End Automation of AI Research](https://www.nature.com/articles/s41586-026-10265-5) (Nature 2026)

---

## 🤝 如何贡献

欢迎贡献！请阅读 [贡献指南](CONTRIBUTING.md) 了解如何提交Pull Request。

**贡献步骤**：
1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-tool`)
3. 提交你的改动 (`git commit -m 'Add some amazing tool'`)
4. 推送到分支 (`git push origin feature/amazing-tool`)
5. 打开一个 Pull Request

**收录标准**：
- 项目必须与AI辅助科研相关
- 优先收录有GitHub仓库的开源项目
- 项目应至少有一个可验证的发布版本或论文
- Star数量不是硬性要求，但会影响排序

---

> 免责声明：本仓库中的信息仅供学术研究参考。部分AI工具生成的内容可能需要人工审核，请遵守相关学术伦理规范。

---

<p align="center">
  <i>如果这个项目对你有帮助，请给它一个 ⭐️ Star！</i><br>
  <i>Made with ❤️ by the research community</i>
</p>
