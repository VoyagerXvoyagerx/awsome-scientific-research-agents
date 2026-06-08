# 贡献指南

感谢你对 **Awesome Research Agents** 的兴趣！我们欢迎各种形式的贡献，包括添加新项目、修正错误、改进文档等。

## 贡献步骤

1. **Fork 本仓库**

2. **创建特性分支**
   ```bash
   git checkout -b feature/amazing-tool
   ```

3. **修改内容**
   - 在对应的分类表格中添加新项目
   - 确保表格格式与其他行保持一致
   - 按 star 数量从高到低排序（如有）

4. **提交改动**
   ```bash
   git commit -m "Add: 项目名称 - 简短描述"
   ```

5. **推送到分支**
   ```bash
   git push origin feature/amazing-tool
   ```

6. **提交 Pull Request**
   - 在 PR 描述中说明添加的项目及其价值
   - 如有相关论文或演示链接，请一并提供

## 收录标准

- 项目必须与 **AI 辅助科研** 相关
- 优先收录有 GitHub 仓库的**开源项目**
- 项目应至少有一个可验证的发布版本或论文
- Star 数量不是硬性要求，但会影响排序

## 表格格式规范

添加新项目时，请遵循以下格式：

```markdown
| 缩写 | 项目描述 | 类型 | Stars | Paper | 链接 |
```

- **缩写**：项目的简称或常用缩写
- **描述**：一句话概括项目核心功能
- **类型**：`agent` / `skill` / `tool` / `model` 等
- **Stars**：使用 shields.io 动态 badge，格式为 `![GitHub stars](https://img.shields.io/github/stars/owner/repo?style=flat-square&logo=github)`
- **Paper**：论文链接，优先使用 [ModelScope Papers](https://modelscope.cn/papers/) 链接，格式为 `https://modelscope.cn/papers/XXXX.XXXXX/`
- **链接**：GitHub 仓库链接，如有 Demo/官网可一并附上

## 示例

```markdown
| MyAgent | 基于LLM的自动实验设计Agent | agent | ![GitHub stars](https://img.shields.io/github/stars/owner/myagent?style=flat-square&logo=github) | [arXiv 2025](https://modelscope.cn/papers/2501.12345/) | [GitHub](https://github.com/owner/myagent) / [Demo](https://myagent.ai) |
```

## 其他贡献方式

- 报告失效链接
- 修正项目描述
- 更新 star 数量（badge 会自动刷新，无需手动更新）
- 改进文档或翻译

---

如有疑问，欢迎通过 [Issue](https://github.com/VoyagerXvoyagerx/awsome-scientific-research-agents/issues) 提出讨论。
