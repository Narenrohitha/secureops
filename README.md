# 🔐 SecureOps Platform

**Production-Grade DevSecOps on AWS EKS**

[![AWS](https://img.shields.io/badge/AWS-EKS-FF9900?style=flat&logo=amazon-aws)](https://aws.amazon.com/eks/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-1.29-326CE5?style=flat&logo=kubernetes)](https://kubernetes.io/)
[![DevSecOps](https://img.shields.io/badge/DevSecOps-Complete-0A0A0A?style=flat)](https://github.com/Narenrohitha/secureops)

**25 Phases · 6 Workflows · Zero to Hero**

[📖 Blog](https://medium.com/@narengl2001) · [💼 LinkedIn](https://linkedin.com/in/naren-g-7bb580229/) · [⭐ Star this Repo](https://github.com/Narenrohitha/secureops)

---

## 🎯 What You'll Build

A complete, production-ready DevSecOps platform on AWS EKS.

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

---

## ⚙️ 6 Production Workflows

| Workflow | What It Does |
|----------|--------------|
| 🔄 **WF1** | CI/CD Security Pipeline → Code → Jenkins → SonarQube → Trivy → Docker → ECR → EKS |
| 🔁 **WF2** | GitOps Drift Detection → Auto-reverts manual changes within 3 minutes |
| 💥 **WF3** | Chaos Engineering → Pod kills, network delays, resilience testing |
| 🛡️ **WF4** | Policy Enforcement → OPA Gatekeeper blocks bad deployments |
| 💰 **WF5** | FinOps/Cost Governance → Kubecost tracks $ per namespace |
| 💾 **WF6** | Disaster Recovery → Velero backups to S3 every hour, restore <15 min |

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




secureops/
├── app/                    # Flask application
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── k8s/                    # Kubernetes manifests
│   ├── deployment.yaml
│   └── argocd-app.yaml
├── monitoring/             # Prometheus + Grafana
├── chaos/                  # Chaos Mesh experiments
├── backup/                 # Velero schedules
├── Jenkinsfile             # 11-stage CI/CD pipeline
└── README.md


📖 Full guide: Medium Blog

🎯 For Recruiters
I have built:
✅ Complete CI/CD pipeline (Jenkins → SonarQube → Trivy → Docker → ECR → EKS)

✅ GitOps with ArgoCD (Self-healing, drift detection <3 min)

✅ Chaos engineering (Pod kills, network delays)

✅ Security enforcement (OPA blocks :latest & privileged containers)

✅ Cost governance (Real-time $ per namespace)

✅ Disaster recovery (Hourly S3 backups, <15 min restore)

I can:
Skill	Level
EKS & Kubernetes	⭐⭐⭐⭐⭐
CI/CD Pipelines	⭐⭐⭐⭐⭐
GitOps (ArgoCD)	⭐⭐⭐⭐⭐
Security Scanning	⭐⭐⭐⭐⭐
Monitoring (Prometheus/Grafana)	⭐⭐⭐⭐⭐
📍 Open for: DevOps Engineer · SRE · Cloud Engineer
📍 Location: Remote / India / Anywhere
⏱️ Availability: Immediate joiner

📞 Connect With Me
https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin
https://img.shields.io/badge/GitHub-Follow-181717?logo=github
https://img.shields.io/badge/Medium-Blog-000000?logo=medium

📊 Grafana Dashboard IDs
ID	Dashboard
1860	Node Exporter Full
6417	Kubernetes Cluster Overview
315	Kubernetes Pods Monitoring
8670	Kubecost Cost Overview
15469	Velero Backup
15763	OPA Gatekeeper
🔧 Quick Troubleshooting
Problem	Fix
kubectl can't connect	aws eks update-kubeconfig --name secureops-cluster
ImagePullBackOff	Recreate ECR secret
Vault sealed	vault operator unseal <KEY>
ECR login expired	Re-run aws ecr get-login-password | docker login
💰 Cost Optimization
bash
# Scale nodes to 0 (saves ~$30/month)
aws eks update-nodegroup-config --cluster-name secureops-cluster \
  --nodegroup-name secureops-nodes --scaling-config minSize=0,desiredSize=0

# Scale back up
aws eks update-nodegroup-config --cluster-name secureops-cluster \
  --nodegroup-name secureops-nodes --scaling-config minSize=2,desiredSize=2
📄 License
MIT License — Free to use, learn, and contribute.

⭐ Star this repo if you find it useful!

Built on AWS EKS | 25 Phases | 6 Workflows | Production Ready


