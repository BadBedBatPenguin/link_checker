## Links checker

Links checker is a small CLI app that gets responses from given links and shows response codes for main HTTP methods.

## How to run project

Clone repo and move to its directory:

```Shell
git clone https://github.com/BadBedBatPenguin/link_checker.git
cd link_checker
```

Upgrade pip and install dependencies from requirements.txt:

```Shell
pip install --upgrade pip
pip install -r requirements.txt
```

Run tests:

```Shell
pytest
```

## Running project
To get info on web sites just use command "get" and give as much URLs as you need separated with whitespace:

```Shell
python -m links_checker get https://google.com https://github.com
```
## Autor

Tsyos Max ([BadBedBatPenguin](https://github.com/BadBedBatPenguin))
(time taken to make this app is about 6-8 hours)
