# Branches

## Introduction

Branches are a powerful tool for collaboration when used correctly, but they can be very
difficult to wrap your head around.  Essentially, a branch allows you to have multiple
lines of development for a repository.
You have already been using the 'master' (or 'main') branch of your repository.
If, for example, you want to implement a new feature but will break the application for
some time in the process, you can create a new branch for it.  The branch and the master
branch will coexist, and other developers can still access the working master branch.
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
For this example, we want to add a second operation2 function that takes two inputs a, b
and subtract b from a.

```
git checkout -b [Branch Name]
```

You can check if it worked with git status.
Next, you need to also announce the new branch to the git repository.
Since the local name of the branch can differ to its name on GitHub, the command is as
follows:

```
git push origin [local branch Name]:[remote branch Name]
```

Obviously, the branch names should often be the same to avoid confusion.
'origin' references the original remote location of the repository.

Now all changes that you commit won't be tracked in the master branch, but rather in this
new branch.  Implement the new operation, call it from the main Function and print out the
value (similar to how operation is used).
Then add and commit and push the changes as you would do normally.

## Visualizing Branches

### In the command line

To show all branches for this repository, you can list them via:

```
git branch (local branches only)
 
git branch -r (remote branches only)
 
git branch -a (all branches)
```

You should see the HEAD, main and your new branch.
The HEAD branch refers to the default branch and points to the main/master branch by
default.

Viewing the branches visually is a bit hard on the terminal.  You can use:

```
git log --graph --decorate --oneline
```
 
or just:
 
```
git log --graph
```

But it will not really show you the newly created branch.
(But there is one you can see in the history if you scroll down. If you find it, you can
see that git sometimes automatically creates and merges branches when merge conflicts
occur.)

### On GitHub

Github can show you all branches if you go to:

`[REPO URL]/branches` e.g. https://github.com/NoRyyZ/GitWorkshopExercises/branches

Try this for your forked repository!
If you want a visual representation, you can use

`[REPO URL]/network` e.g. https://github.com/NoRyyZ/GitWorkshopExercises/network

### Using GUIs

Most git GUIs (e.g. GitKraken, GitHub client) provide multiple tools to work with
branches.  I would recommend using them, especially for visualization!
However, their use will not be covered here.

## Merging Branches

To merge your new branch into the main one, first swap to the branch you want to merge
into.  You can swap between existing branches via

```
git checkout [branch Name]
```

After swapping to the main branch, take a look at the file you changed.  The changes are
stored by git, but you cannot see them since you are now in the main branch again.

In order to merge the changes from your new branch, use:

```
git merge [branch name]
```

You should now see the changes applied when looking at the file.
After a successful merge, you can delete the old branch via

```
git branch -d [branch Name]
```

To delete the remote branch use

```
git push origin --delete [branch Name]
```

Or keep it around if you still need it. Remember that you still need to push your changes
(but no commit!).

## Remembering Merge Conflicts

In the previous exercise **Merge Conflicts**, you took a look at how to solve merge
conflicts.  When pulling the unaccounted changes in that exercise, git actually performs
two commands:

```
git fetch

git merge
```

The first one gets the changes, the second one merges the remote main branch with the
unaccounted changes and the local main branch.  This is why you should sometimes use
`--ff-only` as option since it omits the automatic merge.
You can see, that git sometimes automatically creates new branches, merges and deletes
them.  (This all is mostly true, if you want an in-depth analysis of what git pull truly
does, go to: https://stackoverflow.com/a/45148040)

When using `--rebase`, pull calls git rebase instead of merge.

## (Optional) When and how to use branches

This is a tough one.

There is no one true solution that tells you when to use branches.
The common understanding is that using too many branches creates confusion and a really
hard to manage repository.  So you should use them scarcely but often enough (I know that
is a dumb statement, but stay with me).

The philosophy of how to organize branches depends on the project and people you are
working with.  If you work in a company, chances are high that the team decide on a common
guideline.  For work with other students, you should specify one in order to stay
consistent.

My personal proposal depends on your approach.

If you already have a working software (e.g. version 1.0) and your task is to maintain
that software, add new features, fix bugs, ... , then I would ensure that the main branch
is never worked on directly.  It should **always** contain the most recent, **correctly
functioning** version.
For new version, you create a new branch where new features are added.  Once the new
version is done and tested, you can merge it back.
For bugfixes, single features, you should use branches as well by either branching from
the new version branch or the main branch directly.  You should limit who can merge
branches back into the main branch to add a layer of control/review before changes are
merged.
For this, you can use so called 'pull requests', which will be discussed in the next exercise.

If you are building new software that does not work yet, the main branch cannot contain a
'working' version.  But again, letting everyone work directly on the main branch can lead
to problems.
E.g. the one we created in the Exercises 'Merge Conflicts' will be a common occurrence.
Giving everyone their own branch allows you to keep everything clean, but you also need to
sync branches if new changes are applied to the main branch.

As you can see, there is no 'best' solution.
Try to split the project into different independent sections and create a branch for each
of them.  This minimizes the amount of possible conflicts and makes merging a lot simpler.
When a new part of the branch is ready, merge it back into the main and from the main into
the other branches.  How to do this is shown in the next exercise.

## Summary

Branching allows you to separate changes in the repository and produce concurrent states
of development.  The main branch is the default branch of your repository.
You can freely switch between branches and git will automatically updated your local files
to show the state of the branch.  It also stashes local commits to the old branch such
that nothing is lost.
Using branches in a team requires some work and thought but can prevent a lot of headaches.
