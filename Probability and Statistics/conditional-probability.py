def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    # Your code here
    n = len(data)
    
    num_x = 0
    num_x_and_y = 0

    for i in range(len(data)):
      #print(f"This is for {data}. x is {x} and y is {y}")
      if (data[i][0]==x) and (data[i][1] == y):
        num_x_and_y += 1
      if data[i][0] == x:
        #print("Add one to num_x")
        num_x += 1
    
    p_x = num_x / n
    p_y_and_x = num_x_and_y / n

    if p_x != 0:
      return round(p_y_and_x / p_x, 4)
    else:
      return 0.0
