# Ansible Network Health Module

Custom Ansible module written in Python for performing basic network health checks.

This module can:
- Check ICMP ping reachability
- Verify TCP port connectivity
- Return structured JSON results to Ansible

---

# Features

- ICMP ping checks
- TCP port validation
- JSON-based structured output
- Custom Ansible module implementation
- Works with localhost or remote hosts

---

# Project Structure

```text
ansible-network-health-module/
│
├── playbook.yml
├── README.md
│
└── library/
    └── network_health.py
