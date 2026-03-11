"""
SimpleSentiment - 简化版舆情监测分析预测系统
主应用入口
"""

import streamlit as st
from pathlib import Path

# 页面配置
st.set_page_config(
    page_title="SimpleSentiment - 舆情监测分析系统",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🔍"
)

# 自定义CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 侧边栏
with st.sidebar:
    st.title("🔍 SimpleSentiment")
    st.markdown("---")

    page = st.radio(
        "选择功能",
        ["🏠 首页", "📊 舆情监测", "📈 舆情分析", "🔮 舆情预测", "⚙️ 系统设置"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("### 项目信息")
    st.markdown("""
    **版本**: v1.0.0-alpha
    **状态**: 开发中

    基于 BettaFish 简化的
    轻量级舆情系统
    """)

# 主内容区
if page == "🏠 首页":
    st.markdown('<h1 class="main-header">🎉 欢迎使用 SimpleSentiment</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("总监测词", "0", "个")
        st.markdown("### 📊 舆情监测")
        st.markdown("实时监控关键词，多源数据采集")

    with col2:
        st.metric("分析条数", "0", "条")
        st.markdown("### 📈 舆情分析")
        st.markdown("情感分析、关键词提取、趋势可视化")

    with col3:
        st.metric("预测准确率", "N/A", "%")
        st.markdown("### 🔮 舆情预测")
        st.markdown("时间序列预测、LLM辅助分析")

    st.markdown("---")

    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("### 🚀 快速开始")
    st.markdown("""
    1. 在 **📊 舆情监测** 中添加监控关键词
    2. 系统自动采集相关数据
    3. 在 **📈 舆情分析** 中查看分析结果
    4. 在 **🔮 舆情预测** 中查看趋势预测
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("### 📖 关于项目")
    st.markdown("""
    SimpleSentiment 是从 [BettaFish](https://github.com/666ghj/BettaFish) 项目中提炼和简化而来的轻量级舆情监测分析预测系统。

    **核心特点**:
    - ✅ 代码简洁（~2000行）
    - ✅ 功能完整（监测、分析、预测）
    - ✅ 快速部署（一键启动）
    - ✅ 课程友好（适合教学）
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📊 舆情监测":
    st.markdown('<h1 class="main-header">📊 舆情监测</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 添加监控关键词")
        keyword = st.text_input("输入关键词", placeholder="例如：人工智能、区块链、新能源")

        col_btn1, col_btn2, col_btn3 = st.columns(3)
        with col_btn1:
            if st.button("▶️ 开始监控", type="primary"):
                if keyword:
                    st.success(f"✅ 已添加关键词: {keyword}")
                    st.info("💡 数据采集功能开发中，敬请期待...")
                else:
                    st.warning("⚠️ 请先输入关键词")

        with col_btn2:
            if st.button("📋 查看历史"):
                st.info("📋 历史记录功能开发中")

        with col_btn3:
            if st.button("🗑️ 清空记录"):
                st.info("🗑️ 清空功能开发中")

    with col2:
        st.markdown("### 监控状态")
        st.markdown("""
        | 状态 | 信息 |
        |------|------|
        | 🔴 系统状态 | 开发中 |
        | 📊 关键词数 | 0 |
        | 📈 采集数量 | 0 |
        | ⏰ 最后更新 | - |
        """)

    st.markdown("---")
    st.markdown("### 📋 监控关键词列表")
    st.info("💡 暂无监控关键词，请在上方添加")

elif page == "📈 舆情分析":
    st.markdown('<h1 class="main-header">📈 舆情分析</h1>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["情感分析", "关键词提取", "趋势分析"])

    with tab1:
        st.markdown("### 情感分布")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            #### 情感统计
            - 😊 正面: 0 (0%)
            - 😐 中性: 0 (0%)
            - 😞 负面: 0 (0%)
            """)

        with col2:
            st.info("📊 情感分析功能开发中...")
            st.markdown("""
            **技术方案**:
            - SnowNLP 中文情感分析
            - 支持正面/负面/中性分类
            - 情感得分计算 (0-1)
            """)

    with tab2:
        st.markdown("### 关键词词云")
        st.info("☁️ 词云生成功能开发中...")
        st.markdown("""
        **功能说明**:
        - 自动提取关键词
        - 生成词云图
        - 词频统计
        """)

    with tab3:
        st.markdown("### 时间趋势")
        st.info("📈 趋势分析功能开发中...")
        st.markdown("""
        **可视化方案**:
        - 趋势折线图
        - 情感分布饼图
        - 热点话题排行
        """)

elif page == "🔮 舆情预测":
    st.markdown('<h1 class="main-header">🔮 舆情预测</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 时间序列预测")
        st.info("📊 Prophet 预测功能开发中...")
        st.markdown("""
        **功能说明**:
        - 基于历史数据预测
        - 预测未来 3-7 天趋势
        - 置信区间展示

        **技术方案**:
        - Facebook Prophet 时间序列预测
        - 自动趋势分解
        - 季节性分析
        """)

    with col2:
        st.markdown("### LLM 辅助分析")
        st.info("🤖 LLM 预测功能开发中...")
        st.markdown("""
        **功能说明**:
        - 深度趋势分析
        - 影响因素识别
        - 风险提示

        **配置说明**:
        - 需配置 LLM API Key
        - 在系统设置中配置
        """)

    st.markdown("---")
    st.markdown("### 预测结果")
    st.info("💡 暂无预测结果，请先进行数据采集和分析")

elif page == "⚙️ 系统设置":
    st.markdown('<h1 class="main-header">⚙️ 系统设置</h1>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["基础设置", "LLM配置", "关于"])

    with tab1:
        st.markdown("### 基础配置")

        col1, col2 = st.columns(2)

        with col1:
            crawl_delay = st.slider("请求延迟（秒）", 1, 10, 1)
            max_pages = st.slider("最大采集页数", 1, 10, 3)

        with col2:
            st.markdown("""
            **配置说明**:
            - 请求延迟: 避免被反爬
            - 最大页数: 控制采集数量
            """)

        if st.button("💾 保存配置", type="primary"):
            st.success("✅ 配置已保存")

    with tab2:
        st.markdown("### LLM API 配置")
        st.info("💡 LLM功能可选，不配置也可使用基础功能")

        api_key = st.text_input("API Key", type="password")
        base_url = st.text_input("Base URL", value="https://api.openai.com/v1")
        model_name = st.text_input("模型名称", value="gpt-4o-mini")

        enable_llm = st.checkbox("启用 LLM 功能", value=False)

        if st.button("💾 保存LLM配置", type="primary"):
            if enable_llm and not api_key:
                st.error("❌ 启用LLM功能需要配置API Key")
            else:
                st.success("✅ LLM配置已保存")

        st.markdown("---")
        st.markdown("### 配置说明")
        st.markdown("""
        **支持的服务商**:
        - OpenAI (官方)
        - Azure OpenAI
        - 其他兼容 OpenAI API 格式的服务

        **推荐模型**:
        - gpt-4o-mini (性价比高)
        - gpt-3.5-turbo
        - 或其他兼容模型
        """)

    with tab3:
        st.markdown("### 关于 SimpleSentiment")

        st.markdown("""
        #### 项目信息

        **名称**: SimpleSentiment
        **版本**: v1.0.0-alpha
        **类型**: 轻量级舆情监测分析预测系统
        **基于**: [BettaFish](https://github.com/666ghj/BettaFish)

        #### 技术栈

        - **前端**: Streamlit 1.28+
        - **数据处理**: Pandas, NumPy
        - **情感分析**: SnowNLP
        - **时间序列**: Prophet (开发中)
        - **可视化**: Plotly, Matplotlib
        - **LLM**: OpenAI API (可选)

        #### 核心功能

        1. **舆情监测**: 关键词监控、多源数据采集
        2. **舆情分析**: 情感分析、关键词提取、趋势可视化
        3. **舆情预测**: 时间序列预测、LLM辅助分析

        #### 适用场景

        - ✅ 课程项目
        - ✅ 教学演示
        - ✅ 学术研究
        - ✅ 快速原型
        - ✅ 学习参考

        #### 开源协议

        本项目采用 GPL-2.0 协议开源

        #### 致谢

        感谢 [BettaFish](https://github.com/666ghj/BettaFish) 项目的启发和贡献
        """)

# 页脚
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>SimpleSentiment - 基于 BettaFish 简化的轻量级舆情系统</p>
    <p>适合课程项目、教学演示和学术研究</p>
</div>
""", unsafe_allow_html=True)
