#!/usr/bin/env python3
# *-* coding: UTF-8 *-*
# Author: Jessica Roady

import json
import spacy

data = []
with open("data/zora_data_06.json", "r", encoding="utf-8") as f:
    for line in f:
        item = json.loads(line)

        if ("language" in item) and ("eng" in item["language"]) and ("subject" in item) \
                and ("Medicine" not in item["subject"]) and ("description" in item):
            data.append(item)


total_pubs = len(data)
total_tokens = 0

abstracts = [item["description"] for item in data]

nlp = spacy.load("en_core_web_sm")

for a in abstracts:
    a = a[0]
    doc = nlp(a)
    total_tokens += len(doc)

print(f"Avg. token count: {total_tokens / total_pubs}")
