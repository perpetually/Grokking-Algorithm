def countdown(i):
  print (i)
  # base case
  if i <= 0:
    return
  # recursive case
  else:
    countdown(i-1)

countdown(5)


# 调用另一个函数时，当前函数暂停并处于未完成状态