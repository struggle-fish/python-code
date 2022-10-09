import subprocess

obj = subprocess.Popen('echo 123 ; ls / ; ls /root', shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       )

# print(obj)
# res=obj.stdout.read()
# print(res.decode('utf-8'))

err_res = obj.stderr.read()
print(err_res.decode('utf-8'))
