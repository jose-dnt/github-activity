# GitHub User Activity CLI
# Fetches and displays recent public events for a given GitHub user

import json
import sys
import requests


def main():

    if len(sys.argv <= 1):
        return

    username = sys.argv[1]

    response = requests.get(f"https://api.github.com/users/{username}/events")
    if response.status_code != 200:
        return
    
    events = json.loads(response.content.decode("utf-8"))

    for event in events:
        repo_name = event["repo"]["name"]

        # Handle different types of GitHub events
        match event["type"]:
            case "PushEvent":
                commits = len(event["payload"]["commits"])
                print(f"Pushed {commits} commits to {repo_name}")
            case "IssuesEvent":
                action = event["payload"]["action"]
                print(f"{action.capitalize()} an issue in {repo_name}")
            case "IssueCommentEvent":
                action = event["payload"]["action"]
                print(
                    f"{'Commented' if action == 'created' else f'{action.capitalize()} a comment'} on an issue in {repo_name}"
                )
            case "CreateEvent":
                ref_type = event["payload"]["ref_type"]
                ref_name = event["payload"]["ref"]
                print(
                    f"Created a {ref_type} named {f'{ref_name} in {repo_name}' if ref_name else repo_name}"
                )
            case "DeleteEvent":
                ref_type = event["payload"]["ref_type"]
                ref_name = event["payload"]["ref"]
                print(
                    f"Deleted a {ref_type} named {f'{ref_name} in {repo_name}' if ref_name else repo_name}"
                )
            case "ForkEvent":
                fork_name = event["payload"]["forkee"]["full_name"]
                print(f"Forked {repo_name} to {fork_name}")
            case "WatchEvent":
                print(f"Starred the repository {repo_name}")
            case "PullRequestEvent":
                action = event["payload"]["action"]
                match action:
                    case "review_requested":
                        action = "Requested a review on"
                    case "review_request_removed":
                        action = "Removed a review request from"
                    case "synchronize":
                        action = "Synchronized"
                    case _:
                        action = action.capitalize()
                print(f"{action} a pull request in {repo_name}")
            case "PullRequestReviewEvent":
                print(f"Submitted a review on a pull request in {repo_name}")
            case "PullRequestReviewCommentEvent":
                action = event["payload"]["action"]
                print(
                    f"{'Commented' if action == 'created' else f'{action.capitalize()} a comment'} on a pull request diff in {repo_name}"
                )
            case "PullRequestReviewThreadEvent":
                action = event["payload"]["action"]
                print(
                    f"{'Marked a pull request review thread as unresolved' if action == 'unresolved' else f'{action.capitalize()} a pull request review thread'} in {repo_name}"
                )
            case "MemberEvent":
                action = event["payload"]["action"]
                member_name = event["payload"]["member"]["name"]
                match action:
                    case "added":
                        print(f"Added {member_name} as a collaborator to {repo_name}")
                    case "edited":
                        print(f"Edited permissions for {member_name} in {repo_name}")
                    case "deleted":
                        print(
                            f"Removed {member_name} as a collaborator from {repo_name}"
                        )
            case "ReleaseEvent":
                action = event["payload"]["action"]
                release_name = event["payload"]["release"]["name"]
                print(f"{action.capitalize()} a release {release_name} in {repo_name}")
            case "CommitCommentEvent":
                action = event["payload"]["action"]
                print(
                    f"{'Commented' if action == 'created' else f'{action.capitalize()} a comment'} on a commit in {repo_name}"
                )
            case "GollumEvent":
                action = event["payload"]["action"]
                pages = len(event["payload"]["pages"])
                print(f"{action.capitalize()} {pages} wiki pages in {repo_name}")
            case "PublicEvent":
                print(f"Made {repo_name} public")


if __name__ == "__main__":
    main()