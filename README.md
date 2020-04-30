# Gandi DDNS
An Auto IP Update Script Using Gandi LiveDNS API

支持同一Gandi账户下的多域名 A,AAAA 记录修改

我太菜了，又不是不能用.jpg

## English Version
    
   ### Usage
    
   #### Install Requirements First 
    For RHEL/CentOS/Fedora Users:
    yum install -y python3 python3-pip
    pip3 install requests
    
    For Debian/Ubuntu Users:
    apt install -y python3 python3-pip
    pip3 install requests
    
   #### Get a Gandi API
   > Start by [retrieving your API Key](https://account.gandi.net/) from the "Security" section in new Account admin panel to be able to make authenticated requests to the API.
    
   Then Setup Follow config.json
   
   Running Just By
    
    python3 ddns.py
   
   Using Crontab to Update DNS Automatic
    
## 中文版

   ### 准备环境
    对于 RHEL/CentOS/Fedora 用户:
    yum install -y python3 python3-pip
    pip3 install requests
    
    对于 Debian/Ubuntu 用户:
    apt install -y python3 python3-pip
    pip3 install requests
    
   ### 获取Gandi API
   > 进入 [管理页](https://account.gandi.net/) 的安全选项以申请API

   接着修改config.json中的信息
   
   ### 配置Crontab
   先建立一个sh文件
    
    #！/usr/bin/bash
    cd /root
    /usr/bin/python3 /root/ddns.py >> /root/ddns.log 2>&1
   
   然后
    
    crontab -e
    
   按照需求修改写入的命令
   
    */5 * * * * /root/ddns.sh
    
   即可