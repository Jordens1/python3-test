import psutil
import time, datetime, os

# linux系统资源监测脚本
# 当前时间  3形式  time,datetime
# 系统资源  	内存  swap  (total  free  buffer)

# 		 	磁盘信息 分区剩余空间和总空间，文件系统类型，挂载点

# 		 	cpu  当前空闲时间，逻辑核心数
# 		 	用户  当前登录用户信息

def allInfo():

    now_mtime = time.time()
    now_gtime = time.localtime(now_mtime)
    now_stime = time.strftime('%Y-%m-%d %X', now_gtime)

    swap_total = psutil.swap_memory().total
    swap_free = psutil.swap_memory().free
    swap_used = psutil.swap_memory().used

    mem_total = psutil.virtual_memory().total
    mem_free = psutil.virtual_memory().free
    mem_buffers = psutil.virtual_memory().buffers
    #print('the mem information is : mem_total: %-.2f , mem_free: %-.2f , mem_buffes: %-.2f ' % (mem_total, mem_free, mem_buffers))

    disk_info = psutil.disk_io_counters('/')

    cpu_idle = psutil.cpu_times(percpu=False).idle
    cpu_count = psutil.cpu_count(logical=False)

    login_user = psutil.users()
    disk_parition = psutil.disk_partitions(all=False)

    alarm_allInfo = {'now_mtime':now_mtime, 'now_gtime':now_gtime, 'now_stime':now_stime,
               'swap_total':swap_total, 'swap_free':swap_free, 'swap_used':swap_used,
               'mem_total':mem_total, 'mem_free':mem_free, 'mem_buffers':mem_buffers,
               'cpu_idle':cpu_idle, 'cpu_idle':cpu_idle, 'cpu_count':cpu_count,
               'login_user':login_user, 'disk_info':disk_info, 'disk_parition':disk_parition}

    return alarm_allInfo









