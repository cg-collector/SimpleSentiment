# 🚀 一句话启动指南

## 准备
1. 把范文放到项目根目录，命名为 `reference_paper.pdf`
2. 进入项目目录

## 启动

### 交互模式（推荐）
```bash
claude
```
然后说：
> 阅读 CLAUDE.md，按里面定义的工作流自动执行全部 Phase。论文题目是《基于多源数据融合的轻量级舆情监测分析与预测系统设计与实现》，范文是 ./reference_paper.pdf。大纲生成后暂停让我确认，其他步骤全自动跑完，最终输出 output/thesis.docx。

### 全自动模式
```bash
./start.sh
# 或用 tmux 挂机: tmux new -s thesis -d './start.sh'
```

## 恢复中断
> 继续执行 CLAUDE.md 工作流，检查 output/ 看完成到哪了，从断点继续。

## 只重写某章
> 重新写第4章，按 CLAUDE.md 的写作规范和AIGC自检流程执行。

## 只生成docx
> 读 output/full_paper.md，按 CLAUDE.md 的格式规范生成 output/thesis.docx。
