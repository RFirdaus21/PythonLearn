import matplotlib.pyplot as plt

def circle(radius) : 
    x = 0
    y = radius
    p = 1 - radius

    # Titik-titik yang akan digambar menggunakan set
    points = [] 

    # Midpoint Algorithm
    while x<=y:
        points.extend([(x, y), (x, -y), (-x, y), (-x, -y), 
                        (y, x), (y, -x), (-y, x), (-y, -x)])

        if p <= 0 : 
            x += 1
            p += 2 * x + 1

        else : 
            y -= 1
            x += 1
            p += 2 * (x - y) + 1
        
    return points

def circle_plot(points) : 


    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.scatter(x, y, color='red')
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    plt.axis('equal')
    plt.title('Gambar Lingkaran Menggunakan Algoritma Midpoint')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)  
    plt.show()

radius = 20
points = circle(radius)
circle_plot(points)