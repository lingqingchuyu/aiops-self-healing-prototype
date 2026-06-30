AIOps 告警降噪与自愈原型

基于开源技术栈（Prometheus + Grafana + Docker + Python）实现的智能运维自愈原型系统。当服务响应时间超标时，系统自动执行容器重启，实现故障自愈闭环。

 项目背景

在分布式、云原生环境下，传统运维面临数据爆炸、系统复杂、响应迟缓等挑战。本项目通过 AIOps 理念，构建了一个 **监控 → 检测 → 自愈 → 可视化** 的完整闭环，验证了开源工具链在运维自动化中的可行性。

系统架构说明：

本项目采用分层解耦的微服务架构，所有组件均基于开源技术构建，各模块职责清晰：

业务服务层：基于 Python 和 Flask 框架开发，模拟订单系统的核心业务逻辑，对外暴露 /order 接口用于接收请求，并集成 Prometheus Client 库以标准格式暴露服务运行指标。该部分遵循 BSD-3-Clause 协议。

监控采集层：采用 Prometheus 作为监控数据采集与存储组件。它通过 Pull 模式定期抓取业务服务 /metrics 接口的指标数据，并按时间序列存储，为后续分析和告警提供数据基础。Prometheus 采用 Apache-2.0 协议。

可视化层：使用 Grafana 构建仪表盘，连接 Prometheus 数据源，将响应时间等关键指标以曲线图形式实时展示，便于观测系统状态变化趋势。Grafana 采用 AGPL-3.0 协议。

自愈控制层：通过 Python 脚本实现，该脚本持续调用 Prometheus API 查询业务服务的平均响应时间，当检测到指标超过预设阈值时，自动调用 Docker CLI 命令重启业务服务容器，完成故障自愈闭环。该脚本为项目自有代码，未使用第三方开源组件。

容器编排层：利用 Docker Compose 定义并管理所有容器化服务（业务服务、Prometheus、Grafana），实现一键启动、停止和依赖管理，简化部署流程。Docker Compose 采用 Apache-2.0 协议。

各层之间通过标准 HTTP 接口和容器网络进行通信，形成了“数据采集 → 监控告警 → 异常检测 → 自愈执行 → 可视化反馈”的完整智能运维链路。

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





