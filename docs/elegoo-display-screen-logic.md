# Elegoo Neptune 3 Series — DGUS/TJC Display Screen Logic

## Overview

The Elegoo Neptune 3 Pro / Plus / Max uses a Nextion-style DGUS display connected via serial (MYSERIAL1). The Marlin firmware communicates with the display using a custom RTS (Real-Time Screen) protocol over serial. Screen navigation and UI state are managed through the `RTSSHOW` class in `DGUSDisplayDef.cpp`.

**Display Protocol:**
- Frame header: `0x5A 0xA5`
- Commands: `0x80` (write reg), `0x81` (read reg), `0x82` (write var), `0x83` (read var)
- Termination: `\xFF\xFF\xFF`

---

## Screen Map

| Page ID | Nextion File | Description |
|---------|-------------|-------------|
| 0 | `main.txt` | Main home screen |
| 1 | `file1.txt`–`file5.txt` | SD Card file browser (5 pages, 5 files each) |
| 8 | `printfiles.txt` | Print file browser (8 items, shows dirs + .gcode) |
| 10 | `printpause.txt` | Print pause screen (paused state) |
| 11 | `printpause.txt` | Printing screen (active print) |
| 12 | `printpause.txt` | SD card pause screen (SD paused) |
| 25 | `pauseconfirm.txt` | Pause confirmation dialog |
| 26 | `resumeconfirm.txt` | Stop/Resume confirmation dialog |
| 27 | `wait.txt` | Processing / Please wait screen |
| 28 | `adjusttemp.txt` | Temperature adjustment screen |
| 34 | `ledcontrl.txt` | LED/Light control screen |
| 42 | `multiset.txt` | Advanced settings screen |
| 44 | `leveldata.txt` | Bed leveling data display |
| 46 | `nosdcard.txt` | No SD card screen |
| 47 | `main.txt` | No SD card on main |
| 49 | `leveling_*.txt` | Bed leveling mesh points |
| 51 | `adjusttemp.txt` | Temp adjustment (via icon) |
| 52 | `adjustspeed.txt` | Speed/Flow adjustment |
| 53 | `adjustzoffset.txt` | Z-offset adjustment |
| 69 | `printpause.txt` | Resume icon state |
| 70 | `language.txt` | Language selection |
| 75 | `ledcontrl.txt` | LED control (via icon) |
| 76 | `multiset.txt` | PLR disabled icon |
| 77 | `multiset.txt` | PLR enabled icon |
| 78 | `information.txt` | Machine info screen |
| 80 | `printfiles.txt` | File browser (via icon) |
| 88 | `multiset.txt` | Advanced settings (via icon) |
| 140 | `speedsetting.txt` | Max speed/accel settings |
| 181 | `leveldata.txt` | Bed level data (via icon) |
| 194 | `printfiles.txt` | Print files (via icon) |
| 195 | `printfiles.txt` | Print files press state |
| 218 | `prefilament.txt` | Filament load/unload pre-screen |
| 236 | `heatfilament.txt` | Filament heating screen |
| 247 | `noFilamentPush.txt` | No filament push warning |
| 254 | `warn1_filament.txt` | Filament warning 1 |
| 255 | `warn2_filament.txt` | Filament warning 2 |
| 262 | `prefilament.txt` | Filament pre-screen |
| 277 | `printcnfirm.txt` | Print confirmation |
| 286 | `continueprint.txt` | Continue print dialog |
| 317 | `info.txt` | Info screen |
| 330 | `adjustzoffset.txt` | Z-offset (via icon) |
| 349 | `leveling.txt` | Bed leveling screen |
| 362 | `autohome.txt` | Auto home screen |
| 381 | `motorsetting.txt` | Motor settings |
| 394 | `motorsetvalue.txt` | Motor set value |
| 407 | `motortest.txt` | Motor test screen |
| 420 | `hardwaretest.txt` | Hardware test screen |
| 433 | `err_heatfail.txt` | Heater failure error |
| 446 | `err_bedheat.txt` | Bed heat error |
| 459 | `err_bedover.txt` | Bed overheat error |
| 472 | `err_bedunder.txt` | Bed underheat error |
| 485 | `err_nozzleheat.txt` | Nozzle heat error |
| 498 | `err_nozzleover.txt` | Nozzle overheat error |
| 511 | `err_nozzleunde.txt` | Nozzle underheat error |
| 524 | `err_homefail.txt` | Homing failure error |
| 537 | `err_probefail.txt` | Probe failure error |
| 550 | `err_sd.txt` | SD card error |
| 563 | `err_sdread.txt` | SD read error |
| 576 | `err_sdwrite.txt` | SD write error |
| 589 | `warn_aux.txt` | Auxiliary warning |
| 602 | `warn_rdlevel.txt` | Read level warning |
| 615 | `warn_zoffset.txt` | Z-offset warning |
| 628 | `factorysetting.txt` | Factory reset screen |
| 641 | `cancleheat.txt` | Cancel heat screen |
| 654 | `askprint.txt` | Ask print dialog |
| 667 | `printfinish.txt` | Print finish screen |
| 680 | `filamentresume.txt` | Filament resume screen |
| 693 | `nofilament.txt` | No filament screen |
| 706 | `keybdB.txt` | Keyboard input screen |
| 719 | `languageset.txt` | Language set screen |
| 732 | `speedsetvalue.txt` | Speed set value screen |
| 745 | `tempset.txt` | Temperature set screen |
| 758 | `tempsetvalue.txt` | Temp set value screen |
| 771 | `leveling_aux.txt` | Leveling auxiliary |
| 784 | `leveling_16.txt` | Leveling 16-point |
| 797 | `leveling_25.txt` | Leveling 25-point |
| 810 | `leveling_36.txt` | Leveling 36-point |
| 823 | `leveling_49.txt` | Leveling 49-point |
| 836 | `leveling_63.txt` | Leveling 63-point |
| 849 | `leveling_64.txt` | Leveling 64-point |
| 862 | `leveldata_aux.txt` | Level data auxiliary |
| 875 | `leveldata_16.txt` | Level data 16-point |
| 888 | `leveldata_25.txt` | Level data 25-point |
| 901 | `leveldata_36.txt` | Level data 36-point |
| 914 | `leveldata_49.txt` | Level data 49-point |
| 927 | `leveldata_64.txt` | Level data 64-point |
| 940 | `aux49_data.txt` | Aux 49 data points |
| 953 | `aux63_data.txt` | Aux 63 data points |
| 966 | `aux64_data.txt` | Aux 64 data points |
| 979 | `tips_level.txt` | Leveling tips |
| 992 | `boot.txt` | Boot/logo screen |

---

## Main Screen (`main.txt` — Page 0)

### Layout
- **Top bar**: Machine name, firmware version
- **Center**: Nozzle temp / Bed temp display
- **Bottom tab bar** (4 tabs, language-dependent):
  - Tab 0: **Print** (打印 / Print / Imprimir / Imprimer / Stampa / Печать / Drucken / プリント)
  - Tab 1: **Prepare** (准备 / Prepare / Preparación / Préparer / Preparare / Подготовить / Vorbereiten / 準備)
  - Tab 2: **Settings** (设置 / Settings / Ajustes / Réglages / Impostazioni / Настройки / Einstellungen / 設定)
  - Tab 3: **Level** (调平 / Level / Nivel / Niveler / Livello / Уровень / Niveau / レベル)

### Navigation
| Tab | Target Page |
|-----|------------|
| Print (t0) | Page 8 — `printfiles.txt` (file browser) |
| Prepare (t1) | Page 218 — `prefilament.txt` (filament menu) |
| Settings (t2) | Page 88 — `multiset.txt` (settings) |
| Level (t3) | Page 349 — `leveling.txt` (bed leveling) |

### Live Updates
- Nozzle temp: `main.nozzletemp.txt` = `"current / target"` (e.g., `"200 / 200"`)
- Bed temp: `main.bedtemp.txt` = `"current / target"`
- X axis: `main.xvalue.val` = position × 100
- Y/Z coordinates updated via `RTS_SndData`

### Buttons

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| Print tab (m0) | 18 | Send read-var to `0x1002` | `MainPageKey` (0x1002) | 1 |
| Prepare tab (m1) | 24 | Navigate to `premove` page | — | — |
| Settings tab (m2) | 26 | Navigate to `set` page | — | — |
| Level tab (m3) | 22 | Navigate to `warn_rdlevel` page | — | — |
| Machine model pic (p0) | 11 | Updates based on `main.va0.val` | — | — |

### Key Actions

| Key Enum | Key Data | Action |
|----------|----------|--------|
| `MainPageKey` | 1 | SD card update, navigate to `printfiles` (multifile) or `file1` (single), or `nosdcard` if no card |
| `MainPageKey` | 2 | Abort print: clear queue, quickstop steppers, stop timers, reset progress/time VPs |
| `MainPageKey` | 3 | Toggle fan icon (head0 and head1) |
| `MainPageKey` | 4 | Update filament sensor icon based on `enable_filment_check` |
| `MainPageKey` | 5 | Update dual X carriage mode icons (two-color/copy/mirror/single) |
| `MainPageKey` | 6 | SD card file list refresh |
| `MainPageKey` | 8 | Set `Multifile_flag=false` (single file mode) |
| `MainPageKey` | 9 | Set `Multifile_flag=true` (multi-file mode) |

---

## File Browser Screens

### `file1.txt`–`file5.txt` (Pages 1–5)
- Standard SD card file list
- 5 files per page, up to 25 files total
- Touch press on file row sends var read command (`0x83`) with file index
- Touch release sends command `0x83` with index to select file

### `printfiles.txt` (Page 8)
- Shows 8 items (files + directories)
- Icons: `192` = file, `193` = directory, `196` = default/clear
- Touch on t0 (up arrow): page up in directory
- Touch on directory row: sends `0x83 0x10 0x02 0x01 0x00 0x07` (enter directory)
- Touch on file row: sends `0x83 0x22 0x04 0x01 0x00 0x00`–`0x07` (select file)

### Buttons

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| t0 (up arrow) | — | Send `0x83 0x10 0x02 0x01 0x00 0x07` — page up | — | — |
| File rows (8 items) | — | Touch press reads var; touch release writes index to select | `SelectFileKey` (0x2199) | file index (0-7) |

---

## Print Pause / Resume Screen (`printpause.txt` — Page 10/11/12)

### States
| State | Page | Button Labels (EN) |
|-------|------|-------------------|
| Not printing / idle | 10 | Settings / Pause / Stop / Printing |
| Printing | 11 | Settings / Pause / Stop / Printing |
| SD paused | 12 | Settings / Resume / Stop / Printing |

### Buttons

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| Settings (set) | 30 | Navigate to `adjusttemp` | `AdjustmentKey` (0x1004) | 1 |
| Pause/Resume (pause) | 33 | If `restFlag1==1`: resume; else show pause confirm | `ResumePrintKey` (0x100C) / `PausePrintKey` (0x100A) | 1 / 0x01 |
| Stop (stop) | 31 | Navigate to `resumeconfirm` | `StopPrintKey` (0x1008) | 0xF0 |
| LED (led) | 44 | Toggle LED3 | `BedLevelFunKey` (0x1044) | 0x08 |
| Printing (t4) | — | Status indicator | — | — |

### Pause Flow
1. User presses Pause → `PausePrintKey` case
2. `waitway = 1` (block input), `pause_action_flag = true`
3. Show `wait.txt` (Page 27)
4. `ExtUI::pausePrint()` called
5. After pause completes → show Page 10 or 11

### Resume Flow (`ResumePrintKey` case, data[0] == 1)
1. Check filament sensor
2. Send `G92.9 E<pause_e>` to restore extruder position
3. Call `ExtUI::resumePrint()`
4. Update time, set `sdcard_pause_check = true`
5. Show Page 11

### M600 Filament Change Resume (data[0] == 3)
1. Update filament sensor icons
2. If `RTS_M600_Flag` → call `marlin.user_resume()`, clear flag
3. Show Page 680 (`filamentresume.txt`)

### Power Loss Continue Resume (data[0] == 4)
1. Restore file name, send `M23 <filename>` (lowercase) + `M24`
2. Show pause screen with picture preview
3. Set `PoweroffContinue = true`

### Key Actions

| Key Enum | Key Data | Origin Page | Action |
|----------|----------|-------------|--------|
| `AdjustmentKey` | 1 | 10/11/12 | Navigate to `adjusttemp` page |
| `AdjustmentKey` | 2 | 10/11/12 | Show correct pause page (10/11/12) based on print state |
| `StopPrintKey` | 0xF0 | 10/11/12 | Show appropriate pause page (11 if printing, 12 if SD paused, 10 otherwise) |
| `PausePrintKey` | 0xF1 | 10/11/12 | Pause print: set `waitway=1`, call `ExtUI::pausePrint()`, show wait page |
| `PausePrintKey` | 0x01 | 10/11/12 | Show `pauseconfirm` page if still printing |
| `ResumePrintKey` | 1 | 10/11/12 | Resume print: check filament, enqueue G92.9 E, call `ExtUI::resumePrint()`, show page 11 |
| `ResumePrintKey` | 2 | 10/11/12 | M600 filament change resume: check filament, preheat if needed, send M23/M24 |
| `ResumePrintKey` | 3 | 10/11/12 | Power loss recovery resume: update filament icons, call `marlin.user_resume()`, show `filamentresume` |
| `ResumePrintKey` | 4 | 10/11/12 | SD card resume: mount card, start/resume file printing, show page 11 |

### Confirmation Dialogs

**Pause Confirmation (Page 25 — `pauseconfirm.txt`)**

| Button | Key Enum | Key Data |
|--------|----------|----------|
| Confirm/Cancel | `PausePrintKey` (0x100A) | 0x01 |

**Stop/Resume Confirmation (Page 26 — `resumeconfirm.txt`)**

| Button | Key Enum | Key Data |
|--------|----------|----------|
| Confirm/Cancel | `StopPrintKey` (0x1008) | 1 / 0xF1 / 0xF0 |

---

## Temperature Adjustment Screen (`adjusttemp.txt` — Page 28/51)

### Layout
- Top icons: Nozzle, Heatbed, Load, Unload, Filament, Speed, Adjust
- `va0` = 1 (nozzle tab selected), `va1` = 3 (10°C unit)
- `targettemp` number box shows target temp

### Controls
| Input | Action |
|-------|--------|
| Nozzle temp set | `M104 S<temp>` |
| Bed temp set | `M140 S<temp>` |
| Fan toggle | `thermalManager.set_fan_speed(0, 0/255)` |
| Fan2 toggle | `thermalManager.set_fan_speed(1, 0/255)` |

### Sub-pages
- `adjustspeed.txt` (Page 52) — Speed/Flow/Fan adjustment
- `adjustzoffset.txt` (Page 53) — Z-offset adjustment

### Buttons

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| Nozzle icon (q1) | 6 | Select nozzle temp tab | `TempScreenKey` (0x1030) | 1 |
| Heatbed icon (q2) | 7 | Select bed temp tab | `TempScreenKey` (0x1030) | 3 |
| Load icon (q3) | 4 | Navigate to filament load | `SettingScreenKey` (0x103E) | 0x0A |
| Unload icon (q4) | 5 | — | — | — |
| Speed icon (q5) | 1 | Navigate to speed adjustment | `AdjustmentKey` (0x1004) | 6 |
| Z-offset icon (q6) | 2 | Navigate to Z-offset adjustment | `AdjustmentKey` (0x1004) | 7 |
| Adjust icon (q7) | 3 | Advanced accel/speed settings | `TempScreenKey` (0x1030) | 0x0F / 0x10 |
| Filament icon (q8) | 8 | Navigate to filament screen | `SettingScreenKey` (0x103E) | 2 |
| targettemp (number box) | 20 | Set target temperature | `Heater0TempEnterKey` (0x1034) / `HotBedTempEnterKey` (0x103A) | temp value |

### Key Actions

| Key Enum | Key Data | Origin Page | Action |
|----------|----------|-------------|--------|
| `TempScreenKey` | 1 | 28/51 | Select nozzle tab: `temp_ctrl=1`, send nozzle target to display |
| `TempScreenKey` | 3 | 28/51 | Select bed tab: `temp_ctrl=0`, send bed target to display |
| `TempScreenKey` | 5 | 28/51 | Unit 1°C: `unit=1`, update icon |
| `TempScreenKey` | 6 | 28/51 | Unit 5°C: `unit=5`, update icon |
| `TempScreenKey` | 7 | 28/51 | Unit 10°C: `unit=10`, update icon |
| `TempScreenKey` | 8 | 28/51 | ++ temperature: increment target by `unit` |
| `TempScreenKey` | 9 | 28/51 | -- temperature: decrement target by `unit` |
| `TempScreenKey` | 0x0A | 28/51 | Speed tab: `speed_ctrl=1`, navigate to `adjustspeed` |
| `TempScreenKey` | 0x0B | 28/51 | Flow tab: `speed_ctrl=2`, navigate to `adjustspeed` |
| `TempScreenKey` | 0x0C | 28/51 | Fan tab: `speed_ctrl=3`, navigate to `adjustspeed` |
| `TempScreenKey` | 0x0D | 28/51 | ++ speed/flow/fan: increment based on `speed_ctrl` |
| `TempScreenKey` | 0x0E | 28/51 | -- speed/flow/fan: decrement based on `speed_ctrl` |
| `TempScreenKey` | 0x0F | 28/51 | Advanced set max speed: `advaned_set=1` |
| `TempScreenKey` | 0x10 | 28/51 | Advanced set max accel: `advaned_set=2` |
| `TempScreenKey` | 0x11-0x14 | 28/51 | -- max feedrate/accel for X/Y/Z/E axes |
| `TempScreenKey` | 0x15-0x18 | 28/51 | ++ max feedrate/accel for X/Y/Z/E axes |
| `TempScreenKey` | 0xF1 | 28/51 | Cancel all: clear all targets, navigate to page 15 |
| `TempScreenKey` | 0xF0 | 28/51 | Cancel: navigate to page 15 |
| `Heater0TempEnterKey` | temp value | 28/51 | Set hotend 0 target temperature (byte-swap on TJC displays) |
| `HotBedTempEnterKey` | temp value | 28/51 | Set bed target temperature (byte-swap on TJC displays) |
| `SettingScreenKey` | 0x0A | 28/51 | Navigate to `prefilament` page |
| `SettingScreenKey` | 2 | 28/51 | Filament preheat |

---

## Speed/Flow Adjustment (`adjustspeed.txt` — Page 52)

### Controls
| Button | Action |
|--------|--------|
| Print Speed | `motion.feedrate_percentage = val` |
| Flow | `planner.flow_percentage[0] = val`, `planner.refresh_e_factor(0)` |
| Fan | `thermalManager.set_fan_speed(0, val)` |
| Reset Speed | Set to 100% |
| Reset Flow | Set to 100% |

### Buttons

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| targetspeed (number box) | — | Display/adjust speed, flow, or fan value | — | — |
| Reset Speed button | — | Reset feedrate to 100% | `AdjustmentKey` (0x1004) | 8 |
| Reset Flow button | — | Reset flow to 100% | `AdjustmentKey` (0x1004) | 9 |
| Fan full button | — | Set fan to 255 | `AdjustmentKey` (0x1004) | 0x0A |

### Key Actions

| Key Enum | Key Data | Origin Page | Action |
|----------|----------|-------------|--------|
| `AdjustmentKey` | 6 | 28/51 | Navigate to speed screen: `speed_ctrl=1`, send feedrate % |
| `AdjustmentKey` | 8 | 52 | Reset speed: `motion.feedrate_percentage=100` |
| `AdjustmentKey` | 9 | 52 | Reset flow: `planner.flow_percentage[0]=100` |
| `AdjustmentKey` | 0x0A | 52 | Fan full: `thermalManager.fan_speed[0]=255` |

---

## Z-Offset Adjustment (`adjustzoffset.txt` — Page 53)

### Controls
| Input | Action |
|-------|--------|
| Z-offset value | `zprobe_zoffset = val / 100` |
| Apply | `babystep.add_mm(Z_AXIS, zprobe_zoffset - last_zoffset)` |
| Probe offset | `probe.offset.z = zprobe_zoffset` |

Unit modes: 0.1mm (icon 1), 0.01mm (icon 2)

### Buttons

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| z_offset (number box) | — | Set Z-offset value | `ZOffsetKey` (0x1026) | signed 16-bit / 100 |
| Unit icons (q5/q6/q7) | — | Toggle unit: 0.1mm / 0.01mm / 1mm | `BedLevelFunKey` (0x1044) | 4 / 5 / 6 |

### Key Actions

| Key Enum | Key Data | Origin Page | Action |
|----------|----------|-------------|--------|
| `AdjustmentKey` | 7 | 28/51 | Navigate to Z-offset screen, set unit to 0.1mm |
| `ZOffsetKey` | signed 16-bit / 100 | 53 | Apply babystepping, update `probe.offset.z` |
| `BedLevelFunKey` | 4 | 349 | Unit 0.01mm |
| `BedLevelFunKey` | 5 | 349 | Unit 0.1mm |
| `BedLevelFunKey` | 6 | 349 | Unit 1mm |

---

## Settings Screen (`multiset.txt` — Page 42/88)

### Menu Items
| Item | Target Page | Description |
|------|------------|-------------|
| Advanced Settings (t0) | — | Title |
| Key Sound (t1) | — | Beep enable/disable |
| Backlight (t2) | — | Screen brightness |
| Motor Settings (t5) | 381/407 | Motor test/settings |
| Speed Settings (t6) | 140 | Max speed/accel |
| Resume Printing (t7) | — | PLR toggle (`plr.pic`) |
| Multiple File Display (t8) | — | `Multifile_flag` toggle |

### PLR Icon
- `plr.pic=77` → PLR enabled
- `plr.pic=76` → PLR disabled

### Multifile Display
- `multiset.file.pic=77` → multifile enabled
- `multiset.file.pic=76` → single file mode

### Buttons

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| Backlight icon (q4) | 20 | Toggle backlight on/off | — | — |
| Settings (m0) | 12 | Navigate to `set` page | — | — |
| Key Sound (keysound) | 8 | Toggle beep on/off | — | — |
| PLR (plr) | 22 | Toggle PLR | `PowerContinuePrintKey` (0x105F) | 3 |
| Multifile (file) | 24 | Toggle multifile mode | `MainPageKey` (0x1002) | 8 / 9 |
| Brightness slider (h0) | 9 | Set backlight brightness | — | — |

### Key Actions

| Key Enum | Key Data | Origin Page | Action |
|----------|----------|-------------|--------|
| `SettingScreenKey` | 0x0D | 42/88 | Read PLR enabled/disabled state, navigate to multiset |
| `PowerContinuePrintKey` | 1-3 | 42/88 | PLR enable/disable, resume, cancel |
| `MainPageKey` | 8 | 42/88 | Set `Multifile_flag=false` (single file mode) |
| `MainPageKey` | 9 | 42/88 | Set `Multifile_flag=true` (multi-file mode) |

### Model Detection (`main.va0.val`)
| Value | Model |
|-------|-------|
| 1 | Neptune 3 Pro (225×225×280) |
| 2 | Neptune 3 Plus (320×320×400) |
| 3 | Neptune 3 Max (420×420×500) |

---

## Language Screen (`language.txt` — Page 70)

### Languages (8 total)
| Index | Language |
|-------|----------|
| 0 | Chinese (Simplified) |
| 1 | English |
| 2 | Spanish |
| 3 | French |
| 4 | Italian |
| 5 | Russian |
| 6 | German |
| 7 | Japanese |

Selected language highlighted with icon `133`, others show `70`.

### Buttons

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| Language options (8 icons) | — | Select language | `SelectLanguageKey` (0x105C) | 1-8 |

### Key Actions

| Key Enum | Key Data | Origin Page | Action |
|----------|----------|-------------|--------|
| `SelectLanguageKey` | 1 | 70 | Chinese (Simplified) |
| `SelectLanguageKey` | 2 | 70 | English |
| `SelectLanguageKey` | 3 | 70 | Spanish |
| `SelectLanguageKey` | 4 | 70 | French |
| `SelectLanguageKey` | 5 | 70 | Italian |
| `SelectLanguageKey` | 6 | 70 | Russian |
| `SelectLanguageKey` | 7 | 70 | German |
| `SelectLanguageKey` | 8 | 70 | Japanese |

---

## Machine Info Screen (`information.txt` — Page 78)

### Displayed Info
| Field | Source |
|-------|--------|
| Machine | `PRINTER_MACHINE_TEXT_VP` (model name) |
| Size | `PRINTER_PRINTSIZE_TEXT_VP` (X×Y×Z) |
| Firmware Version | `SOFTVERSION` |
| UI Version | `LCDVERSION` (optional) |
| Manufacturer | `CORP_WEBSITE` |
| Contact | Website URL |

---

## LED Control Screen (`ledcontrl.txt` — Page 34/75)

### Controls
- LED toggle via `OUT_WRITE(LED3_PIN, HIGH/LOW)`
- Timer `tm0` runs while on page, stops on page exit

### Buttons

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| LED toggle | — | Toggle LED2/LED3 | `BedLevelFunKey` (0x1044) | 7 / 8 |
| Timer tm0 | — | Runs while on page, reads LED status | — | — |

---

## Bed Leveling Screens

### `leveling.txt` (Page 349)
- Entry point for bed leveling operations
- Sub-modes based on `AUTO_BED_LEVELING_BILINEAR`

### `leveldata.txt` (Page 44/181)
- Shows Z-offset value: `leveldata.z_offset.val = zprobe_zoffset * 100`
- Shows mesh points: `leveldata.x0.val` through `leveldata.x11.val`
- Values ≥ 2647 are cleared to 0

### Model-specific mesh screens
| Model | Screen File | Points |
|-------|------------|--------|
| Neptune 3 Pro | `leveling_36.txt` / `leveldata_36.txt` | 6×6 |
| Neptune 3 Plus | `leveling_49.txt` / `aux49_data.txt` | 7×7 |
| Neptune 3 Max | `leveling_63.txt` / `aux63_data.txt` | 8×8 |

### Buttons (Page 349)

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| Home Z | — | Home Z for leveling | `BedLevelFunKey` (0x1044) | 1 |
| Babystep +Z | — | Increment zprobe_zoffset | `BedLevelFunKey` (0x1044) | 2 |
| Babystep -Z | — | Decrement zprobe_zoffset | `BedLevelFunKey` (0x1044) | 3 |
| Unit 0.01mm | — | Set unit | `BedLevelFunKey` (0x1044) | 4 |
| Unit 0.1mm | — | Set unit | `BedLevelFunKey` (0x1044) | 5 |
| Unit 1mm | — | Set unit | `BedLevelFunKey` (0x1044) | 6 |
| LED2 toggle | — | Toggle LED2 | `BedLevelFunKey` (0x1044) | 7 |
| LED3/caselight | — | Toggle caselight | `BedLevelFunKey` (0x1044) | 8 |
| G29 auto-level | — | Run G29 | `BedLevelFunKey` (0x1044) | 9 |
| Update info | — | Refresh printpause info | `BedLevelFunKey` (0x1044) | 10 |
| Update temps | — | Refresh main temps | `BedLevelFunKey` (0x1044) | 11 |
| Boot/model | — | Model info | `BedLevelFunKey` (0x1044) | 12 |
| Leveling points 1-7 | — | Move to mesh points | `BedLevelFunKey` (0x1044) | 0x0D-0x13 |
| Reset bed level | — | Reset leveling | `BedLevelFunKey` (0x1044) | 0x14 |
| Save EEPROM | — | Save settings | `BedLevelFunKey` (0x1044) | 0x15 |
| Refresh after resume | — | Refresh printpause | `BedLevelFunKey` (0x1044) | 0x16 |

### Key Actions (Page 181)

| Key Enum | Key Data | Origin Page | Action |
|----------|----------|-------------|--------|
| `BedLevelFunKey` | 10 | 349 | Update printpause page info (speed, time, percent) |
| `BedLevelFunKey` | 11 | 349 | Update main screen temps |

### Leveling Mesh Screens (Pages 771/784/797/810/823/836/849)

| Key Enum | Key Data | Origin Page | Action |
|----------|----------|-------------|--------|
| `BedLevelFunKey` | 0x0D-0x13 | 349 | Move to leveling mesh points 1-7 |

---

## Boot Screen (`boot.txt` — Page 992)

### Flow
1. Display logo (picture 89)
2. Progress bar `j0.val` animates 0→100
3. After boot → navigate to `main` (Page 0)
4. If power loss recovery valid → show `continueprint.txt` with filename and picture preview
5. If no recovery → show `main` directly

### Picture Preview (from SD)
- Searches G-code for `;simage:` marker
- Reads image data in chunks, sends to display via `printpause.va0.txt` / `printpause.va1.txt`
- Stops at `M10086` marker or 100KB limit
- Writes accumulated text to `printpause.cp0` picture object

---

## Wait Screen (`wait.txt` — Page 27)

### Purpose
- Shown during processing operations
- Text: "Processing please wait" (multi-language)
- Auto-returns to previous page via `losspage` variable after timeout
- Touch press resets idle timer

### Buttons

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| Touch press | — | Reset idle timer (`rest_count=0`) | — | — |

> **Note:** Input is blocked when `waitway > 0`. `RTS_HandleData()` returns immediately. Auto-returns to `losspage` after timeout.

---

## Filament Screens

### `prefilament.txt` (Page 218/262)
- Menu: Move, Temp, Extruder, Load, Unload
- Navigation to sub-pages for each operation

### `heatfilament.txt` (Page 236)
- Preheat nozzle to filament change temperature
- Shows current vs target temp

### `nofilament.txt` / `warn1_filament.txt` / `warn2_filament.txt`
- Filament runout warnings
- Icon-based status: `CHANGE_FILAMENT_ICON_VP`

### `filamentresume.txt` (Page 680)
- Shown after filament change complete
- Returns to print or main screen

### Buttons (Pages 381/394/407)

| Key Enum | Key Data | Origin Page | Action |
|----------|----------|-------------|--------|
| `ResumePrintKey` | 3 | 10/11/12 | Power loss recovery resume: show `filamentresume` after M600 |

### Filament Pre-screen (Pages 218/262 — `prefilament.txt`)

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| Move/Temp/Extruder/Load/Unload | — | Menu navigation | `SettingScreenKey` (0x103E) | 0x0A / 2 |
| Filament length input | — | Set load length | `Heater0LoadEnterKey` (0x1054) | length value |
| Filament speed input | — | Set load speed | `Heater1LoadEnterKey` (0x1058) | speed value |

### Temperature Set Screens (Pages 745/758 — `tempset.txt` / `tempsetvalue.txt`)

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| Nozzle temp ± | — | Adjust preset nozzle temp | `SetPreNozzleTemp` (0x2200) | 1 / 2 |
| Bed temp ± | — | Adjust preset bed temp | `SetPreBedTemp` (0x2201) | 1 / 2 |

---

## Error Screens

| Screen | Condition |
|--------|-----------|
| `err_heatfail.txt` (433) | Heater failure |
| `err_bedheat.txt` (446) | Bed not reaching target |
| `err_bedover.txt` (459) | Bed overheat |
| `err_bedunder.txt` (472) | Bed underheat |
| `err_nozzleheat.txt` (485) | Nozzle not reaching target |
| `err_nozzleover.txt` (498) | Nozzle overheat |
| `err_nozzleunde.txt` (511) | Nozzle underheat |
| `err_homefail.txt` (524) | Homing failure |
| `err_probefail.txt` (537) | Probe failure |
| `err_sd.txt` (550) | SD card error |
| `err_sdread.txt` (563) | SD read error |
| `err_sdwrite.txt` (576) | SD write error |

### Error Screen Keys (Pages 433-615)

| Page | File | Condition | Key Enum | Key Data |
|------|------|-----------|----------|----------|
| 433 | `err_heatfail.txt` | Heater failure | `Err_Control` (0x2203) | — |
| 446 | `err_bedheat.txt` | Bed not reaching target | `Err_Control` (0x2203) | — |
| 459 | `err_bedover.txt` | Bed overheat | `Err_Control` (0x2203) | — |
| 472 | `err_bedunder.txt` | Bed underheat | `Err_Control` (0x2203) | — |
| 485 | `err_nozzleheat.txt` | Nozzle not reaching target | `Err_Control` (0x2203) | — |
| 498 | `err_nozzleover.txt` | Nozzle overheat | `Err_Control` (0x2203) | — |
| 511 | `err_nozzleunde.txt` | Nozzle underheat | `Err_Control` (0x2203) | — |
| 524 | `err_homefail.txt` | Homing failure | `Err_Control` (0x2203) | — |
| 537 | `err_probefail.txt` | Probe failure | `Err_Control` (0x2203) | — |
| 550 | `err_sd.txt` | SD card error | `Err_Control` (0x2203) | — |
| 563 | `err_sdread.txt` | SD read error | `Err_Control` (0x2203) | — |
| 576 | `err_sdwrite.txt` | SD write error | `Err_Control` (0x2203) | — |
| 589 | `warn_aux.txt` | Auxiliary warning | `Err_Control` (0x2203) | — |
| 602 | `warn_rdlevel.txt` | Read level warning | `Err_Control` (0x2203) | — |
| 615 | `warn_zoffset.txt` | Z-offset warning | `Err_Control` (0x2203) | — |

---

## Hardware Test Screen (`hardwaretest.txt` — Page 407)

### Tests
- Nozzle temperature read
- Bed temperature read
- Fan speed read
- SD card test
- Motor test (via `motorsetvalue.txt`)
- LCD version check

### Buttons (Pages 381/394/407)

| Button | ID | Display Side Action | Key Enum | Key Data |
|--------|----|---------------------|----------|----------|
| Unit selection | — | 0.1mm / 1mm / 10mm | `AxisPageSelectKey` (0x1046) | 1 / 2 / 3 |
| G28 commands | — | Full/axis homing | `AxisPageSelectKey` (0x1046) | 4 / 5 / 6 / 7 |
| ±X movement | — | Move X axis | `XaxismoveKey` (0x1048) | 1 / 2 |
| ±Y movement | — | Move Y axis | `YaxismoveKey` (0x104A) | 1 / 2 |
| ±Z movement | — | Move Z axis | `ZaxismoveKey` (0x104C) | 1 / 2 |
| Tool change | — | T0/T1 | `SelectExtruderKey` (0x104E) | 1 / 2 |

### Key Actions (Page 407)

| Key Enum | Key Data | Origin Page | Action |
|----------|----------|-------------|--------|
| `HardwareTest` | — | 407 | Tests nozzle temp, bed temp, fan speed, SD card, motor test, LCD version |

---

## Key State Variables

| Variable | Type | Purpose |
|----------|------|---------|
| `waitway` | char | Input block state (0=normal, >0=blocked) |
| `pause_action_flag` | bool | Pause in progress |
| `sdcard_pause_check` | bool | SD card pause state |
| `print_preheat_check` | bool | Preheat before resume |
| `PoweroffContinue` | bool | Power loss recovery continue |
| `RTS_M600_Flag` | bool | M600 filament change in progress |
| `Home_stop_flag` | bool | Homing in progress |
| `Move_finish_flag` | bool | Move completion |
| `restFlag1` | uint8_t | Pause/resume state flag |
| `restFlag2` | uint8_t | Secondary pause flag |
| `enable_filment_check` | bool | Filament sensor enabled |
| `save_dual_x_carriage_mode` | char | Dual X carriage mode (0-3) |
| `Multifile_flag` | bool | Multi-file display mode |
| `CardUpdate` | bool | SD card file list needs refresh |
| `lcd_sd_status` | bool | Last known SD status |

---

## Update Cycle (`EachMomentUpdate`)

Runs periodically (every `RTS_UPDATE_VALUE` ms):

1. **Power-on init**: Show boot screen, progress bar, then main
2. **Temperature**: Send hotend/bed temps to display
3. **Coordinates**: Send X/Y/Z positions
4. **Print progress**: Send percentage and estimated remaining time
5. **Print time**: Send elapsed hours/minutes
6. **Filament sensor**: Update icon based on sensor state
7. **Fan status**: Update fan icons
8. **LED control**: LED2 status based on Z height and print state
9. **SD card**: Monitor card insertion/removal

---

## G-Code Commands Used

| Command | Purpose |
|---------|---------|
| `G0 Z<pos>` | Move Z axis (pause resume) |
| `G92.9 E<pos>` | Set extruder position (pause resume) |
| `M104 S<temp>` | Set hotend target |
| `M109 S<temp>` | Wait for hotend temp |
| `M140 S<temp>` | Set bed target |
| `M106 S<speed>` | Set fan speed |
| `M23 <file>` | Select SD file |
| `M24` | Start/resume SD print |
| `M84` | Disable steppers |
| `M420 S1` | Apply bed leveling |
| `M500` | Save EEPROM settings |
| `M501` | Load EEPROM settings |
| `M502` | Reset EEPROM settings |
| `M503` | Report EEPROM settings |
| `M504` | Validate EEPROM settings |

---

## Icon Reference

| Icon ID | Meaning |
|---------|---------|
| 1 | Main background |
| 2 | Boot logo |
| 6 | Filament pre-screen |
| 13 | Settings background |
| 30 | File press state |
| 34 | Filament icon |
| 36 | Z-offset icon |
| 37 | Nozzle icon |
| 50 | Wait screen background |
| 51 | Temp adjust background |
| 52 | Speed adjust background |
| 53 | Z-offset adjust background |
| 54 | Temp screen icon |
| 58 | Temp screen icon |
| 69 | Resume icon |
| 70 | Language option (unselected) |
| 75 | LED control background |
| 76 | PLR disabled icon |
| 77 | PLR enabled icon |
| 78 | Info screen background |
| 88 | Advanced settings background |
| 89 | Boot logo picture |
| 133 | Language option (selected) |
| 140 | Speed settings background |
| 150 | Advanced settings icon |
| 181 | Level data background |
| 192 | File icon |
| 193 | Directory icon |
| 194 | Print files background |
| 195 | Print files press state |
| 196 | Default/clear icon |

---

## Variable Address Reference (VP)

| Variable | Purpose |
|----------|---------|
| `HEAD0_SET_TEMP_VP` | Hotend 0 target temp |
| `HEAD1_SET_TEMP_VP` | Hotend 1 target temp |
| `BED_SET_TEMP_VP` | Bed target temp |
| `HEAD0_CURRENT_TEMP_VP` | Hotend 0 current temp |
| `HEAD1_CURRENT_TEMP_VP` | Hotend 1 current temp |
| `BED_CURRENT_TEMP_VP` | Bed current temp |
| `HEAD0_FAN_ICON_VP` | Hotend fan icon |
| `HEAD1_FAN_ICON_VP` | Bed fan icon |
| `MOTOR_FREE_ICON_VP` | Motors disabled icon |
| `PRINT_PROCESS_ICON_VP` | Print progress icon |
| `PRINT_PROCESS_VP` | Print progress percent |
| `PRINT_SPEED_RATE_VP` | Feedrate percentage |
| `PRINT_TIME_HOUR_VP` | Print time hours |
| `PRINT_TIME_MIN_VP` | Print time minutes |
| `PRINT_SURPLUS_TIME_HOUR_VP` | Remaining time hours |
| `PRINT_SURPLUS_TIME_MIN_VP` | Remaining time minutes |
| `AXIS_X_COORD_VP` | X axis coordinate |
| `AXIS_Y_COORD_VP` | Y axis coordinate |
| `AXIS_Z_COORD_VP` | Z axis coordinate |
| `AUTO_BED_LEVEL_ZOFFSET_VP` | Z-offset value |
| `AUTO_BED_LEVEL_1POINT_VP` | Bed mesh point |
| `CHANGE_FILAMENT_ICON_VP` | Filament sensor icon |
| `ICON_FILMENT_DETACT` | Filament detected icon |
| `PRINT_MODE_ICON_VP` | Print mode icon |
| `SELECT_MODE_ICON_VP` | Select mode icon |
| `TWO_COLOR_MODE_ICON_VP` | Two-color mode icon |
| `COPY_MODE_ICON_VP` | Copy mode icon |
| `MIRROR_MODE_ICON_VP` | Mirror mode icon |
| `SINGLE_MODE_ICON_VP` | Single mode icon |
| `PRINT_FILE_TEXT_VP` | Print file name text |
| `SELECT_FILE_TEXT_VP` | Select file name text |
| `FILENAME_NATURE_VP` | Filename number |
| `PRINTER_MACHINE_TEXT_VP` | Machine name |
| `PRINTER_VERSION_TEXT_VP` | Firmware version |
| `PRINTER_PRINTSIZE_TEXT_VP` | Print size |
| `PRINTER_WEBSITE_TEXT_VP` | Website URL |
| `START1_PROCESS_ICON_VP` | Boot progress |
| `SPEED_SET_VP` | Speed set value |
| `ICON_ADJUST_PRINTING_EXTRUDER_OR_BED` | Temp adjust icon |
| `ICON_ADJUST_PRINTING_TEMP_UNIT` | Temp unit icon |
| `ICON_ADJUST_PRINTING_SPEED_FLOW` | Speed/flow icon |
| `ICON_ADJUST_PRINTING_S_F_UNIT` | S/F unit icon |
| `ICON_ADJUST_Z_OFFSET_UNIT` | Z-offset unit icon |
| `ICON_LEVEL_SELECT` | Level select icon |
