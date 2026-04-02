---
sidebar_label: 'bot安装'
sidebar_position: 1    
---
import MyButton from './mybutton';

<MyButton onClick={() => {
var pElements = document.getElementsByTagName('p'); 
var hElements = document.getElementsByTagName('h1'); 
var aElements = document.getElementsByTagName('a'); 
var hzh = ['bot安装','bot安装'];
var hen = ['Bot Installation','Bot Installation'];
var azh = ['跳到主要内容','','帮助中心','','','','','','','','','','','','','','','','','','','','','机器人(Bot)','编辑此页','上一页 bot市场','下一页bot 配置','网站首页','关于我们','教学实践','合作伙伴','API文档','Git常用命令','引擎使用手册','服务协议','官网邮箱：gitlink@ccf.org.cn','QQ群','公众号'];
var aen = ['Jump to main content','','Help Center','','','','','','','','','','','','','','','','','','','','','Robot (Bot)','Edit this page','last page Bot market','next page Bot configuration','Website homepage','About Us','Teaching practice','Partners','API documentation','Common Git commands','Engine User Manual','Service Agreement','Official website email: gitlink@ccf.org.cn','QQ group','Official Account'];
var zhtranalate = ['Bot安装是进行bot安装和管理控制的重要模块，主要包括bot安装、安装查询、安装管理等功能。','在bot详情页，用户点击“安装此Bot”按钮后，可以看到该bot工作所需的各项权限信息。若用户同意授予bot所需的相关权限即可进行安装。用户可选择将bot安装到所有仓库（用户拥有的所有仓库）中，也可以选择指定的仓库进行安装。','','在个人“设置”或者“仓库设置”中，用户可以看到目前已经安装的Bot情况，点击“配置”按钮可以对bot安装情况进行配置，点击“卸载”按钮可以进行卸载。','','在bot安装配置页中，用户可以掌握该bot的安装位置和工作状态。若用户需要更改bot的工作仓库时，可以进行更改安装位置。bot的工作状态包括激活和挂起，用户可根据需要对bot的状态进行调整，将其挂起或者激活，会影响到bot对仓库数据的访问权限。','','©Copyright 2024 CCF 开源发展委员会','Powered by Trustie& IntelliDE 京ICP备13000930号'];
var entranslate = ['Bot installation is an important module for bot installation and management control, which mainly includes functions such as bot installation, installation queries, and installation management.','On the bot details page, after clicking the "Install this bot" button, users can see the necessary permission information for the bot to work. If the user agrees to grant the necessary permissions to the bot, installation can proceed. Users can choose to install the bot in all warehouses (all warehouses owned by the user) or select a specified warehouse for installation.','','In personal "settings" or "warehouse settings", users can see the current installation status of bots. Click the "configure" button to configure the bot installation status, and click the "uninstall" button to uninstall.','','In the bot installation configuration page, users can grasp the installation location and working status of the bot. If the user needs to change the workspace of the bot, they can change the installation location. The working status of bots includes activation and suspension. Users can adjust the status of bots as needed. Suspending or activating bots can affect their access to warehouse data.','','© Copyright 2024 CCF Open Source Development Committee','Powered by Trust&IntelliDE Beijing ICP Preparation No. 13000930'];
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
if (aElements[0].innerText == azh[0]){
  for (var i = 0; i < aElements.length; i++) {  
    if (aElements[i].innerText != ''){
      if (i < aElements.length){
        aElements[i].innerText = aen[i];  
      }
    }
}
}
else{
  for (var i = 0; i < aElements.length; i++) {  
    if (aElements[i].innerText != ''){
      if (i < aElements.length){
        aElements[i].innerText = azh[i];  
      }
    }
}
}
}}>中/英</MyButton>


# bot安装

Bot安装是进行bot安装和管理控制的重要模块，主要包括bot安装、安装查询、安装管理等功能。 

在bot详情页，用户点击“安装此Bot”按钮后，可以看到该bot工作所需的各项权限信息。若用户同意授予bot所需的相关权限即可进行安装。用户可选择将bot安装到所有仓库（用户拥有的所有仓库）中，也可以选择指定的仓库进行安装。

![botinstall1](../../static/img/bot/botinstall1.png)

在个人“设置”或者“仓库设置”中，用户可以看到目前已经安装的Bot情况，点击“配置”按钮可以对bot安装情况进行配置，点击“卸载”按钮可以进行卸载。

![botinstall2](../../static/img/bot/botinstall2.png)

在bot安装配置页中，用户可以掌握该bot的安装位置和工作状态。若用户需要更改bot的工作仓库时，可以进行更改安装位置。bot的工作状态包括激活和挂起，用户可根据需要对bot的状态进行调整，将其挂起或者激活，会影响到bot对仓库数据的访问权限。

![botinstall3](../../static/img/bot/botinstall3.png)