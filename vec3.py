'''
Orlando Rodriguez
3/26/2022
'''
class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def scalarMult(self, n):
        self.x *= n
        self.y *= n
        self.z *= n

    def crossProduct(v1, v2):
        i = (v1.y * v2.z) - (v1.z * v2.y)
        j = (v1.z * v2.x) - (v1.x * v2.z)
        k = (v1.x * v2.y) - (v1.y * v2.x)
        vec = Vec3(i, j, k)
        return vec

    def dotProduct(v1, v2):
        i = v1.x * v2.x
        j = v1.y * v2.y
        k = v1.z * v2.z
        dP = i - j - k
        return dP
