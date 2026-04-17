Here's your **ULTRA-ATTRACTIVE README.md** — packed with badges, emojis, tables, and visual appeal. Copy-paste this directly into your GitHub repo:

---

```markdown
<div align="center">

# 🔐 SecureOps Platform

## Production-Grade DevSecOps on AWS EKS

[![AWS](https://img.shields.io/badge/AWS-EKS-FF9900?style=for-the-badge&logo=amazon-aws)](https://aws.amazon.com/eks/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-1.29-326CE5?style=for-the-badge&logo=kubernetes)](https://kubernetes.io/)
[![DevSecOps](https://img.shields.io/badge/DevSecOps-Complete-0A0A0A?style=for-the-badge&logo=devops)](https://github.com/Narenrohitha/secureops)
[![Open Source](https://img.shields.io/badge/Open%20Source-Love-red?style=for-the-badge&logo=github)](https://github.com/Narenrohitha/secureops)

**25 Phases · 6 Workflows · Zero to Hero**

[📖 Blog](https://medium.com/@narengl2001) · [💼 LinkedIn](https://linkedin.com/in/naren-g-7bb580229/) · [⭐ Star this Repo](https://github.com/Narenrohitha/secureops)

</div>

---

## 🎯 What You'll Build

> A **complete, production-ready DevSecOps platform** on AWS EKS with CI/CD, GitOps, Security, Monitoring, Chaos Engineering, FinOps, and Disaster Recovery.

| Category | Tools |
|----------|-------|
| **CI/CD** | Jenkins · ArgoCD · GitHub Actions |
| **Container** | Docker · ECR · Helm |
| **Orchestration** | Kubernetes · Amazon EKS |
| **Security** | Trivy · SonarQube · OWASP · OPA Gatekeeper · Wazuh SIEM |
| **Secrets & Access** | HashiCorp Vault · Teleport |
| **Monitoring** | Prometheus · Grafana · AlertManager |
| **Chaos** | Chaos Mesh |
| **Cost** | Kubecost |
| **Backup/DR** | Velero · S3 |
| **Infrastructure** | AWS (EC2, EKS, ECR, IAM, VPC, S3, Route53) |

---

## ⚙️ 6 Production Workflows

| # | Workflow | What It Does | Status |
|---|----------|--------------|--------|
| 🔄 | **WF1** | CI/CD Security Pipeline → Code → Jenkins → SonarQube → Trivy → Docker → ECR → EKS | ✅ Live |
| 🔁 | **WF2** | GitOps Drift Detection → Auto-reverts manual changes within 3 minutes | ✅ Live |
| 💥 | **WF3** | Chaos Engineering → Pod kills, network delays, resilience testing | ✅ Live |
| 🛡️ | **WF4** | Policy Enforcement → OPA Gatekeeper blocks bad deployments | ✅ Live |
| 💰 | **WF5** | FinOps/Cost Governance → Kubecost tracks $ per namespace | ✅ Live |
| 💾 | **WF6** | Disaster Recovery → Velero backups to S3 every hour, restore <15 min | ✅ Live |

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              DEVELOPER                                       │
│                                 │                                            │
│                                 ▼                                            │
│                           ┌──────────┐                                       │
│                           │ GitHub   │                                       │
│                           └────┬─────┘                                       │
│                                │                                             │
│                                ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                         CI/CD PIPELINE                               │    │
│  │  Jenkins → SonarQube → Trivy → Docker Build → ECR Push              │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                │                                             │
│                                ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      AMAZON EKS CLUSTER                              │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │    │
│  │  │  ArgoCD     │  │  Production │  │  Monitoring │                 │    │
│  │  │  (GitOps)   │  │  (2+ pods)  │  │ (Prometheus │                 │    │
│  │  └─────────────┘  └─────────────┘  │  + Grafana) │                 │    │
│  │  ┌─────────────┐  ┌─────────────┘  └─────────────┘                 │    │
│  │  │  OPA        │  │  Chaos Mesh                                     │    │
│  │  │  Gatekeeper │  │  (Chaos Engineering)                            │    │
│  │  └─────────────┘  └────────────────────────────────────────────────┘    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │   Jenkins    │  │  SonarQube   │  │    Wazuh     │  │   Teleport   │    │
│  │   (EC2)      │  │   (EC2)      │  │   (EC2)      │  │   (EC2)      │    │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │    Vault     │  │    S3        │  │    ECR       │  │  CloudWatch  │    │
│  │   (EC2)      │  │  (Backups)   │  │  (Registry)  │  │  (Logging)   │    │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start (5 Commands)

```bash
# 1. Clone the repository
git clone https://github.com/Narenrohitha/secureops.git
cd secureops

# 2. Create EKS cluster (15-20 minutes)
eksctl create cluster -f cluster-config.yaml

# 3. Connect kubectl to your cluster
aws eks update-kubeconfig --name secureops-cluster --region us-east-1

# 4. Deploy the application
kubectl apply -f k8s/deployment.yaml

# 5. Access your app
kubectl get svc -n ingress-nginx
```

> ⚡ **That's it!** Your DevSecOps platform is now live on AWS EKS.

---

## 📁 Project Structure

```
secureops/
│
├── 📂 app/                      # Flask application
│   ├── app.py                   # Main application code
│   ├── Dockerfile               # Multi-stage build
│   ├── requirements.txt         # Python dependencies
│   └── templates/               # HTML templates
│
├── 📂 k8s/                      # Kubernetes manifests
│   ├── deployment.yaml          # Deployment + Service + Ingress + HPA
│   ├── argocd-app.yaml          # ArgoCD application
│   └── opa/                     # OPA Gatekeeper policies
│
├── 📂 terraform/                # Infrastructure as Code
│   ├── eks/                     # EKS cluster config
│   ├── iam/                     # IAM roles & policies
│   └── networking/              # VPC, subnets, security groups
│
├── 📂 monitoring/               # Observability stack
│   ├── prometheus-values.yaml
│   ├── grafana-dashboards/
│   └── alertmanager-config.yaml
│
├── 📂 security/                 # Security configurations
│   ├── trivy/                   # Vulnerability scanning
│   ├── opa-policies/            # Rego policies
│   └── vault/                   # Vault injector configs
│
├── 📂 chaos/                    # Chaos Mesh experiments
│   ├── pod-kill.yaml
│   ├── network-delay.yaml
│   └── cpu-stress.yaml
│
├── 📂 backup/                   # Velero backup schedules
│   └── schedules.yaml
│
├── 📄 Jenkinsfile               # 11-stage CI/CD pipeline
├── 📄 cluster-config.yaml       # EKS cluster definition
└── 📄 README.md                 # You are here!
```

---

## 📋 25-Phase Complete Guide

| Part | Phases | Topics |
|------|--------|--------|
| **A** | 1-5 | Foundation → SSH, IAM, EKS Cluster, Node Groups, kubectl |
| **B** | 6-7 | Core CI Tools → Jenkins, SonarQube |
| **C** | 8-10 | Application → Python App, Docker, ECR, EKS Deploy |
| **D** | 11-12 | GitOps + Monitoring → ArgoCD, Prometheus, Grafana |
| **E** | 13-15 | Security Tools → Wazuh, Teleport, Vault |
| **F** | 16-20 | Advanced Workflows → Jenkins Pipeline, OPA, Chaos Mesh, Kubecost, Velero |
| **G** | 21-25 | Final Steps → Drift Detection, Testing, Dashboards, Troubleshooting, Cost Guide |

📖 **Full detailed guide:** [Medium Blog](https://medium.com/@narengl2001)

---

## 🛠️ Tech Stack Deep Dive

### 🔄 CI/CD & GitOps
| Tool | Purpose |
|------|---------|
| **Jenkins** | 11-stage CI/CD pipeline with security scanning |
| **ArgoCD** | GitOps continuous deployment with drift detection |
| **GitHub** | Source code & manifest repository |

### 🐳 Container & Orchestration
| Tool | Purpose |
|------|---------|
| **Docker** | Multi-stage container builds |
| **ECR** | Private AWS container registry |
| **EKS** | Managed Kubernetes cluster |
| **Helm** | Kubernetes package manager |

### 🔒 Security (Shift-Left)
| Tool | Purpose |
|------|---------|
| **SonarQube** | Code quality & security analysis |
| **Trivy** | Vulnerability scanning (filesystem + images) |
| **OWASP** | Dependency vulnerability check |
| **OPA Gatekeeper** | Policy enforcement (no :latest, no privileged) |
| **Wazuh** | SIEM security monitoring |
| **Teleport** | Zero-trust access gateway |
| **Vault** | Secrets management & injection |

### 📊 Observability
| Tool | Purpose |
|------|---------|
| **Prometheus** | Metrics collection |
| **Grafana** | Visualization & dashboards |
| **AlertManager** | Alert routing & notifications |

### 💥 Chaos Engineering
| Tool | Purpose |
|------|---------|
| **Chaos Mesh** | Pod kills, network delays, CPU stress |

### 💰 FinOps
| Tool | Purpose |
|------|---------|
| **Kubecost** | Real-time cost tracking per namespace |

### 💾 Disaster Recovery
| Tool | Purpose |
|------|---------|
| **Velero** | Cluster backups to S3, point-in-time restore |

---

## 🎯 For Recruiters & Hiring Managers

### ✅ I have built:

- **Complete CI/CD pipeline** → Jenkins → SonarQube → Trivy → Docker → ECR → EKS
- **GitOps with ArgoCD** → Self-healing cluster, drift detection (<3 min auto-revert)
- **Chaos engineering** → Pod kills, network delays, resilience validation
- **Security enforcement** → OPA Gatekeeper blocks :latest tags & privileged containers
- **Cost governance** → Real-time namespace-level cost tracking with Kubecost
- **Disaster recovery** → Hourly S3 backups, <15 min restore time

### ✅ I can:

| Skill | Proficiency |
|-------|-------------|
| Deploy & manage production EKS clusters | ⭐⭐⭐⭐⭐ |
| Build secure CI/CD pipelines | ⭐⭐⭐⭐⭐ |
| Implement GitOps workflows | ⭐⭐⭐⭐⭐ |
| Integrate security scanning at every stage | ⭐⭐⭐⭐⭐ |
| Monitor & alert on infrastructure health | ⭐⭐⭐⭐⭐ |
| Infrastructure as Code (Terraform) | ⭐⭐⭐⭐ |
| Container orchestration (Kubernetes) | ⭐⭐⭐⭐⭐ |

### 📍 Open for:

- DevOps Engineer
- Site Reliability Engineer (SRE)
- Cloud Engineer
- Platform Engineer

📍 **Location:** Remote / India / Anywhere  
⏱️ **Availability:** Immediate joiner

---

## 📞 Connect With Me

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/naren-g-7bb580229/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/Narenrohitha)
[![Medium](https://img.shields.io/badge/Medium-Blog-000000?style=for-the-badge&logo=medium)](https://medium.com/@narengl2001)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail)](mailto:naren.cloud@outlook.com)

</div>

---

## 📊 Dashboard Access Guide

### Fixed IPs (EC2 Servers)

| Tool | URL | Default Login |
|------|-----|---------------|
| Jenkins | `http://<JENKINS_IP>:8080` | admin / your password |
| SonarQube | `http://<SONARQUBE_IP>:9000` | admin / your password |
| Wazuh | `https://<WAZUH_IP>:443` | admin / (generated) |
| Teleport | `http://<TELEPORT_IP>:3080` | admin / your password |
| Vault | `http://<VAULT_IP>:8200` | root token |

### Dynamic ELB URLs (Run these commands)

```bash
# Get all dashboard URLs
kubectl get svc ingress-nginx-controller -n ingress-nginx -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
kubectl get svc argocd-server -n argocd -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
kubectl get svc kube-prometheus-stack-grafana -n monitoring -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
kubectl get svc kubecost-cost-analyzer -n kubecost -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
kubectl get svc chaos-dashboard -n chaos-mesh -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
```

### Grafana Dashboard IDs

| ID | Dashboard Name |
|----|----------------|
| 1860 | Node Exporter Full |
| 6417 | Kubernetes Cluster Overview |
| 315 | Kubernetes Pods Monitoring |
| 8670 | Kubecost Cost Overview |
| 15469 | Velero Backup Monitoring |
| 15763 | OPA Gatekeeper |
| 11074 | Application Metrics |
| 13659 | Wazuh Security Events |

---

## 🔧 Troubleshooting Quick Reference

| Problem | Fix |
|---------|-----|
| kubectl can't connect | `aws eks update-kubeconfig --name secureops-cluster` |
| Pods stuck in Pending | Check node resources: `kubectl describe pod <name>` |
| ImagePullBackOff | Recreate ECR secret (Phase 5, Step 4) |
| Vault sealed | `vault operator unseal <KEY1> <KEY2> <KEY3>` |
| ECR login expired | Re-run `aws ecr get-login-password \| docker login` |
| ArgoCD OutOfSync | Check selfHeal: `kubectl get application -n argocd -o yaml` |

---

## 💰 Cost Optimization Guide

| Action | Monthly Savings |
|--------|-----------------|
| Scale nodes to 0 at night | ~$30 |
| Stop EC2 servers when not used | Free tier (750 hrs/month) |
| Delete cluster when on break | ~$72 |
| **Total potential savings** | **~$102/month** |

```bash
# Scale nodes to 0 (saves $30/month)
aws eks update-nodegroup-config --cluster-name secureops-cluster \
  --nodegroup-name secureops-nodes --scaling-config minSize=0,desiredSize=0

# Scale back up
aws eks update-nodegroup-config --cluster-name secureops-cluster \
  --nodegroup-name secureops-nodes --scaling-config minSize=2,desiredSize=2
```

---

## 📄 License

MIT License — Free to use, learn, and contribute.

---

<div align="center">

**⭐ If this project helped you, please star the repo! ⭐**

**Built with ☁️ on AWS EKS | 25 Phases | 6 Workflows | Production Ready**

[⬆ Back to Top](#-secureops-platform)

</div>
