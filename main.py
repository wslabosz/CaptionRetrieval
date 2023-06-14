from dynamo import Captions, CaptionsTable
from format import retrieve_caption
from transcript import retrieve_transcript

ctable = CaptionsTable()

def lambda_handler(event, context):
    video_id = event['video_id']

    item = ctable.get_captions(video_id)
    print(item)

    if item:
        return {
            'statusCode': 200,
            'body': item['script']
        }
    else:
        transcript, is_generated = retrieve_transcript(video_id)
        caption = retrieve_caption(transcript)
        caption_record = Captions(video_id, caption, is_generated)
        ctable.put_captions(caption_record)
        return {
            'statusCode': 200,
            'body': caption_record.script
        }