from django.shortcuts import render
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube

load_dotenv()
os.environ["GOOGLE_API_KEY"] = "AIzaSyCIdEZJK6cu1KsmPHLQGgAAV_H3guA24sQ"
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def video_summarizer(request):
    summary = None
    if request.method == 'POST':
        youtube_link = request.POST.get('youtube_link')
        if youtube_link:
            # Process the YouTube video and summarize as in Streamlit code
            video_id = youtube_link.split("=")[1]
            # (Add transcript extraction, summary generation here)
            summary = "Generated summary text here"
    
    return render(request, 'video_summarizer/index.html', {'summary': summary})