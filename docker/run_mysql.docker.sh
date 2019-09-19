#1 下载镜像 docker pull [option] name[:tag][@DIGEST]
#文档 https://hub.docker.com/_/mysql?tab=description
#mysql 就是
docker pull mysql:5.7

#运行mysql
#讲解：-p 内部端口映：映射主机的端口 -name 运行实例名称 -e MYSQL_ROOT_PASSWORD= 设置的mysql root用户密码 -d 运用的镜像
docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:5.7