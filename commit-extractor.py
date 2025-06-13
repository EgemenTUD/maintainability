import os
import subprocess
import shutil
import time

def extract_commits_by_author(repo_path, author_email, group_name, student_name):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_path = os.path.join(desktop_path, f"{group_name}_{student_name}")

    if os.path.exists(output_path):
        print(f"Error: The output path '{output_path}' already exists.")
        print("Please delete it manually if you want to regenerate the project.")
        return

    shutil.copytree(repo_path, output_path)
    os.chdir(output_path)

    try:
        commit_hashes = subprocess.check_output(
            ["git", "log", "--all", "--no-merges", "--author=" + author_email, "--pretty=format:%H"]
        ).decode().splitlines()
    except subprocess.CalledProcessError:
        print("Failed to retrieve commits. Is this a valid Git repo?")
        return

    if not commit_hashes:
        print(f"No commits found for author {author_email}")
        return

    print(f"Found {len(commit_hashes)} non-merge commits by {author_email}")

    subprocess.run(["git", "checkout", "--orphan", "isolated_branch"])
    subprocess.run(["git", "rm", "-rf", "."], shell=True)

    for commit in reversed(commit_hashes):
        result = subprocess.run(["git", "cherry-pick", commit])
        if result.returncode != 0:
            print(f"Conflict on commit {commit}, skipping...")
            subprocess.run(["git", "cherry-pick", "--abort"])

    print(f"Isolated project created at: {output_path}")

    # sonar-project.properties
    sonar_config = f"""
# SonarQube configuration for {group_name}_{student_name}
sonar.projectKey={group_name}_{student_name}
sonar.projectName={group_name.capitalize()} - {student_name.capitalize()}
sonar.sources=.
sonar.language=
sonar.host.url=http://localhost:9000
sonar.login=<TOKEN>
"""
    sonar_file_path = os.path.join(output_path, "sonar-project.properties")
    with open(sonar_file_path, "w", encoding="utf-8") as f:
        f.write(sonar_config.strip())

    print(f"SonarQube config file created at: {sonar_file_path}")
    print("You can now edit the token or other settings as needed.")

if __name__ == "__main__":
    extract_commits_by_author(
        repo_path=r"C:\Users",         # Path to group repo
        author_email="",               # Student's commit email
        group_name="",                 # Group identifier
        student_name=""                # Student's name
    )
