# Local English Translations for RimWorld

An English language patch for a personal RimWorld mod collection. It adds **1,006 translation entries across 13 mods**, covering gaps in Chinese, Japanese, and Korean source text.

This is a translation-only mod. It contains no original mod assemblies, textures, or gameplay definitions. Install the original Workshop mods separately. Each translation folder loads only when its corresponding mod is active. You can use any subset of the listed mods.

## Exactly which mods are patched

Names below match the installed mods' metadata. Counts are translation entries, not a claim that every screen or string in a mod is translated. Some mods already have English translations; this patch fills selected gaps.

| Original mod | Steam Workshop | Package ID | Entries |
| --- | --- | --- | ---: |
| 赶海 \| Beach Combing | [3829985020](https://steamcommunity.com/sharedfiles/filedetails/?id=3829985020) | `chickencolonel.beachcombing` | 18 |
| The Dead Man's Switch - Ghost Production Line | [3822948276](https://steamcommunity.com/sharedfiles/filedetails/?id=3822948276) | `administrator.ghostproductionline` | 5 |
| The Dead Man's Switch | [3819799478](https://steamcommunity.com/sharedfiles/filedetails/?id=3819799478) | `aoba.deadmanswitch.core` | 40 |
| Defensive Network | [3754128439](https://steamcommunity.com/sharedfiles/filedetails/?id=3754128439) | `wuhuansuiyue.defensivenetworkexpanded` | 2 |
| Expert Stairs | [3688237449](https://steamcommunity.com/sharedfiles/filedetails/?id=3688237449) | `milple.expertstairs` | 1 |
| 冶龍工业武器包 — Yelong weapon pack | [3632467682](https://steamcommunity.com/sharedfiles/filedetails/?id=3632467682) | `hun.smeltedloongweapon` | 43 |
| The Dead Man's Switch - AssemblyMaster | [3611546460](https://steamcommunity.com/sharedfiles/filedetails/?id=3611546460) | `maple.deadmanswitch.superassemblymaster` | 3 |
| [MR]shadow company | [3041454630](https://steamcommunity.com/sharedfiles/filedetails/?id=3041454630) | `lemontea.shadowcompany` | 10 |
| RimLife Expansion Production Plus | [2523034535](https://steamcommunity.com/sharedfiles/filedetails/?id=2523034535) | `daylight.rlesexpansionproductps` | 833 |
| [Y]Wetware - BandWidthCasket | [3815756779](https://steamcommunity.com/sharedfiles/filedetails/?id=3815756779) | `yushiren.bandwidthcasket` | 6 |
| 鼠族财富扩展-叙事者-雪铁芋 — Ratkin wealth storyteller | [3492795395](https://steamcommunity.com/sharedfiles/filedetails/?id=3492795395) | `thewwworld.ratkinwealthstoryteller` | 2 |
| Ratkin Xenotype | [3368691176](https://steamcommunity.com/sharedfiles/filedetails/?id=3368691176) | `sg.ratkin` | 1 |
| Ancient urban ruins | [3316062206](https://steamcommunity.com/sharedfiles/filedetails/?id=3316062206) | `xmb.ancienturbanruins.mo` | 42 |
| **Total** | | | **1,006** |

Translations include item and building labels, descriptions, recipes, jobs, work labels, storyteller text, and selected narrative rules. Exact coverage is visible in `Translations/<package ID>/Languages/English/DefInjected/`.

## Install on another computer

### 1. Find the correct RimWorld folder

In Steam, right-click **RimWorld → Properties → Installed Files → Browse**. Open the `Mods` folder inside that installation. This also works when Steam uses a custom library drive.

Common locations are:

- Linux: `~/.local/share/Steam/steamapps/common/RimWorld/Mods`
- Windows: `C:\Program Files (x86)\Steam\steamapps\common\RimWorld\Mods`
- macOS: `~/Library/Application Support/Steam/steamapps/common/RimWorld/Mods`

Use Steam's Browse button as the authoritative location. The commands below require Git to be installed.

### 2. Clone the patch into Mods

Open a terminal in the `Mods` folder and run:

```sh
git clone https://github.com/Silkenmeerkat/rimworld-local-english-translations.git LocalEnglishTranslations
```

The resulting layout must be:

```text
RimWorld/
  Mods/
    LocalEnglishTranslations/
      About/
        About.xml
      Common/
      LoadFolders.xml
      Translations/
```

`About` must be directly inside `LocalEnglishTranslations`. Avoid an extra nested repository folder.

### 3. Enable the patch

1. Ensure the original mods you use and their dependencies are installed on this computer.
2. Start RimWorld and select **English** as the game language.
3. Open **Mods** and enable **Local English Translations**.
4. Place it after the patched mods, preferably at the bottom of the mod list.
5. Restart RimWorld when prompted, then load your save.

A save's missing-mod prompt can help identify original mods that need to be installed. This repository does not synchronize saves, subscribe to Workshop mods, or copy your active mod list. Continue using your usual save-transfer method. Enable the translation patch on both computers for the same English text.

### Install without Git

On GitHub, select **Code → Download ZIP**. Extract the archive, rename the extracted folder to `LocalEnglishTranslations`, and place it directly in RimWorld's `Mods` folder. Enable it as described above. ZIP installations must be updated by downloading a fresh copy; `git pull` works only for Git clones.

## Update on the laptop

Close RimWorld. Open a terminal in `Mods/LocalEnglishTranslations` and run:

```sh
git pull --ff-only
```

Then start RimWorld again. For the common Linux installation path, the equivalent command is:

```sh
git -C "$HOME/.local/share/Steam/steamapps/common/RimWorld/Mods/LocalEnglishTranslations" pull --ff-only
```

No GitHub login is needed to clone or pull this public repository over HTTPS. Keep local translation edits on a separate branch if you want to maintain your own changes. If Git reports conflicting local edits, preserve those edits before updating.

Updates published here are separate from Steam Workshop updates. When a source mod changes its definition names or text, this patch may need an update too.

## Compatibility and verification

- The patch declares RimWorld **1.6 and 1.7** support. It was generated against the mods installed alongside RimWorld 1.7; version declarations are not a claim of full testing on both versions.
- Source text was taken from the newest installed version folder for each mod. A mod's load-folder rules may select a different subset in another game version or mod configuration.
- Most translations were generated locally with **Ollama qwen3.5:9b**, followed by selected terminology corrections. Expect occasional awkward wording or inconsistent names.
- Offline checks cover XML parsing, duplicate keys, conditional folders, source text paths, preserved placeholders, and rich-text tags. Repository regression tests also check unique language-file paths across load roots and English labels for all seven blessed devilstrand cloth colors.
- Translation filenames include their source package ID. RimWorld overlays a mod's load folders, so reusing a filename such as `ThingDef/Local.xml` across those folders can hide another folder's translations. This fixes the filename collisions in the initial release.
- Run the repository tests with `python3 -m unittest discover -s tests`.
- Full in-game verification has **not** been completed. Hard-coded DLL strings, text embedded in images, inherited abstract definitions, and text introduced by XML patch operations may remain untranslated.
- Existing English translations were retained unless selected entries still contained CJK text. Contributor names in Project RimFactory's already-English credits were deliberately left unchanged; that mod is not included in this patch.
- This patch does not alter original Workshop files or intentionally change gameplay. Keeping the original files untouched allows Steam to update them normally.

If text remains untranslated, include the original mod name, a screenshot, your RimWorld version, and the relevant item or screen name in a GitHub issue. A screenshot alone may not reveal whether the text comes from XML, code, or an image.

## Remove

Disable **Local English Translations** in RimWorld's Mods menu and restart. You can then remove its folder. The original Workshop mods remain unchanged.

## Attribution

All original mods and their content belong to their respective authors. This repository is an unofficial local translation patch and is not endorsed by those authors or Ludeon Studios. Workshop links above identify the original projects. No original mod binaries or artwork are bundled.
