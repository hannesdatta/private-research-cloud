# Private Research Cloud

Using VMs in the cloud (e.g., via AWS EC2, or Surf Research Cloud) is an extremely useful way to accelarate one's progress when working on empirical research projects. Yet, setting up the cloud - even in relatively well-managed environments like Surf's Research Cloud - can incur a significant time investment for beginners. Plus, it just doesn't offer some of the flexibility I'm used to when working with clouds like, e.g., EC2.

So, the purpose of this project is to, eventually, build a web interface to EC2/RDS at AWS.

Features:
- create database of own users (e.g., coauthors, students) that can launch, pause and stop VMs that have been preconfigured on my AWS account
- edit that lists of users to grant access to certain machines, databases
- provide billing details per user
- E-mail based login procedure (i.e., email-based authentication link)

Required skills for me to learn:
- how to create email based login procedure
- deploying (Flask) apps (e.g., on Docker)

Ultimately, this web-based client could evolve into my own research cloud.
