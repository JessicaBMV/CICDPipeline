![Python application test with Github Actions](https://github.com/JessicaBMV/CICDPipeline/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

[![Build Status](https://dev.azure.com/jessmenesses110754/jessmenesses11/_apis/build/status/JessicaBMV.CICDPipeline?branchName=main)](https://dev.azure.com/jessmenesses110754/jessmenesses11/_build/latest?definitionId=1&branchName=main)

# Overview

This a a project that guides you through the creation of a continuous delivery system.
It starts by giving you an introduction to github actions and how to configure it. 
As a second step it helps you create a flask web application using azure webapp services. 
The last step is the implementation of azure devops resources, in which it shows you how to create an azure pipeline and how to connect it to the source code in github to deploy the flask application.

## Architectural Diagram
<img src='/images/CICDPipeline.png'/>

## Project Plan

* A link to a Trello board for the project
https://trello.com/invite/b/fj9KGkSi/9b382eafc2427e3cadc8f5aff5be04cb/flask-ml-app

* A link to a spreadsheet that includes the original and final project plan
https://docs.google.com/spreadsheets/d/1CjIaZvRG48ieOfN02LPeZaYDcxK9k12fbnniU8McjxE/edit?usp=sharing


## Instructions

To be able to use this repository and deploy it you have to follow the next steps:

1. Configure your azure shell by clicking on the shell icon on your azure portal.
2. Once you have configured you azure shell, you have to clone your repository to your shell.
3. Change to the directory of your project.
4. To Create your webapp you have to type the next command:

```
az webapp up --name <NAME OF APP> --sku FREE  -l <LOCATION>

```
This will automatically create a resource group and your webapp.

5. This webapp need a start up command to be able to work, so you'll need to do the next command: 

```
az webapp config set -g <your-resource-group> -n <your-appservice> --startup-file 'gunicorn -w 4 -b 0.0.0.0:8000 "ml_app:create_app()"'

```
This will make your app be ready to be used. 

6. You will have to change the make_predict_Azure_app.sh the line 28 where the request is made to my webapp to the webapp you just created. 

If you want to set up the azure pipelines follow the azure tutorial : [Use CI/CD to deploy a Python web app to Azure App Service on Linux](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops)

The azure-pipelines.yaml is all set up in this repository and the only thing you will need to change is the azure subscription/ connection string on the task AzureWebApp@1.


## Outputs
* Project running on Azure App Service
<img src='/images/webapp-running.png'/>


* Project cloned into Azure Cloud Shell
<img src='/images/clone-repo.png'/>

* Passing tests that are displayed after running the `make all` command from the `Makefile`
<img src='/images/make-all.png'/>

* Output of a test run
<img src='/images/make-test.png'/>

* App deployed
<img src='/images/home.png'/>

* App Deployed prediction postman
<img src='/images/postman-prediction.png'/>

* Prediction on Cloud Shell 
<img src='/images/prediction.png'/>


## Enhancements

- Application Scalatibility.
- Improve dataset to get better results.
- Train the machine learning model with the new data set and improve accuracy.
- Create the web application frontend to be user friendly.
- Create a mobile app of the web application.



## Demo 

https://youtu.be/kkaKirvZXZ0 

## Resources
- [Use CI/CD to deploy a Python web app to Azure App Service on Linux](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops)
- [Build GitHub repositories](https://docs.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops&tabs=yaml)

