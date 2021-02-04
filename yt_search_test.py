from youtubesearchpython import VideosSearch


def get_available_videos(topic,limit=20):
    VS = VideosSearch(topic,limit=limit)
    data = []
    temp = VS.result()
    [data.append(temp["result"][i]["title"]) for i in range(len(temp["result"]))]
    while True:
        try:
            VS.next()
            temp = VS.result()
            [data.append(temp["result"][i]["title"]) for i in range(len(temp["result"]))]
        except:
            break
    VS = None
    return {"result":data}


if __name__ == "__main__":
    #print(get_video_metadata("https://www.youtube.com/watch?v=xC-c7E5PK0Y"))
    data = get_available_videos("Data Science",20)
    print(len(data["result"]))

    