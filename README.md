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


启动所有容器
docker compose up -d --build
验证自愈效果
访问 http://localhost:5000/order，多次刷新模拟请求。

观察 heal_script.py 终端输出，当响应时间超过阈值时，触发自愈。

执行 docker ps，查看 order-service 容器的启动时间是否刷新。

<img width="2350" height="1226" alt="屏幕截图 2026-06-29 151051" src="https://github.com/user-attachments/assets/263fa40d-e44d-4716-a989-6d1c83d381fa" />

自愈日志

<img width="2350" height="1226" alt="屏幕截图 2026-06-29 151915" src="https://github.com/user-attachments/assets/f2a52e6f-815b-4826-9d00-9f850e51bb15" />


Grafana 响应时间曲线

<img width="2880" height="1704" alt="屏幕截图 2026-06-29 160313" src="https://github.com/user-attachments/assets/dd5874a7-5a65-4a23-9529-3a9e712627f0" />



踩坑记录
Docker 镜像加速器失效：中科大镜像源不稳定，更换为 DaoCloud 镜像源解决。

Flask 与 Werkzeug 版本冲突：Flask 2.2.3 与 Werkzeug 3.1.8 不兼容，升级 Flask 至 2.3.3 并固定 Werkzeug 2.3.8 解决。



开源协议
本项目遵循 MIT License（可替换为 GPL 或 Apache，建议 MIT 更宽松）。使用到的开源工具及其协议：

Prometheus：Apache-2.0

Grafana：AGPL-3.0

Flask：BSD-3-Clause

参考资料
Prometheus 官方文档

Grafana 官方文档

Docker Compose 文档

本课程项目参考了 CSDN 博客《智能运维 AIOps 实战教程》的思路，并结合开源社区的最佳实践实现。





