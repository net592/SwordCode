#!/bin/bash
os_version=`cat /etc/redhat-release |grep -Po '\d+(\.\d+)+?'|awk -F \. '{print $1}'`
salt_num=`ps -ef|grep /usr/bin/salt-minion|grep -v grep|wc -l`
salt_rpm=`rpm -qa|grep salt`

# 清理老的salt进程
echo -e "\033[31m 发现程序 old-salt:$salt_num JCSAgentCore:$num2 \033[0m"
if [ $salt_num -eq 3 ];then
    echo -e "\033[31m ######jcs Already Installed,Pls Check!!!###### \033[0m"
    ps aux|grep "/usr/bin/salt-minion"|grep -v grep|awk '{print $2}'|xargs kill -9 
    for i in $salt_rpm
        do  
            echo $i
            rpm -e $i
        done
else
    echo -e "\033[42m ######jcs NOT Installed,Begin Install!!!###### \033[0m"
    #wget -q -O /export/servers/jcloud-jcs-agent-linux-deploy.py https://bj-jcs-agent-linux.s3-internal.cn-north-1.jdcloud-oss.com/jcloud-jcs-agent-linux-deploy.py
fi

python_rpm=`rpm -qa|grep sre-python`
if [ $python_rpm -eq 1 ];then
    echo -e "\033[31m ######sre-python Already Installed,Pls Check!!!###### \033[0m"
else
    if [ $os_version == 7 ];then
        rpm -ivh http://mirrors.jd-it.top/rpm/sre-python-36-1.el7.x86_64.rpm
    elif [ $os_version == 6 ];then
        rpm -ivh http://mirrors.jd-it.top/rpm/sre-python-36-1.el7.x86_64.rpm
    else
        echo "\033[31m ######No Mattch $os_version Error,Pls Check!!!###### \033[0m"    
    if [ $? -eq 0 ];then
        echo -e "\033[42m ######install sre-python Successful!!!###### \033[0m"
    else
        echo -e "\033[31m ######install sre-python Error,Pls Check!!!###### \033[0m"   
    fi
fi

# 安装salt
salt_num=`ps -ef|grep /usr/bin/salt-minion|grep -v grep|wc -l`
if [ $salt_num -eq 1 ];then
    echo -e "\033[31m ######salt Already Installed,Pls Check!!!###### \033[0m"
else
    # 安装salt
    mkdir -p /etc/salt/pki/minion
    rm -rf /etc/salt/pki/minion/minion_master.pub
    echo "master: salt1.sre.jd-it.top" > /etc/salt/minion
    echo `hostname` >  /etc/salt/minion_id
    /usr/local/python36/bin/pip3 install salt --retries=1 --timeout=3  --index-url http://mirrors.jd.com/pypi/simple --trusted-host mirrors.jd.com 
    /usr/local/python36/bin/salt-call state.highstate --return=stree_redis
    if [ $? -eq 0 ];then
        echo -e "\033[42m ######install salt Successful!!!###### \033[0m"
    else
        echo -e "\033[31m ######install salt Error,Pls Check!!!###### \033[0m"   
        exit
    fi
fi