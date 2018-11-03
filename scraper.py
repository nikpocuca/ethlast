# Import URL library. 
import urllib.request
import time
import pandas as pd 

# Import Beautiful Soup

from bs4 import BeautifulSoup

# I will need to iteration to go through all the nationality 
# I also need to iterate through pages. 
# specify the url

fullwiki = "https://www.familyeducation.com/baby-names/browse-origin/surname"
page = urllib.request.urlopen(fullwiki)
soup = BeautifulSoup(page)
last_name = []
name_section = soup.find("ul", {"class": "baby-names-list links col-xs-12 col-sm-4"})
for lastnames in name_section.findAll('a'):
    last_name.append(lastnames.string)

df = pd.DataFrame(columns = ['name','origin'])

def getNames(l_input):
    df = pd.DataFrame(columns = ['name','origin'])
    count = 0
    test = 0
    while test == 0:
        # While some condition 
        dNames = "https://www.familyeducation.com/baby-names/browse-origin/surname/"+lname+"?page=" + str(count)
        page = urllib.request.urlopen(dNames)
        soup = BeautifulSoup(page)
        baby_section = soup.find("ul", {"class": "baby-names-list links col-xs-12 col-sm-4"})
        print("hit " + str(count) )
        print(str(lname) + " " + str(count))
        if baby_section.findAll('a') == []:
            return(df)
        else:
            for entrys in baby_section.findAll('a'):
                df = df.append({'name':str(entrys.string),'origin':str(lname)},ignore_index=True)
            count += 1
    return(df)

full_df = pd.DataFrame(columns = ['name','origin'])
for lname in last_name:
    getNames(lname).to_csv(lname + ".csv")
