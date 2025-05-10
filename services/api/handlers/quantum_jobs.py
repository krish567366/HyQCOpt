from fastapi import APIRouter, Depends
from ..middleware.auth import verify_token
import boto3

router = APIRouter()
sqs = boto3.client('sqs')

@router.post("/submit-job")
async def submit_job(problem: dict, _ = Depends(verify_token)):
    response = sqs.send_message(
        QueueUrl=os.getenv('JOB_QUEUE_URL'),
        MessageBody=json.dumps(problem)
    )
    return {'job_id': response['MessageId']}