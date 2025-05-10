from hyqcopt import configure_backend
from sqlalchemy import create_engine
from contextlib import contextmanager

class TenantIsolator:
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id
        self.engine = create_engine(os.getenv('DB_URI'))
        
    @contextmanager
    def database_session(self):
        """Isolated database session"""
        with self.engine.connect() as conn:
            conn.execute(f"SET search_path TO tenant_{self.tenant_id}")
            yield conn
            
    def configure_quantum_backend(self):
        """Isolate quantum resources"""
        configure_backend(
            s3_bucket=f"tenant-{self.tenant_id}-results",
            aws_role=f"tenant-{self.tenant_id}-quantum-role",
            qpu_quota=self.tenant.tier.qpu_hours
        )