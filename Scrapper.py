from indeed import get_jobs as iget_jobs
from so import get_jobs as sget_jobs
from save import save_to_file


indeed_jobs = iget_jobs()
so_jobs = sget_jobs()
jobs = so_jobs + indeed_jobs

save_to_file(jobs)