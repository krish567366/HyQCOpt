resource "aws_db_instance" "main" {
  backup_retention_period      = 35
  backup_window                = "07:00-09:00"
  maintenance_window           = "Sun:03:00-Sun:05:00"
  storage_type                 = "io1"
  iops                         = 1000
  replicate_source_db          = aws_db_instance.replica.arn
  deletion_protection          = true
}

resource "aws_db_instance" "replica" {
  replicate_source_db = aws_db_instance.main.identifier
  availability_zone   = "us-east-1b"
}