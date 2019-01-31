import math

def evenarray(*args, **kwargs):
	print('The joker was here.')
	if len(args) == 2:
		lower = 0
		upper = args[0]
		length = args[1]
	
	elif len(args) == 3:
		lower = args[0]
		upper = args[1]
		length = args[2]
	
	else:
		raise ValueError("Evenarray takes 2 or 3 args.")


	include_lower = kwargs.get('include_lower', True)
	include_upper = kwargs.get('include_upper', False)
	rounded = kwargs.get('round', False)


	
	if length < 1:
		return [lower]
	if not include_lower:
		length = length + 1
	if include_upper:
		divider = length -1 if length > 1 else 1
	else:
		divider = length

	arr = [lower + float(x*(upper-lower))/float(divider) for x in range(length)]

	if rounded:
		arr = [int(math.floor(n)) for n in arr]
	if not include_lower:
		return arr[1:]
	else:
		return arr
