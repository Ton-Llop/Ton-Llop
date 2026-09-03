<div align="center">

# Ton Llop

**DevSecOps · Platform & Infrastructure Engineering**<br>

Engineering student at Universitat Rovira i Virgili (Tarragona). I mostly work around backend systems, infrastructure, containers and CI/CD, with a growing focus on security and on-premises AI.

<p>
  <a href="https://www.linkedin.com/in/antoni-llop/"><img src="https://img.shields.io/badge/LinkedIn-antoni--llop-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:tonichi003@gmail.com"><img src="https://img.shields.io/badge/Email-tonichi003@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <img src="https://img.shields.io/badge/Location-Tarragona,%20Spain-4B5563?style=flat-square" alt="Location" />
  <img src="https://komarev.com/ghpvc/?username=Ton-Llop&label=Profile%20views&color=4B5563&style=flat-square" alt="Profile views" />
</p>

</div>

---

## About me

I enjoy building systems where there is more going on than just handling an HTTP request: queues, background workers, containers, retries, failures and services that need to coordinate with each other.

Most of what I work on sits somewhere between backend development and infrastructure. I like figuring out how services should communicate, how to deploy them, how to observe what they are doing and, especially, what happens when something fails.

Lately I've been spending more time on DevSecOps and on running AI workloads locally. I'm interested in the practical side of infrastructure: resource limits, networking, security, performance and the trade-offs behind different deployment decisions.

I also enjoy lower-level topics such as computer architecture and C. They are quite different from infrastructure work, but understanding what happens closer to the hardware helps me reason about systems and performance.

Some of my work lives in private repositories, mainly research software and a mobile application, so the public repositories here are only part of what I've worked on.

I work in English, Spanish and Catalan.

## What I'm working on

* **Local AI infrastructure** — exploring what it actually takes to run LLMs on-premises: hardware requirements, GPU and RAM usage, storage, power consumption and the trade-offs between local and cloud inference. I'm building [Jaull](https://github.com/Ton-Llop/Jaull) around this.

* **DevOps & distributed systems** — experimenting with queue-based architectures, worker scaling, containers, Kubernetes and infrastructure as code.

* **DevSecOps** — learning how to bring security into the development and deployment workflow through network isolation, scanning, secrets management and safer defaults.

* **Homelab** — maintaining a small [homelab](https://github.com/Ton-Llop/Homelab) where I can try all of this on real infrastructure, break things, understand why they broke and document what I learn.

## Selected projects

### Platform & infrastructure

**GSX Infrastructure** · `Public`<br>
An application stack that I deployed in two different ways: locally with Docker Compose and with Kubernetes managed through Terraform. It includes separate network zones, default-deny NetworkPolicies and monitoring with Prometheus, Alertmanager and Grafana.<br>
`Terraform` `Kubernetes` `Docker` `Flask` `Redis` `Prometheus` `Grafana`<br>
→ [Repository](https://github.com/Ton-Llop/GSX-Infrastructure)

**Scalable and Elastic Ticket Service** · `Public`<br>
A distributed ticket-processing system built around RabbitMQ and PostgreSQL. Producers publish work to a queue, Fargate workers process it, and worker capacity is adjusted according to the queue backlog. The project also covers retries, dead-letter queues, idempotency and concurrent processing, with benchmarks for throughput and latency.<br>
`Python` `AWS ECS Fargate` `RabbitMQ` `PostgreSQL` `Docker`<br>
→ [Managed-services version](https://github.com/Ton-Llop/Scalable-and-Elastic-Ticket-Service-AWS-Managed-Systems-) · [Self-hosted EC2 version](https://github.com/Ton-Llop/scalable-tickets)

### AI infrastructure

**Jaull** · `Public`<br>
A project I'm building to understand whether a local LLM deployment will actually fit and behave well on a given machine before running it. It analyses the available hardware, estimates model memory requirements and validates those predictions against real executions.<br>
`Python` → [Repository](https://github.com/Ton-Llop/Jaull)

### Production software

**Lipopotamo — scientific data platform** · `Internal project`<br>
A multi-service platform used for scientific data processing around NMR workflows. I've worked on asynchronous workers, external scientific software execution, batch and sample management, report generation, execution history, partial re-runs and versioned data merging. The platform uses Keycloak for authentication and runs as several communicating services with Docker Compose.<br>
`Python` `FastAPI` `MongoDB` `React` `TypeScript` `Vite` `Keycloak` `Docker Compose`

### Security

**Ninjadorks** · `Public`<br>
A search automation tool I built while learning about OSINT and security research. It can build advanced queries for Google and DuckDuckGo, export results, retrieve selected files and analyse collected content with regex or model-assisted processing.<br>
`Python` `Selenium` → [Repository](https://github.com/Ton-Llop/Google-Dorks) · [Learning labs](https://github.com/Ton-Llop/Cybersecurity-Learning-Labs)

### Homelab & configuration as code

**Homelab** · `Public`<br>
My small self-hosted lab for learning infrastructure by actually running it. I use it to experiment with networking, containers, monitoring, self-hosted services and automation, while keeping the configuration and documentation in Git.<br>
`Python` `Shell` → [Homelab](https://github.com/Ton-Llop/Homelab) · [Debian config](https://github.com/Ton-Llop/Debian-Config)

<details>

<summary><b>Coursework &amp; earlier projects</b></summary>

<br>

**Beer Counter — mobile application** · `Private project`<br>
A social mobile app with authentication, statistics, achievements, friends, leagues, seasons, data export, deep links, moderation and account deletion. The backend uses PostgreSQL with Row Level Security and RPC functions, together with automation workflows.<br>
`Flutter` `Dart` `Supabase` `PostgreSQL` `n8n` → [Google Play](https://play.google.com/store/apps/details?id=com.ton.beerfantasy)

**Single-cycle MIPS processor** · `Public`<br>
A complete single-cycle MIPS datapath and control unit implemented and simulated at gate level.<br>
`Verilog` `TKGate` → [Repository](https://github.com/Ton-Llop/Procesador-MIPS-Monociclo)

**Superscalar processor simulation & Alloyed branch predictor** · `Public`<br>
Simulation of out-of-order execution behaviour and implementation of a hybrid branch predictor to study prediction accuracy.<br>
`C` → [Superscalar](https://github.com/Ton-Llop/P1-AC) · [Alloyed predictor](https://github.com/Ton-Llop/P2-AC)

**Graph centrality at scale** · `Public`<br>
Implementations of PageRank and betweenness centrality for GraphML and Pajek NET graphs, designed to remain usable with graphs containing tens of thousands of vertices.<br>
`Java` → [Repository](https://github.com/Ton-Llop/Practica-final-ED)

**Collaborative filtering & recommendation** · `Public`<br>
Implementations of collaborative filtering techniques for recommendation, together with a separate supply-chain data analysis project.<br>
`Python` → [Recommenders](https://github.com/Ton-Llop/P2-SIO) · [Supply chain analysis](https://github.com/Ton-Llop/P1-SIO)

</details>

## Tech stack

### Infrastructure & cloud

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square\&logo=docker\&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square\&logo=kubernetes\&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square\&logo=terraform\&logoColor=white)
![AWS](https://img.shields.io/badge/AWS%20EC2%20%7C%20ECS%20Fargate-232F3E?style=flat-square\&logo=amazonwebservices\&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square\&logo=prometheus\&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square\&logo=grafana\&logoColor=white)
![Keycloak](https://img.shields.io/badge/Keycloak-4D4D4D?style=flat-square\&logo=keycloak\&logoColor=white)

<sub>Infrastructure as code · container orchestration · network segmentation · observability · metrics · alerting · dashboards</sub>

### CI/CD & security

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square\&logo=githubactions\&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square\&logo=n8n\&logoColor=white)

<sub>Currently going deeper on: Ansible · Helm · Argo CD · Trivy</sub>

### Languages

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square\&logo=typescript\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square\&logo=javascript\&logoColor=black)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=flat-square\&logo=dart\&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square\&logo=kotlin\&logoColor=white)
![Java](https://img.shields.io/badge/Java-E76F00?style=flat-square\&logo=openjdk\&logoColor=white)
![C](https://img.shields.io/badge/C-4B5563?style=flat-square\&logo=c\&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square\&logo=postgresql\&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square\&logo=gnubash\&logoColor=white)
![Verilog](https://img.shields.io/badge/Verilog-1E6B52?style=flat-square)

### Backend & data

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square\&logo=fastapi\&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square\&logo=postgresql\&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square\&logo=mongodb\&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square\&logo=redis\&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square\&logo=supabase\&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square\&logo=rabbitmq\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-1F2937?style=flat-square\&logo=flask\&logoColor=white)

<sub>REST APIs · WebSockets · asynchronous processing · queue-based architectures · background workers</sub>

### Frontend & mobile

![React](https://img.shields.io/badge/React-61DAFB?style=flat-square\&logo=react\&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square\&logo=vite\&logoColor=white)
![Chakra UI](https://img.shields.io/badge/Chakra%20UI-319795?style=flat-square\&logo=chakraui\&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square\&logo=flutter\&logoColor=white)
![Android](https://img.shields.io/badge/Android-3DDC84?style=flat-square\&logo=android\&logoColor=white)

### Tooling

![Linux](https://img.shields.io/badge/Linux-1F2937?style=flat-square\&logo=linux\&logoColor=white)
![WSL](https://img.shields.io/badge/WSL-0078D4?style=flat-square\&logo=windows\&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square\&logo=git\&logoColor=white)
![Neovim](https://img.shields.io/badge/Neovim-57A143?style=flat-square\&logo=neovim\&logoColor=white)
![tmux](https://img.shields.io/badge/tmux-1BB91F?style=flat-square\&logo=tmux\&logoColor=white)

## Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Ton-Llop/Ton-Llop/main/activity-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Ton-Llop/Ton-Llop/main/activity-light.svg" />
  <img alt="Contributions in the last year" src="https://raw.githubusercontent.com/Ton-Llop/Ton-Llop/main/activity-light.svg" width="100%" />
</picture>

</div>

## Get in touch

I'm interested in platform and infrastructure engineering, DevSecOps, distributed systems and on-premises AI. I'm also open to internships where I can keep learning and work on real systems in these areas.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Antoni%20Llop-0A66C2?style=flat-square\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/antoni-llop/)
[![Email](https://img.shields.io/badge/Email-tonichi003@gmail.com-EA4335?style=flat-square\&logo=gmail\&logoColor=white)](mailto:tonichi003@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-@Ton--Llop-181717?style=flat-square\&logo=github\&logoColor=white)](https://github.com/Ton-Llop)

</div>
