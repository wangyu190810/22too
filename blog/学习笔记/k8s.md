# k8s 笔记

目前大多数服务都上了k8s用来做资源的整合

记录一下常用的k8s操作

## k8s 配置文件操作
基本配置都在k8sdenmo 文件夹下有一个最基本的k8s服务

### 整体流程

* 项目本身的Dockerfile 文件用来定义对应的服务
* 打包docker 镜像，用来供应给下游使用
* 创建myweb-rc.yaml 服务，用来对docker镜像管理和启动
* 创建myweb-svc.yaml 服务，用来对k8s的对外端口进行管理

具体执行，已经写入到build.ps1 文件中

## k8s 服务操作

### 常用命令

```shell

# 查看当前的名命空间
kubectl get ns

#创建一个环境叫做 test的命名空间
kubectl create ns test

# 切换环境到test命名空间
kubectl  config set-context --current --namespace=test

# 查看当前的命名空间下的pods，默认为defaluth环境
kubectl get pods

#合并当前的服务到一个yaml文件下
kubectl kustomize k8s/overlays/dev > gen-deployment.yaml

```



