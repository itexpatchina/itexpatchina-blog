import os
import re
import requests

USERNAME = "itexpatchina"
POSTS_DIR = "content/posts"

def main():
    # Ensure the output directory for posts exists
    os.makedirs(POSTS_DIR, exist_ok=True)

    # GitHub API endpoint for listing user public repositories
    api_url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner"
    headers = {"Accept": "application/vnd.github.v3+json"}

    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    print(f"Fetching public repositories for '{USERNAME}'...")
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        print(f"Error: Failed to fetch repositories (HTTP {response.status_code}): {response.text}")
        exit(1)

    repos = response.json()
    print(f"Found {len(repos)} repositories total.")

    synced_count = 0
    for repo in repos:
        # Skip forks, private repositories, or the central blog site repository itself
        if repo.get("fork") or repo.get("private") or repo.get("name") == "itexpatchina-blog":
            continue

        repo_name = repo["name"]
        description = repo.get("description") or "Technical guide and open-source project."
        html_url = repo["html_url"]
        updated_at = repo.get("updated_at", "2026-01-01")[:10]

        # Attempt to fetch README.md from main branch first, then master
        readme_content = None
        for branch in ["main", "master"]:
            raw_url = f"https://raw.githubusercontent.com/{USERNAME}/{repo_name}/{branch}/README.md"
            resp = requests.get(raw_url)
            if resp.status_code == 200:
                readme_content = resp.text
                break

        if not readme_content:
            print(f"⚠️  Skipping '{repo_name}': No README.md found.")
            continue

        # Strip redundant top H1 header if it matches the title
        clean_readme = re.sub(r'^#\s+.*$', '', readme_content, count=1, flags=re.MULTILINE)

        # Format Hugo Front Matter metadata block
        front_matter = f"""---
title: "{repo_name.replace('-', ' ').replace('_', ' ').title()}"
date: {updated_at}
description: "{description.replace('"', "'")}"
tags: ["GitHub", "Projects", "OpenSource"]
draft: false
---

> 🔗 **Source Repository:** [{html_url}]({html_url})

{clean_readme.strip()}
"""

        file_path = os.path.join(POSTS_DIR, f"{repo_name}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(front_matter)

        print(f"✅ Synced '{repo_name}' -> '{file_path}'")
        synced_count += 1

    print(f"\n✨ Successfully synced {synced_count} public repositories into Hugo blog posts!")

if __name__ == "__main__":
    main()
