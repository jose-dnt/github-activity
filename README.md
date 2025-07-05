# GitHub User Activity CLI

A simple Python-based command-line tool to fetch and display recent public events for any GitHub user.  
This project demonstrates using the GitHub Events API.
This project is an implementation of the Task Tracker project from [roadmap.sh](https://roadmap.sh/projects/github-user-activity).

---

## Features

- **Fetch recent activity** from any GitHub username  
- **Display user actions** like pushes, issues, pull requests, comments, forks, releases, and more
  
---

## Requirements

- Python 3.10 or higher (for `match-case` syntax) 
- Internet connection (calls GitHub’s API)

---

## Usage

Run the script via Python:

```bash
python github-activity.py <github-username>
```

Example:

```bash
python github-activity.py torvalds
```

---

## Example Output

```text
Pushed 2 commits to torvalds/linux
Opened an issue in someuser/somerepo
Commented on an issue in anotheruser/anotherrepo
Created a branch named feature-x in myorg/myrepo
Deleted a tag named v1.0 in myuser/myrepo
Forked octocat/Hello-World to myuser/Hello-World
Starred the repository octocat/Hello-World
Opened a pull request in myrepo/project
Submitted a review on a pull request in user/repo
Commented on a pull request diff in org/repo
Marked a pull request review thread as unresolved in user/repo
Added alice as a collaborator to org/repo
Published a release v2.0 in user/repo
Commented on a commit in user/repo
Created 1 wiki pages in user/repo
Made user/repo public
```

---

## License

MIT License. Free to use and modify!
