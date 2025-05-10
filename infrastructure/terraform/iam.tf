resource "aws_iam_policy" "quantum_worker" {
  
  name = "HyQCOptQuantumWorker"
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "braket:CreateQuantumTask",
          "braket:GetQuantumTask"
        ]
        Resource = "*"
      },
      {
        Effect = "Allow"
        Action = [
          "sqs:ReceiveMessage",
          "sqs:DeleteMessage"
        ]
        Resource = aws_sqs_queue.quantum_jobs.arn
      }
    ]
  })
}