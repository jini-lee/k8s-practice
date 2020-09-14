# Deployment

## Apply deployment
```
$ kubectl apply -f deployment
```

## Status of deployment
```
$ kubectl get deployment simpleapp
$ kubectl get po
``` 

## Check web page
```
$ kubectl get svc simpleapp
```
EXTERNAL-IP로 웹에 접속해본다.

## Update
minReadySeconds를 세팅해두고 업데이트 과정을 다소 느리게하여 RollingUpdate를 모니터링할 수 있다.
이는 deployment에 선언되어 있는데 아래 명령어로도 수행할 수 있다.
```
kubectl patch deployment simpleapp -p '{"spec": {"minReadySeconds": 10}}'
```

RollingUpdate를 모니터링하기 위해 curl를 요청하는 루프로 v1 -> v2로 변경되는 과정을 확인한다.
```
$ # 다른 탭에 while curl을 실행해 둔다
$ while true; do curl http://a814daa44364c44e689ecad679818c22-1332074331.ap-northeast-1.elb.amazonaws.com; done
```

kubectl set image로 변경된 이미지를 적용한다.
```
$ kubectl set image deployment simpleapp pyapp=zaddyjini/simpleapp:v2
```

v1만 실행되다가 점차적으로 v2가 스케일업되고 v1은 스케일다운됨을 확인할 수 있다. 최종적으론 v2만 확인이 될 것이다.

