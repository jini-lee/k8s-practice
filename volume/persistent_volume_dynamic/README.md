# 쿠버네티스 EBS 동적 프로비저닝 PersistentVolum 예제
StorageClass 리소스를 타입별로 하나 이상 생성해두면 
적절한 타입의 StroageClass를 참조하는 PVC를 생성할 때 쿠버네티스는 프로비저너(해당 예제는 kubernetes.io/aws-ebs)에게
PVC로 요청된 접근 모드, 스토리지 용량 등의 파라미터를 기반으로 퍼시스턴트 스토리지와 PV를 프로비저닝하도록 요청한다. 


### StorageClass 생성
```
$ kubectl create -f ebs-gp2-sc.yaml 
```

### PersistentVolumeClaim 생성 

```
$ kubectl create -f pvc.yaml 
```

### 동적 프로비저닝된 PV, PVC 확인
``` 
$ kubectl get mongodb-pvc
$ kubectl get pv 
```
