resource "aws_braket_quantum_task_queue" "hyqcopt" {
  name       = "hyqcopt-saas-queue"
  policy     = data.aws_iam_policy_document.quantum_access.json
  tags = {
    Environment = "production"
    SaaS-Tier   = "enterprise"
  }
}

resource "aws_db_instance" "tenant_dbs" {
  count               = var.tenant_count
  identifier          = "hyqcopt-tenant-${count.index}"
  allocated_storage   = 100
  engine              = "postgres"
  instance_class      = "db.m5.large"
  db_name             = "tenant_${count.index}"
  parameter_group_name = aws_db_parameter_group.tenant_policy.name
}