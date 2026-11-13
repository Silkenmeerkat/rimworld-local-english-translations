import collections
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class LanguageRootTests(unittest.TestCase):
    def test_unique_overlay_paths(self):
        """Load-folder overlays must never hide another translation XML file."""
        for version in ET.parse(ROOT / 'LoadFolders.xml').getroot():
            paths = {}
            for folder in version:
                base = ROOT / folder.text
                self.assertTrue(base.is_dir(), str(base))
                for file in base.rglob('*.xml'):
                    relative = file.relative_to(base).as_posix().lower()
                    self.assertNotIn(relative, paths,
                                     f'{version.tag}: {file} hides {paths.get(relative)}')
                    paths[relative] = file

    def test_translation_count_and_unique_keys(self):
        count = 0
        seen = set()
        for file in (ROOT / 'Translations').rglob('*.xml'):
            root = ET.parse(file).getroot()
            self.assertEqual(root.tag, 'LanguageData')
            package = file.relative_to(ROOT / 'Translations').parts[0]
            def_type = file.parent.name
            for entry in root:
                identity = (package, def_type, entry.tag)
                self.assertNotIn(identity, seen)
                seen.add(identity)
                self.assertTrue(entry.text)
                count += 1
        self.assertEqual(count, 1006)

    def test_devilstrand_unlock_labels_survive_overlay(self):
        """Model file discovery before checking the labels in the research UI."""
        for version in ET.parse(ROOT / 'LoadFolders.xml').getroot():
            overlay = {}
            for folder in version:
                base = ROOT / folder.text
                for file in base.rglob('*.xml'):
                    overlay[file.relative_to(base).as_posix().lower()] = file
            labels = {}
            for file in overlay.values():
                if file.parent.name == 'ThingDef':
                    labels.update({entry.tag: entry.text for entry in ET.parse(file).getroot()})
            for color in ['White', 'Purple', 'Green', 'Red', 'Blue', 'Yellow', 'Black']:
                key = f'BlessDevilCloth{color}.label'
                self.assertIn(key, labels, f'{version.tag}: missing {key}')
                self.assertIn('Blessed Devil', labels[key])
                self.assertIsNone(re.search('[\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]', labels[key]))


if __name__ == '__main__':
    unittest.main()
