from transformers import BartTokenizer, BartForConditionalGeneration

# Load model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Conversation input
conversation = """
User: Hi, I have an issue with my order.
Agent: Can you share the order ID?
User: Yes, it is 4567.
Agent: Your refund has been initiated.
"""

# Tokenize
inputs = tokenizer(
    conversation,
    max_length=1024,
    truncation=True,
    return_tensors="pt"
)

# Generate summary
summary_ids = model.generate(
    inputs["input_ids"],
    max_length=150,
    min_length=40,
    length_penalty=2.0,
    num_beams=4,
    early_stopping=True
)

# Decode
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Summary:", summary)
