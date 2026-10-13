# Migration lab: GitLab to GitHub

## Goal

Migrate this repository to GitHub while preserving Git history, branches, and tags. Then enable the GitHub Actions workflow and compare its behavior with GitLab CI.

## 1. Inspect the source repository

```bash
git log --oneline --graph --decorate --all
git branch -a
git tag --list
git show-ref
```

Record the output before migration.

## 2. Create an empty GitHub repository

Create a new, empty repository on GitHub. Do not initialize it with a README, license, or `.gitignore`; the lab already has content and history.

## 3. Mirror-push migration (recommended for preserving Git refs)

Run from this repository, replacing the URL with your destination:

```bash
git remote add github https://github.com/OWNER/REPO.git
git push github --all
git push github --tags
```

For a full mirror in a disposable destination, you can instead use:

```bash
git clone --mirror <GITLAB_REPOSITORY_URL> migration-lab.git
cd migration-lab.git
git remote set-url origin https://github.com/OWNER/REPO.git
git push --mirror
```

**Caution:** `git push --mirror` force-updates and deletes destination refs to match the source. Use it only with an empty or intentionally replaceable destination. A mirror clone is bare; use a normal clone for local editing.

## 4. Validate history and refs

Compare the source and destination:

```bash
git log --oneline --graph --decorate --all
git branch -a
git tag --list
git for-each-ref --format='%(refname) %(objectname)'
```

For stronger checks, compare commit IDs for each branch and tag. Git commits are content-addressed; unchanged Git objects retain their IDs when pushed.

## 5. Enable GitHub Actions

The workflow is at `.github/workflows/ci.yml`. Push the branch, open a pull request, and push a version tag to test each trigger:

```bash
git checkout main
git push github main
git checkout -b practice/ci-change
# Make a small change, commit it, push the branch, then open a PR in GitHub.
git push -u github practice/ci-change
git tag -a v1.3.0 -m "Practice release"
git push github v1.3.0
```

The repository contains a few existing sample tags; use a new version tag for the exercise.

## 6. Migration discussion prompts

- Which GitLab CI features have direct GitHub Actions equivalents?
- How would you migrate CI/CD variables and secrets securely?
- What happens to merge requests, approvals, issues, releases, packages, and artifacts? Which are Git data, and which need separate migration?
- Are protected branches, required checks, CODEOWNERS, and environments configured on GitHub?
- Do you need to migrate Git LFS objects, submodules, wiki repositories, or GitLab-specific integrations?
- Does the GitHub workflow run on pushes, pull requests, and tags as intended?

## Important scope note

Git preserves commit history, branches, and tags. A Git push alone does **not** migrate GitLab issues, merge requests, pipeline history, artifacts, project settings, variables, or permissions. Plan those separately.
