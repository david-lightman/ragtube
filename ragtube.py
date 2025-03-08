#!/usr/bin/env python
# script to summarize youtube vids
# lightman
import argparse
from youtube_transcript_api import YouTubeTranscriptApi
import ollama

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([item['text'] for item in transcript])
        return full_text
    except Exception as e:
        print(f"error retrieving transcript: {e}")
        return None

def summarize_with_ollama(transcript_text):
    # will need ot tweak this prompt, likely
    prompt = f"Summarize the following video transcript clearly and concisely. Do not make up information. Unless requested answer questions using information from the following context:\n\n{transcript_text}\n\nSummary:"
    # using llama3:latest on mac m3
    response = ollama.chat(model='llama3:latest', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

def interactive_rag_conversation(transcript_text, summary):
    print("\n\nentering RAG interactive mode (type 'exit' to quit):")
    conversation = [
        {"role": "system", "content": f"You are an assistant with context from the following video transcript:\n\n{transcript_text}\n\nHere's a concise summary of the transcript:\n{summary}"}
    ]
    
    while True:
        user_input = input(" > ")
        if user_input.lower() in ['exit', 'quit']:
            print("Done.\n")
            break

        conversation.append({"role": "user", "content": user_input})
        response = ollama.chat(model='llama3:latest', messages=conversation)
        assistant_reply = response['message']['content']
        
        print(f"llama3: {assistant_reply}")
        conversation.append({"role": "assistant", "content": assistant_reply})


def main():
    #video_id = 'T-D1OfcDW1M'  
    parser = argparse.ArgumentParser(description="Fetch YouTube transcript and summarize using Ollama/Llama3.")
    parser.add_argument("video_id", help="The EwwTube video ID")
    args = parser.parse_args()

    print("fetching transcript...")
    transcript_text = get_transcript(args.video_id)
    
    if not transcript_text:
        print("fetch failed (bad video id?!)... exiting...")
        return
    
    print("retrieved transcript - starting summarization with llama3:latest...\n")
    summary = summarize_with_ollama(transcript_text)
    print(f"summary:\n{summary}")

    interactive_rag_conversation(transcript_text, summary)


if __name__ == "__main__":
    main()

