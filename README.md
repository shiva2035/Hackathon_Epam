# Hackathon_Epam
## Latest Edit by Gautam
step 1: upload resumes to "/Resumes" folder
step 2: upload "single" Job description to "/JD" folder
step 3: parse all the Resumes(using universal tech stack) and dump the following structure to database
    {[{
    'mailid1':{
        'techstack':'java angular ..',
        'githubid':''
    },
    'mailid2':{
        'techstack':'.net angular ..',
        'githubid':''
    }
    }]
    }
step 4: match resumes (tech stacks in database) with JD and rank using githubid
step 5: get top 20/30 profiles using matching and ranking (logic discussed with Shekar and saradhi)
step 6: mail to those profiles with some questions
step 7: filter again using simple logic