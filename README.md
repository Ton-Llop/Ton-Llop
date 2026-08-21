<div align="center">

# Ton Llop

**Engineering student at Universitat Rovira i Virgili (Tarragona)**<br>
Backend, distributed systems and infrastructure — from message queues and containers up to MIPS processors in Verilog.

<p>
  <a href="https://www.linkedin.com/in/antoni-llop/"><img src="https://img.shields.io/badge/LinkedIn-antoni--llop-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:tonichi003@gmail.com"><img src="https://img.shields.io/badge/Email-tonichi003@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <img src="https://img.shields.io/badge/Location-Tarragona,%20Spain-4B5563?style=flat-square" alt="Location" />
  <img src="https://komarev.com/ghpvc/?username=Ton-Llop&label=Profile%20views&color=4B5563&style=flat-square" alt="Profile views" />
</p>

</div>

---

## About me

I build systems that have to keep working when things go wrong: queues that lose messages, workers that die halfway through a job, containers that need to find each other, pipelines that must not process the same request twice.

Most of my work sits between the backend and the infrastructure underneath it — designing APIs, wiring services together with Docker, moving processing off the request path into workers, and then measuring whether the result actually scales. I also spend time closer to the metal, in computer architecture and low-level C, and I like that both ends of that spectrum inform each other.

Part of what I do lives in private repositories (research software and a mobile application), so the public side of this profile is only part of the picture.

I work in English, Spanish and Catalan.

## What I'm working on

- **Scientific data platform** — modular, containerized services for scientific data processing, built with FastAPI and a React/TypeScript frontend.
- **Local AI infrastructure** — researching how an organization can run models on-premises: compute server, NAS storage, rented vs. owned GPUs, and the cost/performance/consumption trade-off against cloud inference.
- **Distributed systems** — queue-based architectures, worker autoscaling, and understanding where the real bottleneck is instead of guessing.
- **Cybersecurity** — an ongoing learning track: tooling, automation and hands-on labs.

## Selected projects

### Distributed systems & cloud

**Scalable and Elastic Ticket Service** · `Public`<br>
A ticket-processing system on AWS managed services: producers publish to RabbitMQ, stateless Fargate workers consume and commit to PostgreSQL, and a scaler adjusts worker count from queue backlog. Implements idempotency keys, at-least-once delivery with retries and dead-letter queues, and consistency guarantees under concurrency. Includes a benchmark suite measuring throughput, speedup and p50/p95/p99 latency across worker counts.<br>
`Python` `AWS ECS Fargate` `RabbitMQ` `PostgreSQL` `Docker`<br>
→ [Managed-services version](https://github.com/Ton-Llop/Scalable-and-Elastic-Ticket-Service-AWS-Managed-Systems-) · [self-hosted EC2 version](https://github.com/Ton-Llop/scalable-tickets)

**GSX Infrastructure** · `Public`<br>
A full application stack deployed two ways — Docker Compose locally and Kubernetes manifests orchestrated with Terraform — with network segmentation (DMZ / internal / data / monitoring), default-deny NetworkPolicies, and an observability layer of Prometheus, Alertmanager and Grafana.<br>
`Terraform` `Kubernetes` `Docker` `Flask` `Redis` `Prometheus` `Grafana`<br>
→ [Repository](https://github.com/Ton-Llop/GSX-Infrastructure)

### Scientific & production software

**Lipopotamo — scientific data platform** · `Internal project`<br>
Modular platform for processing and managing scientific data, with workflows around NMR analysis. Asynchronous processing through specialized workers, execution of scientific software, management of batches/samples/runs and their outputs, report generation, execution history, partial re-runs and versioned merge strategies — across multiple communicating services.<br>
`Python` `FastAPI` `MongoDB` `React` `TypeScript` `Vite` `Keycloak` `Docker Compose`

**Beer Counter — mobile application** · `Private project`<br>
A complete social mobile app: authentication, statistics, achievements, friends, leagues and seasons, data export, deep links, moderation and account deletion. Backed by PostgreSQL with Row Level Security and RPC functions, plus automation workflows.<br>
`Flutter` `Dart` `Supabase` `PostgreSQL` `n8n` → [Link](https://play.google.com/store/apps/details?id=com.ton.beerfantasy)


### Computer architecture

**Single-cycle MIPS processor** · `Public` — full datapath and control unit implemented and simulated at gate level.<br>
`Verilog` `TKGate` → [Repository](https://github.com/Ton-Llop/Procesador-MIPS-Monociclo)

**Superscalar processor simulation & Alloyed branch predictor** · `Public` — modelling out-of-order execution behaviour and implementing a hybrid branch predictor, then analysing prediction accuracy.<br>
`C` → [Superscalar](https://github.com/Ton-Llop/P1-AC) · [Alloyed predictor](https://github.com/Ton-Llop/P2-AC)

### Algorithms & data

**Graph centrality at scale** · `Public`<br>
PageRank and betweenness centrality over graphs loaded from GraphML and Pajek NET, designed to stay usable on real-world web graphs of 10K–100K+ vertices.<br>
`Java` → [Repository](https://github.com/Ton-Llop/Practica-final-ED)

**Collaborative filtering & recommendation** · `Public`<br>
Implementation of collaborative filtering methods for personalization and recommendation, plus supply-chain data analysis.<br>
`Python` → [Recommenders](https://github.com/Ton-Llop/P2-SIO) · [Supply chain analysis](https://github.com/Ton-Llop/P1-SIO)

### Security (learning track)

**Ninjadorks** · `Public`<br>
Search-automation toolkit for authorized research: advanced query building across Google and DuckDuckGo, structured JSON/HTML export, selective file retrieval, and regex or model-assisted analysis of the results.<br>
`Python` `Selenium` → [Repository](https://github.com/Ton-Llop/Google-Dorks) · [Learning labs](https://github.com/Ton-Llop/Cybersecurity-Learning-Labs)

## Tech stack

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white)
![Java](https://img.shields.io/badge/Java-E76F00?style=flat-square&logo=openjdk&logoColor=white)
![C](https://img.shields.io/badge/C-4B5563?style=flat-square&logo=c&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![Verilog](https://img.shields.io/badge/Verilog-1E6B52?style=flat-square)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

**Backend & data**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-1F2937?style=flat-square&logo=flask&logoColor=white)

<sub>Also: REST APIs · WebSockets · asynchronous processing · queue-based and worker architectures</sub>

**Frontend & mobile**

![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Chakra UI](https://img.shields.io/badge/Chakra%20UI-319795?style=flat-square&logo=chakraui&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)
![Android](https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=android&logoColor=white)

**Infrastructure & cloud**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS%20EC2%20%7C%20ECS%20Fargate-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)
![Keycloak](https://img.shields.io/badge/Keycloak-4D4D4D?style=flat-square&logo=keycloak&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white)

**Tooling**

![Linux](https://img.shields.io/badge/Linux-1F2937?style=flat-square&logo=linux&logoColor=white)
![WSL](https://img.shields.io/badge/WSL-0078D4?style=flat-square&logo=windows&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Neovim](https://img.shields.io/badge/Neovim-57A143?style=flat-square&logo=neovim&logoColor=white)
![tmux](https://img.shields.io/badge/tmux-1BB91F?style=flat-square&logo=tmux&logoColor=white)

## Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Ton-Llop/Ton-Llop/main/activity-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Ton-Llop/Ton-Llop/main/activity-light.svg" />
  <img alt="Contributions in the last year" src="https://raw.githubusercontent.com/Ton-Llop/Ton-Llop/main/activity-light.svg" width="100%" />
</picture>

</div>

## Get in touch

Open to collaborating on backend platforms, distributed and queue-based systems, cloud infrastructure, scientific software, local AI infrastructure, and complete web or mobile applications. Also interested in internships and thesis projects in these areas.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Antoni%20Llop-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/antoni-llop/)
[![Email](https://img.shields.io/badge/Email-tonichi003@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:tonichi003@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-@Ton--Llop-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Ton-Llop)

</div>
