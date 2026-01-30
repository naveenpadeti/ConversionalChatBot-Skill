def rule_based_ner(text):
    entities = {}

    words = text.lower().split()

    cities = ["vijayawada", "hyderabad", "chennai", "bangalore"]
    dates = ["today", "tomorrow"]

    for word in words:
        if word in cities:
            entities.setdefault("LOCATION", []).append(word)

        if word in dates:
            entities["DATE"] = word

    return entities

text = "I want to travel from Vijayawada to Hyderabad tomorrow"
print(rule_based_ner(text))

slots = {
    "source": None,
    "destination": None,
    "date": None
}

def update_slots(entities, slots):
    locations = entities.get("LOCATION", [])

    if len(locations) == 2:
        slots["source"] = locations[0]
        slots["destination"] = locations[1]

    if "DATE" in entities:
        slots["date"] = entities["DATE"]

user_input = "Book a ticket from Vijayawada to Hyderabad tomorrow"

entities = rule_based_ner(user_input)
update_slots(entities, slots)

print(slots)

import spacy

nlp = spacy.load("en_core_web_sm")

text = "I want to travel from Vijayawada to Hyderabad on 25 March"
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, "→", ent.label_)

def smart_chatbot(user_input, context):
    doc = nlp(user_input)

    for ent in doc.ents:
        if ent.label_ == "GPE":
            if context["source"] is None:
                context["source"] = ent.text
            else:
                context["destination"] = ent.text

        if ent.label_ == "DATE":
            context["date"] = ent.text

