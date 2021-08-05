import requests

f = open("C:\Dev\ImageDownloader/proplast.txt", "r")

for artnr in f:
    i = 0
    i_max = 3

    while i < i_max:
        try:
            artnr = artnr.rstrip()
            response = requests.get("https://www.proplast-online.de/out/pictures/generated/product/1/540_340_75/" + artnr + "_" + str(i) + ".jpg")
            file = open("C:\Dev\ImageDownloader\images/" + artnr + "_" + str(i) + ".jpg", "wb")
            file.write(response.content)
            file.close()
            i += 1
        except:
            print(artnr + "_" + str(i) + " : does not exist.")



f.close()