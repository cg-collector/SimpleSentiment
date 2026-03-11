# BettaFish 项目结构说明

## 📁 项目概述

本项目包含两个主要部分：

1. **BettaFish** - 原始的大型多智能体舆情分析系统（完整版）
2. **SimpleSentiment** - 简化版舆情监测分析预测系统（改进版）

---

## 🎯 推荐使用 SimpleSentiment

如果你是以下用户，推荐使用 SimpleSentiment：

✅ **课程项目** - 需要完整但简洁的系统实现
✅ **教学演示** - 需要清晰易懂的代码结构
✅ **学术研究** - 需要轻量级可定制的框架
✅ **快速原型** - 需要快速验证想法
✅ **学习参考** - 学习舆情系统的核心原理

**SimpleSentiment 路径**: `/SimpleSentiment/`

**快速启动**:
```bash
cd SimpleSentiment
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 项目目录结构

```
BettaFish/                          # 项目根目录
│
├── 📘 README.md                    # 项目主说明（已更新为突出SimpleSentiment）
├── 📘 README-EN.md                 # 英文版说明
├── 📘 PROJECT_STRUCTURE.md         # 本文件 - 项目结构说明
├── 📘 SIMPLIFIED_STRUCTURE.md      # SimpleSentiment详细结构说明
│
├── ⚙️  .gitignore                  # Git忽略配置
├── ⚙️  .env.example                # 环境变量模板
├── ⚙️  requirements.txt            # Python依赖包（完整版）
├── ⚙️  config.py                   # 全局配置（完整版）
│
├── 🚀 SimpleSentiment/             # 【推荐】简化版舆情系统
│   ├── app.py                      # Streamlit主应用
│   ├── config.py                   # 配置文件
│   ├── requirements.txt            # 简化版依赖
│   ├── .env.example                # 环境变量模板
│   ├── README.md                   # SimpleSentiment说明
│   ├── 开发进度记录.md             # 开发日志
│   │
│   ├── data/                       # 数据目录
│   ├── collectors/                 # 数据采集模块
│   ├── analyzers/                  # 舆情分析模块
│   ├── predictors/                 # 舆情预测模块
│   ├── pages/                      # Streamlit页面
│   ├── utils/                      # 工具函数
│   └── tests/                      # 测试文件
│
├── 🌐 BettaFish完整版系统/          # 原始大型系统（保留）
│   ├── QueryEngine/                # 新闻搜索Agent
│   ├── MediaEngine/                # 多模态分析Agent
│   ├── InsightEngine/              # 数据库分析Agent
│   ├── ReportEngine/               # 报告生成Agent
│   ├── ForumEngine/                # Agent协作引擎
│   ├── MindSpider/                 # 社交媒体爬虫
│   ├── SentimentAnalysisModel/     # 情感分析模型
│   ├── SingleEngineApp/            # 单Agent应用
│   ├── app.py                      # Flask主应用
│   └── ...                         # 其他完整功能
│
├── 📚 docs/                        # 项目文档
│   ├── README.md                   # 文档说明
│   ├── 项目设计文档.md             # 详细设计文档
│   ├── 快速开始指南.md             # 快速上手指南
│   ├── 课题进展报告.md             # 项目进展报告
│   ├── 爬虫测试与使用建议.md       # 爬虫使用指南
│   ├── 思路.md                     # 项目思路
│   └── images/                     # 文档图片
│
├── 🖼️ static/                      # 静态资源
│   ├── image/                      # 图片文件
│   └── v2_report_example/          # 报告示例
│
├── 🌐 templates/                   # Flask模板（完整版）
│   └── index.html                  # 主界面
│
├── 📊 logs/                        # 日志目录（忽略）
├── 📊 final_reports/               # 最终报告（忽略）
├── 📊 *_streamlit_reports/         # Streamlit报告（忽略）
│
└── 🧪 tests/                       # 测试文件
    └── ...                         # 单元测试
```

---

## 🔄 两个版本对比

| 特性 | BettaFish (完整版) | SimpleSentiment (简化版) |
|------|-------------------|------------------------|
| **代码量** | 数万行 | ~2000行 |
| **Agent数量** | 4+ 专业Agent | 简化版 |
| **部署方式** | Docker推荐 | 一键启动 |
| **学习曲线** | 陡峭 | 平缓 |
| **适用场景** | 生产环境 | 教学/课程 |
| **功能完整性** | 全功能 | 核心功能 |
| **数据库** | PostgreSQL | SQLite |
| **爬虫** | 13+平台 | 新闻API+简化爬虫 |
| **情感分析** | 多模型集成 | SnowNLP+LLM可选 |
| **预测功能** | 高级预测 | Prophet+LLM |

---

## 📖 使用建议

### 🎓 学生/教师

使用 **SimpleSentiment**：
- 代码结构清晰，易于理解
- 功能完整但不复杂
- 适合课程项目和论文

### 🔬 研究者

根据需求选择：
- **SimpleSentiment**: 快速验证想法，定制开发
- **BettaFish**: 需要完整功能和多平台支持

### 👨‍💻 开发者

- 学习参考：先看 SimpleSentiment 理解核心原理
- 深度研究：再研究 BettaFish 的高级特性

---

## 🚀 快速开始

### SimpleSentiment (推荐)

```bash
# 进入项目目录
cd SimpleSentiment

# 安装依赖
pip install -r requirements.txt

# 配置环境（可选）
cp .env.example .env

# 启动系统
streamlit run app.py
```

### BettaFish 完整版

```bash
# 使用Docker启动（推荐）
docker compose up -d

# 或源码启动（需要配置）
pip install -r requirements.txt
python app.py
```

---

## 📚 文档导航

### SimpleSentiment 文档
- [开发进度记录](SimpleSentiment/开发进度记录.md) - 详细的开发日志
- [快速开始指南](docs/快速开始指南.md) - 10分钟快速上手

### 项目设计文档
- [项目设计文档](docs/项目设计文档.md) - 详细的设计思路
- [课题进展报告](docs/课题进展报告.md) - 项目进展和成果

### 完整版文档
- [原README文档](README-EN.md) - 完整版英文说明
- [贡献指南](CONTRIBUTING.md) - 如何贡献代码

---

## 🤝 贡献指南

欢迎针对两个版本提交贡献：

1. **SimpleSentiment**: 欢迎教学改进、功能简化建议
2. **BettaFish**: 欢迎功能增强、性能优化

---

## 📞 联系方式

- **Issues**: [GitHub Issues](https://github.com/cg-collector/SimpleSentiment/issues)
- **Discussions**: [GitHub Discussions](https://github.com/cg-collector/SimpleSentiment/discussions)

---

**最后更新**: 2025-03-11
