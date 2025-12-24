from math_Tookit import MathToolkit

toolkit = MathToolkit()

print("Interactive Calculator")
print("Operations: +, -, *, /")
print("Type 'quit' to exit")

while True:
    try:
        user_input = input("\nEnter calculation (e.g., 5 + 3): ").strip()
        if user_input.lower() == 'quit':
            break
            
        parts = user_input.split()
        if len(parts) != 3:
            print("Format: number operator number")
            continue
            
        a, op, b = float(parts[0]), parts[1], float(parts[2])
        
        if op == '+':
            result = toolkit.add_numbers(int(a), int(b))
        elif op == '-':
            result = toolkit.subtract_numbers(int(a), int(b))
        elif op == '*':
            result = toolkit.multiply_numbers(int(a), int(b))
        elif op == '/':
            result = toolkit.divide_numbers(int(a), int(b))
        else:
            print("Invalid operator. Use +, -, *, /")
            continue
            
        print(f"Result: {result}")
        
    except ValueError:
        print("Please enter valid numbers")
    except KeyboardInterrupt:
        break
        
print("\nGoodbye!")