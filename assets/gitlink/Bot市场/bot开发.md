---
sidebar_label: 'bot开发'     
sidebar_position: 3     
---
import MyButton from './mybutton';

<MyButton onClick={() => {
var pElements = document.getElementsByTagName('p'); 
var hElements = document.getElementsByTagName('h1'); 
var hzh = ['bot开发','bot开发'];
var hen = ['Bot Development','Bot Development'];
var zhtranalate = ['Bot开发是开发者进行bot注册的重要模块。' , '在个人“设置”中，用户可以看到目前已经注册的bot列表，点击对应bot的“编辑”按钮可以对已注册的bot进行配置；点击“Bot注册”按钮开始注册新的bot。' , '' , '在注册页中，开发者需要填写bot注册的相关信息，包括bot的名称、Webhook 地址，详细介绍等，系统将对开发者输入的信息进行合法性校验，确保bot各项信息的完整性和有效性。此外，系统将自动生成bot的唯一标识，同时调用 GitLink 平台的相关接口生成bot的身份凭证信息，包括客户端密钥和私钥等。' , '开发者需通过这些身份信息结合平台接口进行bot身份认证后，调用相关接口完成bot的相关功能。' , '平台开发API链接（待完善）：https://www.gitlink.org.cn/docs/api#introduction' , '' , '' , '©Copyright 2024 CCF 开源发展委员会' , 'Powered by Trustie& IntelliDE 京ICP备13000930号'];
var entranslate = ['Bot development is an important module for developers to register their bots.' , 'In personal settings, users can see a list of registered bots and click the "Edit" button on the corresponding bot to configure the registered bots; Click the "Bot Registration" button to start registering a new bot.' , '' , 'In the registration page, developers need to fill in the relevant information for bot registration, including the name of the bot, Webhook address, detailed introduction, etc. The system will verify the legality of the information entered by the developer to ensure the completeness and validity of all bot information. In addition, the system will automatically generate a unique identifier for the bot, and call the relevant interfaces of the GitLink platform to generate the identity credential information of the bot, including the client key and private key.' , 'Developers need to use these identity information in combination with the platform interface for bot identity authentication, and then call the relevant interface to complete the relevant functions of the bot.' , 'Platform development API link (to be improved): https://www.gitlink.org.cn/docs/api#introduction' , '' , '' , '© Copyright 2024 CCF Open Source Development Committee' , 'Powered by Trust&IntelliDE Beijing ICP Preparation No. 13000930'];
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

# Bot开发

Bot开发是开发者进行bot注册的重要模块。

在个人“设置”中，用户可以看到目前已经注册的bot列表，点击对应bot的“编辑”按钮可以对已注册的bot进行配置；点击“Bot注册”按钮开始注册新的bot。

![botcreate1](../../static/img/bot/botcreate1.png)

在注册页中，开发者需要填写bot注册的相关信息，包括bot的名称、Webhook 地址，详细介绍等，系统将对开发者输入的信息进行合法性校验，确保bot各项信息的完整性和有效性。此外，系统将自动生成bot的唯一标识，同时调用 GitLink 平台的相关接口生成bot的身份凭证信息，包括客户端密钥和私钥等。

开发者需通过这些身份信息结合平台接口进行bot身份认证后，调用相关接口完成bot的相关功能。

平台开发API链接（待完善）：https://www.gitlink.org.cn/docs/api#introduction

![botcreate2](../../static/img/bot/botcreate2.png)

![botcreate3](../../static/img/bot/botcreate3.png)