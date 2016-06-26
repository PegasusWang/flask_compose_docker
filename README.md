###flask docker
主要是flask应用使用docker集成redis，mongodb，mysql的演示。
可以基于此快速构建一个小型项目开发原型，避免了安装各种数据库的麻烦。


###使用
先安装docker和docker-compose

```
git clone https://github.com/PegasusWang/flask_compose_docker
docker-compose build
docker-compose up
```

访问路由请参考app.py代码。
