months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            m, d, y = date.split("/")
            m, d, y = int(m), int(d), int(y)
            
        elif "," in date:
            parts = date.split(" ")
            month_name = parts[0]
            day_str = parts[1].replace(",", "")
            year_str = parts[2]
            
            if month_name in months:
                m = months.index(month_name) + 1
                d = int(day_str)
                y = int(year_str)
            else:
                continue
        else:
            continue 

       
        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y}-{m:02}-{d:02}")
            break

    except (ValueError, IndexError):
        pass