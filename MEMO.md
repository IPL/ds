## 运行结果
```commandline
(base) ➜  python git:(main) ✗ make dev-tests
docker-compose build
[+] Building 1.8s (12/12) FINISHED                                                                                               docker:desktop-linux
 => [recruit internal] load build definition from Dockerfile                                                                                     0.0s
 => => transferring dockerfile: 268B                                                                                                             0.0s
 => [recruit internal] load metadata for docker.io/library/python:3.9-alpine                                                                     1.7s
 => [recruit internal] load .dockerignore                                                                                                        0.0s
 => => transferring context: 2B                                                                                                                  0.0s
 => [recruit 1/6] FROM docker.io/library/python:3.9-alpine@sha256:97b255a01c06e7964a57b1c3c67124c99db48de6ba529ef56b1500e4527f5f3c               0.0s
 => [recruit internal] load build context                                                                                                        0.0s
 => => transferring context: 37B                                                                                                                 0.0s
 => CACHED [recruit 2/6] RUN apk add build-base                                                                                                  0.0s
 => CACHED [recruit 3/6] RUN pip install --no-cache-dir --upgrade pip                                                                            0.0s
 => CACHED [recruit 4/6] COPY requirements.txt .                                                                                                 0.0s
 => CACHED [recruit 5/6] RUN pip install --no-cache-dir -r requirements.txt                                                                      0.0s
 => CACHED [recruit 6/6] WORKDIR /srv                                                                                                            0.0s
 => [recruit] exporting to image                                                                                                                 0.0s
 => => exporting layers                                                                                                                          0.0s
 => => writing image sha256:d4d0a7e10f7b0c0fdf9c19a0ff4461a0e9a13efa45ac47537e9cfa7d8c8bb9c5                                                     0.0s
 => => naming to docker.io/recruit/python                                                                                                        0.0s
 => [recruit] resolving provenance for metadata file                                                                                             0.0s
docker-compose --compatibility up -d --remove-orphans
[+] Running 1/0
 ✔ Container recruit_python  Running                                                                                                             0.0s 
docker-compose exec recruit make tests
python -m unittest tests/*.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.015s

OK
```

## 运行环境修改
1. 在Dockerfile中增加RUN apk add build-base。
2. 在Dockerfile中增加pip install upgrade和pip install requirements.txt。
```
diff --git a/python/Dockerfile b/python/Dockerfile
index adde205..4a5bdef 100644
--- a/python/Dockerfile
+++ b/python/Dockerfile
@@ -1,4 +1,9 @@
 FROM python:3.9-alpine
+RUN apk add build-base
 
-WORKDIR /srv
+RUN pip install --upgrade pip
+
+COPY requirements.txt .
+RUN pip install -r requirements.txt
 
+WORKDIR /srv
```


## 单元测试问题
1. 原有的test_greeting只验证返回值的长度大于0，没有检查具体的内容。
2. 考虑到字符串morning和evening的长度相同，所以只检查长度有可能会漏检(False Negative)。
3. 即使修改为检查具体内容，也因为使用的是系统时间，无法同时覆盖三种情况。

### 单元测试改进
综上，进行了扩充，共增加了6个测试用例：
1. 增加了三个方法，分别传入三个时间段的time，检查返回结果。
2. 引入freezegun用于mock时间，增加了三个无参数的测试用例。

## 其他
1. 修改.gitignore文件，增加了对.DS_Store文件的过滤。更完整的Python项目的ignore文件模版在[这里](https://github.com/github/gitignore/blob/main/Python.gitignore)。
2. 增加python/requirements.txt文件，引入freezegun用于在单元测试中mock时间，并指定版本。