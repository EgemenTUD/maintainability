# Maintainability & Experience Analysis Scripts

This repository contains the scripts developed and used to analyze the relationship between programming experience and code maintainability in student projects. Each script addresses a different part of the workflow from data extraction to statistical analysis.

## 📁 Contents

### 1. `commit-extractor.py`
This script isolates all commits authored by a specific student across **all branches** of a group repository.

**Main features:**
- Clones a copy of the full group repository.
- Filters commits authored by the specified student (via email).
- Reconstructs an isolated version of the project containing only that student’s contributions.
- Initializes a `sonar-project.properties` file to prepare the repo for SonarQube analysis.

**Parameters to edit:**
- `repo_path`: Local path to the original group repo.
- `author_email`: Email associated with the student’s commits.
- `group_name` and `student_name`: Used to name the output folder and project.

---

### 2. `shapiro-wilk-test.py`
A standalone script to perform the **Shapiro-Wilk normality test** for each maintainability metric.

**Functionality:**
- Takes a dictionary of metric data.
- Returns a DataFrame showing W-statistic, p-value, and whether the distribution is normal (`p > 0.05`).

---

### 3. `pearson.py`
A simple script to compute the **Pearson correlation coefficient** between two metrics.

**Usage:**
- Edit the `x` and `y` variables with your data arrays.
- The script outputs the correlation coefficient and p-value.

---

### 4. `effect-size.py`
This script calculates **Cohen’s _d_** to quantify the effect size between two groups (e.g., high vs. low experience).

**Main features:**
- Accepts two numerical lists or arrays.
- Computes the pooled standard deviation and Cohen’s _d_.
- Interprets the effect size (small, medium, or large).

**Usage:**
- Replace the sample `group1` and `group2` variables with your actual data.
- Run the script to print both the raw effect size and its interpretation.

---

## 🔍 How SonarQube Was Used to Compute Maintainability Metrics

1. **Setup SonarQube Locally**
   - Download and unzip the latest SonarQube Community Edition.
   - Run `StartSonar.bat` (Windows) or equivalent for your OS.
   - Access the dashboard at [http://localhost:9000](http://localhost:9000).

2. **Create a Project**
   - On the SonarQube dashboard, create a new project matching the `projectKey` and `projectName` used in the script’s `sonar-project.properties`.

3. **Generate a Token**
   - Go to your SonarQube user account settings.
   - Create a **new token**, and copy it into the `sonar-project.properties` file as `sonar.login=<YOUR_TOKEN>`.

4. **Edit and Finalize the Config**
   - Open `sonar-project.properties` in the extracted student folder.
   - Set the appropriate `sonar.language` (e.g. `py`, `java`, `js`, `rs` for Rust).

5. **Run Analysis**
   - Open a terminal in the student's folder.
   - Run `sonar-scanner`.
   - After a few seconds, results will be uploaded and visible on the SonarQube dashboard.

### 6. Collect Metrics

For each student's isolated repository, the following maintainability metrics were extracted using the **SonarQube API** or calculated manually:

- **Code Smells per 1000 LOC**  
  Retrieved from SonarQube’s API (`code_smells` and `ncloc` metrics), then calculated as:  
  `Code Smells / (LOC / 1000)`

- **Comment Density (%)**  
   Retrieved from SonarQube’s API (`commented_lines` and `ncloc` metrics), then calculated as:  
  `Commented Lines / (LOC / 1000)`

- **Code Duplication (%)**  
  Retrieved from the `duplicated_lines_density` metric in SonarQube.

- **Average File Size (LOC)**  
  Calculated by dividing `ncloc` (non-comment lines of code) by the total number of files, both obtained via the API (`ncloc` and `file_count`).

- **Naming Quality (1–5, manually scored)**  
  Assessed manually by reviewing class, method, and variable naming clarity, consistency, and descriptiveness.

Each metric was normalized (e.g., scaled between 0 and 1 or inverted if lower values were preferable) before being combined into a maintainability score.


---

## 🧪 Final Analysis
After collecting all SonarQube metrics and programming experience scores, the following statistical tests were performed using the provided scripts:
- Shapiro-Wilk test (to verify normality assumptions)
- Pearson correlation test (to quantify the relationship between experience and maintainability)

---
