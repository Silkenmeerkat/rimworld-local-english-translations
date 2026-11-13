Local English Translations

Enable in RimWorld's Mods menu and place after all translated mods, preferably at the bottom. Restart RimWorld with English selected.

This patch adds 1,006 English DefInjected entries across 13 mods. It does not edit Workshop files, gameplay definitions, saves, or the active mod configuration. LoadFolders.xml gates each translation folder by its source package ID.

Most translations were generated on this machine with Ollama qwen3.5:9b. Selected terminology was manually corrected. Existing English entries were retained unless they still contained untranslated CJK text. Contributor names in Project RimFactory's English credits were intentionally left unchanged.

Offline checks passed for XML parsing, unique keys, conditional folders, source target paths, preserved placeholders, and rich-text tags. In-game rendering and translation quality have not been fully verified. Hard-coded DLL strings, text embedded in textures, source XML patch operations, and inherited abstract-definition text may require additional work. Source files from the newest installed version folder were used for each mod; the game may choose a different subset through its load-folder rules.

Audit files and generation scripts:
/home/cburt/agent-runs/rimworld-translation

To uninstall, disable Local English Translations in the Mods menu. Original mods remain unchanged.
