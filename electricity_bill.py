def calculate_bill(u):
    s1 = min(u, 100)
    s2 = min(max(u - 100, 0), 100)
    s3 = max(u - 200, 0)
    bill = s1 * 1 + s2 * 2 + s3 * 5
    print(f"\n--- Electricity Bill Breakdown ---")
    print(f"Slab 1 (0-100 @ ₹1): {s1} units = ₹{s1 * 1}")
    print(f"Slab 2 (101-200 @ ₹2): {s2} units = ₹{s2 * 2}")
    print(f"Slab 3 (200+ @ ₹5): {s3} units = ₹{s3 * 5}")
    print(f"Total Units: {u} | Total Bill: ₹{bill}")
while True:
    try:
        u = int(input("Enter units: "))
        if u >= 0:
            calculate_bill(u)
            break
    except:
        print("Invalid input")

           
            
