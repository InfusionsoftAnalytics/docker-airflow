import git

print('Pulling DAGs repo...')
g = git.Git('.')
g.pull('origin','master')
print('Pull successful. Goodbye!')