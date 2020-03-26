#!/usr/local/homebrew/bin/python3
# -*- coding:utf-8 -*-

import os

file_ls = ["001-01-课程介绍",
           "002-02-云服务的三种模式",
           "003-03-saas的概述",
           "004-04-什么是saashrm",
           "005-05-原型分析法与用例图",
           "006-06-Power Designer介绍",
           "007-07-Power Designer绘制用例图",
           "008-08-系统设计",
           "009-09-api文档",
           "010-10-工程搭建：前置知识点和开发环境要求",
           "011-11-工程搭建：搭建父工程",
           "012-12-工程搭建：搭建子工程之搭建环境构造返回实体类",
           "013-13-工程搭建：搭建子工程之分布式id生成器",
           "014-14-工程搭建：搭建子工程之搭建实体类模块和lombok插件",
           "015-15-企业微服务：搭建环境",
           "016-16-企业微服务：实现crud操作之创建实体类",
           "017-17-企业微服务：实现crud操作之dao接口",
           "018-18-企业微服务：实现crud操作之service",
           "019-19-企业微服务：实现crud操作之保存企业",
           "020-20-企业微服务：实现crud操作之删除更新查询企业",
           "021-21-企业微服务：使用postman测试接口",
           "022-01-内容介绍",
           "023-02-多租户以及基于多租户的数据库设计需求",
           "024-03-多租户数据库设计方法：独立数据库，共享schema",
           "025-04-多租户数据库设计方法：独立数据库",
           "026-05-多租户数据库设计方法：共享数据库表",
           "027-06-数据库设计：三范式",
           "028-07-数据库设计：反三范式",
           "029-08-数据库设计：pd工程创建数据库表-上",
           "030-09-数据库设计：pd工程创建数据库表-下",
           "031-10-脚手架工程：介绍安装",
           "032-11-脚手架工程：工程目录结构",
           "033-12-前端框架：执行流程分析之路由与菜单",
           "034-13-前端框架：发送请求获取数据的执行逻辑",
           "035-14-前端框架：mockjs模拟数据",
           "036-15-前端企业管理：搭建环境",
           "037-16-前端企业管理：配置API",
           "038-17-企业列表：构造数据",
           "039-18-企业列表：构造页面",
           "040-19-企业列表：构造序号和专改列",
           "041-20-企业详情：配置路由构造页面",
           "042-21-企业详情：构造数据",
           "043-22-企业详情：完成企业详情展示",
           "044-23-前后端联合测试",
           "045-24-总结",
           "046-01-内容介绍与组织机构管理的需求分析",
           "047-02-部门微服务：开发步骤与实体类",
           "048-03-部门微服务：基本dao和service代码编写",
           "049-04-部门微服务：保存部门",
           "050-05-部门微服务：查询企业列表",
           "051-06-部门微服务：部门的修改和删除",
           "052-07-部门微服务：抽取公共代码和测试",
           "053-08-部门前端：构造模块",
           "054-09-部门前端：编写请求API",
           "055-10-部门前端：构造数据",
           "056-11-部门前端：构造部门树形列表",
           "057-12-部门前端：美化树形列表",
           "058-13-部门前端：构造添加部门弹出框",
           "059-14-部门前端：添加和修改部门",
           "060-15-部门前端：页面优化以及抽取组件",
           "061-16-RBAC模型：设计思路",
           "062-17-RBAC模型：表设计分析",
           "063-18-SaaS权限控制：需求分析",
           "064-19-SaaS权限控制：设计思路和表分析",
           "065-20-用户管理：搭建系统微服务",
           "066-21-用户管理：实体类介绍",
           "067-22-用户管理：用户dao和service代码",
           "068-23-用户管理：controller代码",
           "069-24-用户管理：构造前端页面",
           "070-25-用户管理：构造前端页面-下",
           "071-26-总结",
           "072-01-角色管理与今日内容介绍",
           "073-02-权限基本操作：实体类和dao",
           "074-03-权限基本操作：api介绍和基本service与controller",
           "075-04-权限基本操作：权限的更新和保存",
           "076-05-权限基本操作：查询列表",
           "077-06-权限基本操作：根据id查询和删除",
           "078-07-权限基本操作：测试权限的操作",
           "079-08-分配角色：需求分析",
           "080-09-分配角色：代码实现",
           "081-10-分配权限：代码实现",
           "082-11-分配权限，分配角色：测试",
           "083-11-分配权限，分配角色：页面回显",
           "084-12-常见认证机制-上",
           "085-13-常见认证机制-下",
           "086-14-jwt：介绍以及创建token",
           "087-15-jwt：token的解析",
           "088-16-jwt：自定义claims设置数据",
           "089-17-hrm中的jwt认证：构造工具类",
           "090-18-hrm中的jwt认证：需求分析与用户登录-上",
           "091-19-hrm中的jwt认证：用户登录-下",
           "092-20-hrm中的jwt认证：获取用户数据-上",
           "093-21-hrm中的jwt认证：token校验获取用户数据",
           "094-22-总结",
           "095-01-今日内容介绍以及前端权限控制需求分析",
           "096-02-前端权限控制：获取用户信息接口构造数据",
           "097-03-前端权限控制：前端菜单控制",
           "098-04-前端权限控制：实现思路分析-待修改",
           "099-05-前端权限控制：按钮的权限控制",
           "100-06-有状态服务和无状态服务",
           "101-07-有状态服务和无状态服务的区别与联系",
           "102-08-基于jwt的用户鉴权：拦截器概述",
           "103-09-基于jwt的用户鉴权：使用拦截器统一处理claims",
           "104-10-基于jwt的用户鉴权：配置拦截器并测试",
           "105-11-基于JWT的API权限校验：需求分析",
           "106-12-基于JWT的API权限校验：代码实现",
           "107-13-基于JWT的API权限校验：测试",
           "108-14-shiro介绍",
           "109-15-shiro的内部体系结构",
           "110-16-shiro认证与授权：基于ini的用户认证",
           "111-17-shiro认证与授权：基于ini的用户授权",
           "112-18-shiro认证与授权：自定义realm-上",
           "113-19-shiro认证与授权：自定义realm-中",
           "114-20-shiro认证与授权：自定义realm-下",
           "115-21-shiro认证与授权：执行流程分析",
           "116-01-今日内容介绍与案例介绍",
           "117-02-Shiro与Springboot整合：配置依赖改造登录方法",
           "118-03-自定义realm：认证的操作步骤分析",
           "119-04-自定义realm：实现认证逻辑",
           "120-05-自定义realm：实现授权逻辑",
           "121-06-Shiro与Springboot整合：配置-上",
           "122-07-Shiro与Springboot整合：配置-下",
           "123-08-Shiro与Springboot整合：测试",
           "124-09-shiro鉴权：通过过滤器鉴权",
           "125-10-shiro鉴权：通过注解鉴权",
           "126-11-shiro的会话管理：介绍",
           "127-12-shiro的会话管理：应用场景分析",
           "128-13-Shiro结合redis的统一会话管理：自定义会话管理器",
           "129-14-Shiro结合redis的统一会话管理：配置会话管理器",
           "130-15-Shiro结合redis的统一会话管理：测试与总结",
           "131-16-SasSHRM中基于shiro的认证授权：需求分析",
           "132-17-SasSHRM中基于shiro的认证授权：环境搭建",
           "133-18-SasSHRM中基于shiro的认证授权：登录改造",
           "134-19-SasSHRM中基于shiro的认证授权：自定义realm-认证",
           "135-20-SasSHRM中基于shiro的认证授权：自定义realm-授权",
           "136-21-SasSHRM中基于shiro的认证授权：系统微服务配置shiro(需修改)",
           "137-22-SasSHRM中基于shiro的认证授权：测试认证",
           "138-23-SasSHRM中基于shiro的认证授权：用户授权",
           "139-01-员工管理需求和表说明",
           "140-02-员工管理基本代码的说明",
           "141-03-微服务发现组件Eureka：简介以及Eureka服务端开发",
           "142-04-微服务发现组件Eureka：微服务注册",
           "143-05-微服务调用组件Feign：简介以及搭建环境",
           "144-06-微服务调用组件Feign：案例测试",
           "145-07-报表的概述",
           "146-08-POI的概述",
           "147-09-POI的入门：概述和创建EXCEL",
           "148-10-POI的入门：创建单元格设置数据",
           "149-11-POI的入门：单元格样式处理",
           "150-12-POI的入门：绘制图形",
           "151-13-POI的入门：加载解析Excel-上",
           "152-14-POI的入门：加载解析Excel-下",
           "153-15-POI文件导入：需求说明",
           "154-16-POI文件导入：代码实现-解析Excel构造用户列表",
           "155-17-POI文件导入：代码实现-批量保存用户列表",
           "156-18-POI文件导入：跨服务器调用查询部门信息",
           "157-19-POI文件导入：总结",
           "158-01-课程介绍与POI导出人事报表：需求说明",
           "159-02-POI导出人事报表：代码实现-上",
           "160-03-POI导出人事报表：代码实现-下",
           "161-04-模板打印：概述",
           "162-05-模板打印：代码实现-加载模板抽取公共样式",
           "163-06-模板打印：代码实现和总结",
           "164-07-自定义工具类：工具类介绍",
           "165-08-自定义工具类：工具类测试",
           "166-09-自定义工具类：导入工具类测试",
           "167-10-百万数据报表：概述",
           "168-11-百万数据报表：导出测试",
           "169-12-百万数据报表：分析以及解决办法",
           "170-13-百万数据报表导出：需求以及思路分析",
           "171-14-百万数据报表导出：使用SXSSFWorkbook完成百万数据报表打印",
           "172-15-百万数据报表导出：原理分析与总结",
           "173-16-百万数据报表读取：需求分析",
           "174-17-百万数据报表读取：解决方案及原理分析",
           "175-18-百万数据报表读取：步骤分析以及自定义时间处理器",
           "176-19-百万数据报表读取：代码实现及测试",
           "177-20-百万数据报表读取：代码实现以及总结",
           "178-01-图片上传：课程介绍与需求说明",
           "179-02-DataURL：概述",
           "180-03-DataURL：实现原理及优缺点分析",
           "181-04-DataURL：实现员工头像保存",
           "182-05-DataURL：员工头像回显",
           "183-06-七牛云存储：概述和申请账号的说明",
           "184-07-七牛云存储：通过SDK上传图片",
           "185-08-七牛云存储：更新图片和访问图片",
           "186-09-七牛云存储：断点续传",
           "187-10-七牛云存储：实现员工头像保存",
           "188-11-JasperReport：概述",
           "189-12-JasperReport：声明周期",
           "190-13-JasperReport：开发步骤总结",
           "191-14-Jaspersoft Studio：介绍和安装",
           "192-15-Jaspersoft Studio：创建工程以及模板结构介绍",
           "193-16-Jaspersoft Studio：创建第一个案例模板",
           "194-17-Jaspersoft Studio：整合springboot搭建环境",
           "195-18-Jaspersoft Studio：配置controller输出PDF文件",
           "196-19-Jaspersoft Studio：中文乱码处理以及总结",
           "197-01-人工智能：内容介绍与人工智能的概述",
           "198-02-人工智能：基于人工智能的人脸登录介绍",
           "199-03-百度云AI：概述",
           "200-04-百度云AI：账号注册以及注册应用",
           "201-05-百度云API入门：搭建环境",
           "202-06-百度云API入门：人脸注册",
           "203-07-百度云API入门：人脸检测",
           "204-08-百度云API入门：人脸搜索",
           "205-09-百度云API入门：人脸更新",
           "206-10-刷脸登录：需求分析",
           "207-11-二维码生成：通过zxing生成二维码到本地",
           "208-12-二维码生成：通过zxing生成dataUrl的二维码",
           "209-13-刷脸登录：搭建环境-上",
           "210-14-刷脸登录：搭建环境-下",
           "211-15-刷脸登录：功能介绍和人脸注册",
           "212-16-刷脸登录：生成二维码",
           "213-17-刷脸登录：轮询查询二维码登录状态",
           "214-18-刷脸登录：人脸检测",
           "215-19-刷脸登录：人脸登录",
           "216-20-刷脸登录：构造前端工程",
           "217-21-刷脸登录：测试以及总结",
           "218-01-代码生成器概述：内容介绍",
           "219-02-代码生成器概述：需求分析",
           "220-03-代码生成器概述：实现思路",
           "221-04-FreeMarker：概述",
           "222-05-FreeMarker的入门：入门案例",
           "223-06-FreeMarker的入门：字符串模板",
           "224-07-FreeMarker的模板：概述和数据模型",
           "225-08-FreeMarker的模板：if指令和list指令",
           "226-09-FreeMarker的模板：include和assign指令",
           "227-10-元数据：概述",
           "228-11-DataBaseMetaData元数据：获取数据库基本信息",
           "229-12-DataBaseMetaData元数据：获取所有数据库名称",
           "230-13-DataBaseMetaData元数据：获取指定数据库的表信息",
           "231-14-DataBaseMetaData元数据：获取指定数据库表中的字段属性",
           "232-15-ParameterMetaData元数据：获取参数个数",
           "233-16-ResultSetMetaData元数据：获取查询结果的字段信息",
           "234-17-构造代码生成器环境：需求分析",
           "235-18-构造代码生成器环境：实体类和工具类介绍",
           "236-19-构造代码生成器环境：配置界面",
           "237-01-代码生成器之数据模型：概述与需求分析",
           "238-02-代码生成器之数据模型：处理自定义properties数据",
           "239-03-代码生成器之元数据处理：操作步骤分析",
           "240-04-代码生成器之元数据处理：代码实现-上",
           "241-05-代码生成器之元数据处理：代码实现-下（需要修改）",
           "242-06-代码生成器的实现：需求分析",
           "243-07-代码生成器的实现：程序入口GeneratorFacade",
           "244-08-代码生成器的实现：测试GeneratorFacade获取数据模型",
           "245-09-代码生成器的实现：核心处理类Generator的介绍",
           "246-10-代码生成器的实现：核心处理类Generator的实现-上",
           "247-11-代码生成器的实现：核心处理类Generator的实现-中",
           "248-12-代码生成器的实现：核心处理类Generator的实现-下",
           "249-13-模板制作：需求分析",
           "250-14-模板制作：项目路径处理",
           "251-15-模板制作：实体类模板",
           "252-16-模板制作：持久层模板",
           "253-17-模板制作：业务层模板",
           "254-18-模板制作：视图层模板",
           "255-19-代码生成器：测试",
           "256-20-代码生成器：总结"]


def func(path):
    files = []
    for i in os.listdir(path):
        path2 = os.path.join(path, i)  # 拼接绝对路径
        if os.path.isdir(path2):  # 判断如果是文件夹,调用本身
            func(path2)
        else:
            files.append(i)
    return files


# file_path = "/Users/zing/Movies/test/"
file_path = "/Users/zing/Movies/springboot/"
if __name__ == '__main__':
    file_name = func(file_path)
    file_name.sort()
    for name in file_name:
        index = name[0:3]
        for real_name in file_ls:
            if real_name.startswith(index):
                os.rename(file_path + name, file_path + real_name + ".flv")
    # for i in file_ls:
    # print(i)
