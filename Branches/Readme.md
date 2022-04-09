# Branches

## Introduction

Branches are a powerful tool for collaboration when used correctly, but they can be very difficult to wrap your head around.
Essentially, a branch allows you to have multiple lines of development for a repository.
You have already been using the 'master' (or 'main') branch of your repository.
If, for example, you want to implement a new feature but will break the application for some time in the process, you can create a new branch for it.
The branch and the master branch will coexist, and other developers can still access the working master branch.
Once the feature is ready, both branches can be merged again.


## (Optional) Resources for more information

https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell

https://www.atlassian.com/git/tutorials/using-branches

## Setup

For this exercise, you can work alone.
Choose one of the code template files in this directory.

## Creating a new branch

To begin developing a new feature, create a new branch with a fitting name.
In companies, these are often the name of the ticket in the companies ticketing system.
For this example, we want to add a second operation2 function that takes two inputs a, b and subtract b from a.

> git checkout -b [Branch Name]



## Summary

The git history contains all commits, their authors and exact changes.
You can use it to find out what others changed in the project in order to be up-to-date with the status of the project.
The git history should never be altered!