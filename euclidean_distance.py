import math

# 1. Adım: Noktaların Tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# 2. Adım: Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 3. Adım: Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Adım: Minimum Mesafenin Bulunması
min_distance = min(distances)

print("Noktalar arasındaki minimum mesafe:", min_distance)
