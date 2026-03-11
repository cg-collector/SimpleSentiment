# 简化版舆情系统目录结构

```
SimpleSentiment/                    # 新项目名称
├── config.py                       # 配置文件
├── requirements.txt                # 依赖包（精简版）
├── .env                            # 环境变量
├── app.py                          # Streamlit主应用
│
├── data/                           # 数据目录
│   ├── raw/                        # 原始数据
│   └── database.db                 # SQLite数据库
│
├── collectors/                     # 数据采集模块
│   ├── __init__.py
│   ├── news_api.py                 # 新闻API采集
│   ├── weibo_crawler.py            # 微博爬虫
│   └── base.py                     # 采集器基类
│
├── analyzers/                      # 舆情分析模块
│   ├── __init__.py
│   ├── sentiment.py                # 情感分析
│   ├── keyword_extractor.py        # 关键词提取
│   └── trend_analyzer.py           # 趋势分析
│
├── predictors/                     # 舆情预测模块
│   ├── __init__.py
│   ├── time_series.py              # 时间序列预测
│   └── llm_predictor.py            # LLM辅助预测
│
├── models/                         # 模型文件
│   ├── sentiment_model.pkl         # 情感分析模型
│   └── README.md                   # 模型说明
│
├── utils/                          # 工具函数
│   ├── __init__.py
│   ├── database.py                 # 数据库操作
│   ├── llm_client.py               # LLM客户端
│   └── visualizer.py               # 可视化工具
│
└── tests/                          # 测试文件
    ├── test_collectors.py
    └── test_analyzers.py
```

---

## 核心文件说明

### 1. app.py - Streamlit主应用
```python
import streamlit as st

# 侧边栏导航
page = st.sidebar.radio("选择功能", [
    "舆情监测",
    "舆情分析",
    "舆情预测",
    "系统设置"
])

if page == "舆情监测":
    from pages import monitoring
    monitoring.show()
elif page == "舆情分析":
    from pages import analysis
    analysis.show()
elif page == "舆情预测":
    from pages import prediction
    prediction.show()
```

### 2. collectors/news_api.py - 新闻API采集
```python
class NewsAPICollector:
    """使用公开新闻API采集数据"""

    def collect(self, keyword: str, days: int = 7):
        """采集指定关键词的新闻"""
        # 调用NewsAPI或国内新闻API
        pass

    def save_to_db(self, data):
        """保存到数据库"""
        pass
```

### 3. analyzers/sentiment.py - 情感分析
```python
class SentimentAnalyzer:
    """情感分析器"""

    def __init__(self):
        # 加载预训练模型或LLM
        self.model = load_model()

    def analyze(self, text: str):
        """分析文本情感"""
        # 返回: positive/negative/neutral + 置信度
        pass
```

### 4. predictors/time_series.py - 时间序列预测
```python
class TrendPredictor:
    """趋势预测器"""

    def predict(self, historical_data, days=7):
        """预测未来几天的趋势"""
        # 使用prophet或简单模型
        pass
```

---

## 精简的依赖包

```
# Web框架
streamlit>=1.28.0

# 数据处理
pandas>=2.0.0
numpy>=1.24.0

# 数据库
sqlalchemy>=2.0.0
sqlite3  # Python内置

# 爬虫
requests>=2.31.0
beautifulsoup4>=4.12.0
playwright>=1.40.0  # 可选，如需动态页面

# LLM
openai>=1.3.0

# 机器学习
scikit-learn>=1.3.0
transformers>=4.30.0  # 如需本地模型

# 可视化
plotly>=5.17.0
wordcloud>=1.9.3
matplotlib>=3.7.0

# 时间序列预测
prophet>=1.1.0  # Meta的预测库

# 工具
python-dotenv>=1.0.0
```

---

## 配置文件

### .env
```bash
# 数据库
DB_PATH=data/database.db

# LLM配置
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-4o-mini

# 新闻API
NEWS_API_KEY=your_newsapi_key

# 爬虫配置
CRAWL_DELAY=1  # 请求间隔（秒）
```

---

## 功能优先级

### 第一阶段（核心功能）
1. ✅ 数据采集：新闻API + 简单微博爬虫
2. ✅ 情感分析：基础情感分类
3. ✅ 数据展示：Streamlit简单界面

### 第二阶段（分析增强）
4. ✅ 关键词提取和词云
5. ✅ 趋势图表
6. ✅ 数据存储和查询

### 第三阶段（预测功能）
7. ✅ 时间序列预测
8. ✅ LLM趋势分析

---

## 预计工作量

- **总代码量**: 约1500-2500行（vs 原项目数万行）
- **开发时间**: 1-2周（课程项目足够）
- **难度**: 中等，适合课程项目

---

## 下一步操作

1. 是否开始创建简化项目？
2. 先从哪个模块开始？（建议先做数据采集）
3. 需要我帮你写具体代码吗？
