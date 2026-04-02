---
sidebar_label: 'bot配置'      
sidebar_position: 2    
---
import MyButton from './mybutton';

<MyButton onClick={() => {
var pElements = document.getElementsByTagName('p'); 
var hElements = document.getElementsByTagName('h1'); 
var hzh = ['bot配置','bot配置'];
var hen = ['Bot Configure','Bot Configure'];
var zhtranalate = ['Bot配置是开发者进行bot维护和配置的重要模块，主要包括bot基本信息维护、权限&订阅事件管理、高级选项配置等功能。','Bot的基本信息维护中，开发者可以看到bot的各项基本信息，并可以根据需要对bot的头像，名称，Webhook地址等进行修改。','','Bot的权限&订阅事件管理中，开发者可根据对仓库资源的访问需要为bot分配不同的权限和等级，比如增加代码库权限，将拉取请求的写权限变为读权限等。开发者还能更改当前bot订阅的事件列表，比如订阅代码库推送，取消拉取请求分配订阅等，以实现bot功能的更新与升级。','','Bot高级选项配置中，开发者可以改变bot的公私有状态，从而影响到bot的使用范围。需要注意的是，公开状态下的bot在已有其他仓库安装的情况下不能变成私有。开发者可选择将bot上架到市场，需要填写上架信息，包括市场简介，主要功能，次要功能等各项信息。','开发者还能进行bot的删除和转让操作，发起转让意味着更改bot的所有权，需要输入接受者的用户名。在接受者确定接受后，即可完成bot的所有权变更，拒绝则会取消本次的转让操作。','','©Copyright 2024 CCF 开源发展委员会','Powered by Trustie& IntelliDE 京ICP备13000930号'];
var entranslate = ['Bot configuration is an important module for developers to maintain and configure bots, mainly including basic bot information maintenance, permission&subscription event management, advanced option configuration, and other functions.' , 'In the basic information maintenance of bots, developers can see various basic information of bots and modify their avatars, names, Webhook addresses, etc. as needed.' , '' , 'In the permission and subscription event management of bots, developers can assign different permissions and levels to bots based on their access needs to warehouse resources, such as adding code library permissions, changing write permissions for pull requests to read permissions, etc. Developers can also modify the event list of the current bot subscription, such as subscribing to code library push notifications, canceling pull request allocation subscriptions, etc., to achieve updates and upgrades of bot functionality.' , '' , 'In the advanced options configuration of bots, developers can change the public and private status of bots, thereby affecting their usage scope. It should be noted that bots in public status cannot become private when installed in other warehouses. Developers can choose to put their bots on the market and need to fill in the listing information, including market introduction, main functions, secondary functions, and other related information.' , 'Developers can also perform bot deletion and transfer operations, initiating transfer means changing the ownership of the bot, and the recipients username needs to be entered. After the recipient confirms acceptance, the ownership change of the bot can be completed. Refusal will cancel the transfer operation.' , '' , '© Copyright 2024 CCF Open Source Development Committee' , 'Powered by Trust&IntelliDE Beijing ICP Preparation No. 13000930'];
if (pElements[0].innerText == zhtranalate[0]){
  for (var i = 0; i < pElements.length; i++) {  
    if (pElements[i].innerText != ''){
      if (i < pElements.length){
        pElements[i].innerText = entranslate[i];  
      }
    }
}
}
else{
  for (var i = 0; i < pElements.length; i++) {  
    if (pElements[i].innerText != ''){
      if (i < pElements.length){
        pElements[i].innerText = zhtranalate[i];  
      }
    }
}
}
if (hElements[0].innerText == hzh[0]){
  for (var i = 0; i < hElements.length; i++) {  
    if (hElements[i].innerText != ''){
      if (i < hElements.length){
        hElements[i].innerText = hen[i];  
      }
    }
}
}
else{
  for (var i = 0; i < hElements.length; i++) {  
    if (hElements[i].innerText != ''){
      if (i < hElements.length){
        hElements[i].innerText = hzh[i];  
      }
    }
}
}
}}>中/英</MyButton>

# Bot配置

Bot配置是开发者进行bot维护和配置的重要模块，主要包括bot基本信息维护、权限&订阅事件管理、高级选项配置等功能。

Bot的基本信息维护中，开发者可以看到bot的各项基本信息，并可以根据需要对bot的头像，名称，Webhook地址等进行修改。

![botconfig1](../../static/img/bot/botconfig1.png)

Bot的权限&订阅事件管理中，开发者可根据对仓库资源的访问需要为bot分配不同的权限和等级，比如增加代码库权限，将拉取请求的写权限变为读权限等。开发者还能更改当前bot订阅的事件列表，比如订阅代码库推送，取消拉取请求分配订阅等，以实现bot功能的更新与升级。

![botconfig2](../../static/img/bot/botconfig2.png)


Bot高级选项配置中，开发者可以改变bot的公私有状态，从而影响到bot的使用范围。需要注意的是，公开状态下的bot在已有其他仓库安装的情况下不能变成私有。开发者可选择将bot上架到市场，需要填写上架信息，包括市场简介，主要功能，次要功能等各项信息。

开发者还能进行bot的删除和转让操作，发起转让意味着更改bot的所有权，需要输入接受者的用户名。在接受者确定接受后，即可完成bot的所有权变更，拒绝则会取消本次的转让操作。

![botconfig3](../../static/img/bot/botconfig3.png)
