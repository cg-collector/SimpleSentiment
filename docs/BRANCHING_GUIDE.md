# 🔀 垂直领域分支开发指南

## 分支命名规范

```
main                        ← 通用基础版，不要直接在这上面做领域定制
├── domain/legal            ← 法律舆情
├── domain/finance          ← 金融舆情
├── domain/healthcare       ← 医疗舆情
└── domain/education        ← 教育舆情
```

---

## Prompt 1：创建法律领域分支并完成定制开发

在 Claude Code 里说：

```
基于当前 main 分支创建一个新分支 domain/legal，将 SimpleSentiment 舆情系统定制为法律领域专用版本。

具体要做的事情：

1. 创建并切换分支
   git checkout -b domain/legal

2. 配置层改动
   - config.py: 新增法律领域配置区块，包含：
     - 默认监控关键词：司法判决、法律援助、知识产权、劳动仲裁、合同纠纷、
       刑事案件、民事诉讼、最高法、检察院、律师、法治、立法、司法解释等
     - 法律新闻数据源URL
     - 领域标识 DOMAIN = "legal"

3. 数据采集层改动
   - collectors/: 新增或修改采集器，支持法律类数据源：
     - 法治日报、最高人民法院公告、中国裁判文书网（如果有公开接口）
     - 微博法律话题过滤（#法律# #司法# 等超话）
   - 采集后的数据打上领域标签

4. 分析层改动
   - analyzers/sentiment.py: 调整情感分析逻辑，区分：
     - 法律文本本身（判决书、法规）→ 偏中性事实
     - 公众对法律事件的评论 → 正常情感分析
   - analyzers/keyword_extractor.py: 加载法律领域专用词典
     - 创建 data/legal_dict.txt，包含法律术语（侵权、违约、管辖、
       上诉、执行、调解、仲裁、辩护、量刑等）
     - 分词时优先使用领域词典

5. 预测层改动
   - predictors/llm_predictor.py: 修改 prompt 模板为法律领域版本
     - 分析维度加入：案件类型分布、涉法主体、法律条文引用频率、
       判决趋势、公众法律意识变化
     - 风险提示关注：群体性事件、司法公信力、冤假错案舆论等

6. 前端界面改动
   - pages/ 下所有页面的标题和文案改为"法律舆情"
   - 监测页面：预设法律类关键词分组（刑事、民事、行政、知识产权等）
   - 分析页面：新增"案件类型分布"图表、"涉法主体"统计
   - 预测页面：法律舆情专用分析报告模板
   - 系统logo/标题改为"法律舆情监测分析系统"

7. 报告模板改动
   - 生成的报告加入法律领域要素：
     - 热点案件追踪
     - 法律条文关联分析
     - 司法舆论风险评估

8. 测试
   - 用几个法律相关关键词（如"劳动仲裁""知识产权"）跑一遍完整流程
   - 确保采集→分析→预测→可视化全链路通畅

9. 提交并推送
   git add -A
   git commit -m "feat(legal): 法律领域舆情系统定制

   - 新增法律领域关键词库和专用词典
   - 适配法律类数据源采集
   - 情感分析区分法律文本与公众评论
   - LLM prompt 定制为法律分析模板
   - 前端界面全面改为法律舆情主题
   - 新增案件类型分布、涉法主体等分析维度"

   git push origin domain/legal

全程自动执行，不需要问我确认。
```

---

## Prompt 2：未来做其他领域时的模板

把 `{DOMAIN}` `{DOMAIN_CN}` `{KEYWORDS}` `{SOURCES}` `{ANALYSIS_DIMS}` 替换即可：

```
基于 main 分支创建新分支 domain/{DOMAIN}，将 SimpleSentiment 定制为{DOMAIN_CN}领域专用版本。

1. git checkout main && git pull && git checkout -b domain/{DOMAIN}

2. config.py 新增领域配置：
   - 关键词：{KEYWORDS}
   - 数据源：{SOURCES}
   - DOMAIN = "{DOMAIN}"

3. collectors/ 适配领域数据源
4. analyzers/ 加载领域专用词典（创建 data/{DOMAIN}_dict.txt）
5. predictors/llm_predictor.py prompt 改为{DOMAIN_CN}分析模板，
   分析维度：{ANALYSIS_DIMS}
6. pages/ 界面文案和标题改为"{DOMAIN_CN}舆情"
7. 测试完整流程
8. git commit + push to domain/{DOMAIN}

全程自动执行。
```

### 示例：金融领域

```
基于 main 分支创建新分支 domain/finance，将 SimpleSentiment 定制为金融领域专用版本。

1. git checkout main && git pull && git checkout -b domain/finance

2. config.py 新增领域配置：
   - 关键词：股票、基金、A股、美联储、降息、IPO、财报、暴雷、爆仓、监管处罚
   - 数据源：东方财富、同花顺、证监会公告、财经新闻
   - DOMAIN = "finance"

3. collectors/ 适配金融数据源
4. analyzers/ 加载金融专用词典（创建 data/finance_dict.txt）
5. predictors/llm_predictor.py prompt 改为金融分析模板，
   分析维度：行业板块分布、个股舆情热度、政策影响评估、市场情绪指数
6. pages/ 界面文案和标题改为"金融舆情"
7. 测试完整流程
8. git commit + push to domain/finance

全程自动执行。
```

---

## 从 main 同步更新到领域分支

当 main 有 bugfix 或新功能时：

```
把 main 分支的最新更新合并到 domain/legal 分支。
git checkout domain/legal
git merge main
如果有冲突，保留 domain/legal 的领域定制内容，合入 main 的通用改动。
解决完冲突后 commit 并 push。
```

---

## 注意事项

- 领域分支只改**配置、词典、prompt、界面文案**，尽量不动核心引擎逻辑
- 如果某个领域需要的功能改动是通用的（比如新增一种图表类型），先在 main 上做，再 merge 到各分支
- 这样 main 始终是最完整最稳定的基础版本
