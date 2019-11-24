# NUAA_ClassSchedule

**Hackathon 2019 East China**  

**Team:**  **看什么看你个小秃头**  

**Author: Tony Huang, Cooook Zhang, Pinyi Qian**

## Description

这是【看什么看你个小秃头】团队的Super_iCal项目，我们实现了通过爬虫登录南京航空航天大学新教务系统，获取课表及考试信息，解析后生成iCal日历及xlsx表格文件，进而导入Outlook等日历。  

>- 话说大家平常是怎么看课表的呀？  
>- **上教务系统** / **截图** / **小程序** / **手动建课表** / **问同学** / ...   
>
>- I have an idea! 大家有没有想过把课表导入到日历呀？！  
>你看，这么做不仅可以**自定义课程**，和其他安排放在一起；  
>还可以利用**桌面插件**，方便快捷地获取课表；  
>还能根据自己的需要**设定提醒**……  
>更多用途可以自由发挥，多棒的主意呢！  
>   
>说实话，这的确就是偶然间想到的一个小想法呢，说干就干，于是就有了这个项目啦！  
>还在犹豫什么呢，不如就来试试吧！嘿嘿嘿~  

**欢迎来围观，欢迎提issue & PR呀！**  



---
## Usage
**食用指南**  

**请在`Python 3`环境下食用**。   

本项目仅能在南航校内账户使用。  

### **Step**

- Step 1   
 进入你喜欢的目录，将本仓库clone到本地，或直接下载`zip`文件（Download ZIP）   
- Step 2  
 进入目录，安装所需的库（Linux下使用pip3，Windows下使用pip）  
```
    pip3 install -r requirements.txt
```

- Step 3  


Windows 环境下：  
```
    python main.py
```

Linux 环境下：  
```
    python3 main.py
```
或者 直接执行main.py （前提是将文件权限设为**可执行**）  
```
    chmod +x *
    ./main.py
```



**命令行参数说明：**  

```
usage: main.py [-h] [-i ID] [-p PWD] [-c {0,1}] [--noexam] [--notxt]
               [--noxlsx]

Get NUAA class schedule at ease! 一个小jio本，让你获取课表更加便捷而实在~

optional arguments:
  -h, --help            show this help message and exit
  -i ID, --id ID        Student ID 学号
  -p PWD, --pwd PWD     Student password 教务处密码
  -c {0,1}, --choice {0,1}
                        Input `0` for personal curriculum(default), `1` for
                        class curriculum. 输入`0`获取个人课表(无此参数默认为个人课表)，输入`1`获取班级课表
  --noexam              Don't export exam schedule. 加入此选项则不导出考试安排
  --notxt               Don't export `.txt` file. 加入此选项则不导出`.txt`文件
  --noxlsx              Don't export `.xlsx` file. 加入此选项则不导出`.xlsx`表格
```

示例：  
```
    python main.py -i <your ID> -p <your password> 
```

同时也支持在控制台输入学号密码啦，且为了保护，密码不带回显，输完之后`<ENTER>`就好啦！  

当然，和上面的初始参数也是互相兼容的，解析的优先级由高到低为：  
命令行参数->代码内的初始设置->控制台输入  


- Step 4  
运行后即可得到解析好的课表啦~   
在`NUAAiCal-Data`目录下就可以看到生成好的`.ics`日历文件，`.txt`文本文件，还有`.xlsx`表格文件啦！  
  
  而且，导出选项可通过命令行参数进行选择。  


- Step 5  
将生成好的`.ics`日历文件导入你喜欢的日历，然后尽情享用吧~！  
**顺手再点个Star吧~**   
**在导入iCal日历前，请确认时区已设定为 `UTC/GMT+08:00` 即北京时间，否则可能会出现导入后时间不正确的情况！**   

    
### **Screenshots 使用截图**    

**使用命令行参数：**  
![V0.10.0.20191116](img/V0.10.0.20191116.png)  

**控制台输入：**  
![V0.4.0.20191026-1](img/V0.4.0.20191026-1.png)  

**使用`.exe`程序执行：**  
![exe](img/exe.png)  
Or 从命令行执行：  
![exe2](img/exe2.png)  

**GUI界面：**

![GUI](img/GUI.png)

**导出`.ics`文件：**   
![successful_export_example](img/successful_export_example.png)  

**将`.ics`导入到Outlook的效果：**   
![Outlook_example.png](img/Outlook_example.png)  

Outlook客户端：  
![Outlook_example_iPad.png](img/Outlook_example_iPad.png)  

**将课表导出到`.xlsx`文件：**  
![xlsx_file](img/V0.8.0.20191112.png)

**导出到文本文件：**

![Export_txt](img/Export_txt.png)

**WEB端部署：**（暂未完成，测试中）  

![image-20191124124120567](img/Web.png)

### Raw Data

课表解析部分原始JavaScript数据片段：   

```javascript
var teachers = [{id:2270,name:"任艳芳",lab:false}];
var actTeachers = [{id:2270,name:"任艳芳",lab:false}];
var assistant = _.filter(actTeachers, function(actTeacher) {
    return (_.where(teachers, {id:actTeacher.id,name:actTeacher.name,lab:actTeacher.lab}).length == 0) && (actTeacher.lab == true);
});
var assistantName = "";
if (assistant.length > 0) {
    assistantName = assistant[0].name;
    actTeachers = _.reject(actTeachers, function(actTeacher) {
        return _.where(assistant, {id:actTeacher.id}).length > 0;
    });
}
var actTeacherId = [];
var actTeacherName = [];
for (var i = 0; i < actTeachers.length; i++) {
    actTeacherId.push(actTeachers[i].id);
    actTeacherName.push(actTeachers[i].name);
}

    activity = new TaskActivity(
        actTeacherId.join(','),
            actTeacherName.join(','),
            "8340",
            "信息检索与利用",
            "548",
            "10302(将军路)",
            "00000011111110000000000000000000000000000000000000000",
            "",
            null,
            assistantName,
            "",
            "",
            "");
    index =0*unitCount+8;
    table0.activities[index][table0.activities[index].length]=activity;
    index =0*unitCount+9;
    table0.activities[index][table0.activities[index].length]=activity;
    
```

其中的`TaskActivity`函数如下：  
```javascript
// new taskAcitvity
function TaskActivity(teacherId,teacherName,courseId,courseName,roomId,roomName,vaildWeeks,taskId,remark,assistantName,experiItemName,schGroupNo, teachClassName){
    this.teacherId=teacherId;
    this.teacherName=teacherName;
    this.courseId=courseId;
    this.courseName=courseName;
    this.roomId = roomId;
    this.roomName = roomName;
    this.vaildWeeks = vaildWeeks;	// 53个01组成的字符串，代表了一年的53周
    this.taskId=taskId;
    this.marshal=marshalValidWeeks;
    this.addAbbreviate=addAbbreviate;
    this.clone=cloneTaskActivity;
    this.canMergeWith=canMergeWith;
    this.isSame=isSameActivity;
    this.toString=activityInfo;
    this.adjustClone=adjustClone;
    this.leftShift=leftShift;
    this.needLeftShift=needLeftShift;
    this.remark = remark;
    this.assistantName=assistantName;
    this.experiItemName=experiItemName;
    this.schGroupNo=schGroupNo;
    this.teachClassName = teachClassName;
}
```

本项目中通过**正则匹配**、**BeautifulSoup**等方式解析匹配得到相应的信息，而后进行之后的处理。  

---
## TODO

- [x] 登录新教务管理系统  Login to the new Educational Administration System   
- [x] 获取课表  Get class schedule data   
- [x] 解析课表  Parse class schedule data  
- [x] 导出课表到`.txt`文件  Export class schedule data to `.txt` file  
- [x] 命令行参数  Get args from terminal  
- [x] 基于对象重构  Refactor based on object  
- [x] 生成`.ics`日历文件 :calendar:  Generate `.ics` file  
- [x] 生成`.xlsx`表格文件  Generate `.xlsx` file  
- [x] 打包为可执行程序 Packing  
- [x] 图形化界面  GUI  
- [x] 导出考试安排  Export examination schedule  
- [ ] 搭建网络服务，在线导出日历文件  Web service  
- [ ] 提供课表订阅服务  Subscribe service  
- [ ] 使用情况分析  Usage analysis  
- [ ] 适配研究生课表  Adapt to postgraduate's class schedule  
- [ ] 适配教师课表  Adapt to teacher's class schedule  
- [ ] etc.     

  

---
## Reference

1. 开源项目 `miaotony/NUAA_ClassSchedule`     
   
    > https://github.com/miaotony/NUAA_ClassSchedule    
    
       大概可以看作是本项目的前期准备吧嘻嘻嘻~
    
2. 开源项目`NUAA-Open-Source/NUAA-iCal-Python`  

   >项目网址：[点这里](https://github.com/NUAA-Open-Source/NUAA-iCal-Python)  
   https://github.com/NUAA-Open-Source/NUAA-iCal-Python    

   这是个（已经毕业了的）学长开发的小项目，但老接口随着新教务系统的启用而关闭，进而原脚本无法继续使用。

   在开发本项目过程中，解析课表之后，受到了此项目的启发，参考其实现了iCal日历文件的生成。在此非常感谢原作者！  

3. ISCNU iCal课表
    >网址：[点这里](https://i.scnu.edu.cn/ical/)   
    https://i.scnu.edu.cn/ical/

    这里有一些关于iCal的使用方法，可以参考一波。  

---
## Copyright

网络非法外之地，本项目相关技术内容仅供学习研究，请在合理合法范围内使用！  
The relevant technical content of this project is only for study and research, please use within the reasonable and legal scope!

**License:**    
**[GPL-3.0](LICENSE)**  

未经允许不得商用！  
Non-commercial use!    

最终解释权归本项目开发者所有。  
The final interpretation right belongs to the developer of the project.  


Copyright © 2019 [MiaoTony](https://github.com/miaotony), Cooook, Pinyi Qian   

