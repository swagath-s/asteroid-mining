import config
import requests

def findAsteroid():
	entered = config.entr.get()
	entered = int(entered)
	assert entered<450000
	spkid = 2000000 + entered
	print spkid
	r = requests.get("http://www.asterank.com/api/asterank?query={\"spkid\":"+str(spkid)+"}&limit=1")   
	dat = r.json()[0]

	name = dat['name']
	if name=="":
		name = "None given"
	price = "approximately $"+str(dat['price'])
	if price=="$0.0":
		price = "an unknown amount"
	ID = str(dat['spkid'])
	closeness = str(dat['closeness'])
	
	config.canv.create_text(200, 50, width = 300, text="Name: "+name+"\nID:"+ID+"\nIt will cost "+price+" to mine this asteroid.")
	config.canv.pack()