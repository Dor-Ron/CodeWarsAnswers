def get_grade(*args):  # change (s1, s2, s3) to args
    return 'F' if sum(args)/len(args) < 60 else 'D' if sum(args)/len(args) < 70 else 'C' if sum(args)/len(args) < 80 else 'B' if sum(args)/len(args) < 90 else 'A'

# prob shouldve assigned sum(args)/len(args) to a variable, but then it woulldnt be a one-liner solution :/ 
