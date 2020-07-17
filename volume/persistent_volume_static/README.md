# 쿠버네티스 EBS 정적프로비저닝 PersistentVolum 예제
AWS Elastic Block Storage를 미리 프로비저닝 한 상태에서 진행해야한다.
생성된 EBS volumeID를 PersistentVolume의 manifest에 등록해야한다.


### PersistentVolume, PersistentVolumeClaim apply 
```
$ kubectl create -f mongodb-pv-ebs.yaml
$ kubectl create -f mongodb-pvc.yaml

# pvc가 생성될 때 적절한 pv가 있는지 찾고 클레임에 바인딩한다.
```

### pod apply

```
$ kubectl apply -f pod.yaml
```

### mongodb 접속 후 데이터를 써보고 pod, pvc, pv 삭제후 재생성 후 데이터 확인
``` 
$ kubectl exec -it mongodb mongo
> db.foo.insert({"bar": "test"})

$ kubectl delete -f ./ 
$ kubectl apply -f ./

$ kubectl exec -it mongodb mongo
> db.foo.find()
```

### 리클레임 정책
예제에서 리클레임 정책을 Retain으로 하여 클레임이 해제돼도 볼륨과 컨텐츠가 유지된다.
하지만 PV가 이미 PVC에 바인딩 되었기 때문에 PVC를 삭제한 후  PVC를 재생성하더라도
처음과 같이 바인딩 되지 않는다. 수동으로 PV를 재사용하는 유일한 방법은 PV를 삭제 한 후 다시 생성해야 PVC에 바인딩된다.  
