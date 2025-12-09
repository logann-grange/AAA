import platform
import psutil
import socket
import datetime
from flask import Flask, render_template

def cpu_process() :
    process = []

    for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_info']):
        process.append({
            #'pid': proc.info['pid'],
            'nom' : proc.info['name'],
            'cpu' : proc.info['cpu_percent'],
            'ram' : round(proc.info['memory_info'].rss / (1024**2), 2)
        })
    return process

app = Flask(__name__)
@app.route('/')

def transfert_data() :

    #System
    system_name = socket.gethostname()
    system_os = platform.system()
    system_cpu = platform.processor()
    system_arch = platform.machine()
    users_nb = len(psutil.users())
    #Time
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    start_time = boot_time.strftime('%d/%m/%Y à %H:%M:%S')
    #CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    nb_core = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    cpu_color = ""
    #RAM
    ram_usage = round(psutil.virtual_memory().used / (1024**3), 2)
    ram_total = round(psutil.virtual_memory().total / (1024**3), 2)
    ram_percent = psutil.virtual_memory().percent
    ram_color = ""
    #Disk
    disk_usage = psutil.disk_usage("/").used
    disk_max = psutil.disk_usage("/").total
    #Network
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()

    #CPU police color
    if cpu_usage <= 50 :
        cpu_color = "green"
    elif cpu_usage <= 80 :
        cpu_color = "orange"
    else :
        cpu_color = "red"

    #RAM police color
    if cpu_usage <= 50 :
        cpu_color = "green"
    elif cpu_usage <= 80 :
        cpu_color = "orange"
    else :
        cpu_color = "red"
    
    
    data = {
        'system_name' : system_name,
        'system_cpu' : system_cpu,
        'system_os' : system_os,
        'system_arch' : system_arch,
        'users_nb' : users_nb,
        'start_time' : start_time,
        'uptime' : uptime,
        'uptime_day' : uptime.days,
        'uptime_hour' : uptime.seconds // 3600,
        'uptime_min' : (uptime.seconds % 3600) // 60,
        'cpu_usage' : cpu_usage,
        'cpu_freq' : cpu_freq.current,
        'nb_core' : nb_core,
        'cpu_color' : cpu_color,
        'ram_usage' : ram_usage,
        'ram_percent' : ram_percent,
        'ram_total' : ram_total,
        'ram_color' : ram_color,
        'ip' : ip,
        'cpu_process' : cpu_process(),
    }

    return render_template('template.html', **data)

app.run(debug=True)


