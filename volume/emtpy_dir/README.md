# 쿠버네티스 볼륨 예제

## 일시적인 데이터를 저장하는 데 사용되는 간단한 빈 디렉토리인 emtpyDir 예제

### 도커빌드, 이미지 저장소에 push
```
$ docker build -t zaddyjini/emptydir .
$ docker push zaddyjini/emptydir
```

### pod apply

```
$ kubectl apply -f pod.yaml
```

### 포트 포워딩을 통한 파드 접근, 메시지 확인
``` 
$ kubectl port-forward emptydir 8080:80
$ curl http://localhost:8080
```
