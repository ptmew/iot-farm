# iot-farm

## Project setup
```
npm install
```

## Build Docker file
```
sudo bash build.sh
```
or
```
docker build -t iot-server:dev .
```

## Run Container
```
sudo bash run.sh
```
or
```
docker run -v ${PWD}:/app -v /app/node_modules -p 8081:8080 --rm iot-server:dev
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
