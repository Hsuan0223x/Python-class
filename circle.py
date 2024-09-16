import math

def calculate_circle_properties(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return radius, perimeter, area

def main():
    radius = float(input("請輸入圓的半徑: "))
    radius, perimeter, area = calculate_circle_properties(radius)
    print(f"Radius: {radius:.2f}")
    print(f"Perimeter: {perimeter:.2f}")
    print(f"Area: {area:.2f}")

if __name__ == "__main__":
    main()