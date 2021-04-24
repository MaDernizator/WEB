import schedule
import time
import os
import threading


def delete_anonym():
    for folder, subfolders, files in os.walk(f'static/generated_documents'):
        if 'anonym' in folder:
            for file in files:
                if float(time.time()) - float(
                        os.path.getctime(f'static/generated_documents/anonym/{file}')) > 43200:
                    os.remove(f'static/generated_documents/anonym/{file}')


def delete_user():
    print(2)
    for folder, subfolders, files in os.walk(f'static\generated_documents'):
        if files:
            for file in files:
                a = '\\'
                os.remove(f'static\generated_documents\\{folder.split(a)[-1]}\{file}')


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


# schedule.every(1).seconds.do(run_threaded, delete_anonym)
# schedule.every(1).seconds.do(run_threaded, delete_user)
schedule.every(1).hours.do(run_threaded, delete_anonym)
schedule.every(1825).days.do(run_threaded, delete_user)


def clearing():
    while 1:
        schedule.run_pending()
        time.sleep(1)
