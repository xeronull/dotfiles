#!/bin/bash

sync_fork() {
  printf "\nList the current configured remote repository for your fork.\n"
  git remote -v
  
  if [[ $1 == *".git" ]]; then
    git remote add upstream $1
  else
    git remote add upstream $1".git"
  fi
  
  printf "\nVerify the new upstream repository you've specified for your fork.\n"
  git remote -v
  
  printf "\nFetch the branches and their respective commits from the upstream repository.\n"
  git fetch upstream
  
  printf "\nCheck out your fork's local master branch.\n"
  git checkout master
  
  printf "\nMerge the changes from upstream/master into your local master branch.\n"
  read -p "Wanna merge it? (Y/n) " -n 1 -r
  echo #
  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    git merge upstream/master
  else
    printf "\nJust do `git merge upstream/master` to merge.\n"
  fi
}

if [ $# -eq 0 ]; then
  read -p "Enter original GitHub repo URL: " upstream_repo
else
  upstream_repo = "$1"
fi

sync_fork upstream_repo
