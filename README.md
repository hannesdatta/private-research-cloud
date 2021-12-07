# Private Research Cloud on AWS

Using VMs in the cloud (e.g., via AWS EC2, or Surf Research Cloud) is an extremely useful way to accelarate one's progress when working on empirical research projects. Yet, setting up the cloud - even in relatively well-managed environments like Surf's Research Cloud - can incur a significant time investment for beginners (e.g., lengthy onboarding procedure, comprehensive but daunting documentation). Plus, it just doesn't offer some of the flexibility I'm used to when working with clouds like, e.g., EC2 (e.g., number of CPUs, hard disk space, etc.).

So, the purpose of this project is to, eventually, build a web interface to EC2/RDS at AWS.

## Features

Features:
-  I will be able to pre-configure machines for students and coauthors (e.g., with Ubuntu Desktop + RStudio for students, with RStudio Server for coauthors, including some data)
-  Students and coauthors will be able to start these machines, and login to them to conduct their work; after finishing their work, they can pause the machines again.
-  I will obtain user- and machine-level billing overviews

## Roadmap

See [here](https://github.com/hannesdatta/private-research-cloud/milestones) for an overview about the project's milestones and associated issues (to dos). Comments & feedback appreciated. 

## Running the App

- Install Flask

```
$ pip install Flask
$ pip install Flask-SQLAlchemy
$ pip install flask-login
$ pip install boto3
```

- Set environment variables 

```
$ export TSH_CLOUD_SECRETKEY=<app_secret_key_here>
$ export TSH_CLOUD_DATABASE_URI="mysql://<USERNAME>:<PASSWORD>@<URL>/tilburg_science_cloud"
$ export TSH_EMAIL_PASSWORD="SECRET-EMAIL-PASSWORD"

```

## Development

- Additionally, set these variables:
    
```
$ export FLASK_APP=cloud
$ export FLASK_DEBUG=1
```

- Run the app

```
$ flask run
```

## Deployment

- Followed the Docker tutorial here: https://aws.amazon.com/getting-started/hands-on/serve-a-flask-app/
- https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04
