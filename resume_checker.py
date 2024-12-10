import os
import PyPDF2
import matplotlib.pyplot as plt
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

resume_keywords = {
    "App Developer": [
        "Android", "Flutter", "Dart", "Kotlin", "iOS", "Swift", "Java", "React Native"
    ],
    "Web Developer": [
        "HTML", "CSS", "JavaScript", "React", "Angular", "Vue", "Node.js", "Bootstrap", "SASS", "Web Development"
    ],
    "Data Scientist": [
        "Python", "R", "Pandas", "NumPy", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Data Analysis", "Data Visualization"
    ],
    "Cyber Security Analyst": [
        "Cyber Security", "Network Security", "Firewalls", "Intrusion Detection", "Penetration Testing", "Blockchain", "Encryption", "Threat Analysis"
    ],
    "Product Manager": [
        "Product Management", "Roadmap", "Scrum", "Agile", "User Stories", "Market Research", "Stakeholder Management", "MVP", "A/B Testing"
    ],
    "Software Engineer": [
        "Software Development", "Java", "C++", "Python", "Algorithms", "Data Structures", "Software Design", "Version Control", "Agile"
    ],
    "DevOps Engineer": [
        "DevOps", "CI/CD", "Jenkins", "Docker", "Kubernetes", "AWS", "Azure", "Ansible", "Infrastructure as Code", "Terraform"
    ],
    "Machine Learning Engineer": [
        "Machine Learning", "Deep Learning", "Python", "Scikit-Learn", "TensorFlow", "Keras", "PyTorch", "Model Deployment", "Feature Engineering"
    ],
    "UI/UX Designer": [
        "User Interface", "User Experience", "Wireframes", "Prototyping", "Adobe XD", "Figma", "Sketch", "Usability Testing", "Interaction Design"
    ],
    "Cloud Engineer": [
        "Cloud Computing", "AWS", "Azure", "Google Cloud", "Kubernetes", "Cloud Security", "Serverless", "Cloud Architecture", "DevOps"
    ],
    "Blockchain Developer": [
        "Blockchain", "Smart Contracts", "Ethereum", "Solidity", "Hyperledger", "Cryptocurrency", "Decentralized Applications", "Consensus Algorithms"
    ],
    "Default": []
}

resources = {
    "App Developer": [
        "Resource: https://developer.android.com/",
        "Course: https://www.udemy.com/course/the-complete-guide-to-flutter-development/"
    ],
    "Web Developer": [
        "Resource: https://developer.mozilla.org/",
        "Course: https://www.coursera.org/specializations/full-stack-react"
    ],
    "Data Scientist": [
        "Resource: https://www.kaggle.com/",
        "Course: https://www.coursera.org/specializations/jhu-data-science"
    ],
    "Cyber Security Analyst": [
        "Resource: https://www.cybrary.it/",
        "Course: https://www.udemy.com/course/the-complete-hacker-course/"
    ],
    "Product Manager": [
        "Resource: https://www.productcoalition.com/",
        "Course: https://www.coursera.org/specializations/product-management"
    ],
    "Software Engineer": [
        "Resource: https://www.geeksforgeeks.org/",
        "Course: https://www.udacity.com/course/intro-to-computer-science--ud009"
    ],
    "DevOps Engineer": [
        "Resource: https://www.devops.com/",
        "Course: https://www.udemy.com/course/devops-project/"
    ],
    "Machine Learning Engineer": [
        "Resource: https://www.fast.ai/",
        "Course: https://www.coursera.org/specializations/machine-learning-data-science"
    ],
    "UI/UX Designer": [
        "Resource: https://www.smashingmagazine.com/",
        "Course: https://www.udemy.com/course/ux-and-ui-design/"
    ],
    "Cloud Engineer": [
        "Resource: https://aws.amazon.com/training/",
        "Course: https://www.udemy.com/course/azure-cloud/"
    ],
    "Blockchain Developer": [
        "Resource: https://www.ethereum.org/",
        "Course: https://www.udacity.com/course/intro-to-blockchain--ud197"
    ]
}

def extract_text_from_pdf(file_path):
    text = ''
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def evaluate_resume(file_path, resume_type):
    text = extract_text_from_pdf(file_path)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words]

    if resume_type not in resume_keywords:
        resume_type = "Default"

    keywords_lower = {keyword.lower() for keyword in resume_keywords[resume_type]}
    matching_keywords = {token for token in filtered_tokens if token in keywords_lower}
    non_matching_keywords = keywords_lower - matching_keywords

    score = round((len(matching_keywords) / len(keywords_lower)) * 5, 1) if keywords_lower else 0

    # Resources for missing keywords
    missing_resources = [resources[resume_type][i % len(resources[resume_type])] for i, keyword in enumerate(resume_keywords[resume_type]) if keyword.lower() in non_matching_keywords]

    return score, non_matching_keywords, missing_resources

def plot_pie_chart(score, resume_type):
    labels = ['Matched Keywords', 'Missing Keywords']
    sizes = [score, 5 - score]
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)
    return img
