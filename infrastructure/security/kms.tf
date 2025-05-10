resource "aws_kms_key" "data_encryption" {
  description             = "HyQCOpt data encryption"
  deletion_window_in_days = 30
  enable_key_rotation     = true
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Action   = "kms:*"
        Resource = "*"
      }
    ]
  })
}

resource "aws_ssm_parameter" "db_password" {
  name  = "/hyqcopt/db_password"
  type  = "SecureString"
  value = var.db_password
  key_id = aws_kms_key.data_encryption.key_id
}