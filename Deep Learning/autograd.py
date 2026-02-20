class Value:
	def __init__(self, data, _children=(), _op=''):
		self.data = data
		self.grad = 0
		self._backward = lambda: None
		self._prev = set(_children)
		self._op = _op
	def __repr__(self):
		return f"Value(data={self.data}, grad={self.grad})"

	def __add__(self, other):
		 # Implement addition here
		other = other if isinstance(other, Value) else Value(other)
		out = Value((self.data+other.data), _children=(self, other), _op='+')
		def _backward():
			self.grad += int(1.0 * out.grad)
			other.grad += int(1.0 * out.grad)
		out._backward = _backward
		return out

	def __mul__(self, other):
		# Implement multiplication here
		other = other if isinstance(other, Value) else Value(other)
		out = Value((self.data*other.data), _children=(self, other), _op='*')
		def _backward():
			self.grad += int(other.data * out.grad)
			other.grad += int(self.data * out.grad)
		out._backward = _backward
		return out

	def relu(self):
		# Implement ReLU here
		if self.data <= 0.0:
			out = Value(0.0, _children=(self, ), _op='relu')
		else:
			out = Value(self.data, _children=(self, ), _op='relu')
		def _backward():
			self.grad += int((self.data > 0) * out.grad)
		out._backward = _backward
		return out

	def backward(self):
		# Implement backward pass here
		topo = []
		visited = set()
		def build_topo(v):
			if v not in visited:
				visited.add(v)
				for child in v._prev:
					build_topo(child)
				topo.append(v)
		build_topo(self)

		self.grad = 1
		for node in reversed(topo):
			node._backward()
		
