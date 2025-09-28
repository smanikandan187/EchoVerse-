from transformers import pipeline

# Initialize pipeline once
pipe = pipeline("text-generation", model="ibm-granite/granite-3b-code-instruct-128k")

tone_instructions = {
    "Neutral": "Rewrite the following text in a neutral and clear tone.",
    "Suspenseful": "Rewrite the following text to create suspense and tension.",
    "Inspiring": "Rewrite the following text to sound inspiring and motivational."
}

def rewrite_text(text, tone):
    prompt = f"{tone_instructions[tone]}\n\nOriginal Text: {text}\n\nEnhanced Text:"
    # Use the pipeline with list of messages - adapting for generation
    output = pipe(prompt, max_length=2048, do_sample=False)
    # Extract generated text after prompt
    generated_text = output[0]['generated_text']
    # Remove the prompt part to return only rewritten text
    rewritten = generated_text[len(prompt):].strip()
    return rewritten