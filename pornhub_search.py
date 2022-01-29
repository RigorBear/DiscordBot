import pornhub

a = ['ass', "boobs"]

client = pornhub.PornHub("5.135.164.72", 3128, a)

for photo_url in client.getPhotos(5):
    print(photo_url)

for video in client.getVideos(10,page=2):
    print(video)