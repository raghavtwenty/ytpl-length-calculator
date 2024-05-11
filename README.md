# YouTube Playlist Length Calculator
_A Python Flask website that calculates the total duration of the videos in a YouTube playlist_
<br><br><br>


### 🌟 EXPERIENCE HERE 🌟
https://ytpl-length-calculator.onrender.com
<br><br><br>


### PROTOTYPE VIDEO
https://github.com/raghavtwenty/ytpl-length-calculator/assets/126254197/5d099cec-d4d4-492a-b882-f4726e4e65e4

<br><br>

### HOW TO EXECUTE

Get the YouTube data v3 API key from <a href="console.cloud.google.com"> console.cloud.google.com </a> <br>
inside .env file
```
YT_API_KEY = "your api key"
```

#### Terminal
```
git clone https://github.com/raghavtwenty/ytpl-length-calculator.git
```
<br>

```
cd ytpl-length-calculator/
```
<br>

Place the .env file in this folder
<br>

```
pip install -r requirements.txt
```
<br>

```
python application.py
```
<br>


### INTRODUCTION
Introducing a Python Flask web application tailored for YouTube enthusiasts and learners alike, providing a convenient solution to gauge the total duration of playlists. By seamlessly integrating YouTube API, users can effortlessly explore playback speed details and customize video ranges, enhancing their viewing experience and learning efficiency.
<br><br><br>


### REQUIRED
- PC or Laptop <br>
- Pogramming language: Python <br>
- Frameworks: Flask <br>
- API: YouTube data V3 API key
<br><br><br>


### WORKING
This is flask web app which can be used to know the total duration of the youtube playlist. <br>
- The flask app is first started, It runs on localhost 5000 (port number).<br>
- The YouTube playlist link is given as the input. <br>
- It retrieves videos details for the given playlist link using YouTube API. <br>
- Asks for custom video range from the user. <br>
- Based on the range, It outputs the playback speed & corresponding duration. 
<br><br><br>


### ADVANTAGES
- Able to find the total duration of the youtube playlist. <br>
- Custom video range of the playlist can be given as the input.
<br><br><br>


### OUTPUT

- Home Page <br><br>
![1](https://github.com/raghavtwenty/ytpl-length-calculator/assets/126254197/f6f8062b-f886-4634-94b5-fd6c2c701d48)


- Videos Page <br><br>
![2](https://github.com/raghavtwenty/ytpl-length-calculator/assets/126254197/88e10fa3-5367-4b76-bd1c-debb8cf5d040)
 

- Output Page <br><br>
![3](https://github.com/raghavtwenty/ytpl-length-calculator/assets/126254197/49d81376-ca79-422e-9928-65222a422325)


- Link Error Handling Page <br><br>
![4](https://github.com/raghavtwenty/ytpl-length-calculator/assets/126254197/33605a91-f73a-4ca8-bbd4-6668119fb47c)


- Video Number Error Handling Page <br><br>
![5](https://github.com/raghavtwenty/ytpl-length-calculator/assets/126254197/c7531e73-b643-478c-8ad0-ee89fd6a293b)

<br><br>

_END OF README_
