import textract
import os,glob, re
from nltk.corpus import stopwords

all_resumes = []
skill_set_universal = ['java','python', 'c','c++','swift', '.net','machine learning', 'SML', 'mysql', 'mongodb','apache']
output = []
def extract_text(directory_name):
    os.chdir(directory_name)
    for file in glob.glob("*.pdf"):
        text = textract.process(file, encoding='ascii')
        words = text.split()
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word not in stop_words]
        all_resumes.append(filtered_words)

def extract_email(resume):
    email = ""
    for token in resume:
        match = re.findall(r'[\w\.-]+@[\w\.-]+', token)
        if match :
            email = token
            break
    return email

def extract_phone(resume):
    token = ' '.join(resume)
    regex = re.compile("\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}")
    return re.findall(regex, token)

def extract_links(resume):
    link = re.findall(r'(https?://[^\s]+)', ' '.join(resume))
    return link

def extract_skills(resume):
    skills = []
    for w in resume:
        if w.lower() in skill_set_universal:
            skills.append(w.lower())
    return set(skills)

def process_resumes(directory_name):
    for resume in directory_name:

        email = extract_email(resume)
        skills = extract_skills(resume)
        phone = extract_phone(resume)
        links = extract_links(resume)
        output.append({"email": email, "skills":skills, "phone": phone, "links":links})



""" Processing of Resumes Starts Here..."""

extract_text("Resumes")
process_resumes(all_resumes)

for o in output:
    print o
    print "\n"