sample_data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

def go(data):
    # data = sample_data
    data = data.splitlines()

    coords = []
    s = ""

    for line in data:
        for char in line:
            y = None
            try:
                y = int(char)
            except:
                pass
                
            if y:
                s = s + str(y)
        
        coords.append(s[:1] + s[-1:])
        s = ""
    
    answer = 0
    for a in coords:
        answer += int(a)
    
    print(answer)

    return answer
