from vec3 import Vec3 as v3

def main():
    print("Hello World")
    print(arithmetic(1, 2))
    if debuggingPractice() != 14:
        print("debuggingPractice returns {}, SHOULD return 14".format(debuggingPractice()))
    else:
        print("debuggingPractice is working as should")


def arithmetic(a, b):
    return a + b * x

def debuggingPractice():
    v1 = v3(1, 2, 3)
    v2 = v3(1, 2, 3)

    return v3.dotProduct(v1, v2)

if __name__ == "__main__":
    main()