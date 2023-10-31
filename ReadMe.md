## Example for Python Kafka

##### Run Kafka (external port 9094)
```bash
  cd ./docker/kafka
  docker-compose up -d 
```
You can use broker if available - 45.141.79.89:9094
Then run Consumer And/Or Producer.

#### Consumer
```bash
 python3 main.py consume --topic 'kafka-topic' --kafka '45.141.79.89:9094'
```

#### Producer
```bash
 python3 main.py produce --message 'Hello World' --topic 'kafka-topic' --kafka '45.141.79.89:9094'
```

##### Docker for script
```bash
  docker image build -t pyscript:latest .
  ./script.sh
```

