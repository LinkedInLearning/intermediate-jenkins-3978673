# 03_01 Distribute Builds With Agents

## Controller vs. Agents

- The **Jenkins controller** manages jobs and schedules execution.
- Best practice: **avoid running builds on the controller**.
- Use **nodes (agents)** to run jobs and free controller resources.

## SSH Nodes

- Jenkins connects to a remote server via **SSH**.
- Requirements:

  - SSH access enabled
  - A user + SSH key for Jenkins
  - **Java installed** (agents are Java-based)
- Works with **any operating system** that meets these requirements.

## Docker (Container) Agents

- Jobs run inside **ephemeral containers**.
- Each build gets a **clean, isolated environment**.
- Benefits:

  - Consistent builds
  - Fewer dependency conflicts
- Requirement: **Docker daemon running** on the host node.

## Agent Configuration in Pipelines

- `agent any` → run on the first available agent.
- Use **labels** to target specific agents with required capabilities.
- Useful when agents have different tools, OSes, or resources.

## Tool Configuration

- Tools (like Maven) can be configured globally in Jenkins.
- Defined under **Manage Jenkins → Tools**.
- Tools can:
  - Install automatically
  - Be referenced by **name** in pipelines
- Ensures consistent tool versions across builds.

## Code Checkout for Agents

- Jenkins checks out the repository **on the controller** to read the `Jenkinsfile`.
- When execution moves to an agent:
  - The source code is **not present by default**.
- Pipelines must explicitly include a **checkout step**

```groovy
pipeline {
  agent 'linux'

  stages {
    stage('Checkout Jenkins code from GitHub') {
      steps {

        git branch: 'master',
          url: 'https://github.com/jenkinsci/jenkins.git'

      }
    }
  }
}
```

<!-- FooterStart -->
---
[← 02_05 Solution: Connect Jenkins to Github](../../ch2_integrate_jenkins_with_version_control_systems/02_05_solution_connect_jenkins_to_github/README.md) | [03_02 Add an SSH agent to Jenkins →](../03_02_add_an_ssh_agent_to_jenkins/README.md)
<!-- FooterEnd -->
