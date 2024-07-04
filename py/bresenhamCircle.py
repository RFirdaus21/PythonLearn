import matplotlib.pyplot as plt

# Fungsi untuk menggambar lingkaran dengan algoritma Bresenham
def draw_circle(radius):
    x = 0
    y = radius
    d = 3 - 2 * radius  

    points = []

    while x <= y:
        points.extend([(x, y), (x, -y), (-x, y), (-x, -y),
                       (y, x), (y, -x), (-y, x), (-y, -x)])

        if d < 0: 
            d += 4 * x + 6
        else: 
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

# Panggil fungsi untuk menggambar lingkaran
radius = 20
points = draw_circle(radius)

x = [point[0] for point in points]
y = [point[1] for point in points]

x.append(points[0][0])
y.append(points[0][1])

# Gambar garis lingkaran dengan scatter 
plt.scatter(x, y, color='green')

plt.axis('equal')  
plt.title('Lingkaran dengan Algoritma Bresenham')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
