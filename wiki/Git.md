# Editing Basics

You need an acount on [Github](github.com) to edit the wiki. By default, you can only submit *merge requests* which are provisional changes that require collaborator approval. To gain collaborator status, send a message to DIS requesting it.

## Editing Options

There are two options for editing online:

* Edit - Simply directs you to the github page for the file.

* Edit with Prose.io - A third-party editor for github documents. Somewhat nicer interface.

To edit offline, see the *Git Guide* section below.

## Syntax

This wiki uses [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). If you need to practice things, please do it in the [sandbox](/wiki/Sandbox.md).

If you need to do tables, consider [using this markdown table generator](http://www.tablesgenerator.com/markdown_tables). It has a gui, and can import markdown or csv.

# Git Guide

To edit the wiki offline, which allows scripting and automation, you need to use and understand Git.

In short, Git is a version control system, which means it keeps a record of all changes to its repository. This enables distributed collaboration and gives you the flexibility to use your own tools and workflow.

Git is powerful and complex, and I can't provide a quick rundown that will fit every use case, so here's some external resources:

* Use [this](https://try.github.io/levels/1/challenges/1) to quickly learn the basics.
* Use [this](https://git-scm.com/book/en/v2) if you want a more comprehensive approach.

## Generic Auto-update script

Please make sure you understand what each command in the below segment is doing before using it, to save you and everyone else some headache.

    git pull #Full update. If you need finer control see 'git fetch' and 'git checkout'
    
    <perform changes here>
    
    git add <files> #this adds new files to the repo. Otherwise they will be ignored
    
    git commit -a -m "Example commit message"
    
    git push
    
NB: When you run **git pull** and **git push** they will ask for your password. If you don't want to provide it every time, it is best to use [ssh](https://help.github.com/articles/connecting-to-github-with-ssh/).
