# dockerfile

## sshd

``` 
docker build -t sshd:v1 -f Dockerfile.sshd --build-arg PASSWORD=12345678  .
```

```
docker run -d --name sshd -p 10022:22 sshd:v1
```

```
ssh root@localhost -p 10022
```