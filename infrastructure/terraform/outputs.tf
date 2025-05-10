output "job_queue_url" {
  value = aws_sqs_queue.quantum_jobs.id
}

output "lambda_processor_arn" {
  value = aws_lambda_function.job_processor.arn
}

output "api_gateway_endpoint" {
  value = aws_api_gateway_deployment.hyqcopt.invoke_url
}