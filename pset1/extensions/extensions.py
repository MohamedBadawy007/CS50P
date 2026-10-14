filename = input("File name: ").lower().strip()

'''
parts = filename.split(".")

ext = parts[-1]

match ext:
    case "gif":
        print("image/gif")

    case "jpeg" | "jpg":
        print("image/jpeg")
'''

if filename.endswith(".gif"):
    print("image/gif")

elif filename.endswith(".jpeg") or filename.endswith(".jpg"):
    print("image/jpeg")

elif filename.endswith(".png"):
    print("image/png")

elif filename.endswith(".pdf"):
    print("application/pdf")

elif filename.endswith(".txt"):
    print("text/plain")

elif filename.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")
