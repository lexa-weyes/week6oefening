def genereer():
    website=open("index2.html","r")
    tekst=website.read()
    website.close()

    geschiedenis=open("history.json","r")
    data=geschiedenis.read()
    geschiedenis.close()
    data =data.strip("[")
    data =data.strip("]")

    index_body=tekst.split("body")
    data=data.replace("timestamp:","<h1>timestamp:</h1>")

    index_body[1]=f">\n<p>{data}\n</p>\n</"

    tekst ="body".join(index_body)
    with open("index.html", 'w') as web:
        web.write(tekst)