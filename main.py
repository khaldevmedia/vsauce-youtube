# Required Third-Party Libraries:
# Install using: pip install youtube_transcript_api

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import re
from urllib.parse import urlparse, parse_qs
import string

# Global Variables
VIDEO_URL = "https://www.youtube.com/shorts/hIMIsbLodzM"  # Replace with your YouTube video URL
LANGUAGE = 'en'  # Default language

def get_video_id(url):
    """
    Extracts the video ID from a YouTube URL.
    Supports standard, shorts, and shortened URLs.
    """
    parsed_url = urlparse(url)
    if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        if parsed_url.path == '/watch':
            query = parse_qs(parsed_url.query)
            video_id = query.get('v', [None])[0]
            if video_id:
                return video_id
        elif parsed_url.path.startswith('/shorts/'):
            video_id = parsed_url.path.split('/')[2]
            if len(video_id) == 11:
                return video_id
    elif parsed_url.hostname in ['youtu.be']:
        video_id = parsed_url.path.lstrip('/')
        if len(video_id) == 11:
            return video_id
    raise ValueError("Invalid YouTube URL or unable to extract Video ID.")

def download_captions(video_url, language='en'):
    """
    Downloads the auto-generated captions for the given YouTube video URL.
    Saves them to a file named after the video ID.
    Returns the transcript as a single string.
    """
    try:
        video_id = get_video_id(video_url)
        filename = f"{video_id}.txt"  # Set filename based on video ID

        # Fetch the transcript list
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Try to fetch the manually created transcript first
        try:
            transcript = transcript_list.find_manually_created_transcript([language])
        except NoTranscriptFound:
            # If not available, fetch the auto-generated transcript
            transcript = transcript_list.find_generated_transcript([language])
        
        # Fetch the transcript data
        transcript_data = transcript.fetch()
        
        # Combine all text segments into a single string
        full_text = " ".join([entry['text'] for entry in transcript_data])
        
        # Save to file named after the video ID
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(full_text)
        
        print(f"Captions saved to {filename}")
        return full_text

    except TranscriptsDisabled:
        print("Transcripts are disabled for this video.")
        return ""
    except NoTranscriptFound:
        print("No transcripts found for this video.")
        return ""
    except ValueError as ve:
        print(f"Error: {ve}")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""

def check_unused_letters(text):
    """
    Checks which letters of the English alphabet are not used in the given text.
    Returns a set of unused letters.
    """
    # Define the set of all English lowercase letters
    all_letters = set(string.ascii_lowercase)
    
    # Normalize the text to lowercase and extract letters
    used_letters = set(re.findall(r'[a-z]', text.lower()))
    
    # Determine unused letters
    unused_letters = all_letters - used_letters
    
    return unused_letters

def main():
    # Download captions and get the transcript text
    transcript_text = download_captions(VIDEO_URL, LANGUAGE)
    
    if not transcript_text:
        print("No transcript available to analyze.")
        return
    
    # Optional: Check transcript length (e.g., Shorts are short)
    if len(transcript_text) < 100:  # Arbitrary threshold, adjust as needed
        print("Transcript is very short. Letter usage may be limited.")
    
    # Check for unused letters
    unused = check_unused_letters(transcript_text)
    
    if not unused:
        print("All letters of the English alphabet were used in the video captions.")
    else:
        unused_sorted = sorted(unused)
        print("The following letters were NOT used in the video captions:")
        print(", ".join(unused_sorted))

if __name__ == "__main__":
    main()
