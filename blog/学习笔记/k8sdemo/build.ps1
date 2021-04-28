docker build -t ootoo/demo:v1 .
kubectl.exe create -f myweb-svc.yaml
kubectl.exe create -f myweb-rc.yaml

