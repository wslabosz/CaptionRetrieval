from typing import List


class TranscriptionItem():
    text: str
    start: float
    duration: float


def retrieve_caption(transcript: List[TranscriptionItem]) -> str:
    return " ".join([item['text'] for item in transcript])