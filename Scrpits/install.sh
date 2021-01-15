#!/bin/bash
stty erase ^h
cat << EOF
                                             
                :,;;iiiii;i;.:i..            
             .,iii;i;;;;;;;i;ii;             
            ;ii;;;;;;;;;;;;;;;ivl;           
          .i;;;;;;;;;;;;;;;;;;;i;vi          
         ,i;;;;,;,;,;;;;;,;:,.:.,;ii.        
        ,i;;,ii;,:..:;;;,,,iijLMl;;il        
       .i;;;;UDOSqZCv,;,;q8qOXJUv,;,il       
       i;;;;;,.  :iMv;;;;i.     .;;;,Y;      
      ;;;;;;;,.;@q  ,;;;; .;yL2Sc,;;;;L      
      ;;;;;;;,.@B@;:;;;;:Q@@2Uili;;;;;l;     
     .i;;;;,;.,@@C..,:;::;MISSSl.:;,;,li     
     ,;;;;;lVy:;;..;,,:,., ..;ll,yVy;;iV     
     ,i;;;;;ii;.,:;SB66Z8C;:;:,:;;i;;:iY     
     ;;;;;;;,;;;;;,;CED6c;:;;;;;,;:;;;iV     
     ,i;;;;;;;;;;;;.::;.::;;;;;;;;i;i;il     
     ;;;;;;;;;;;;;;;;;,;;;;;;;;i;i;i;iiY     
     ,i;iii;;;;;;;;;;;;;;;;;;;iii;i;i;vl     
     ,ivilvyii;i;i;i;iii;i;i;iiliviviiiv     
     i    ..,.. . . . . . . .......    y     
    F@Ii                             VGB0    
   X@GZ8EY       ;2I::.V2,        lqBQZI@2   
  c@6GMIOB8t .lq8@@B.  6B@EC;  ;MBBQ2IMIq@F  
 v@D213K3KS8B8@QSI8v   ;E06EBQQB8O3MCF313Z@M 
l@BEiU22F2F330KCFSK     iDM2CSSGF2F3FCMF;Z8@i
 ;B@KXGMCF2KC13F23I     Fq3K21CFCKCKCKGKKB@y 
  .DlOOICIMIM3CIKGS8i  EEGC3KIMICIMIM32ZjD;  
     UIJtJtJtJ1J1XF2EUqqFJ1JtJtJtJtc1XCK     
EOF
echo -e "\e[1;33m 欢迎使用 Install 脚本V1.0 By ENT-SRE@xuzeming6,huangchaoqun6\e[0m"
sleep 1

os_version=`cat /etc/redhat-release |grep -Po '\d+(\.\d+)+?'|awk -F \. '{print $1}'`
salt_num=`ps -ef|grep /usr/bin/salt-minion|grep -v grep|wc -l`
salt_rpm=`rpm -qa|grep salt|wc -l`


# 清理老的salt进程
if [ $salt_num -ge 1 ];then
    echo -e "\033[31m ######发现程序 old-salt:$salt_num  \033[0m"
    ps aux|grep "/usr/bin/salt-minion"|grep -v grep|awk '{print $2}'|xargs kill -9 
    for i in $salt_rpm
        do
            echo $i
            rpm -e $i
        done
else
    echo -e "\033[42m ######pysalt NOT Installed,Begin Install!!!###### \033[0m"
    #wget -q -O /export/servers/jcloud-pysalt-agent-linux-deploy.py https://bj-pysalt-agent-linux.s3-internal.cn-north-1.jdcloud-oss.com/jcloud-pysalt-agent-linux-deploy.py
fi

python_rpm=`rpm -qa|grep sre-python|wc -l`
if [ $python_rpm -eq 1 ];then
    echo -e "\033[42m ######sre-python Already Installed,Pls Check!!!###### \033[0m"
else
    if [ $os_version == 7 ];then
        rpm -ivh http://mirrors.jd-it.top/rpm/sre-python-36-1.el$os_version.x86_64.rpm
    elif [ $os_version == 6 ];then
        rpm -ivh http://mirrors.jd-it.top/rpm/sre-python-36-1.el$os_version.x86_64.rpm
    else
        echo "\033[31m ######No Mattch $os_version Error,Pls Check!!!###### \033[0m"    
    fi

    if [ $? -eq 0 ];then
        echo -e "\033[42m ######install sre-python Successful!!!###### \033[0m"
    else
        echo -e "\033[31m ######install sre-python Error,Pls Check!!!###### \033[0m"   
    fi
fi

# 安装salt
salt_num=`ps -ef|grep /usr/bin/salt-minion|grep -v grep|wc -l`
if [ $salt_num -ge 1 ];then
    echo -e "\033[31m ######salt Already Installed,Pls Check!!!###### \033[0m"
else
    echo "install salt"
    # 安装salt
    mkdir -p /etc/salt/pki/minion
    rm -rf /etc/salt/pki/minion/minion_master.pub
    echo "master: salt1.sre.jd-it.top" > /etc/salt/minion
    echo `hostname` >  /etc/salt/minion_id
    /usr/local/python36/bin/pip3 install salt --retries=1 --timeout=3  --index-url http://mirrors.jd.com/pypi/simple --trusted-host mirrors.jd.com 
    /usr/local/python36/bin/salt-call state.highstate --return=stree_redis
    if [ $? -eq 0 ];then
        echo -e "\033[42m ######Ent-SRE You Salt Run Successful!!!###### \033[0m"
    else
        echo -e "\033[31m ######Salt Run Error,Pls Check!!!###### \033[0m"   
    fi
fi
