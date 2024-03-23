import json
import csv
import requests
    # import json


def convert_json_to_csv(json_file, csv_file):
    # Read JSON data from file
    with open(json_file, 'r',encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract column headers from JSON keys
    headers = list(data['articles'][0])
    print(headers)
    # Write data to CSV file
    with open(csv_file, 'w', newline='',encoding='utf8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        
        # Write headers
        writer.writeheader()
        
        # Write rows
        for row in data['articles']:
            writer.writerow(row)

def retJson():
    url = ('https://newsapi.org/v2/everything?q=Larsen+Toubro&from=2024-03-15&sortBy=publishedAt&apiKey=b6e7ad29e9bb4e509191ead6af1d88d0')
    data = requests.get(url).json()
    return data 
def conJson(data):

    # Path to the JSON file
    json_file_path = './data.json'

    # Write JSON data to the file
    # with open(json_file_path, 'w',encoding='utf-8') as json_file:
    #     json.dump(data, json_file, indent=4)
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    # print("JSON data has been written to", json_file_path)
data=retJson()
conJson(data)
convert_json_to_csv("data.json","csv_file.csv")