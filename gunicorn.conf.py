from multiprocessing import cpu_count

reload: bool = True
bind: str = "127.0.0.1:8000"
workers = cpu_count() * 2 + 1

