
def merge(array, p, q, r, f):
  start, middle, end = p, q, r
  
  Aleft = array[start:middle+1] 
  Aright = array[middle+1:end+1] 
  
  n_left = len(Aleft)
  n_right = len(Aright)
  
  left, right, dest = 0, 0, start
  
  while left < n_left and right < n_right:
    # Aleft[0] is an user object or time record object, f(user) => userObject.username
    if f(Aleft[left]) < f(Aright[right]):
      array[dest] = Aleft[left]
      left += 1
    elif f(Aleft[left]) > f(Aright[right]):
      array[dest] = Aright[right]
      right += 1
    else:
      # special case if the value interested is the same
      # then compare the tuple as a whole, instead of getting only username
      if f(Aleft[left]) == f(Aright[right]):
        if Aleft[left] < Aright[right]:
          array[dest] = Aleft[left]
          left += 1
        else:
          array[dest] = Aright[right]
          right += 1
    dest += 1

  while left < n_left:
    array[dest] = Aleft[left]
    left += 1
    dest += 1
      
  while right < n_right:
    array[dest] = Aright[right]
    right += 1
    dest += 1
    
    
def mergesort_recursive(array, p, r, f):
  start, end = p, r
  n = end - start + 1  # [2,3,2,4]   4-0-1 = 3, 4-1-1=2,cannot 4-2-1=1  [2,3,2,4] or [3,2,4]
  if(n > 1):
    middle = (start + end)//2
    mergesort_recursive(array, start, middle, f)
    mergesort_recursive(array, middle+1, end, f)
    merge(array, start, middle, end, f)

def mergesort(array, byfunc=None):
  # function is .username
  mergesort_recursive(array, 0, len(array)-1, byfunc)


class Stack:
  def __init__(self):
    self.__items = []
      
  def push(self, item):
    self.__items.append(item)

  def pop(self):
    if len(self.__items) >= 1:
        return self.__items.pop(-1)

  def peek(self):
    if len(self.__items) >= 1:
        return self.__items[-1]

  @property
  def is_empty(self):
    return len(self.__items) == 0

  @property
  def size(self):
    return len(self.__items)

class EvaluateExpression:

  valid_char = '0123456789+-*/() '
  operators = '+-*/()'
  operands = "0123456789"

  # initiate class with expression passed in
  def __init__(self, string=""):
    self.expr = string

  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    for i in new_expr:
      if i not in self.valid_char:
        self.expr = ""
        return
    self.expr = new_expr
  
  def insert_space(self):
    new_string = ""
    for char in self.expr:
      if char in self.operators:
        new_string += " " + char + " "
      else:
        new_string += char
    return new_string
  
  def process_operator(self, operand_stack, operator_stack):

    if (len(operand_stack._Stack__items) > 1):
      # keep compute until there is only (
      # check to make sure there is operator at the top of the operator stack
      # if there is no brackets need to check if theres still operater to continue
      while not operator_stack.is_empty and operator_stack.peek() != '(':
        op1 = operator_stack.pop()
        number1 = int(operand_stack.pop()) # number at the back
        number2 = int(operand_stack.pop()) 
        if(op1 == '+'):
          operand_stack.push(number1 + number2)
        elif(op1 == '/'):
          operand_stack.push(number2 // number1)
        elif(op1 == '-'):
          operand_stack.push(number2 - number1)
        elif(op1 == '*'):
          operand_stack.push(number1 * number2)
              
  def process_operator_special(self, operand_stack, operator_stack):

    if (len(operand_stack._Stack__items) > 1):
      # check if * or / is in the list first
      # if dont have do nothing
      if '*' in operator_stack._Stack__items or '/' in operator_stack._Stack__items:
        # run once only
        if operator_stack.peek() == '(':
          operator_stack.pop()
        op1 = operator_stack.pop()
        number1 = int(operand_stack.pop()) # number at the back
        number2 = int(operand_stack.pop()) # number in front
        if(op1 == '/'):
          operand_stack.push(number2 // number1)
        elif(op1 == '*'):
          operand_stack.push(number1 * number2)
          
          
  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()

    # for all the char in the expression
    for char in tokens:
      # if the char is a number
      if char in self.operands:
        # append it to operand_stack
        operand_stack.push(char)
      else:
        # else check each operator
        if char == '(':
          # just push into operator_stack
          operator_stack.push(char)
        elif char == '+' or char == '-':
          self.process_operator(operand_stack, operator_stack)
          operator_stack.push(char)
        elif char == '*' or char == '/':
          # this make sure the only * is at the back
          self.process_operator_special(operand_stack, operator_stack)
          operator_stack.push(char)
        elif char == ')':
          self.process_operator(operand_stack, operator_stack)

    # compute the rest of operators between ( 
    while len(operator_stack._Stack__items) > 0:
      self.process_operator(operand_stack, operator_stack) 
      # pop out the ( after computing 
      operator_stack.pop()

    return operand_stack.pop()



def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records] # create a list of records
  mergesort(times, lambda x: x.elapsed_time) # get the time from records
  return times[:3]

