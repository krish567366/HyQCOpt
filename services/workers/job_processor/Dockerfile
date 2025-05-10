FROM public.ecr.aws/lambda/python:3.9

# Install core HyQCOpt
COPY ../../core /var/task/core
RUN pip install -e /var/task/core

# Install quantum backends
RUN pip install qiskit-aws braket-sdk

# Copy processor code
COPY app.py ./

CMD ["app.lambda_handler"]