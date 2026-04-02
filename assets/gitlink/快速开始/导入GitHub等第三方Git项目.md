---
sidebar_label: '导入GitHub等第三方Git项目'      
sidebar_position: 5     
---

# 导入GitHub等第三方Git项目

## 1. 导入项目

在首页选择**导入项目**

![](/img/quickstart/import_homepage.png)

## 2. 填写信息

填写需要导入的第三方Git项目地址和项目信息，如果导入项目为私有仓库，则需输入目标平台用户token进行授权。

![](/img/quickstart/import_info.png)

## 3. 授权验证

在使用GitLink平台导入其他平台（如GitHub、Gitee）的开源项目时，如果项目为私有，则无法通过正常途径导入，需要输入对应平台有权限的token值进行校验。

![](/img/quickstart/import_verify.png)

下面将列举一些典型开源平台的token获取方式。

### GitHub token获取方式

1. 登录GitHub账号

2. 访问用户头像下的settings菜单

   ![img](https://forum.gitlink.org.cn/api/attachments/422328)

3. 访问最下方的Developer settings

   ![img](https://forum.gitlink.org.cn/api/attachments/422329)

4. 在跳转页访问Token（classic），新建一个classic token（若已保存token）

   ![img](https://forum.gitlink.org.cn/api/attachments/422362)

5. 在token配置页面，输入token用途，并确保该token已勾选“repo”选项，否则将导入失败

   ![img](https://forum.gitlink.org.cn/api/attachments/422364)

   点击创建按钮

   ![img](https://forum.gitlink.org.cn/api/attachments/422366)

6. 复制该token

   ![img](https://forum.gitlink.org.cn/api/attachments/422368)

   并将该token输入至GitLink导入项目认证填写框

   ![img](https://forum.gitlink.org.cn/api/attachments/422376)

### Gitee token获取方式

1. 登录Gitee账号

2. 访问用户头像下的设置菜单

   ![img](https://forum.gitlink.org.cn/api/attachments/422333)

3. 访问“安全设置”栏下方“私人令牌”菜单

   ![img](https://forum.gitlink.org.cn/api/attachments/422334)

4. 点击生成新令牌，并在令牌生成页面配置令牌名称，并确保令牌已勾选“project”权限选项，并保存该令牌

   ![img](https://forum.gitlink.org.cn/api/attachments/422371)

   ![img](https://forum.gitlink.org.cn/api/attachments/422370)

5. 在令牌生成成功的弹窗，复制该令牌，并将该token输入至GitLink导入项目认证填写框

   ![img](https://forum.gitlink.org.cn/api/attachments/422374)

   ![img](https://forum.gitlink.org.cn/api/attachments/422375)

## 4. 导入成功

提示正在从第三方Git项目地址迁移

![](/img/quickstart/import_wait.png)

迁移成功则导入项目成功

![](/img/quickstart/import_success.png)