AIOps 告警降噪与自愈原型

基于开源技术栈（Prometheus + Grafana + Docker + Python）实现的智能运维自愈原型系统。当服务响应时间超标时，系统自动执行容器重启，实现故障自愈闭环。

 项目背景

在分布式、云原生环境下，传统运维面临数据爆炸、系统复杂、响应迟缓等挑战。本项目通过 AIOps 理念，构建了一个 **监控 → 检测 → 自愈 → 可视化** 的完整闭环，验证了开源工具链在运维自动化中的可行性。

技术架构

![架构图](screenshots/architecture.png) 

| 组件 | 技术选型 | 作用 | 开源协议 |

| 业务服务 | Python + Flask | 模拟订单系统，暴露 `/order` 接口 | BSD-3-Clause |
| 监控采集 | Prometheus | 抓取服务指标，存储时序数据 | Apache-2.0 |
| 可视化 | Grafana | 展示响应时间趋势曲线 | AGPL-3.0 |
| 自愈控制 | Python + Docker CLI | 查询 Prometheus API，超标时重启容器 | — |
| 容器编排 | Docker Compose | 一键启动所有服务 | Apache-2.0 |

快速开始

前提条件
- Docker Desktop（或 Docker Engine + Compose）
- Python 3.8+（用于运行自愈脚本）

启动项目
```bash
# 克隆仓库
git clone https://github.com/你的用户名/aiops-self-healing-prototype.git
cd aiops-self-healing-prototype

# 启动所有容器
docker compose up -d --build

