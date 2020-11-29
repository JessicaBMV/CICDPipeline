# Overview

This a a project that guides you through the creation of a continuous delivery system.
It starts by giving you an introduction to github actions and how to configure it. 
As a second step it helps you create a flask web application using azure webapp services. 
The last step is the implementation of azure devops resources, in which it shows you how to create an azure pipeline and how to connect it to the source code in github to deploy the flask application.

## Project Plan

* A link to a Trello board for the project
https://trello.com/invite/b/fj9KGkSi/9b382eafc2427e3cadc8f5aff5be04cb/flask-ml-app

* A link to a spreadsheet that includes the original and final project plan
https://docs.google.com/spreadsheets/d/1CjIaZvRG48ieOfN02LPeZaYDcxK9k12fbnniU8McjxE/edit?usp=sharing


## Instructions

* Architectural Diagram
<img src='/images/CICDPipeline.png'/>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell
<img src='/images/clone-repo.png'/>

* Passing tests that are displayed after running the `make all` command from the `Makefile`
<img src='/images/make-all.png'/>

* Output of a test run
<img src='/images/make-test.png'/>


* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>



## Demo 

<TODO: Add link Screencast on YouTube>

![Python application test with Github Actions](https://github.com/JessicaBMV/CICDPipeline/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

[![Build Status](https://dev.azure.com/jessmenesses110754/jessmenesses11/_apis/build/status/JessicaBMV.CICDPipeline?branchName=main)](https://dev.azure.com/jessmenesses110754/jessmenesses11/_build/latest?definitionId=1&branchName=main)
