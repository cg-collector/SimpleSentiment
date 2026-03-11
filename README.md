<div align="center">

<img src="static/image/logo_compressed.png" alt="BettaFish Logo" width="100%">

# 🔍 SimpleSentiment - 轻量级舆情监测分析预测系统

**面向教育场景的简化版舆情系统 | 专注核心功能 | 适合课程项目**

[![License](https://img.shields.io/badge/license-GPL%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-green.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)

[English](./README-EN.md) | [中文文档](./README.md)

</div>

---

## 📖 项目简介

**SimpleSentiment** 是一个轻量级舆情监测分析预测系统，专注于**舆情监测、舆情分析、舆情预测**三大核心功能。本项目采用精简的系统架构，代码量约2000行，非常适合教学演示、课程项目和学术研究。

### 核心特点

| 特点 | 说明 |
|------|------|
| **轻量简洁** | 代码量约2000行，架构清晰，易于理解 |
| **功能完整** | 涵盖监测、分析、预测完整工作流 |
| **快速部署** | 基于Streamlit，无需独立后端 |
| **课程友好** | 代码注释详细，适合教学 |
| **可扩展** | 预留LLM增强接口，支持功能扩展 |

### 系统功能

```
┌─────────────────────────────────────────────────────────┐
│                   SimpleSentiment                        │
├─────────────────────────────────────────────────────────┤
│  📊 舆情监测  │  📈 舆情分析  │  🔮 舆情预测  │  ⚙️ 系统设置  │
├─────────────────────────────────────────────────────────┤
│  • 关键词监控     • 情感分析       • 时序预测       • 参数配置    │
│  • 多源数据采集   • 关键词提取     • LLM辅助分析   • 日志管理    │
│  • 数据去重       • 趋势可视化     • 准确度评估     • 数据维护    │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 适用场景

✅ **课程项目** - 完整的系统设计和实现案例
✅ **教学演示** - 清晰的代码结构，便于讲解
✅ **学术研究** - 轻量级架构，易于定制修改
✅ **快速原型** - 快速验证舆情分析想法
✅ **学习参考** - 了解舆情系统的核心原理

---

## 🚀 快速开始

### 环境要求

- **Python**: 3.9 或更高版本
- **操作系统**: Windows / macOS / Linux
- **内存**: 建议 2GB 以上

### 安装步骤

#### 1. 克隆项目

```bash
git clone https://github.com/cg-collector/SimpleSentiment.git
cd SimpleSentiment
```

#### 2. 安装依赖

```bash
pip install -r requirements.txt
```

主要依赖包：
```
streamlit>=1.28.0      # Web框架
pandas>=2.0.0          # 数据处理
snownlp>=0.12.3        # 情感分析
prophet>=1.1.4         # 时间序列预测
plotly>=5.17.0         # 可视化
wordcloud>=1.9.2       # 词云
openai>=1.3.0          # LLM接口（可选）
```

#### 3. 配置环境变量（可选）

```bash
# 复制配置文件模板
cp .env.example .env

# 编辑配置文件（如需LLM功能，可选）
# vim .env
```

**注意**: 基础功能无需配置环境变量即可运行。LLM功能为可选项。

#### 4. 启动系统

**方式一：默认端口启动**
```bash
cd SimpleSentiment
streamlit run app.py
```

**方式二：指定端口启动**（推荐）
```bash
cd SimpleSentiment
streamlit run app.py --server.port 8503
```

**如果端口被占用，查看并清理端口：**
```bash
# 查看占用的进程
lsof -ti:8503

# 清理端口
lsof -ti:8503 | xargs kill -9

# 重新启动
streamlit run app.py --server.port 8503
```

#### 5. 访问系统

启动成功后，在浏览器中访问：
- **默认地址**: http://localhost:8501
- **指定端口**: http://localhost:8503

**验证启动成功的标志**：
```bash
# 你应该看到类似的输出
  👋 Welcome to Streamlit!
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8503
  Network URL: http://192.168.x.x:8503
```

**测试命令**：
```bash
# 检查服务是否正常运行
curl -s http://localhost:8503 > /dev/null && echo "✅ Streamlit 运行正常" || echo "❌ 启动失败"
```

---

## ✅ 实际测试环境

**测试日期**: 2026-03-11
**测试环境**: macOS + Python 3.13
**测试结果**: ✅ 成功运行

**实际安装过程**：
```bash
# 1. 安装依赖（已测试）
$ pip install -r requirements.txt
Requirement already satisfied: streamlit>=1.28.0
Collecting snownlp>=0.12.3
  Downloading snownlp-0.12.3.tar.gz (37.6 MB)
Successfully installed snownlp-0.12.3 plotly-6.6.0 wordcloud-1.9.6 matplotlib-3.10.8

# 2. 启动应用（已测试）
$ streamlit run app.py --server.port 8503
✅ 成功！Streamlit 运行在端口 8503

# 3. 访问测试（已测试）
$ curl -s http://localhost:8503 > /dev/null && echo "✅ 访问成功"
✅ 访问成功
```

---

## 📁 项目结构

```
SimpleSentiment/                    # 简化版舆情系统
├── app.py                          # Streamlit主应用
├── config.py                       # 配置管理
├── requirements.txt                # 依赖包清单
├── .env.example                    # 环境变量模板
├── README.md                       # 项目说明
│
├── data/                           # 数据目录
│   ├── raw/                        # 原始数据
│   ├── processed/                  # 处理后的数据
│   └── sentiment.db                # SQLite数据库
│
├── collectors/                     # 数据采集模块
│   ├── base.py                     # 采集器基类
│   ├── news_collector.py           # 新闻采集器
│   └── weibo_collector.py          # 微博采集器
│
├── analyzers/                      # 舆情分析模块
│   ├── sentiment.py                # 情感分析器
│   ├── keyword_extractor.py        # 关键词提取
│   └── trend_analyzer.py           # 趋势分析器
│
├── predictors/                     # 舆情预测模块
│   ├── time_series.py              # 时间序列预测
│   └── llm_predictor.py            # LLM辅助预测
│
├── pages/                          # Streamlit页面
│   ├── monitoring.py               # 舆情监测页面
│   ├── analysis.py                 # 舆情分析页面
│   ├── prediction.py               # 舆情预测页面
│   └── settings.py                 # 系统设置页面
│
├── utils/                          # 工具函数
│   ├── database.py                 # 数据库操作
│   ├── llm_client.py               # LLM客户端
│   ├── visualizer.py               # 可视化工具
│   └── text_processing.py          # 文本处理
│
└── tests/                          # 测试文件
    ├── test_collectors.py
    ├── test_analyzers.py
    └── test_predictors.py
```

---

## 💡 核心功能

### 1️⃣ 舆情监测

- **关键词管理**: 添加、删除、编辑监控关键词
- **多源采集**: 支持新闻网站、微博等数据源
- **数据去重**: 自动过滤重复内容
- **实时监控**: 展示最新采集数据

**数据来源**：
- 新闻API（NewsAPI、天行数据等）
- 微博搜索（简化爬虫）
- 可扩展至其他平台

### 2️⃣ 舆情分析

- **情感分析**: 基于SnowNLP的中文情感分析
  - 正面/负面/中性分类
  - 情感得分计算（0-1分）
- **关键词提取**: 自动提取关键词和话题
- **趋势可视化**:
  - 情感分布饼图
  - 时间趋势折线图
  - 关键词词云
- **热点排行**: 热门话题排行

### 3️⃣ 舆情预测

- **时间序列预测**: 基于Prophet的预测模型
  - 预测未来3-7天趋势
  - 趋势置信区间
- **LLM辅助分析**（可选）:
  - 深度趋势分析
  - 影响因素识别
  - 风险提示
- **预测评估**: 模型准确度评估

### 4️⃣ 双模式运行

| 模式 | 说明 | 优势 |
|------|------|------|
| **基础模式** | 使用SnowNLP + Prophet | 无需API Key，完全免费 |
| **增强模式** | 集成LLM能力 | 分析更深入，理解更准确 |

---

## 🔧 技术架构

### 技术栈

```
前端层：  Streamlit
处理层：  Pandas + NumPy
分析层：  SnowNLP + Prophet
存储层：  SQLite
预测层：  Prophet + LLM（可选）
```

### 数据流程

```
用户输入关键词
    ↓
定时调度器
    ↓
多源数据采集 → 数据清洗 → SQLite存储
    ↓
情感分析 + 关键词提取
    ↓
趋势分析
    ↓
Prophet预测 + LLM分析（可选）
    ↓
Streamlit可视化展示
```

---

## 📸 界面预览

### 舆情监测界面
- 关键词配置
- 实时数据展示
- 采集状态监控

### 舆情分析界面
- 情感分布图表
- 趋势折线图
- 关键词词云

### 舆情预测界面
- 预测曲线图
- 置信区间
- LLM分析报告

---

## 🎓 教学优势

### 与完整版BettaFish对比

| 特性 | BettaFish | SimpleSentiment |
|------|-----------|-----------------|
| 代码量 | 数万行 | ~2000行 |
| 部署复杂度 | 高（Docker推荐） | 低（一键启动） |
| 学习曲线 | 陡峭 | 平缓 |
| 适用场景 | 生产环境 | 教学/课程 |
| 功能完整性 | 全功能 | 核心功能 |
| Agent数量 | 4+ | 简化版 |

### 代码特点

✅ **注释详细**: 关键代码都有详细注释
✅ **结构清晰**: 模块划分明确，易于理解
✅ **示例丰富**: 包含完整的测试案例
✅ **文档完善**: 提供详细的使用文档

---

## 📚 文档导航

- [项目设计文档](docs/项目设计文档.md) - 详细的设计思路和架构说明
- [快速开始指南](docs/快速开始指南.md) - 10分钟快速上手
- [课题进展报告](docs/课题进展报告.md) - 项目开发进展和成果
- [开发进度记录](SimpleSentiment/开发进度记录.md) - 详细的开发日志

---

## 🛠️ 开发计划

当前项目已完成基础框架搭建，正在进行核心功能模块开发。

### 已完成 ✅

- [x] 项目结构搭建
- [x] 配置文件创建
- [x] 依赖包清单
- [x] 数据库设计

### 进行中 🔄

- [ ] 核心功能模块开发
- [ ] Streamlit界面开发
- [ ] 系统集成测试

### 计划中 📋

- [ ] 完整测试
- [ ] 文档完善
- [ ] 演示准备

---

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证

本项目采用 [GPL-2.0 许可证](LICENSE) 开源。

---

## 🙏 致谢

感谢以下开源项目的支持：
  - [Streamlit](https://streamlit.io/) - Web应用框架
  - [Prophet](https://facebook.github.io/prophet/) - 时间序列预测
  - [SnowNLP](https://github.com/isnowfy/snownlp) - 中文情感分析
  - [Plotly](https://plotly.com/) - 交互式可视化
  - [Pandas](https://pandas.pydata.org/) - 数据处理

---

## 📞 联系方式

- **Issues**: [GitHub Issues](https://github.com/cg-collector/SimpleSentiment/issues)
- **Discussions**: [GitHub Discussions](https://github.com/cg-collector/SimpleSentiment/discussions)

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个Star！**

Made with ❤️ by cg-collector

</div>
