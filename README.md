## FunUtils

 Some codes I wrote to help me with errands. it really made my life easier hope it does for you too ^^

## Requirement

* Python 2.7
* Python 3.x


### Installing

1. clone

```
git clone https://github.com/HoussemCharf/FunUtils.git
```

2. open terminal & execute 
```
python CodeToExecute.py
```

3. Enjoy !


## Contributing

Feel free to contribute in this all you have to do is submit a pull request.

## Contents description

1. **Blockchain** : A small python based application to create a blockchain in less than 50 lines of code.

2. **Bots** : Creates a linkedIn viewer bot that scrapes linkedIn profiles using beautifulsoup.

3. **CSS-JS_minimiser** : JS/HTML page for the purpose of minifying CSS/Javascript codes.

4. **CSV Data Handler**: A console program to delete rows or columns from a CSV file.

```
    Usage:
        python code.py -i sample.csv -o output.csv  -m (row or col) -n 3
```

5. **Extension Changer** : a Python based application capable of changing all extentions of files in same folder to a given one.

6. **FolderExSorter** : a Python based application that sorts a folder according to files extentions.

```
   Example:

   Folder                                           Folder
   |-Music1.mp3       Python FolderExSorter.py      |-MP3
   |-Music2.mp3       =======================>      | |-Music1.mp3
   |-Music3.mp4                                     | |-Music2.mp3
   |-file.pdf                                       |-MP4
                                                    | |-Music3.mp4
                                                    |-PDF
                                                    | |-file.pdf
```

7. **Letter to words** : Python code to convert scrambled letters to words.

8. **MorningAlarm** : A small Python code for morning alarm.

9. **Pandora Web browser script** : a small Javascript code for tamper Monkey to keep pandora playing none stop without "are you still listening popup".

10. **Proxy Grabber** : A console based Python application capable of providing fresh proxy servers list everytime you excute it.

11. **Sorting Algorithms** : Various small sorting functions that return a result given a set of parameters.

12. **Torrent Checker** : Checks the IP address of a torrents to make sure they can be connected too.

13. **MyYoutubeLikedMusicVideosDownloader** : a Python based application capable of parsing your youtube account Like history and download ONLY Music category as an MP3 format.

14. **RasPiPowerOff**: Turn off your Raspberry Pi with a button on your Smartphone.

15. **Wallpaper**: A python script for downloading bing wallpaper of the day and setting it up as the desktop background image. (Ubuntu only)

16. **Xkcd**: A python script for downloading xkcd comics at a given directory
```
python3 xkcd.py n d
-n: no of comics to downlaod
-d: directory where it needs to be downloaded
```

17. **Backup**: A script for backing up files using git. Usage:
   - Create a Github/Gitlab repository (Init and fetching remote)
   - Add backup.py and list.json as mentioned
   - Fill the list.json file with things to backup
   - Run backup.py with varioius arguments
```
python backup.py backup
python backup.py push
python backup.py restore
```

list.json

```
[
  [
    "path_to_original_file",
    "Name of file in current directory"
  ],
  [
    ...
  ],
]
```

18. **ToDo**: A python script that notifies you according to your todo list

19. **Bad Link Filter**: A python script that filters all the dangerous links out of a list using [spoopy.link](https://spoopy.link/).

20. **Net Job Creation**: A python script that queries the US Census Bureau's database to get a trend of net job creation from 1980 - 2014. More info on the classifiers in the data [here](https://www.census.gov/data/developers/data-sets/business-dynamics.html)

## Authors

* **Houssem Charfeddine** - *FunUtils* - [HC](https://github.com/HoussemCharf)
* **Marco Bakera** - *RasPiPoweroff* - [Pintman](https://github.com/pintman)
* **Shashank S** - *Backup,Get Comics,Wallpaper* - [talsperre](https://github.com/talsperre)
* **Aditya Y** - *ToDo* - [Screwed-U-Head](https://github.com/Screwed-Up-Head)
* **Bart E** - *Bad Link Filter* - [Callidus](https://github.com/Baev1)
## License

codes are licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

