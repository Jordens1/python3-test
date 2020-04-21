import psutil


psutil.cpu_times(percpu=False)

psutil.cpu_count(logical=True)
psutil.cpu_count(logical=False)

psutil.cpu_stats()

mem = psutil.virtual_memory()

psutil.swap_memory()

psutil.disk_partitions(all=False)

psutil.disk_usage('/')
psutil.disk_io_counters(perdisk=False,nowrap=True)
psutil.users()
psutil.boot_time()






