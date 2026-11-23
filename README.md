# SuperHub-v2

**SuperHub-v2** is a calm, modern home screen for Supernote: a clock with this month's calendar, ten clean line-icon buttons you name and point at anything, and your recent pages at a glance. It does everything [SuperHub](https://github.com/weedwhitesandwine/SuperHub) does, with a modern look.

SuperHub-v2 is based on [SuperDashboard](https://github.com/AgP42/SuperDashboard) by **AgP42**, used under the MIT licence. Its icons are from [Lucide](https://lucide.dev) (ISC licence). Thank you to AgP42 and the Lucide contributors.

## What it does

- **Home screen**: the clock (date, week number, battery) beside this month's calendar, ten buttons in two rows of five, and your most recent pages as previews. Tap a preview to open it. If a button opens dated notebooks, tap a date on the calendar to open that day's notebook.
- **Buttons are yours**: give each button a picture, a name, a place on the screen, and something to open:
  - a folder, or a note or document
  - any app installed on your Supernote
  - a SuperHub-v2 page: Favourites, Starred pages, Keywords, Search, Note Clips or To-do
  - a **new note**, where you choose its name, folder, page style, handwriting recognition and orientation
  - a **new typed document**, opened in the Supernote's own document editor
  - today's notebook in a folder of dated notebooks (`YYYY/YYYY-MM-DD.note`), for a planner or journal
- **48 line icons** from Lucide, or your own pictures.
- **Starred pages**: every page you drew a five-point star on, as a grid of previews.
- **Note Clips and To-do**: lasso something in a note and tap *SuperHub-v2 Clip* or *SuperHub-v2 To-do* in the lasso toolbar.

## Install

You need Supernote firmware with plugin support: Chauvet **3.29.43 or later** on Manta and Nomad (2.26.40 or later on A5 X and A6 X). SuperHub-v2 was developed on a Manta with 3.31.45.

**From InkHub** (once SuperHub-v2 is listed there): open InkHub on your Supernote, find SuperHub-v2 under Plugins, and install it.

**From this page**:

1. Download `SuperHub-v2.snplg` from [Releases](https://github.com/weedwhitesandwine/SuperHub-v2/releases/latest).
2. Copy it into the **MyStyle** folder on your Supernote (USB cable, Browse & Access, or your cloud sync).
3. On the Supernote: **Settings → Apps → Plugins → Add Plugin**, and choose `SuperHub-v2.snplg`.

## Open it

1. Open any note. In the toolbar, tap the plugin button (the puzzle piece) and choose **SuperHub-v2**.
2. The first time, allow file access when asked. SuperHub-v2 needs it to show your files and save its settings. It never uses the internet.
3. SuperHub-v2 opens on its settings page. Set up your buttons, then tap **Done**.
4. From then on, a small **house** floats over every screen. Tap it to open SuperHub-v2 from anywhere; drag it to move it. (You can hide it in settings and use the toolbar button instead.)

## Set up your buttons

Tap the **gear** at the top left of SuperHub-v2. Tap one of the ten buttons, then:

- **Name**: type the name shown under it.
- **Opens**: choose a folder, a note or document, an app, a SuperHub-v2 page, a new note, a new typed document, or today's notebook.
- **Picture**: choose one of the icons.
- **Place**: choose its position, 1 to 5 on the top row, 6 to 10 on the bottom row.

A fresh install starts with New note, Calendar, To-do and Digest; the other six are empty for you to fill.

**Your own pictures**: copy square PNG or JPG files into `MyStyle/SuperHub-v2/Icons` on your Supernote, then reopen settings. They appear after the built-in icons.

## Your settings

Settings are saved as you change them, in `MyStyle/Plugins/SuperHub-v2/config.json`, with an automatic backup beside it. Updating or reinstalling SuperHub-v2 keeps them. Under **Saved copies of your settings** you can keep named copies and bring them back.

## Permissions

- **File read and write**: to list and open your notes and folders, show previews, make new notes, and save settings in MyStyle.
- **No internet**: SuperHub-v2 works entirely on your Supernote and sends nothing anywhere.

## Build from source

```bash
./buildPlugin.sh           # -> build/outputs/SuperHub-v2.snplg
bash icon-src/build.sh     # regenerate the icons from icon-src/lucide
```

Needs Node 22, JDK 21 and the Android SDK (platform 35, build-tools 35.0.0, NDK 27.1, CMake 3.22). React Native is fixed at 0.79.2 to match the Supernote's plugin host.

## Licence

MIT. See [LICENSE](LICENSE). SuperHub-v2 keeps AgP42's SuperDashboard copyright notice alongside its own. The Lucide icons are under the ISC licence, in [icon-src/lucide/LICENSE](icon-src/lucide/LICENSE).
