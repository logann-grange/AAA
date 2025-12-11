import platform
import psutil
import socket
import os
import webbrowser
from pathlib import Path
import datetime
from flask import Flask, render_template

#=========== Process List ============#
def process() :
    process_list = []

    for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_info']):
        process_list.append({
            #'pid': proc.info['pid'],
            'nom' : proc.info['name'],
            'cpu' : proc.info['cpu_percent'],
            'ram' : round((proc.info['memory_info'].rss / psutil.virtual_memory().total) *100, 2)
        })

    return process_list

#========== Files size unit ==========#
def byte_unit(byte):
    for unite in ['o', 'Ko', 'Mo', 'Go', 'To']:
        if byte < 1024.0:
            return f"{byte:.2f} {unite}"
        byte /= 1024.0
    return f"{byte:.2f} Po"

#======== Top file size ==========#
def top_files(size_files_list) :
    files_list = sorted(size_files_list[0], key=lambda f: os.path.getsize(f), reverse=True)[:5]
    size_list = sorted(size_files_list[1], reverse=True)[:5]

    sorted_list = [files_list, size_list] 

    return sorted_list

#============ Files list =============#
def file_list(files=None, count_file=None, size_list=None ,path=os.path.join(os.path.expanduser('~'), 'Documents')) :
    if files is None:
        files = []
    if count_file is None:
        count_file = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if size_list is None:
        size_list = []

    try:
        dir_list = os.listdir(path)
    except PermissionError:
        #print(f"Accès refusé au dossier : {path}")
        return files
    except Exception as e:
        #print(f"Erreur lors de l'accès à {path} : {e}")
        return files
    
    for element in dir_list:
        element_path = os.path.join(path, element)
        try:
            # Extension test
            if os.path.isfile(element_path) :
                extension = os.path.splitext(element_path)[1]
                size = os.path.getsize(element_path)
                match extension :
                    case '.txt' :
                        count_file[0] += 1
                        files.append(element_path)  # Sauvegarder le fichier dans 
                        size_list.append(byte_unit(size))
                    case '.py' :
                        count_file[1] += 1
                        files.append(element_path)
                        size_list.append(byte_unit(size))

                    case '.pdf' : 
                        count_file[2] += 1
                        files.append(element_path)
                        size_list.append(byte_unit(size))

                    case '.jpg' :
                        count_file[3] += 1
                        files.append(element_path)
                        size_list.append(byte_unit(size))
                    case '.html' :
                        count_file[4] += 1
                        files.append(element_path)
                        size_list.append(byte_unit(size))
                    case '.png' :
                        count_file[5] += 1
                        files.append(element_path)
                        size_list.append(byte_unit(size))
                    case '.css' :
                        count_file[6] += 1
                        files.append(element_path)
                        size_list.append(byte_unit(size))
                    case '.mp3' :
                        count_file[7] += 1
                        files.append(element_path)
                        size_list.append(byte_unit(size))
                    case '.mp4' :
                        count_file[8] += 1
                        files.append(element_path)
                        size_list.append(byte_unit(size))
                    case '.zip' :
                        count_file[9] += 1
                        files.append(element_path)
                        size_list.append(byte_unit(size))

            elif os.path.isdir(element_path):
                file_list(files, count_file, size_list, element_path)
        except PermissionError:
            #print(f"Accès refusé à : {element_path}")
            print()
    files_and_count = [files, count_file, size_list]
    
    #return files
    return files_and_count

def percent_files(count) :
    percent_list = []
    total = 0
    # calcul total number of files
    for nb in count :
        total += nb
    
    for val in count :
        percent_list.append((val/total)*100)
    
    return percent_list

#============ Police color ===========#
def police_color(nb) :
    color = ""

    if nb <= 50 :
        color = "green"
    elif nb <= 80 :
        color = "orange"
    else :
        color = "red"

    return color

app = Flask(__name__)
@app.route('/')

def transfert_data() :

    #============ System =============#
    system_name = socket.gethostname()
    system_os = platform.system()
    system_cpu = platform.processor()
    system_arch = platform.machine()
    users_nb = len(psutil.users())

    load1, load5, load15 = psutil.getloadavg()

    #============= Time ==============#
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    start_time = boot_time.strftime('%d/%m/%Y à %H:%M:%S')

    #============== CPU ==============#
    cpu_usage = psutil.cpu_percent(interval=1)
    nb_core = psutil.cpu_count(logical=True)
    core_percentages = psutil.cpu_percent(interval=1, percpu=True)
    cpu_freq = psutil.cpu_freq()
    cpu_color = police_color(cpu_usage)
    core_color = []
    for percent in core_percentages :
        core_color.append(police_color(percent))


    #============== RAM ==============#
    ram_usage = round(psutil.virtual_memory().used / (1024**3), 2)
    ram_total = round(psutil.virtual_memory().total / (1024**3), 2)
    ram_percent = psutil.virtual_memory().percent
    ram_color = police_color(ram_percent)

    #============ Network ============#
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()

    #============= Files =============#
    files_list = file_list()
    files = files_list[0]
    files_count = files_list[1]
    size_list = files_list[2]
    percent_file_list = percent_files(files_list[1])
    top_file_list = top_files([files, size_list])

    #============= Data ==============#
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
        'core_percent' : core_percentages,
        'core_colors' : core_color,
        'cpu_color' : cpu_color,
        'ram_usage' : ram_usage,
        'ram_percent' : ram_percent,
        'ram_total' : ram_total,
        'ram_color' : ram_color,
        'ip' : ip,
        'cpu_process' : sorted(process(), key=lambda x: x['cpu'], reverse=True)[:3],
        'ram_process' : sorted(process(), key=lambda x: x['ram'], reverse=True)[:3],
        'files_list' : files,
        'files_count' : files_count,
        'percent_file_list' : percent_file_list,
        'size_file_list' : size_list,
        'top_size_file_list' : top_file_list,
        'load1' : load1,
        'load5' : load5,
        'load15' : load15
    }
    return render_template('template.html', **data)


webbrowser.open('http://127.0.0.1:5000')

app.run(debug=True)



