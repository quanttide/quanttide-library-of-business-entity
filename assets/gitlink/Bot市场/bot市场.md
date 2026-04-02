import MyButton from './mybutton';

{
var pElements = document.getElementsByTagName('p');
var hElements = document.getElementsByTagName('h1');
var hzh = ['bot市场','bot市场'];
var hen = ['Bot Market','Bot Market'];
var zhtranalate = ['Bot市场是进行Bot分享与复用的重要模块，主要包括bot的搜索发现，详情查看等功能。','Bot市场主页中展示了目前所有已经上架市场的bot简要信息，包括bot的头像，名称，开发者，简介和安装次数等信息，用户可根据这些基本信息初步判断该bot是否符合自己的项目需求。','在bot市场主页中，用户可以选择指定的bot种类，筛选出特定分类的bot，在这个种类范围内进行搜索与选择。','此外，用户通过在搜索栏中输入关键字进行搜索，可检索出内容包含指定关键字的相关bot。','用户可结合种类筛选和关键字搜索缩小范围，在市场中快速找到符合项目相关需求的bot。','','在bot市场页中，用户点击指定的bot卡片即可进入该bot的详情页。Bot的详情页包含bot的头像，名称，开发者，种类和详细介绍等信息，用户可在此掌握该bot的各项介绍，进一步判断是否将其安装到指定仓库中。','','在bot详情页中，若用户认为该bot满足自己的项目需求，可点击“安装此Bot”按钮，了解该bot的权限信息，将其安装到指定的仓库中，关于安装的更多介绍可见“Bot安装”部分。','去市场看看吧！','©Copyright 2024 CCF 开源发展委员会','Powered by Trustie& IntelliDE 京ICP备13000930号'];
var entranslate = ['The bot market is an important module for sharing and reusing bots, mainly including functions such as searching, discovering, and viewing details of bots.' , 'The Bot Market homepage displays brief information about all bots that have been put on the market, including their avatars, names, developers, introductions, and installation times. Users can use this basic information to preliminarily determine whether the bot meets their project requirements.' , 'On the bot market homepage, users can select a specific type of bot, filter out specific categories of bots, and search and select within this category range.' , 'In addition, users can search for relevant bots containing specified keywords by entering keywords in the search bar.' , 'Users can combine category filtering and keyword search to narrow down the scope and quickly find bots that meet project related needs in the market.' , '' , 'In the bot market page, users can click on the specified bot card to enter the details page of the bot. The details page of the bot includes information such as the bot avatar, name, developer, type, and detailed introduction. Users can grasp the various introductions of the bot here and further determine whether to install it in the designated warehouse.' , '' , 'In the bot details page, if users believe that the bot meets their project requirements, they can click the "Install this bot" button to learn about the bots permission information and install it in the designated warehouse. For more information on installation, please refer to the "Bot Installation" section' , 'Go take a look at the market!' , '©Copyright 2024 CCF Open Source Development Committee' , 'Powered by Trustie& IntelliDE 京ICP备13000930号'];
if (pElements[0].innerText == zhtranalate[0]){
for (var i = 0; i 中/英

# Bot市场

Bot市场是进行Bot分享与复用的重要模块，主要包括bot的搜索发现，详情查看等功能。

Bot市场主页中展示了目前所有已经上架市场的bot简要信息，包括bot的头像，名称，开发者，简介和安装次数等信息，用户可根据这些基本信息初步判断该bot是否符合自己的项目需求。

在bot市场主页中，用户可以选择指定的bot种类，筛选出特定分类的bot，在这个种类范围内进行搜索与选择。

此外，用户通过在搜索栏中输入关键字进行搜索，可检索出内容包含指定关键字的相关bot。

用户可结合种类筛选和关键字搜索缩小范围，在市场中快速找到符合项目相关需求的bot。

![botmarket1](../../static/img/bot/botmarket1.png)

在bot市场页中，用户点击指定的bot卡片即可进入该bot的详情页。Bot的详情页包含bot的头像，名称，开发者，种类和详细介绍等信息，用户可在此掌握该bot的各项介绍，进一步判断是否将其安装到指定仓库中。

![botmarket2](../../static/img/bot/botmarket2.png)

在bot详情页中，若用户认为该bot满足自己的项目需求，可点击“安装此Bot”按钮，了解该bot的权限信息，将其安装到指定的仓库中，关于安装的更多介绍可见“Bot安装”部分。

去市场看看吧！

{
location.href = "https://www.gitlink.org.cn/softbot";
}}>Bot市场
