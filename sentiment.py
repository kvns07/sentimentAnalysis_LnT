import torch
from transformers import BertTokenizer, BertForSequenceClassification
import matplotlib.pyplot as plt
import csv
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)


# sentence = "I have tears of joy"
def sent(sentence):
    inputs = tokenizer(sentence, return_tensors='pt', padding=True, truncation=True)
    outputs = model(**inputs)

    predicted_class = torch.argmax(outputs.logits, dim=1).item()
    return "positive" if predicted_class == 1 else "negative"
w=[]
csv_file_path = 'data.csv'

with open("csv_file.csv", 'r', newline='',encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skip the header row if needed
    next(csv_reader)  # Skip the header row
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each row is a list of values
        # print(row[3])
        w.append(sent(row[3]))
# print(sent("The 30-share BSE Sensex was  up  141.52 points at 72782.71"))
# for i in w:
#     print(i)
labels = ['Positive','Negative']
sizes = []  # Sizes or percentages for each section
colors = ['Blue', 'Red']
a = int(0)
b = int(0)
for i in w:
    if(i=='positive'):
        a=a+1
    else:
        b=b+1
sizes.append(a)
sizes.append(b)

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.savefig('graph.png')













# sentiment = "positive" if predicted_class == 1 else "negative"
# print(f"Sentence: {sentence}")
# print(f"Predicted Sentiment: {sentiment}")