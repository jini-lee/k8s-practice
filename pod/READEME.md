## liveness probe 예제
해당 manifest는 initialDealySeconds가 30으로 설정되어 있어,
쿠버네티스는 컨테이너 생성 후 첫 번째 프로브 실행까지 30초를 대기한다.
이후 프로브를 실행하고 10번의 요청후 의도적으로 500을 응답해 파드의 상태를 확인할 수 있다.

### pod apply
```
$ kubectl apply -f liveness_probe.yaml
```

### pod 상태 확인
도커의 이미지는 10번의 요청 후엔 500을 응답하므로,
10번 새로고침 후 파드 상태를 확인
```
$ kubectl get po unhealthy
``` 

