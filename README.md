# Resume Checker - README

## Overview

The **Resume Checker** project is a Python-based application designed to analyze and evaluate resumes. It provides insightful feedback, including skills matching, keyword identification, and overall resume scoring. This tool is ideal for job seekers, career counselors, and HR professionals looking to streamline the resume review process.

---

## Features

1. **Resume Analysis**  
   Extracts and evaluates key sections from resumes such as skills, work experience, and education.

2. **Keyword Matching**  
   Compares resume content against job descriptions or specific criteria to assess relevance.

3. **Visualization**  
   Generates graphical insights, such as pie charts, to summarize the analysis.

4. **Web Interface**  
   An easy-to-use web interface for uploading and analyzing resumes.

5. **Report Generation**  
   Provides detailed feedback and recommendations for improvement.

---

## File Structure

| File/Folder Name          | Description                                                                |
|---------------------------|----------------------------------------------------------------------------|
| **LICENSE**               | Specifies the MIT license for the repository.                            |
| **My+Resume.pdf / MyResume.pdf / resume.pdf** | Sample resume files used for testing and demonstration purposes.|
| **README.md**             | The detailed documentation of the project.                               |
| **chart.png / pie_chart.png** | Visualizations generated from the resume analysis.                    |
| **index.html**            | Web interface for uploading and analyzing resumes.                       |
| **main.py**               | Entry point for running the web application.                             |
| **requirements.txt**      | Lists all dependencies required for the project.                         |
| **result.html**           | Template to display analysis results on the web interface.               |
| **resume_checker.py**     | Core logic for analyzing resumes.                                         |
| **resume_checker.cpython-312.pyc** | Compiled Python bytecode for the resume checker module.           |
| **tempCodeRunnerFile.py** | Temporary file generated during development.                              |

---

## Requirements

### Prerequisites
- Python 3.8 or higher
- Libraries (listed in `requirements.txt`):
  - Flask
  - pandas
  - matplotlib
  - PyPDF2

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/resume-checker.git
   cd resume-checker
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the Application
1. Start the Flask application:
   ```bash
   python main.py
   ```
2. Open the web interface in your browser at `http://127.0.0.1:5000`.

### Resume Analysis
- Upload a PDF resume via the web interface.
- View analysis results, including keyword matching and graphical insights.

### Customizing Keywords
- Modify the `resume_checker.py` file to include custom job descriptions or criteria for matching.

---

## Sample Input and Output

### Input
- A PDF file containing the user's resume.

### Output
- Analysis report including:
  - Key skills identified
  - Match percentage with job criteria
  - Visual breakdown (e.g., pie chart of skill categories)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request for improvements, bug fixes, or new features.

---

