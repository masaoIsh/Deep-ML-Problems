def find_treasure(start_x: float) -> float:
    """
    Find the x-coordinate where f(x) = x^4 - 3x^3 + 2 is minimized.

  Returns:
        float: The x-coordinate of the minimum point.
    """
    # Your code here
    # f'(x)=4x^3-9x^2
    def grad(x):
      return 4*x**3-9*x**2
    
    close_enough = 1e-6
    learning_rate = 0.09
    x = start_x
    for i in range(1000):
      gradient = grad(x)
      new_x = x - learning_rate * gradient
      if(abs((new_x - x)) < close_enough):
        break
      x = new_x
    

    return x



    
    #return float(9 / 4)

      
