import textract
import os,glob, re
from nltk.corpus import stopwords

all_resumes = []
skill_set_universal = []
skills_list = open("universal_skillset.txt",'r')
for skill in skills_list.readlines():
    skill = skill.replace('\n', '')
    skill_set_universal.append(skill.lower())

skill_set_universal = set(skill_set_universal)
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
    return set(link)

def extract_skills(resume):
    skills = []
    for elem in enumerate(skill_set_universal):
        if any(item.lower() == elem[1].lower() for item in resume):
            skills.append(elem[1])
    return set(skills)

output = []
def process_resumes(directory_name):
    for resume in directory_name:
        email = extract_email(resume)
        skills = extract_skills(resume)
        phone = extract_phone(resume)
        links = extract_links(resume)
        email = email.split('.com',1)[0]
        file = open(email+".txt", "w")
        for i in skills:
            file.write(i + " ")
        file.close()
        output.append({"email": email, "skills":skills, "phone": phone, "links":links})

""" Processing of Resumes Starts Here..."""

extract_text("Resumes")
process_resumes(all_resumes)

for o in output:
    print o
    print "\n"