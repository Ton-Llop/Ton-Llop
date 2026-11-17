<div align="center">

# Ton Llop

Infrastructure, DevOps and local AI · final-year engineering student in Tarragona

**[tonllop.dev](https://tonllop.dev)** · [LinkedIn](https://www.linkedin.com/in/antoni-llop/) · [tonichi003@gmail.com](mailto:tonichi003@gmail.com)

*Every system fails eventually. The craft is in what happens next.*

</div>

## Status

```console
$ systemctl status ton
● ton.service - Antoni Llop, infrastructure and local AI
     Loaded: loaded (/tarragona/urv; final year, graduating Feb 2027)
     Active: active (running), open to internships
     Speaks: catalan, spanish, english, a little german
     CGroup: /homelab/proxmox
             ├─ jaull        finding the local LLM your machine can actually run
             ├─ lipopotamo   NMR pipelines at Biosfer Teslab
             └─ containers   always one more

```

## Expeditions

| | |
|---|---|
| [**Jaull**](https://jaull.tech) | Reads your hardware, recommends which local LLM will fit, then runs and benchmarks it to check. [repo](https://github.com/Ton-Llop/Jaull) |
| **Server to Cluster** | A Debian server run as code, then the same discipline on Kubernetes with Terraform, NetworkPolicies and Prometheus/Grafana. [server](https://github.com/Ton-Llop/Debian-Config) · [cluster](https://github.com/Ton-Llop/GSX-Infrastructure) |
| **Ticket service** | RabbitMQ workers on AWS ECS Fargate that scale with the queue backlog, with retries, dead-letter queues and benchmarks. [repo](https://github.com/Ton-Llop/Scalable-and-Elastic-Ticket-Service-AWS-Managed-Systems-) |
| **Lipopotamo** | Scientific NMR platform at Biosfer Teslab: async workers, execution history and partial re-runs behind Keycloak. Private. |
| **Ninjadorks** | Search automation for authorized security research, with JSON/HTML reports and regex analysis. [repo](https://github.com/Ton-Llop/Google-Dorks) |
| **Beer Fantasy** | Fantasy leagues for nights out with friends. Flutter and Supabase, live on [Google Play](https://play.google.com/store/apps/details?id=com.ton.beerfantasy). |
| **Homelab** | An old desktop running Proxmox, Pi-hole and a power monitor, mostly so I can break things safely. [repo](https://github.com/Ton-Llop/Homelab) |
| **DD-tmux** | My AI coding agents as a Darkest Dungeon party, one torch-lit room per tmux session. [repo](https://github.com/Ton-Llop/DD-tmux) |

The rest, from a MIPS CPU in Verilog to the coursework, is on [tonllop.dev](https://tonllop.dev).

## Inventory

<table>
<tr><td><sub>Infra</sub></td><td><img src="https://cdn.simpleicons.org/docker" height="20" alt="Docker" title="Docker" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/kubernetes" height="20" alt="Kubernetes" title="Kubernetes" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/terraform" height="20" alt="Terraform" title="Terraform" />&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.16.0/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg" height="20" alt="AWS" title="AWS" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/linux/8b949e" height="20" alt="Linux" title="Linux" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/debian" height="20" alt="Debian" title="Debian" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/gnubash" height="20" alt="Bash" title="Bash" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/githubactions" height="20" alt="GitHub Actions" title="GitHub Actions" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/proxmox" height="20" alt="Proxmox" title="Proxmox" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/git" height="20" alt="Git" title="Git" /></td></tr>
<tr><td><sub>Watch &amp; guard</sub></td><td><img src="https://cdn.simpleicons.org/prometheus" height="20" alt="Prometheus" title="Prometheus" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/grafana" height="20" alt="Grafana" title="Grafana" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/keycloak/8b949e" height="20" alt="Keycloak" title="Keycloak" /></td></tr>
<tr><td><sub>Backend &amp; data</sub></td><td><img src="https://cdn.simpleicons.org/python" height="20" alt="Python" title="Python" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/fastapi" height="20" alt="FastAPI" title="FastAPI" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/flask/8b949e" height="20" alt="Flask" title="Flask" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/postgresql" height="20" alt="PostgreSQL" title="PostgreSQL" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/mongodb" height="20" alt="MongoDB" title="MongoDB" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/supabase" height="20" alt="Supabase" title="Supabase" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/redis" height="20" alt="Redis" title="Redis" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/rabbitmq" height="20" alt="RabbitMQ" title="RabbitMQ" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/n8n" height="20" alt="n8n" title="n8n" /></td></tr>
<tr><td><sub>Local AI</sub></td><td><img src="https://cdn.simpleicons.org/huggingface" height="20" alt="Hugging Face" title="Hugging Face" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/nvidia" height="20" alt="CUDA" title="CUDA" /></td></tr>
<tr><td><sub>Front &amp; mobile</sub></td><td><img src="https://cdn.simpleicons.org/react" height="20" alt="React" title="React" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/typescript" height="20" alt="TypeScript" title="TypeScript" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/nextdotjs/8b949e" height="20" alt="Next.js" title="Next.js" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/tailwindcss" height="20" alt="Tailwind CSS" title="Tailwind CSS" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/flutter" height="20" alt="Flutter" title="Flutter" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/dart" height="20" alt="Dart" title="Dart" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/android" height="20" alt="Android" title="Android" /></td></tr>
<tr><td><sub>Down low</sub></td><td><img src="https://cdn.simpleicons.org/c" height="20" alt="C" title="C" />&nbsp;&nbsp;<img src="https://cdn.simpleicons.org/openjdk/8b949e" height="20" alt="Java" title="Java" /></td></tr>
</table>

## Torchlight

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Ton-Llop/Ton-Llop/main/activity-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Ton-Llop/Ton-Llop/main/activity-light.svg" />
  <img alt="Contributions in the last year" src="https://raw.githubusercontent.com/Ton-Llop/Ton-Llop/main/activity-light.svg" width="100%" />
</picture>

Looking for an internship in infrastructure, DevOps or backend. If that's you, the torch is lit: [write to me](mailto:tonichi003@gmail.com).
