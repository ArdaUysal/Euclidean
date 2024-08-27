import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Noktaların tanımlanması
points = [(0, 0), (1, 1), (3, 3), (4, 5)]

# Mesafelerin saklanacağı liste
distances = []

# Mesafelerin hesaplanması
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonucun yazdırılması
print(f"Minimum mesafe: {min_distance}")