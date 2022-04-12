# Git History

## Introduction

One of the big advantages of version control is that you can revert changes if needed.
For this, the git history contains all commits, their creator, ....
This exercise will focus on how you can use git history to solve problems.
(Feel free to mock my commit messages for this repository during the exercise :D)

## (Optional) Resources for more information

## Setup

For this exercise, you can work alone.

## Viewing the commit history

### In the shell

You can view all commits via 

```
git log
```

The output shows all commits. Considering a single entry

```
commit 8f0aef67ed3b08ed62026c8f754191905e1570b3
 
Author: Moritz Flüchter <moritz.fluechter@student.uni-tuebingen.de>
 
Date:   Fri Apr 8 17:49:26 2022 +0200
```

It contains the unique commit ID (a hash), author and date/time of the commit.  Since the
output is very long, you may need to quit using 'q' if you want to enter another command.

You can limit the output to the last x entries via

```
git log -x
```

If you want to see the differences per commit use:

```
git log -p
```

For a shorter output, you can also use the summary of differences with

```
git log --stat
```

(Optional) For more possibilities, you can consider:
https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History

When you choose a commit ID, you can show it via

```
git show [commit ID]
```

Which shows you the commits information and every change.
You can also only use the first 7 characters of the ID.

### In Github

Got to '[Repo URL]/commits' e.g. 'https://github.com/NoRyyZ/GitWorkshopExercises/commits'.

GitHub adds additional features, that give you more powerful ways of interacting with the
history (e.g. looking at the repository before any chosen commit).  While most of it is
also possible in the shell, I'd recommend to sticking to the web-interface when working
with the history.

You can explore the web-interface by clicking around for a bit.

## Altering the Git history

While it is possible to rewrite the git history, **you should almost never do it.**
Even if you know what you're doing, consult your team members/coworkers/... beforehand.

The git history is meant to give a clear overview of what exactly happened in the repository.
Who worked on which part of the code, what changes were made, ... .
This is especially important when the program stops working at some point, and you need to
find the last functioning version.

**!! I CANNOT STRESS IT ENOUGH THAT 99% OF THE TIME PEOPLE WILL MANHUNT YOU IF YOU
ACTIVELY CHANGE THE COMMIT HISTORY !!** (with very good reason)

## Reverting to a previous version

If you want to view a version at the point of a previous commit, you can do so via git
checkout.

```
git checkout [commit ID]
```

To test this, revert this repository to its state after commit
`b1800286ec1e9da2d51ac080ef67fd5b916f5e53` and find the file in the same directory as this
Readme file.

This should also show you why it is never a smart idea to put credentials in a git repository.

To return to the current version use:

```
git checkout main
```

## Git blame

If you want to know who is responsible for a line in the code, you can use

```
git blame [file]
```

(You can exit the file view with `q`).
It shows who was the last one to edit which line in the file.
Furthermore, it provides the commit ID and time.
You can also limit the lines via the `-L` option

```
git blame [file] -L 40,60
```

Try to find out who insulted you in the text file `documentation.txt`.
You can also use the found commit ID to check out the exact changes.

## (Optional) Git bisect

Git bisect can be used to find a commit that introduced a bug.
The documentation can be found here: https://git-scm.com/docs/git-bisect

## Summary

The git history contains all commits, their authors and exact changes.
You can use it to find out what others changed in the project in order to be up-to-date
with the status of the project.  The git history should never be altered!
