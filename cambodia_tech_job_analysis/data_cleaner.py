import pandas as pd

path = "datasets\primary_dataset.csv"
file = pd.read_csv(path)

ICT = ["Computer Science",
"Computer Technology",
"Computer Engineering",
"Computer Information Systems",
"Computer Professional",
"Computer Programming",
"Software Development",
"Software Engineering",
"Data Analytics",
"Data Science",
"Information Technology",
"InformationTechnology",
"Information Systems",
"Information System Management",
"Management information system",
"Management Information Systems",
"Computing",
"Technology",
"System Engineering",
"Geographical Info. Science",
"CISA",
"IS",
"Information and Communication Technology",
"IT Engineering",
"Telecommunication Engineering",
"Telecom Engineering",
"Network Security",
"Networking",
"Telecoms and Networking",
]

for index,row in file.iterrows():
    found = False
    data = file.loc[index:index,"Major 1": "Major 6"]
    for item in data:
        if data[item][index] in ICT:
            found = True
            break
    
    if found == False: 
        file = file.drop(labels=index,axis=0)

for index,row in file.iterrows():
    data = file.loc[index:index,"Major 1": "Major 6"]
    for item in data:
        if data[item][index] not in ICT:
            file.loc[index:index,item:item] = ""

file = file.reset_index(drop=True)

for item in ["Major 1","Major 2","Major 3","Major 4","Major 5","Major 6"]:
    if (file[item].values == '').sum() == len(file):
        file = file.drop(columns=item)

file.to_csv("datasets/dataset_v1.csv",index=False)
