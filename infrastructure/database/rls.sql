-- Enable RLS on critical tables
ALTER TABLE jobs ENABLE ROW LEVEL SECURITY;
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Create tenant isolation policies
CREATE POLICY tenant_jobs_isolation 
  ON jobs USING (tenant_id = current_setting('app.current_tenant'));

CREATE POLICY tenant_users_isolation
  ON users USING (tenant_id = current_setting('app.current_tenant'));