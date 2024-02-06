def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        'Equilateral' if all three sides are equal
        'Isoceles' if exactly one pair of sides are equal
        'Scalene' if no pair of sides are equal
        'NotATriangle' if not a valid triangle
        'Right' if the sum of the square of two sides equals the square of the third side
    """

    # Correct the invalid input checks
    if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
        
    # Check if all sides are integers
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    
    # Sort the sides to simplify the logic for the right triangle
    sides = sorted([a, b, c])

    # Check if it's a valid triangle
    if sides[0] + sides[1] <= sides[2]:
        return 'NotATriangle'
    
    # Check if it's a right triangle
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'Right'
    
    # Check for other types of triangles
    if a == b and b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isoceles'
    else:
        return 'Scalene'
