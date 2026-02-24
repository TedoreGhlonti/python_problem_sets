user = input('File name: ').strip().lower()
if user.endswith(".gif"):
    print("image/gif")
elif user.endswith(".jpg") or user.endswith("jpeg"):
    print("image/jpeg")
elif user.endswith("png"):
    print("image/png")
elif user.endswith("pdf"):
    print("application/pdf")
elif user.endswith(".txt"):
    print("text/plain") 
elif user.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")