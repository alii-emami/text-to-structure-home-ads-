# app/extractors.py
"""
توابع استخراج اطلاعات از متن آگهی (متراژ، تعداد اتاق، NER).
ورودی: متن خام.
خروجی: دیکشنری شامل building_size, rooms_count, has_elevator, has_parking, is_rebuilt.
"""
import re
import torch
from hazm import Normalizer

normalizer = Normalizer()

def extract_area(text):
    patterns = [
        r'(\d+(?:\.\d+)?)\s*متر',
        r'متراژ\s*(\d+(?:\.\d+)?)',
        r'زیربنا\s*(\d+(?:\.\d+)?)',
        r'(\d+(?:\.\d+)?)\s*متری',
        r'بنای\s*(\d+(?:\.\d+)?)\s*متر'
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            num_str = m.group(1).translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789'))
            try:
                return float(num_str)
            except:
                continue
    return None

def extract_rooms(text):
    rooms_map = {'یک':1, 'دو':2, 'سه':3, 'چهار':4, 'پنج':5}
    m = re.search(r'(\d+)\s*(?:خواب|اتاق)', text)
    if m:
        return int(m.group(1))
    for word, num in rooms_map.items():
        if re.search(rf'{word}\s*(?:خواب|اتاق)', text):
            return num
    return None

def extract_ner_entities(text, tokenizer, model, device):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=2)
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
    labels = [model.config.id2label[p.item()] for p in predictions[0]]
    
    entities = {"has_elevator": None, "has_parking": None, "is_rebuilt": None}
    for token, label in zip(tokens, labels):
        if token in ["[CLS]", "[SEP]", "[PAD]"]:
            continue
        if label.startswith("B-") or label.startswith("I-"):
            if "ELEVATOR_POS" in label:
                entities["has_elevator"] = True
            elif "ELEVATOR_NEG" in label:
                if entities["has_elevator"] is None:
                    entities["has_elevator"] = False
            elif "PARKING_POS" in label:
                entities["has_parking"] = True
            elif "PARKING_NEG" in label:
                if entities["has_parking"] is None:
                    entities["has_parking"] = False
            elif "REBUILT_POS" in label:
                entities["is_rebuilt"] = True
            elif "REBUILT_NEG" in label:
                if entities["is_rebuilt"] is None:
                    entities["is_rebuilt"] = False
    return entities

def process_text(text, tokenizer, model, device):
    normalized = normalizer.normalize(text)
    area = extract_area(normalized)
    rooms = extract_rooms(normalized)
    ner_results = extract_ner_entities(normalized, tokenizer, model, device)
    return {
        "building_size": area,
        "rooms_count": rooms,
        "has_elevator": ner_results["has_elevator"],
        "has_parking": ner_results["has_parking"],
        "is_rebuilt": ner_results["is_rebuilt"]
    }