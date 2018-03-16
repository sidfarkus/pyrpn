

def rpn(equation):
  stack = []
  symbols = equation.split()
  
  for symbol in symbols:
    if symbol in ['+', '-', '*', '/', '//']:
      x, y = stack.pop(), stack.pop()
      stack.append(eval("{0}{1}{2}".format(x, symbol, y)))
    else:
      stack.append(int(symbol))
  
  return stack[0] if len(stack) > 0 else 0

print(rpn(''))
print(rpn(' /'))