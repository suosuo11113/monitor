
#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import  psutil
import datetime
from subprocess import PIPE

if __name__ == '__main__':
    #memory
    '''mem = psutil.virtual_memory()
    print(mem.free) #剩余内存
    print (mem.total) #总内存
    print(mem.used)  # 已用内存
    
    print(psutil.cpu_times(percpu=True))
    print(psutil.cpu_times().user)  #执行用户进程的时间百分比
    print(psutil.cpu_times().system) #执行内核进程及中断的时间百分比
    #print(psutil.cpu_times().iowait) #io等待的时间百分比
    print(psutil.cpu_times().idle)  #cpu处于idle状态的时间百分比
    print(psutil.cpu_count()) #获取cpu的逻辑个数
    print(psutil.cpu_count(logical=False)) #获取cpu的物理个数

    print(psutil.disk_partitions()) #获取磁盘完整信息
    print(psutil.disk_usage('C:\\')) #获取分区的使用情况
    print(psutil.disk_io_counters()) #获取硬盘总的io个数
    print(psutil.disk_io_counters(perdisk=True,nowrap=True)) 


    print(psutil.disk_io_counters()) #输出网络io信息 

    print(psutil.users()) #获取当前登录系统的用户信息
    print(psutil.boot_time())  #获取开机时间，时间戳
    print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y%m%d %H:%M:%S")) #获取开机时间，时间戳自定义时间格式


    print(psutil.pids())
    print(psutil.Process(664))'''


    p = psutil.Popen(["python","-c","print('hello')"],stdout=PIPE)
    print(p.name)
    print(p.username())
    print(p.cpu_times())
    print(p.connections())








