from hyqcopt.algorithms import QAOA
from hyqcopt.backends import QiskitBackend
import os
import json
from aws_lambda_powertools import Logger

logger = Logger()
backend = QiskitBackend(os.getenv('QISKIT_SIMULATOR', 'aer_simulator'))

def handler(event, context):
    try:
        problem_data = json.loads(event['body'])
        problem = get_problem_class(problem_data['type'])(**problem_data)
        
        qaoa = QAOA(backend, maxiter=100)
        result = qaoa.solve(problem)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'solution': result['solution'].tolist(),
                'energy': result['energy']
            })
        }
    except Exception as e:
        logger.error(f"QAOA Error: {str(e)}")
        return {'statusCode': 500, 'body': 'Processing failed'}

def get_problem_class(problem_type):
    from hyqcopt.problems import TSP, MaxCut  # Dynamic import
    return {'tsp': TSP, 'maxcut': MaxCut}[problem_type]