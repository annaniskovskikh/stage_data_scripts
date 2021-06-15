#import pandas as pd

#df = pd.read_excel (r'project-6-at-2021-06-09-14-02-22ebc07b - Copie.xlsx', encoding="utf8")
#print (df)

with open('project-6-at-2021-06-09-14-02-22ebc07b - Copie.xlsx', errors="ignore") as fic:
    for line in fic:
        print(line)