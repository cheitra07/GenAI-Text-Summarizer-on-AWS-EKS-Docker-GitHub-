#from transformers import pipeline

#summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#def summarize_text(text):
 #   result = summarizer(text, max_length=100, min_length=30, do_sample=False)
  #  return result[0]["summary_text"]

def summarize_text(text: str) -> str:
    if not text:
        return ""

    sentences = [s.strip() for s in text.split(".") if s.strip()]
    
    if len(sentences) <= 2:
        return ". ".join(sentences) + "."

    return ". ".join(sentences[:2]) + "."
