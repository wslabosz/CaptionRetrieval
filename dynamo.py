import boto3


class Captions:
    def __init__(self, video_id: str, script: str, is_generated: bool):
        self.video_id = video_id
        self.script = script
        self.is_generated = is_generated

class CaptionsTable:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table("caption-store")

    def get_captions(self, id: str) -> Captions:
        response = self.table.get_item(Key={'videoID': id})
        return response.get('Item')

    def put_captions(self, item: Captions) -> None:
        self.table.put_item(Item={
            'videoID': item.video_id,
            'script': item.script,
            'is_generated': item.is_generated
        })

    def update_captions(self, id: str, update_expression, expression_attribute_values) -> None:
        self.table.update_item(
            Key=id,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
