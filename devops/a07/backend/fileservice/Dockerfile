# Use python3
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app


# Install requirements
RUN pip install -r requirements.txt
RUN wget -qO - https://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add - && echo "deb http://www.rabbitmq.com/debian/ testing main" > /etc/apt/sources.list.d/rabbitmq.list && apt-get update && apt-get install -y --allow-unauthenticated rabbitmq-server && rm -rf /var/lib/apt/lists/* && rabbitmq-plugins enable rabbitmq_management
RUN echo "listeners.tcp.default = 0.0.0.0:5672" > /etc/rabbitmq/rabbitmq.conf
# RUN service rabbitmq-server start && rabbitmqctl add_user test test && rabbitmqctl set_user_tags test administrator && rabbitmqctl set_permissions -p / test ".*" ".*" ".*"

CMD service rabbitmq-server start && rabbitmqctl add_user test test ; rabbitmqctl set_user_tags test administrator ; rabbitmqctl set_permissions -p / test ".*" ".*" ".*" ; nameko run FileService

