# Deployment strategy

## simpleapp:v1을 먼저 apply
```
$ kubectl apply -f strategy_deployment.yaml
$ kubectl rollout status deployment simpleapp
Waiting for deployment "simpleapp" rollout to finish: 0 of 3 updated replicas are available...
Waiting for deployment "simpleapp" rollout to finish: 2 of 3 updated replicas are available...
deployment "simpleapp" successfully rolled out
```

## 문제가 있는 app을 update

1. while curl 실행
```
$ while true; do curl ab0a1ea392bbf460db206a199f2d26e3-1306273729.ap-northeast-1.elb.amazonaws.com; done
PYTHON SIMPLE V1!
PYTHON SIMPLE V1!
PYTHON SIMPLE V1!
```

2. 새로운 이미지(unhealthy) 업데이트
```
$ kubectl set image deployment simpleapp pyapp=zaddyjini/unhealthy:1.0
```

3. rollout status, pod 확인
```
$ kubectl rollout status deployment simpleapp
Waiting for deployment "simpleapp" rollout to finish: 1 out of 3 new replicas have been updated...
Waiting for deployment "simpleapp" rollout to finish: 1 out of 3 new replicas have been updated...

$ kubectl get po
simpleapp-9699dd674-5sqhn                           1/1     Running   0          2m46s
simpleapp-9699dd674-ngq6s                           1/1     Running   0          2m46s
simpleapp-9699dd674-wd6lk                           1/1     Running   0          2m46s
simpleapp-c659dbc97-zjt27                           0/1     Running   0          2m13s
```


