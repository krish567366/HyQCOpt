# Generate audit trail collector
cat > services/compliance/soc2.py <<EOL
import boto3
from datetime import datetime

class SOC2Compliance:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.logs = boto3.client('logs')
    
    def collect_evidence(self):
        # Export CloudTrail logs
        self.logs.create_export_task(
            logGroupName='/aws/cloudtrail',
            fromTime=int((datetime.now() - timedelta(days=30)).timestamp() * 1000),
            toTime=int(datetime.now().timestamp() * 1000),
            destination='hyqcopt-soc2-logs',
            destinationPrefix='audit-trail'
        )
        
        # Encrypt and store
        self.s3.put_object(
            Bucket='hyqcopt-compliance',
            Key=f'audit-{datetime.now().isoformat()}.enc',
            ServerSideEncryption='aws:kms:kyber'
        )
EOL