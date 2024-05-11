from data_load_helper import DataLoader
data_loader = DataLoader()

json_file_path = './data/iris.json'  
sas_file_path = './data/airline.sas7bdat'  
xml_file_path = './data/NCT04336761.xml'  
excel_file_path = './data/finance_sample.xlsx'  

print("**"*50)
print("LOADING JSON DATA")
print("**"*50)
print("\n\n\n")
json_data = data_loader.load_json_file(json_file_path)
print(json_data)
print("\n\n\n") 


print("**"*50)
print("LOADING EXCEL DATA")
print("**"*50)
print("\n\n\n")
excel_data = data_loader.load_excel_file(excel_file_path)
print(excel_data)
print("\n\n\n")

print("**"*50)
print("LOADING SAS DATA")
print("**"*50)
print("\n\n\n")
sas_data = data_loader.load_sas7bdat_file(sas_file_path)
print(sas_data)
print("\n\n\n")

print("**"*50)
print("LOADING XML DATA")
print("**"*50)
print("\n\n\n")
xml_data = data_loader.load_xml_file(xml_file_path)
print(xml_data)
print("\n\n\n")