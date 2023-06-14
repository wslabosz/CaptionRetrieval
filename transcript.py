from youtube_transcript_api import (NoTranscriptFound, Transcript,
                                    YouTubeTranscriptApi)


def retrieve_transcript(video_id: str) -> tuple[str, bool]:
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    is_transcript_generated = False
    try:
        transcript: Transcript = transcript_list.find_manually_created_transcript(['en'])  
    except NoTranscriptFound:
        print("manually created transcript doesn't exist")
        try:
            transcript: Transcript = transcript_list.find_generated_transcript(['en'])
            is_transcript_generated = True
        except NoTranscriptFound:
            print("generated transcript doesn't exist")
            return "", is_transcript_generated
        except any:
            print("generated transcript couldn't be retrieved")
            return "", is_transcript_generated
    except any:
        print("manually created transcript couldn't be retrieved")
        return "", is_transcript_generated
    

    return transcript.fetch(), is_transcript_generated