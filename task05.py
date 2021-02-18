def areaOfTriangle( base, height ):
    area = 0.5 * base * height
    return area


base = input("Enter triangle base length: ")
height = input("Enter triangle height: ")




base = float( base )
height = float( height )


# Pass our base and height variables to the function

print('Area of triangle is', areaOfTriangle( base, height ))
area = areaOfTriangle( base, height )
print('The area of the triangle is', area)


