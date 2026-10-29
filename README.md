# 2026 Autumn CME295 · Transformers & LLMs 学习笔记

Stanford **CME 295 Transformers & Large Language Models**（Autumn 2026）自学笔记与学习成果。

- 课程官网：<https://cme295.stanford.edu/>
- 教材（免费）：<https://superstudy.guide/>
- 主讲：Afshine & Shervine Amidi（CS229/CS230 著名速查表作者）

## 目录结构

```
├── 学习计划.md               # 9 讲 → 5 阶段学习路线 + 自定速节奏
├── 参考文献清单.md           # 按讲次整理的论文清单（带 arXiv 编号）
├── 学习总结/
│   ├── 第一讲学习总结.md     # Transformers（token/嵌入 → QKV 注意力 → 多头 → 掩码 → 位置编码）
│   ├── 第二讲学习总结.md     # Large Language Models（BERT vs GPT、RoPE、MHA/MQA/GQA、MoE、解码）
│   └── 第三讲学习总结.md     # LLM Training（预训练 → 中期训练 → SFT → RLHF/DPO → 推理训练）
├── 视频转写稿/               # 第 1~3 讲 YouTube 视频的人工字幕转写（纯文本 + 带时间戳）
├── 动手实验/
│   └── next_word_predictor_slides.html   # 「词 → 向量 → 预测」全流程的可翻页演示
├── 参考论文/
│   └── attention-is-all-you-need.pdf     # Transformer 源头论文（Vaswani et al., 2017）
└── 工具/
    └── download.py           # 课件/论文批量下载脚本（含直连回退）
```

## 视频地址

| 讲次 | 主题 | 视频 |
|------|------|------|
| 1 | Transformers | <https://www.youtube.com/watch?v=114i2Kz-LZA> |
| 2 | Large Language Models | <https://www.youtube.com/watch?v=GaIeu3npx04> |
| 3 | LLM Training | <https://www.youtube.com/watch?v=S3bCDcJhz4s> |

## 说明

- 学习总结由 AI 助理结合课程视频转写稿、官方速查表，以及多份公开学习资料（Khoa Nguyen 笔记、FelisaChow 中文逐讲笔记、SutirthaSaha 十步笔记、Sara Jalili Field Notes）整理而成。
- 视频转写稿通过 `yt-dlp` 抓取官方字幕生成，仅供个人学习参考。
