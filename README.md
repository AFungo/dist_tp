# Networks Final Project

## Commands

### Run airline server:
```bash
python3 run_airline_server.py -i resources/airline_file.json
```

### Run ticket server:
```bash
python3 run_ticket_service_server.py -i resources/ticket_service_file.json
```

### Run client:
```bash
python3 client.py -a ticket_service_address:port
```

### Generate protos
```bash
python -m grpc_tools.protoc -I protos/ --python_out=networking/ticket_service/ --pyi_out=networking/ticket_service --grpc_python_out=networking/ticket_service/ protos/ticket_service.proto

python -m grpc_tools.protoc -I protos/ --python_out=networking/airline/ --pyi_out=networking/airline/ --grpc_python_out=networking/airline protos/airline_service.proto
```

