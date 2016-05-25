# Unsplash Background

This is a small project that allows gnome type desktops to use images from [Unsplash It](https://unsplash.it).

## Usage

Check out or download the project.

Execute `main.py` for a graphical interface (needs some work).

To automate, you can use the provided `g_random_background.py` script.

```
Usage: g_random_background.py -w <width> -h <height>
```

This should download a random image, and set it as your background. Use crontab to give it a schedule.

**Crontab**

```
0 * * * * /path/to/script/g_random_background.py -w 1920 -h 1080 >/dev/null 2>&1
```

This will update your background at the top of the hour, every hour.

## Notes

- Currently only tested on Mint 17
- The scripts only grab a random image at the moment

Contributions are more than welcome. This is my first Python project and I could use some help on a proper installation method.

## To-Do

- Cache downloaded images for re-use
