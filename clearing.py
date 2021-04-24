import schedule
import time
import os


def clearing():
    def delete():
        for folder, subfolders, files in os.walk(f'static/generated_documents/anonym'):
            for file in files:
                os.remove(f'static/generated_documents/anonym/{file}')

    schedule.every(1).hour.do(delete)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    clearing()
