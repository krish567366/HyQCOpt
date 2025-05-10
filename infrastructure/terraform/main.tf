resource "aws_sqs_queue" "quantum_jobs" {
  name                      = "hyqcopt-quantum-queue"
  delay_seconds             = 0
  max_message_size          = 2048
  message_retention_seconds = 86400
}

resource "aws_ecs_service" "quantum_workers" {
  name            = "quantum-worker"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.quantum.arn
  desired_count   = 2

  capacity_provider_strategy {
    capacity_provider = "FARGATE_SPOT"
    weight            = 1
  }

  scaling {
    min_capacity = 2
    max_capacity = 20
  }
}