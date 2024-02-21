def totalMarks(
    physics: int,
    chemistry: int,
    maths: int,
    english: int = 0,
    computer: int = 0,
    
):
    print(f"{physics = }")
    print(f"{chemistry = }")
    print(f"{maths = }")
    print(f"{english = }")
    print(f"{computer = }")
    total = physics + chemistry + maths + english + computer
    print(f"total={total}")

totalMarks(23,44,34,5,5)    

