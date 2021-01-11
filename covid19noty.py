import COVID19Py
import requests
import win10toast

covid19 = COVID19Py.COVID19()

covid19 = COVID19Py.COVID19(data_source='jhu')

latest = covid19.getLatest()

noty = win10toast.ToastNotifier()

noty.show_toast('Covid 19 News', str(latest),duration=20)