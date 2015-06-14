from wsgiref.simple_server import make_server
import psutil, datetime

def monitor(environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'html; charset=utf-8')]
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        start_response(status, headers)
        

        cpu_util = psutil.cpu_percent(interval=1, percpu=True)

        i=1
        line = "<h1>Welcome To The Server Health Monitor</h1>"
        line+= "<table style= width:50%;>"
        line+= "<tr bgcolor=#7CB9E8>"
        line+= "<td>BOOT TIME</td>"
        line+= "<td>"+str(boot_time)+"</td>"
        line+= "</tr>"
        line += "<tr bgcolor=#8AFB17><td rowspan=\"4\">CPU UTILIZATION</td>"

        i = 1
        for cpu in cpu_util:
                line+= "<td bgcolor = yellow>" 
                line += "CPU {} :{}%".format(i, cpu)
                i+=1
                line+= "</td></tr>" 
       

        mem = psutil.virtual_memory()
        THRESHOLD = 100 * 1024 * 1024  # 100MB

        line+= "<tr bgcolor=#E38AAE>"
        line+= "<td>AVAILABLE MEMORY</td>"
        line+= "<td>"+str(mem.available)+"</td>"
        line+= "</tr>"
        line+= "<tr bgcolor=#FFCBA4 >"
        line+= "<td>USED MEMORY</td>"
        line+= "<td>"+str(mem.used)+"</td>"
        line+= "</tr>"
        line+= "<tr bgcolor=#E77471 >"
        line+= "<td>USED PERCENTAGE</td>"
        if mem.percent > 80:             
                line+= "<td bgcolor=red>"+str(mem.percent)+"</td>"
        else:
                line+= "<td bgcolor=#E77471>"+str(mem.percent)+"</td>"
        line+= "</tr>"
        line+= "</table>"
      
        return[bytes(line,'utf-8')]

httpd = make_server('', 8000, monitor)
print("Serving on port 8000...")

httpd.serve_forever()
