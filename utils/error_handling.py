from datetime import datetime


# noinspection PyPep8Naming
def LOG(content):
    f = open("logs.txt", "a")
    f.write(f'{str(datetime.now())}\n{str(content)}]\n{"-----" * 20}\n')
    f.close()
