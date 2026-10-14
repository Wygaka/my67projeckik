# Git-команды для лабораторной работы

Ниже приведен набор команд, соответствующий практической части N2.

```bash
git init -b main
git config user.name "Student Developer"
git config user.email "student@college.local"
git status -s

git switch -c feature/payment
git add src/payment.py
git commit -m "feat(payment): implement payment contract"
git switch main
git merge --no-ff feature/payment -m "merge: integrate feature/payment"
git tag -a v1.0.0 -m "release: version 1.0.0"

git stash push -m "WIP: temporary experimental logic"
git stash list
git stash pop

git switch -c hotfix/patch
git add patch.cfg
git commit -m "fix(core): apply critical patch"
git switch main
git cherry-pick <commit-hash>

git log --oneline --graph --all
git reflog
git bisect start
git bisect bad
git bisect good v1.0.0
git bisect reset
```

В проекте также есть скрипт `scripts/install_pre_commit_hook.ps1`, который устанавливает pre-commit hook для запуска тестов перед коммитом.

