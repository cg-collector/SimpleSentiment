#!/bin/bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

if [ ! -f "config.env" ]; then echo "❌ 找不到 config.env"; exit 1; fi
source config.env

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'; NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}   硕士论文自动写作系统${NC}"
echo -e "${BLUE}========================================${NC}"
echo -e "论文题目: ${GREEN}${PAPER_TITLE}${NC}"

if ! command -v claude &> /dev/null; then
    echo -e "${RED}❌ 未找到 claude，请先 npm install -g @anthropic-ai/claude-code${NC}"; exit 1
fi

mkdir -p output/chapters
SESSION_ID="thesis-$(date +%Y%m%d%H%M%S)"
echo -e "${GREEN}Session: ${SESSION_ID}${NC}"
echo -e "${YELLOW}启动时间: $(date '+%Y-%m-%d %H:%M:%S')${NC}"

claude -p "阅读 CLAUDE.md，按里面定义的工作流自动执行全部 Phase。论文题目是《${PAPER_TITLE}》，范文是 ${REFERENCE_PAPER_PATH}。大纲直接按 CLAUDE.md 里的结构执行不用等确认，全部步骤跑完，最终输出 output/${OUTPUT_FILENAME}。" \
    --dangerously-skip-permissions \
    --max-turns 200 \
    --session-id "$SESSION_ID"

if [ -f "output/${OUTPUT_FILENAME}" ]; then
    echo -e "${GREEN}✅ 完成！output/${OUTPUT_FILENAME} ($(du -h "output/${OUTPUT_FILENAME}" | cut -f1))${NC}"
else
    echo -e "${YELLOW}⚠️ 可能未完成，继续命令：${NC}"
    echo "claude -p \"继续执行\" --continue --session-id ${SESSION_ID} --dangerously-skip-permissions --max-turns 200"
fi
