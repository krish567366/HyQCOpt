from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import boto3
from ..middleware.auth import verify_token

router = APIRouter()
sqs = boto3.client('sqs')

class JobRequest(BaseModel):
    problem: dict
    algorithm: str
    backend: dict
    parameters: dict

@router.post("/jobs")
async def submit_job(
    request: JobRequest,
    user=Depends(verify_token)
):
    if not user.get('premium') and request.algorithm != 'classic':
        raise HTTPException(403, "Quantum algorithms require premium tier")
    
    try:
        response = sqs.send_message(
            QueueUrl=os.getenv('JOB_QUEUE_URL'),
            MessageBody=request.json(),
            MessageGroupId='jobs',
            MessageAttributes={
                'userId': {'StringValue': user['sub'], 'DataType': 'String'}
            }
        )
        return {"job_id": response['MessageId']}
    except Exception as e:
        raise HTTPException(500, f"Submission failed: {str(e)}")