# MacDash

## Getting Started
```
pip install -r requirements.txt
```

Make a copy of `example_config.py` and change the filename to `config.py`.

```
cp example_config.py config.py
```

Set values for the following keys:
```
JSS_RESOURCE_BASE_URL
JSS_USERNAME
JSS_PASSWORD
```
### Use With Docker
Create the base vm for Docker to run on
```
docker-machine create -d virtualbox macdash
```

Make sure docker-machine knows which vm to use
```
eval $(docker-machine env macdash)
```

Build the Docker containers with docker-compose. This is based on settings in docker-compose.yml
```
docker-compose build
```

Start the various docker containers
```
docker-compose up -d
```
